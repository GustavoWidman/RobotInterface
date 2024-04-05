from flask import Blueprint, request, render_template

from utils.logger import log
from classes.robot import RobotWrapper


router = Blueprint('robot', __name__)

@router.route('/current', methods=['GET'])
def current():
	log( str(request.remote_addr), 'current', {} )

	robot = RobotWrapper()

	if robot.init(): return robot.current()

	return 'Robot not initialized', 500

@router.route('/move', methods=['POST'])
def move():
	log( str(request.remote_addr), 'move', request.json if request.json else {} )

	robot = RobotWrapper()

	if robot.init():
		#? Data validation
		data = request.json
		if not data: return 'Invalid data', 400
		if not any(key in data for key in ['x', 'y', 'z']): return 'Invalid data', 400

		data = {key: float(value) for key, value in data.items()}
		# if any item is none, replace with "0.1"
		data = {key: value if value != 0.0 else 0.1 for key, value in data.items()}


		print(data)

		robot.move_safe(x=data['x'], y=data['y'], z=data['z'])
		return 'Moving robot'

	return 'Robot not initialized', 500

@router.route('/home', methods=['POST'])
def home():
	log( str(request.remote_addr), 'home', request.json if request.json else {} )

	robot = RobotWrapper()

	if robot.init():
		robot.home()
		return 'Moving robot to home'

	return 'Robot not initialized', 500

@router.route('/tool', methods=['POST'])
def tool():
	log( str(request.remote_addr), 'tool', request.json if request.json else {} )

	robot = RobotWrapper()

	if robot.init():
		#? Data validation
		data = request.json
		if not data: return 'Invalid data', 400
		if not all(key in data for key in ['tool', 'state']): return 'Invalid data', 400

		data['state'] = data['state'] == 'true'

		robot.tool(data['tool'], data['state'])
		return 'Changing tool state'

	return 'Robot not initialized', 500

@router.route('/move_unsafe', methods=['POST'])
def move_unsafe():
	log( str(request.remote_addr), 'move_unsafe', request.json if request.json else {} )

	robot = RobotWrapper()

	if robot.init():
		#? Data validation
		data = request.json
		if not data: return 'Invalid data', 400
		if not any(key in data for key in ['x', 'y', 'z']): return 'Invalid data', 400

		data = {key: float(value) for key, value in data.items()}
		# if any key is "0.0", replace with 0.1
		data = {key: value if value != 0.0 else 0.1 for key, value in data.items()}

		print(data)

		robot.move(x=data['x'], y=data['y'], z=data['z'])
		return 'Moving robot'

	return 'Robot not initialized', 500

@router.route('/', methods=['GET'])
def test_robot():
	robot = RobotWrapper()

	if robot.init():
		return render_template("dashboard.html")

	return render_template("no_robot.html")



