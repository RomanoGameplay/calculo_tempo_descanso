import os
import keyboard
import time
from src.info import show_time
from src.config import KEY_STOP, KEY_PAUSE, START


class Temporizer:
    """
    Classe responsável pelo temporizador do tempo de descanso
    """

    hours: tuple
    start: bool
    key_pause_temporizer: str
    key_stop_temporizer: str

    def __init__(self, hours: tuple) -> None:
        """
        Método construtor da classe
        """

        self.hours = hours
        self.start = START
        self.key_pause_temporizer = KEY_PAUSE
        self.key_stop_temporizer = KEY_STOP

    def start_temporizer(self) -> None:
        """
        Inicia o temporizador
        """

        hour, minute, second = self.hours

        while self.start:
            if keyboard.is_pressed(self.key_pause_temporizer):
                print('\n\tPausando contagem...')
                self.time_paused()
            elif keyboard.is_pressed(self.key_stop_temporizer):
                print('\n\tEncerrando contagem...\n')
                time.sleep(1)
                raise KeyboardInterrupt

            show_time(hour, minute, second, 'Temporizador')

            time.sleep(1)
            hour, minute, second = self.verify_conditions(hour, minute, second)

    def verify_conditions(self, hour, minute, second) -> tuple:
        """
        Verifica a quantidade de horas, minutos e segundos restantes.

        :param hour: Hora restantes
        :param minute: Minuto restante
        :param second: Segundo restante
        :return: Retorna o tempo restante
        """

        second -= 1

        if minute > 0 > second:
            minute -= 1
            second = 59
        elif minute == 0 < hour and second < 0:
            hour -= 1
            minute = 59
            second = 59
        elif (second < 0) and (minute == 0) and (hour == 0):
            print('\n\nFim do Temporizador!')
            time.sleep(1)
            self.start = False

        return hour, minute, second

    def time_paused(self) -> None:
        """
        Pausa o temporizador
        """

        time.sleep(2)
        while True:
            if keyboard.is_pressed(self.key_pause_temporizer):
                os.system('cls')
                print('\n\tRetomando contagem do temporizador...\n')
                break
            elif keyboard.is_pressed(self.key_stop_temporizer):
                print('\n\nEncerrando contagem...\n')
                time.sleep(1)
                self.start = False
                raise KeyboardInterrupt

    def run(self) -> None:
        """
         Executa o temporizador
        """
        os.system('cls')
        self.start_temporizer()
