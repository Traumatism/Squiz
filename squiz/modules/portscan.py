import threading
import typing
import socket

from squiz.types import IPAddress
from squiz.base import BaseModule, BaseModel

PORTS = (
    21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143,
    161, 179, 389, 443, 445, 465, 548, 554, 587, 636,
    993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8086,
    8087, 8443, 8888, 9999, 27017, 49152, 50000
)


class PortScanResults(BaseModel):

    ip: str
    ports: typing.List[int]

    render_fields = {
        "IP Address": "ip",
        "Ports": "ports_str"
    }

    @property
    def ports_str(self) -> str:
        return ", ".join(map(str, sorted(self.ports)))


class Module(BaseModule):

    name = "Port scan"
    target_types = (IPAddress, )

    def __init__(self) -> None:
        super().__init__()

        self.open_ports: typing.List[int] = []

    def __scan_port(
        self, target: IPAddress, port: int, timeout: typing.Union[float, int]
    ) -> bool:
        """ Scan a port """

        try:
            socket.create_connection((target.value, port), timeout=timeout)
        except Exception:
            return False

        self.open_ports.append(port)
        return True

    def execute(self, **kwargs):
        target = kwargs["target"]

        ports = kwargs.get("tcp_ports", PORTS)
        timeout = kwargs.get("connection_timeout", 5)
        threads = kwargs.get("threads", 10)

        for port in ports:
            while threading.active_count() >= threads:
                continue

            threading.Thread(
                target=self.__scan_port,
                args=(target, port, timeout)
            ).start()

        self.results.append(
            PortScanResults(ip=target.value, ports=self.open_ports)
        )

        return self.ExecutionSuccess()
