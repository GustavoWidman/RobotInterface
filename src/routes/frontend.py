from flask import Blueprint, Response, render_template, request

# from database.wrapper import DB
# from utils.logger import log

router = Blueprint('frontend', __name__)


@router.route('/logs', methods=['GET'])
def logs_page():
	return render_template("logs.html")

@router.route('/', methods=['GET'])
def index_page():
	return render_template("index.html")