from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://banco_pi_owner:npg_nLSXmdj45eAQ@ep-cool-wildflower-a8xnke2o-pooler.eastus2.azure.neon.tech/banco_pi?sslmode=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
