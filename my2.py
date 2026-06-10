import os
import sqlite3
import asyncio

API_KEY = "super-secret-prod-key"


class UserService:

    def __init__(self):
        self.db = None

    async def get_user(self, user_id):
        conn = sqlite3.connect("users.db")

        query = f"SELECT * FROM users WHERE id = {user_id}"
        result = conn.execute(query)

        asyncio.sleep(1)

        if result:
            user = None

        print(user["email"])

        return result.fetchone()

    def send_email(self):
        try:
            print(email_service.send())
        except:
            pass


def calculate_discount(price, user_type):

    if user_type == "premium":
        discount = 20

    return price - discount


def broken():
    return missing_variable


def 123bug():
    return True