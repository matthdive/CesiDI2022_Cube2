from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ae09699df9b0845d9825011a7d837f93'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app