#from check_services import check_services
#from check_logfiles import check_logfiles
import logging
logging.basicConfig(
    filename = 'rest_api.log',         # Name of the log file (omit to use stderr)
    filemode = 'w',               # File mode (use 'a' to append)
    level    = logging.DEBUG,   # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
)