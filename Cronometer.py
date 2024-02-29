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
    paused: bool
    cronometer: str

    def __init__(self) -> None:
        """
        Método construtor da classe
        """

        self.second, self.minute, self.hour = 0, 0, 0
        self.start_time = False
        self.paused = False
        self.cronometer = ''

    def start(self) -> None:
        """
        Inicia contagem do cronômetro
        """

        print('\n\tCronômetro rodando...')
        self.start_time = True

        while self.start_time:
            if keyboard.is_pressed('space'):
                self.time_paused()

            elif keyboard.is_pressed('q'):
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

        self.paused = True

        while self.paused:
            if keyboard.is_pressed('space'):
                print('\n\tReiniciando cronômetro...\n')
                break
            elif keyboard.is_pressed('q'):
                self.start_time = False
                break
            else:
                pass

    def run(self) -> str:
        """
        Roda o processo do Cronômetro

        :return tempo cronometrado
        """

        self.start()
        self.cronometer = '{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)
        print(f'\n\t--> Tempo estudado: {self.cronometer}')
        time.sleep(2.5)
        return self.cronometer
