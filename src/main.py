from flask import Flask

from routes.main import router
from routes.frontend import router as frontend

app = Flask(__name__)
app.register_blueprint(router)
app.register_blueprint(frontend)


if __name__ == '__main__': app.run(host="0.0.0.0", port=3000, debug=True)