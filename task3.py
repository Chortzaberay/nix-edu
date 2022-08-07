
import logging

def error_handler(func):

    def inner(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # open log file to write
        fh = logging.FileHandler(f"{name}.log")
        
        # add new format
        fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        formatter = logging.Formatter(fmt)

        # set format
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        
        try:
            logger.info(f"Call function: {name}")
            result = func(*args, **kwargs)
            logger.info(f"Result: {result}")
            return result

        except Exception as ex:
            logger.error(f"Exception: {ex}")
            raise ex

    return inner
        
            
