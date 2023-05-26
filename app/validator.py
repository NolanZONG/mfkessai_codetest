"""
Validators for transaction data requests

This module defines the validator classes for validating transaction data parameters
"""


from pydantic import BaseModel, validator

from .repository import UserRepository


class TransactionBodyValidator(BaseModel):
    """
    validator class for validating a request body
    """
    user_id: int
    api_key: str
    amount: int

    @validator("user_id")
    def check_user_id(cls, value):
        repository = UserRepository()
        user = repository.get_user_data_by_id(uid=value)
        if user is None:
            raise ValueError("The user does not exist or api_key is invalid")
        return value

    @validator("api_key")
    def check_api_key(cls, value, values):
        if "user_id" in values:
            repository = UserRepository()
            user = repository.get_user_data_by_id(uid=values["user_id"])
            if value != user.api_key:
                raise ValueError("The user does not exist or api_key is invalid")
        return value

    @validator("amount")
    def check_amount(cls, value, values):
        if "user_id" in values:
            repository = UserRepository()
            user = repository.get_user_data_by_id(uid=values["user_id"])
            if sum(ob.amount for ob in user.transactions) + value > 1000:
                raise ValueError("overflow")
        return value
