import time
from logging.handlers import TimedRotatingFileHandler
from dateutil import parser
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from application.utils.cloud_log_formatter import CloudLogFormatter
from flask import Flask
from flask_cors import CORS

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'




def load_blueprints(app):
    from application.userland.controller import mod_userland
    from application.userland.controllers.domain_controller import mod_userland as domain_module
    from application.userland.controllers.user_controller import mod_userland as user_module
    app.register_blueprint(mod_userland)


def create_app(config_file_location=None):
    app = Flask(__name__, template_folder="templates")
    CORS(app)
    if config_file_location:
        app.config.from_pyfile(config_file_location, silent=False)
    else:
        # configure it in order -> prod overrides prp overrides dev
        app.config.from_pyfile('../config/dev.cfg', silent=True)
        app.config.from_pyfile('../config/prp.cfg', silent=True)
        app.config.from_pyfile('../config/prod.cfg', silent=False)

    from application.core.db_models import DomainInfo
    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from application.core.db_models import Users
        return Users.query.get(int(user_id))

    migrate.init_app(app, db)

    login_manager.login_view = 'application/frontend/src/views/LoginView.vue'




    # configure logging
    log_format = (
        "[%(asctime)s] %(levelname)s %(remote_addr)s %(request_type)s %(http_version)s %(url)s %(pathname)s rt:%(response_time)s %(message)s")
    log_formatter = CloudLogFormatter(log_format)
    log_file = app.config['LOG_FILE_PATH']
    log_timed_rotating_handler = TimedRotatingFileHandler(log_file, when="midnight")
    log_timed_rotating_handler.setFormatter(log_formatter)
    log_timed_rotating_handler.setLevel(app.config['LOG_LEVEL'])
    app.static_folder = 'static'
    app.logger.setLevel(app.config['LOG_LEVEL'])
    app.logger.addHandler(log_timed_rotating_handler)

    load_blueprints(app)

    @app.template_filter('ctime')
    def epoch_to_datetime(s):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(s)))

    @app.template_filter('datetimeformat')
    def datetime_format(s):
        if s:
            dt = parser.parse(s)
            return dt.strftime('%Y-%m-%d %H:%M:%S')

    return app


