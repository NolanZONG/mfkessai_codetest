"""
Transaction Repository

This module provides repositories class for managing table data in the database.
"""

from .model import User, Transaction
from .database import SessionLocal


class UserRepository:
    """
    This class provides methods for interacting with the user data in the database.
    """
    def __init__(self):
        """
        Initializes the repository by creating an SQLAlchemy session.
        """
        self.session = SessionLocal()

    def get_user_data_by_id(self, uid: int) -> User:
        """
        Retrieves user data from the database based on the provided id.

        :param uid: The user_id of the user data to query.
        :return: A object of user data record.
        """
        return self.session.query(User).filter(User.id == uid).first()


class TransactionRepository:
    """
    This class provides methods for interacting with the transaction data in the database.
    """
    def __init__(self):
        """
        Initializes the repository by creating an SQLAlchemy session.
        """
        self.session = SessionLocal()

    def insert_transaction_data(self, user_id: int, amount: int, description: str) -> None:
        """
        Insert transaction data into the database based on the provided parameters.

        :param user_id: The user_id of the user data to query.
        :param amount: The amount of the user data to query.
        :param description: The description of the user data to query.
        """
        try:
            self.session.add(
                Transaction(
                    user_id=user_id,
                    amount=amount,
                    description=description,
                )
            )
            self.session.commit()
        except Exception:
            self.session.rollback()
            raise
        finally:
            self.session.close()
