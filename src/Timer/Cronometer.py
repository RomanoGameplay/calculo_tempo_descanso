import time
import keyboard
from src.info import show_time
from src.config import START, KEY_STOP, KEY_PAUSE


class Cronometer:
    """
    Classe responsável por iniciar contagem de um cronômetro
    """

    second: int
    minute: int
    hour: int
    start: bool
    cronometer: str
    key_pause_cronometer: str
    key_stop_cronometer: str

    def __init__(self) -> None:
        """
        Método construtor da classe
        """

        self.second, self.minute, self.hour = 0, 0, 0
        self.start_time = START
        self.cronometer = '00:00:00'
        self.key_pause_cronometer = KEY_PAUSE
        self.key_stop_cronometer = KEY_STOP

    def start(self) -> None:
        """
        Inicia contagem do cronômetro
        """

        while self.start_time:
            if keyboard.is_pressed(self.key_pause_cronometer):
                self.time_paused()
            elif keyboard.is_pressed(self.key_stop_cronometer):
                print('\n\tEncerrando contagem...\n')
                time.sleep(1)
                break

            show_time(self.hour, self.minute, self.second, 'Cronômetro')
            time.sleep(1)
            self.increase_time()

    def increase_time(self):
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
        elif self.minute == 60:
            self.hour += 1
            self.minute = 0

    def time_paused(self) -> None:
        """
        Pausa contagem do Cronômetro
        """

        print('\n\tCronômetro Pausado...')
        time.sleep(2)

        while self.start_time:
            if keyboard.is_pressed(self.key_pause_cronometer):
                print('\n\tContinuando contagem do cronômetro...\n')
                break
            elif keyboard.is_pressed(self.key_stop_cronometer):
                print('\n\tEncerrando contagem...\n')
                time.sleep(1)
                self.start_time = False
                break

    def get_cronometer(self) -> str:
        """
        Entrega o valor do cronômetro

        :return: Tempo cronometrado
        """

        return self.cronometer

    def run(self) -> None:
        """
        Roda o processo do Cronômetro
        """

        self.start()
        self.cronometer = '{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)


if __name__ == '__main__':
    Cronometer().run()
