import os
import click
from execute import execute_freetime_class, execute_cronometer


@click.group()
def time():
    pass


@time.command()
def start_cronometer() -> None:
    """
    python run.py start-cronometer
    Inicia o Cronômetro
    """

    cronometer = execute_cronometer()

    try:
        comando = f'python run.py calculate-freetime {cronometer}'
        os.system(comando)
    except Exception as e:
        print(e)


@time.command()
@click.argument(
    'time',
    type=click.STRING
)
def calculate_freetime(time: str) -> None:
    """
    Executa o processo de cálculo do tempo de descanso.

    :param time: tempo de uma sessão de estudo.
    """

    if time.isdigit():
        print(f'Tempo estudado: {time} ' + ('minuto' if int(time) <= 1 else 'minutos'))
        minutes = int(time)
        hour = minutes // 60
        minutes -= (hour * 60)
        hours = (hour, minutes, 0,)
        print('ou\nTempo estudado: {:02d}:{:02d}:00'.format(hour, minutes))
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
        Cálculo do tempo de descanso:
            -> Linha de comando - python run.py time calculate-freetime 00:34:14
            ou
            -> Linha de comando - python run.py time calculate-freetime 123
    
        Início de contagem do cronômetro:
            -> Linha de comando - python run.py start-cronometer       
    """
    os.system('cls')
    time()
