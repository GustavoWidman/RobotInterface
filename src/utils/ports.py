from serial.tools import list_ports

def serial_ports():
    """
        Lista os dispositivos seriais disponíveis no sistema que se identificam como Dobot Magician Lite

        :raises EnvironmentError:
            Em caso de erro na detecção do sistema operacional
        :returns:
            Uma lista de portas seriais disponíveis
    """

    ports = list_ports.comports()

    dobot_ports = [
        port for port in ports if (
            port.vid == 1155
            and port.pid == 22352
        )
    ]

    return [port.device for port in dobot_ports]