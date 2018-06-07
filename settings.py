# imports
import os
from dotenv import load_dotenv
from os.path import join, dirname

# Get .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

install_path = os.path.abspath(dirname(__file__))

SP_SERVICE_ENDPOINT = os.environ.get('SP_SERVICE_ENDPOINT')

SP_CERTIFICATE = os.environ.get('SP_CERTIFICATE')

SP_SOAP_REQUEST_ENVELOPE = os.environ.get('SP_SOAP_REQUEST_ENVELOPE')

SP_SYSTEM = os.environ.get('SP_SYSTEM')

SP_USER = os.environ.get('SP_USER')

SP_SERVICE_AGREEMENT = os.environ.get('SP_SERVICE_AGREEMENT')

SP_SERVICE = os.environ.get('SP_SERVICE')
