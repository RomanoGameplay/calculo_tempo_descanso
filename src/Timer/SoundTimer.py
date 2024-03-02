import keyboard
import winsound


class SoundTimer:
    """
    Classe responsável por ativar Beep ao final do tempo de descanso
    """

    key_stop_sound: str

    def __init__(self) -> None:
        """
        Método construtor da classe
        """

        self.key_stop_sound = 'ctrl+q'

    def play_sound(self) -> None:
        """
        Aciona o som Beep, de forma contínua
        """
        print(f'\n\tClique no atalho {self.key_stop_sound} para parar o som!\n')
        while True:
            if keyboard.is_pressed(self.key_stop_sound):
                break

            winsound.Beep(frequency=700, duration=275)

    def run(self):
        """
        Executa o som do Beep
        """

        self.play_sound()
