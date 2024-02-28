import os
import click
from execute import execute_freetime_class


@click.command()
@click.argument(
    'time',
    type=click.STRING
)
def execute_calculate(time: str) -> None:
    """
    Executa o processo de cálculo do tempo de descanso.

    :param time: tempo de uma sessão de estudo.
    """
    if time.isdigit():
        print(f'Tempo estudado: {time} minutos')
        minutes = int(time)
        hour = minutes // 60
        minutes -= (hour * 60)
        hours = (hour, minutes, 0,)
    else:
        hours = tuple([int(x) for x in time.split(':')])
        print(f'Tempo estudado: {time}')

    if (hours[1] > 59) or (hours[2] > 59):
        print('<<ERRO!!!>>')
        print(f'<< formato incorreto! {time} >>\n\t<< Os minutos ou segundos devem estar abaixo de 60! >>')
    else:
        execute_freetime_class(hours)


if __name__ == '__main__':
    """Exemplo:
            Linha de comando - python run.py 00:34:14
            ou
            Linha de comando - python run.py 123"""
    os.system('cls')
    execute_calculate()
