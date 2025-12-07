import logging
from datetime import datetime
import os
import sys

# defining the log file name format
file_name = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

dir_path = os.path.join(os.getcwd(), "logs", file_name)

# Creating directory
os.makedirs(dir_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(dir_path, file_name)


# Setting up the basic Configurations
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



if __name__=="__main__":
    logging.info("HI !!")
    logging.info("It is working fine!")