import time
import keyboard


class Cronometer:
    """
    Classe responsável por iniciar contagem de um cronômetro
    """

    second: int
    minute: int
    hour: int
    start_time: bool
    cronometer: str
    key_pause_cronometer: str
    key_stop_cronometer: str

    def __init__(self) -> None:
        """
        Método construtor da classe
        """

        self.second, self.minute, self.hour = 0, 0, 0
        self.start_time = False
        self.cronometer = '00:00:00'
        self.key_pause_cronometer = 'ctrl+space'
        self.key_stop_cronometer = 'ctrl+q'

    def start(self) -> None:
        """
        Inicia contagem do cronômetro
        """

        print('\n\tCronômetro rodando...')
        self.start_time = True

        while self.start_time:
            if keyboard.is_pressed(self.key_pause_cronometer):
                self.time_paused()
            elif keyboard.is_pressed(self.key_stop_cronometer):
                break

            time.sleep(1)
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
        print('\t{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second))
        time.sleep(2)

        while True:
            if keyboard.is_pressed(self.key_pause_cronometer):
                print('\n\tContinuando contagem do cronômetro...\n')
                break
            elif keyboard.is_pressed(self.key_stop_cronometer):
                self.start_time = False
                break
            else:
                pass

    def get_cronometer(self) -> str:
        """
        Entrega o valor do croômetro

        :return: Tempo cronometrado
        """

        return self.cronometer

    def run(self) -> None:
        """
        Roda o processo do Cronômetro
        """

        self.start()
        self.cronometer = '{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)
