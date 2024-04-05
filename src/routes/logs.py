from flask import Blueprint, Response, render_template, request

from database.wrapper import DB
from utils.logger import log

router = Blueprint('logs', __name__)


@router.route('/', methods=['GET'])
def get_all():
	with DB('src/database/archives/logs.json') as db: logs = db.all()

	log( str(request.remote_addr), 'read_logs', {} )


	return render_template("log_list.html", logs=[{
		"doc_id": log.doc_id,
		"data": log
	} for log in logs])


@router.route("/<id>", methods=["DELETE"])
def delete_one(id: int):
	with DB('src/database/archives/logs.json') as db: db.remove(doc_ids=[int(id)])
	log( str(request.remote_addr), 'delete_log', {'id': str(id) } )

	resp = Response()
	resp.headers["HX-Redirect"] = "/logs"
	return resp


@router.route("/all", methods=["DELETE"])
def delete_all():
	with DB('src/database/archives/logs.json') as db: db.truncate()
	log( str(request.remote_addr), 'delete_all_logs', {} )

	resp = Response()
	resp.headers["HX-Redirect"] = "/logs"
	return resp