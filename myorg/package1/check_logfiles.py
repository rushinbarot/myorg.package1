
import sys
import logging
logger = logging.getLogger(__name__)
def check_logfiles():
    """check_log_files expects to have standard input
     be a CSV with two columns.  

     The first column is string and the second is integer. 

    Returns sum of the second column"""
    summ = 0
    for line in (_.strip() for _ in sys.stdin):
        parts = line.split(',')
        summ += int(parts[1])
    print "sum:",summ
    return summ