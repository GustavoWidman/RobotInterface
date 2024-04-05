import pydobot # type: ignore

from typing import Literal
from pydobot.dobot import Dobot # type: ignore

from utils.text import printc
from utils.ports import serial_ports


class RobotWrapper:
	_instance = None
	_initialized = False

	def __new__(cls, auto_init: bool = False):
		if cls._instance is None:
			cls._instance = super(RobotWrapper, cls).__new__(cls)

		if auto_init: cls._instance.init()

		return cls._instance

	def __init__(self, auto_init: bool = False):
		printc("[&6ROBOT&f] &bInstanciando classe do robô...")

		self.x: float
		self.y: float
		self.z: float
		self.r: float


	def init(self):
		"""
			Inicializa a conexão com o robô
		"""
		if self._initialized: return self
		printc("[&6ROBOT&f] &bEstabelecendo conexão com o robô...")

		port = self.scan_ports()
		if port is None: return None

		self.robot = Dobot(port=port)
		printc("[&6ROBOT&f] &aConexão estabelecida com sucesso!")

		self._initialized = True
		self.update_pos()

		return self

	def scan_ports(self) -> str | None:
		"""
			Procura por portas seriais disponíveis e tenta conectar com o robô
		"""

		ports = serial_ports()

		if len(ports) <= 0:
			printc("[&6ROBOT&f] &cNenhum robô foi encontrado, por favor, verifique a conexão ou conecte um robô para prosseguir.")
			return None

		if len(ports) > 1:
			printc("[&6ROBOT&f] &cMais de um robô foi encontrado, por favor, conecte apenas um robô para prosseguir.")
			return None

		return ports[0]

	def update_pos(self) -> None:
		if not self._initialized: self.init()
		self.x, self.y, self.z, self.r, self.j1, self.j2, self.j3, self.j4 = self.robot.pose()

	def current(self) -> dict[str, float]:
		self.update_pos()
		return {
			"x": round(self.x, 2),
			"y": round(self.y, 2),
			"z": round(self.z, 2)
		}

	def movej_to(self, x: float, y: float, z: float, r: float, wait: bool = True):
		if not self._initialized: self.init()

		self.robot._set_ptp_cmd( # type: ignore
			x=x, y=y, z=z, r=r, wait=wait,
			mode=pydobot.enums.PTPMode.MOVJ_XYZ, # type: ignore
		)

	def move(self,
			x: float | None = None,
			y: float | None = None,
			z: float | None = None,
		) -> None:
		if not self._initialized: self.init()

		if not x: x = self.x
		if not y: y = self.y
		if not z: z = self.z

		printc(f"[&6ROBOT&f] &bMovendo robô para (&5{x}&b, &5{y}&b, &5{z}&b)")

		self.movej_to(x, y, z, r=self.r, wait=True)

		self.update_pos()

	def move_safe(self,
		x: float | None = None,
		y: float | None = None,
		z: float | None = None,
	) -> None:
		if not self._initialized: self.init()

		self.move(x=self.x, y=self.y, z=150) # Move to max z
		self.move(x=x, y=y, z=150) # Move horizontally
		self.move(x=x, y=y, z=z) # Move back down

	def home(self):
		if not self._initialized: self.init()

		self.move_safe(250, 0, 150)

	def tool(self, tool: Literal["suction", "gripper"], state: bool):
		if not self._initialized: self.init()

		printc(f"[&6ROBOT&f] &bLigando a ferramenta &5{tool}")

		match tool:
			case "suction": self.robot.suck(state) # type: ignore
			case "gripper": self.robot.grip(state) # type: ignore

		printc(f"[&6ROBOT&f] &bFerramenta &5{tool} &b{'ligada' if state else 'desligada'}.")