import logging
from flask import Flask
from .views import view

app = Flask(__name__)
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)
app.logger.debug('this will show in the log')
app.config.from_object("config")
app.register_blueprint(view)
