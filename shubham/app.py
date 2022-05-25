from flask import Flask
from flask_cors import CORS
# from flask_jwt_extended import JWTManager

from .v1 import v1_blueprint


def create_app():
    app = Flask(__name__)
    CORS(app)
    # Setup the Flask-JWT-Extended extension
    # app.config["JWT_SECRET_KEY"] = "hbdbd6726hlooaqw3343ncn"  # Change this!
    # jwt = JWTManager(app)

    @app.errorhandler(404)
    def page_not_found(error):
        return {"message": "Requested resource does not exist"}, 404

    @app.errorhandler(Exception)
    def error_500(error):
        return {"message": str(error), "status":False, 'type': "custom_error"}, 400

    @app.route('/health')
    def health():
        return {"status":True,"data":{},"type":
            "success_message","message":"success"},200
    app.register_blueprint(v1_blueprint)


    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
