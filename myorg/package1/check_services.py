
# the code of the inner module
import requests
import time
import logging
import os
logger = logging.getLogger(__name__)
SERVICES = ['google.com','python.org','rei.com']
def check_services(services=None):
    response = []
    logger.info('Preparing to check_services')
    if services is None:
        services = SERVICES
    for s in services:
        start = time.time()
        answer = None
        for retries in range(3):
            try:
                answer = requests.get('http://%s' % s)
            except Exception as e:
                pass
        if answer is None:
            # do not record the response time if it was unreachable
            logger.info('Failed on service %r with exception %r' % (s, e))
            elapsed = None
        else:
            end = time.time()
            elapsed = end - start
        response.append({s: elapsed})
    return response
