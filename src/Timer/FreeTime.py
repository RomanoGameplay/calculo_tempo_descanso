from datetime import time


class FreeTime:
    """
    Classe responsável por realizar o cálculo de tempo de descanso
    """

    hours: tuple
    total_seconds: int
    free_times: dict

    def __init__(self, hours: tuple) -> None:
        """
        Método construtor da classe.

        :param hours: tupla representando as horas no formato (horas, minutos, segundos).
        """

        self.hours = hours
        self.total_seconds = self.calculate_total_seconds()

    def calculate_total_seconds(self) -> int:
        """
        Calcula do total de segundos.

        :return: Retorna um inteiro representando o total de segundos.
        """

        hours = (self.hours[0] * 60) * 60
        minutes = self.hours[1] * 60
        seconds = self.hours[2]
        return hours + minutes + seconds

    def calculate_free_time(self, proportion: float) -> float:
        """
        Retorna o tempo de descanso em formato float

        :param proportion: proporção do tempo de descanso em relação ao tempo de estudo
        :return: Retorna o tempo de descanso
        """

        freetimeseconds = (self.total_seconds * proportion) / 60
        freetimeseconds = round(freetimeseconds, 2)
        return freetimeseconds

    @staticmethod
    def format_free_time(freetime: float) -> time:
        """
        Formata o tempo em float para o formato adequado.

        :param freetime: tempo de descanso sem formatação.
        :return: Retorna o tempo de descanso formatado.
        """

        hours = int(freetime) // 60
        minutes = int(freetime - (hours * 60))
        seconds = int(round(round(freetime - int(freetime), 2) * 60, 0))
        formatted_free_time = time(hour=hours, minute=minutes, second=seconds)
        return formatted_free_time

    def show_free_time(self, free_time_one_fifth: float, free_time_one_third: float) -> None:
        """
        Apresenta as informações sobre tempo de descanso de forma formatada.

        :param free_time_one_fifth: tempo de descanso (1/3 do tempo de estudo).
        :param free_time_one_third: tempo de descanso (1/5 do tempo de estudo).
        """

        self.free_times = {
            'fifth': self.format_free_time(free_time_one_fifth),
            'third': self.format_free_time(free_time_one_third),
            'third_fifth': self.format_free_time(free_time_one_third - free_time_one_fifth)
        }

        print(f'\tSe optar por usar 1/5 do tempo de estudo, então seu tempo de descanso será '
              f'{self.free_times["fifth"]}!')
        print(f'\tSe optar por usar 1/3 do tempo de estudo, então seu tempo de descanso será '
              f'{self.free_times["third"]}!')
        print(f'\tCaso queira estender o tempo até 1/3 do tempo, então adicione '
              f'{self.free_times["third_fifth"]}'
              f' ao tempo de descanso!')

    def get_free_times(self):
        return self.free_times

    def run(self) -> None:
        """
        Executa o processo de cálculo do tempo livre!
        """

        free_time_one_fifth = self.calculate_free_time(proportion=0.2)
        free_time_one_third = self.calculate_free_time(proportion=0.33)
        self.show_free_time(free_time_one_fifth, free_time_one_third)
