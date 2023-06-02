"""
FastAPI Application for Transaction Register

This module implements a FastAPI application for registering transaction data.
It provides one API:
- POST /transactions: register transaction record
"""
from typing import Annotated

from fastapi import FastAPI, status, Header, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from repository import TransactionRepository
from schema import Transaction
from validator import TransactionBodyValidator


description = """
## Descriptions
This service is a prototype for the MFK take-home assignment. 
It is implemented in Python 3.11 and integrated with a MySQL database.

## APIs
### Register transaction data
- Register transactions for specific user
- If the total amount of transactions beyond the limit, an error will occur.

"""

tags_metadata = [
    {
        "name": "Register transaction data",
        "description": "Register transactions for specific user"
    }
]

app = FastAPI(
    title="MFK Take-Home Assignment",
    description=description,
    version="1.0.0",
    openapi_tags=tags_metadata,
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(exc: RequestValidationError) -> JSONResponse:
    """
    This function is an error handler to return validation error

    :param exc: exception context
    :return: error message
    """
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body})
    )


@app.post("/transactions", tags=["Register transactions"])
async def transaction_data(transaction: Transaction, apikey: Annotated[str | None, Header()] = None) -> JSONResponse:
    """
    This function is an API endpoint that registers transactions for specific user.

    :param transaction: The transaction data which is in the request doby.
    :param apikey: The user's secure api key.
    :return: Execution result.
    """
    try:
        if not apikey:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="apikey is required")
        TransactionBodyValidator(user_id=transaction.user_id, api_key=apikey, amount=transaction.amount)
        transaction_repository = TransactionRepository()
        transaction_repository.insert_transaction_data(
            user_id=transaction.user_id,
            amount=transaction.amount,
            description=transaction.description
        )
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder({}))
    except ValidationError as vde:
        err_msgs = [item["msg"] for item in vde.errors()]
        if "overflow" in err_msgs:
            return JSONResponse(
                status_code=status.HTTP_402_PAYMENT_REQUIRED,
                content=jsonable_encoder({"msg": "overflow"})
            )
        else:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content=jsonable_encoder({"msg": err_msgs})
            )
