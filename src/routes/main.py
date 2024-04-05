from flask import Blueprint

from routes.robot import router as robot_router
from routes.logs import router as logs_router


router = Blueprint('router', __name__, url_prefix='/api')
router.register_blueprint(robot_router, url_prefix='/robot')
router.register_blueprint(logs_router, url_prefix='/logs')