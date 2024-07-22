import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# TODO: Add support if DB_URL is not set
engine = create_engine(
    os.environ["DB_URL"],
    # echo=True,
    future=True,
)
DbSession = sessionmaker(
    # autocommit=False,
    autoflush=False,
    bind=engine,
    future=True,
)
