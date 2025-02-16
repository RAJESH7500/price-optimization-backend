import os
from datetime import timedelta


# Defining project configs
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "rajesh-kumar"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
        or "postgresql://price_optimization_tool_user:KDdm1ZYf9xULEYDbBp0WMJv703ivVhbh@dpg-cuo4r15ds78s738esq3g-a.oregon-postgres.render.com/price_optimization_tool"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or "rajesh-kumar"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=12)
    

