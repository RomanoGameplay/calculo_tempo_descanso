from FreeTime import FreeTime


def execute_freetime_class(hours: tuple) -> None:
    """
    Executa o cálculo do tempo livre.

    :param hours: Tupla representando tempo de estudo no formato (hora, minuto, segundo)
    """

    freetime = FreeTime(hours=hours)
    freetime.run()
