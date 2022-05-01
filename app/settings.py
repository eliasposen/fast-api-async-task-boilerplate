from os import getenv

# DATABASE
DB_PROVIDER = "postgres"
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")
DB_NAME = getenv("DB_NAME")
DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")

if not all((DB_PROVIDER, DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD)):
    raise ValueError("Required DB variables not defined in environment")

# JWT Authentication
JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = "HS256"
JWT_ACCESS_TOKEN_EXPIRE_MIN = int(getenv("JWT_ACCESS_TOKEN_EXPIRE_MIN", "0"))

if not all((JWT_SECRET_KEY, JWT_ALGORITHM, JWT_ACCESS_TOKEN_EXPIRE_MIN)):
    raise ValueError("Required JWT variables not defined in environment")
