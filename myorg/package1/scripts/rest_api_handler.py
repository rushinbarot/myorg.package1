#!flask/bin/python
""" 
This API attempts to return the 
elapsed response times of several
domains (default-services) or the elapsed
response time of another service given
by user.

TODO Note that this returns a repr'ed exception 
on user input error, so you may want to change that
if the API is facing the public (security issue).

"""
from flask import Flask
import json
import myorg.package1
from myorg.package1.check_services import check_services
import logging
import os

options_js_file = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                            'static/options.js')
options = json.load(open(options_js_file))

logger = logging.getLogger('myorg')
app = Flask(__name__)
logger.info('Init server')
@app.route('/default-services')
def default_services():
    try:
        ret_val = check_services()
        logger.info('Success default-services')
    except Exception as e:
        ret_val = {'help': options['default-services'],
                  'error': repr(e)}
        logger.info('Failed on %r with %r'% ('default-services', repr(e)))
    return json.dumps(ret_val)
@app.route('/other-service/<other_service>', methods=['GET'])
def other_service(other_service):
    try:
        ret_val =check_services(services=[other_service])
        logger.info('Success %r'%other_service)
    except Exception as e:
        ret_val  ={'help': options['other-service'],
                    'error': repr(e),
                }
        logger.info('Failed on %r with %r'% (other_service, repr(e)))
    return  json.dumps(ret_val)
def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()