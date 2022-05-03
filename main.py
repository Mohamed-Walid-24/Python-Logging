import logging

logging.basicConfig(level=logging.DEBUG,filename="Logs.log",filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
"""logging.debug("hi")
logging.info("Information")
logging.warning("Warning incoming")
logging.error("There is an error")
logging.critical("OPS what have you have done")"""

try:
    1/0
except ZeroDivisionError as e:
    logging.error("ZeroDivisionError",exc_info=True)
    #Another way:
    logging.exception("Error in dividing")
