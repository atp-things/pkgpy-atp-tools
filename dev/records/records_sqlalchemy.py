import asyncio
from pprint import pprint

from atptools import Records

from database import DbSession
from database.models import User

print("_______________")
print("Script [start]:", __file__)


async def main():
    print("Asyncio [start]:")

    # read measurements
    with DbSession() as db:
        # rows
        print("rows--------------")
        users = db.query(
            User.email,
            User.name,
        ).all()

        records = Records()
        records.from_sqlalchemy(users)
        print("users_jsonable [type]:", type(records))
        for user in records:
            print("Row type:", type(user))
        pprint(records)

        # models
        print("models--------------")
        users = db.query(User).all()
        records = Records()
        records.from_sqlalchemy(users)
        print("users_jsonable [type]:", type(records))
        for user in records:
            print("Row type:", type(user))
        pprint(records)


asyncio.run(main())

print("Script [end]:", __file__)
print("_______________")
