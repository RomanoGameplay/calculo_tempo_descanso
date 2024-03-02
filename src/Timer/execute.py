from src.Timer.FreeTime import FreeTime
from src.Timer.Cronometer import Cronometer


def execute_freetime_class(hours: tuple) -> None:
    """
    Executa o cálculo do tempo livre.

    :param hours: Tupla representando tempo de estudo no formato (hora, minuto, segundo)
    """

    FreeTime(hours=hours).run()


def execute_cronometer() -> str:
    """
    Executa a classe Cronometer

    :return: Tempo cronometrado
    """

    cronometer_obj = Cronometer()
    cronometer_obj.run()
    cronometer = cronometer_obj.get_cronometer()

    return cronometer
