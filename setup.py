import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cpr_abonnement",
    version = "0.0.1",
    author = "Heini Leander Ovason",
    author_email = "heini@magenta-aps.dk",
    description = ("Python integration with Serviceplatformen web service CPR Abonnement. Available operations are 'AddPNRSubscription' and 'RemovePNRSubscription'"),
    license = "MPL",
    keywords = "serviceplatformen cpr abonnement sf6002",
    url = "",
    packages=['cpr_abonnement'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MPL License",
    ],
    install_requires=[
        "certifi",
        "cffi",
        "chardet",
        "Jinja2",
        "MarkupSafe",
        "pycparser",
        "pyOpenSSL",
        "python-dotenv",
        "requests",
        "six",
        "urllib3",
        "xmltodict",
    ],
    package_data={
        'cpr_abonnement': ['soap_envelope.xml']
    }
    
)
