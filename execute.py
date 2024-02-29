from FreeTime import FreeTime
from Cronometer import Cronometer


def execute_freetime_class(hours: tuple) -> None:
    """
    Executa o cálculo do tempo livre.

    :param hours: Tupla representando tempo de estudo no formato (hora, minuto, segundo)
    """

    FreeTime(hours=hours).run()


def execute_cronometer() -> str:
    """
    Executa a classe Cronometer
    """

    cronometer = Cronometer().run()
    return cronometer
