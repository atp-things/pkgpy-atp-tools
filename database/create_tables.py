import asyncio

from engine import engine
from models import Base

print("_______________")
print("Script [start]:", __file__)


async def main():
    print("Asyncio [start]:")
    Base.metadata.create_all(bind=engine)
    print("Asyncio [end]:")


asyncio.run(main())

print("Script [end]:", __file__)
print("_______________")
