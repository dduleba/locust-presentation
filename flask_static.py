from flask import Blueprint, Flask

bp_locust = Blueprint('locust', __name__, static_folder='www')


def main(debug=False):
    app = Flask(__name__)
    app.register_blueprint(bp_locust)
    app.run(port=8091, debug=debug)

if __name__ == '__main__':
    main(debug=True)
