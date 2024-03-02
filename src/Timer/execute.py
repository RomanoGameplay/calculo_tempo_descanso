from src.Timer.FreeTime import FreeTime
from src.Timer.Cronometer import Cronometer
from src.Timer.SoundTimer import SoundTimer
from src.Timer.Temporizer import Temporizer


def execute_freetime_class(hours: tuple) -> dict:
    """
    Executa o cálculo do tempo livre.

    :param hours: Tupla representando tempo de estudo no formato (hora, minuto, segundo)
    :return: Retorna os tempos calculados
    """

    freetime = FreeTime(hours=hours)
    freetime.run()
    return freetime.free_times


def execute_cronometer() -> str:
    """
    Executa a classe Cronometer

    :return: Retorna o tempo cronometrado
    """

    cronometer_obj = Cronometer()
    cronometer_obj.run()
    cronometer = cronometer_obj.get_cronometer()
    return cronometer


def execute_temporizer(hour: tuple) -> None:
    """
    Executa o temporizador

    :param hour: Tempo de descanso
    """

    Temporizer(hour).run()


def execute_beep() -> None:
    """
    Executa o som de beep
    """

    SoundTimer().run()
