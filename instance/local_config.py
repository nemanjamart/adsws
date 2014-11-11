import os
import logging

LOG_LEVEL=logging.DEBUG
LOG_FILE='logs/adsws.log' #Relative to here
#Set DEBUG=True to log to stderr, which is useful for development only. 
#Note that this will also print the traceback in the response to the client, which is not desirable in production.
DEBUG=True

# Automatically generated by: python manage.py create_local_config

SOLR_SEARCH_HANDLER = 'http://10.0.0.5:8983/solr/select'
SOLR_QTREE_HANDLER = 'http://10.0.0.5:8983/solr/qtree'
SOLR_UPDATE_HANDLER = 'http://10.0.0.5:8983/solr/update'
SOLR_TVRH_HANDLER = 'http://10.0.0.5:8983/solr/tvrh'

CORS_DOMAINS = {
                'http://adslabs.org': 1,
                'http://localhost:8000': 1,
                'http://localhost:6002': 1,
                }

OAUTH2_CACHE_TYPE='simple'
SECRET_KEY = 'fake'
ACCOUNT_VERIFICATION_SECRET = 'fake'

FALL_BACK_ADS_CLASSIC_LOGIN = True
CLASSIC_LOGIN_URL = 'http://adsabs.harvard.edu/cgi-bin/maint/manage_account/credentials'
SITE_SECURE_URL = 'http://0.0.0.0:5000'

# Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
SQLALCHEMY_ECHO = False
#SQLALCHEMY_DATABASE_URI = 'sqlite:////adsws/adsws.sqlite'
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://adsabs:20yoAD$!@adsabs-psql-dev.ci1iae2ep00k.us-east-1.rds.amazonaws.com:5432/adsws'

# Stuff that should be added for every application
CORE_PACKAGES = []

HTTPS_ONLY=False
