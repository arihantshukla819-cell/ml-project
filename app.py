from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
if __name__=="__main__":
    logging.info("the execution has started")



    try:
        pass
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)

    
