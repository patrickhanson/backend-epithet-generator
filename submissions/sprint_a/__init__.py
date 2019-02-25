def configure_app():
    import os.path
    import dotenv
    from flask import Flask
    PROJECT_ROOT = os.path.dirname('/')
    dotenv.load_dotenv(PROJECT_ROOT, '/.env')
    os.path.join(PROJECT_ROOT, '/.env')
    app = Flask(__name__)
    return app


app = configure_app()