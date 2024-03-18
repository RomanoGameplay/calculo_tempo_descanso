Algoritmo para cálculo do tempo de descanso, ou tempo livre, após uma sessão de estudo personalizada e contagem de cronômetro.

Seu uso se faz através da linha de comando, explicitada no arquivo run.py, junto com a formatação adequada para a entrada dos dados

Permite lhe informar o tempo de descanso informando apenas o número de minutos estudados ou por meio de formatação do tipo hh:mm:ss.

1. Exemplo de uso do programa informando tempo formatado, por meio do temrinal de comando:

INPUT

```
python run.py calculate-freetime 01:34:45
```

OUTPUT

```
Tempo estudado: 01:34:45
        Se optar por usar 1/5 do tempo de estudo, então seu tempo de descanso será 00:18:57!
        Se optar por usar 1/3 do tempo de estudo, então seu tempo de descanso será 00:31:16!
        Caso queira estender o tempo até 1/3 do tempo, então adicione 00:12:19 ao tempo de descanso!
```

2. Exemplo de uso do programa informando número de minutos estudados, por meio do temrinal de comando:

INPUT

```
python run.py calculate-freetime 123
```

OUTPUT

```
Tempo estudado: 123 minutos
        Se optar por usar 1/5 do tempo de estudo, então seu tempo de descanso será 00:24:36!
        Se optar por usar 1/3 do tempo de estudo, então seu tempo de descanso será 00:40:35!
        Caso queira estender o tempo até 1/3 do tempo, então adicione 00:15:59 ao tempo de descanso!
```

---
Outra funcionalidade existente é um cronômetro que pode ser pausado e despausado pressionando a tecla "ctrl+space"
Para encerrar a contagem do cronômetro basta pressionar a tecla "ctrl+q". Após isso, o cálculo do tempo de descanso é feito 
automaticamente, mostrando uma saída semelhante aos exemplos anteriores.

Exemplo de uso da funcionalidade do cronômetro, via terminal:

INPUT
```
python run.py start-cronometer
```
Quando o comando é executado no terminal, aparece a mensagem:
```
        Cronômetro rodando...
```
Caso queira pausar o cronômetro, basta pressionar a tecla "ctrl+space" e o tempo do cronômetro será
mostrado e caso queira recomeçar a contagem, basta clicar na tecla "ctrl+space" novamente:
```
        Cronômetro Pausado... # Mensagem é mostrada após pressionar "ctrl+space"
        00:01:36 # tempo corrido até a pausa do cronômetro

        Continuando contagem do cronômetro... # Recomeça contagem do cronômetro
```
E então, ao pressionar a tecla "ctrl+q", o cálculo do tempo de descanso é feito a partir do tempo total 
mostrado no cronômetro.

OUTPUT
```
        # Resultado após pressionar a tecla "ctrl+q"
Tempo estudado: 00:06:24
        Se optar por usar 1/5 do tempo de estudo, então seu tempo de descanso será 00:01:17!
        Se optar por usar 1/3 do tempo de estudo, então seu tempo de descanso será 00:02:07!
        Caso queira estender o tempo até 1/3 do tempo, então adicione 00:00:50 ao tempo de descanso!
```
---
NOVA FUNCIONALIDADE:

Agora, é possível usar o tempo de descanso calculado para iniciar um temporizador através do terminal,
e ao final do temporizador será emitido um som contínuo de "Beep". Pressione "ctrl+q" para encerrar o som

A inserção do tempo no temporizador não é manual, por isso, a entrada do tempo é idêntico ao comando para calcular 
o tempo de descanso, ou seja, pode ser entradas do tipo HH:MM:SS ou inserindo apenas o número de minutos de descanso 
("10", por exemplo). 

Existe também a opção de pausar ou encerrar o temporizador usando os mesmos atalhos que no cronômetro
, ou seja, por meio do "ctrl+space" para pausar e "ctrl+q" para encerrar a contagem.

Exemplo de uso da funcionalidade do temporizador, via terminal:

INPUT
```
python run.py start-temporizer 00:10:23
```

OUPUT
```
    Temporizador: 00:10:16 # O tempo vai diminuindo até chegar ao zero.

```

INPUT
```
python run.py start-temporizer 13
```

OUTPUT
```
    Temporizador: 00:12:42 # Acontece a mesma coisa que na saída do exemplo acima.

```
