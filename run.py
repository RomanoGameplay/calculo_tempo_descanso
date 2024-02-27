import os
import click
from execute import execute_freetime_class


@click.command()
@click.argument(
    'time',
    type=click.STRING
)
def executa_calculo(time: str) -> None:
    """
    Executa o processo de cálculo do tempo de descanso.

    :param time: tempo de uma sessão de estudo.
    """

    hours = tuple([int(x) for x in time.split(':')])

    if (hours[1] > 59) or (hours[2] > 59):
        print('<<ERRO!!!>>')
        print(f'<< formato incorreto! {time} >>\n\t<< Os minutos ou segundos devem estar abaixo de 60! >>')
    else:
        click.echo(f'Tempo estudado: {time}')
        execute_freetime_class(hours)


if __name__ == '__main__':
    """Exemplo:
            Linha de comando - python run.py 00:34:14"""
    os.system('cls')
    executa_calculo()
