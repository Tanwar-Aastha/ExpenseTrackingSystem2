from dotenv import load_dotenv
from logger import logging
from exceptions import CustomException
import mysql.connector
from contextlib import contextmanager
import sys
import os

@contextmanager
def get_cursor(host, username, password, database):
    """
    Create MySQL connection and return cursor using context manager.
    """
    try:
        logging.info("STEP 1: Entering get_cursor()")

        logging.info(f"STEP 2: Credentials received -> Host={host}, User={username}, DB={database}")

        # Try connecting to MySQL
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        logging.info("STEP 3: MySQL connection successful")

        cursor = connection.cursor(dictionary=True)
        logging.info("STEP 4: Cursor created successfully")

        yield cursor   # Give cursor to calling code

        cursor.close()
        logging.info("STEP 5: Cursor closed")

        connection.close()
        logging.info("STEP 6: Connection closed")

    except Exception as e:
        logging.error(f"ERROR in get_cursor(): {str(e)}")
        raise CustomException(e, sys)


# if __name__ == "__main__":
#     load_dotenv()

#     host = os.getenv("HOST")
#     username = os.getenv("USER")
#     ps = os.getenv("PASSWORD")
#     database = os.getenv("CURRENT_DATABASE")

#     logging.info("STEP 0: Environment variables loaded")
#     logging.info(f"ENV -> Host={host}, User={username}, DB={database}")

#     try:
#         with get_cursor(host, username, ps, database) as cursor:
#             logging.info("STEP 7: Inside WITH block — cursor obtained successfully")
#             print("Connection & cursor working")
    
#     except Exception as e:
#         logging.error(f"FINAL ERROR: {str(e)}")
#         print("Error:", e)
