from typing import Literal
from datetime import datetime
from database.wrapper import DB


def log(
	ip: str,
	action: Literal['read_logs', 'move', 'move_unsafe', 'home', 'tool', 'current', 'delete_all_logs', 'delete_log'],
	params: dict[str, str] = {}
):
	with DB('src/database/archives/logs.json') as db:
		db.insert(({ # type: ignore
			"timestamp": str(datetime.now()),
			"ip": ip,
			"action": action,
			"params": params
		}))

