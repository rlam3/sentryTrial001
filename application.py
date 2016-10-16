
from flask import Flask
from extensions import sentry
import logging

def create_app():
    app = Flask(__name__)

    if app.debug == False:
        sentry.init_app(app, dsn='https://a7a14296c26840818363f0a771e18f53:a1b4dd4091e440c7900f62a5fca36038@sentry.io/106553', logging=True,
                        level=logging.ERROR,
                        logging_exclusions=("logger1", "logger2",))

    return app
