from flask import Blueprint, render_template

router = Blueprint('frontend', __name__)


@router.route('/logs', methods=['GET'])
def logs_page():
	return render_template("logs.html")

@router.route('/', methods=['GET'])
def index_page():
	return render_template("index.html")