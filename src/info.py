import sys


def transform_input_time(time: str) -> tuple:
    """
    Faz tratamento do tempo para um formato apropriado

    :param time: Tempo em string

    :return: Tupla com o tempo formatado para inteiro
    """

    if time.isdigit():
        minutes = int(time)
        hour = minutes // 60
        minutes -= (hour * 60)
        hours = tuple([hour, minutes, 0])
        print(f'Tempo estudado: {time} ' + ('minuto' if int(time) <= 1 else 'minutos'),
              end=' ou tempo estudado: {:02d}:{:02d}:00\n'.format(hour, minutes))
    else:
        try:
            hours = tuple([int(x) for x in time.split(':')])
            if len(hours) != 3:
                raise ValueError

            if (hours[1] > 59) or (hours[2] > 59):
                print('\t<<ERRO!!!>>')
                print('\n\t\t<< Os minutos ou segundos devem estar abaixo de 60! >>\n')
                raise ValueError

        except ValueError:
            raise ValueError
        else:
            print(f'Tempo estudado: {time}')

    return hours


def show_time(hour: int, minute: int, second: int, msg: str) -> None:
    """
    Mostra o tempo formatado

    :param hour: horas
    :param minute: minutos
    :param second: segundos
    """

    sys.stdout.write("\r")
    sys.stdout.write("\033[K")
    sys.stdout.write('\t{}: {:02d}:{:02d}:{:02d}'.format(msg, hour, minute, second))
    sys.stdout.flush()
