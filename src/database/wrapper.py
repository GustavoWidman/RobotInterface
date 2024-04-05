from traceback import TracebackException
from types import TracebackType
from typing import Self
from tinydb import TinyDB
import threading


class DB:
	_instances: dict[str, Self] = {}  # Class-level dictionary to store instances
	_lock = threading.Lock()  # Class-level lock for thread-safe singleton creation

	def __new__(cls, path: str):
		with cls._lock:  # Ensure thread-safe singleton pattern
			if path not in cls._instances: cls._instances[path] = super(DB, cls).__new__(cls)
			return cls._instances[path]

	def __init__(self, path: str):
		if hasattr(self, 'is_initialized') and self.is_initialized: return

		self.path = path
		self.lock = threading.Lock()
		self.db = TinyDB(self.path)
		self.is_initialized = True  # Flag to prevent reinitialization

	def __enter__(self):
		self.lock.acquire()
		return self.db

	def __exit__(
		self,
		exc_type: Exception,
		exc_val: TracebackException,
		exc_tb: TracebackType
	):
		self.lock.release()