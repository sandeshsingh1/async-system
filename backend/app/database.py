# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# # 🔥 FORCE correct Docker DB
# DATABASE_URL = "postgresql://postgres:password@db:5432/docdb"

# engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(bind=engine)

# Base = declarative_base()
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")

print("DATABASE_URL =", DATABASE_URL)  # debug

# 🔥 THIS is where you add it
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()