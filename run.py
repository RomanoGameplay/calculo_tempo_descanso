import os
import click
from src.Timer.execute import execute_freetime_class, execute_cronometer, execute_temporizer, execute_beep
from src.info import transform_input_time


@click.group()
def time():
    pass


@time.command()
@click.argument(
    'time',
    type=click.STRING
)
def start_temporizer(time: str) -> None:
    """
    Inicia o Temporizador

    :param time: Tempo de descanso
    """

    try:
        hours = transform_input_time(time)
        execute_temporizer(hours)
        execute_beep()
    except KeyboardInterrupt:
        pass


@time.command()
def start_cronometer() -> None:
    """
    Inicia contagem do cronômetro
    """

    cronometer = execute_cronometer()
    comando = f'python run.py calculate-freetime {cronometer}'
    os.system(comando)


@time.command()
@click.argument(
    'time',
    type=click.STRING
)
def calculate_freetime(time: str) -> None:
    """
    Calcula o tempo de descanso.

    :param time: tempo de uma sessão de estudo.
    """

    try:
        hours = transform_input_time(time)
        execute_freetime_class(hours)
    except ValueError:
        print(f'\tFormato inadequado: ({time})\n')


if __name__ == '__main__':
    """
    Exemplo:
        Cálculo do tempo de descanso:
            -> Linha de comando - python run.py calculate-freetime 00:34:14
            ou
            -> Linha de comando - python run.py calculate-freetime 123
    
        Início de contagem do cronômetro:
            -> Linha de comando - python run.py start-cronometer
        
        Início de contagem do temporizador:
            -> Linha de comando - python run.py start-temporizer 00:34:14
            ou
            -> Linha de comando - python run.py start-temporizer 123
    """

    os.system('cls')
    time()
