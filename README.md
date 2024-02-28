Algoritmo para cálculo do tempo de descanso, ou tempo livre, após uma sessão de estudo personalizada.

Seu uso se faz através da linha de comando, explicitada no arquivo run.py, junto com a formatação adequada para a entrada dos dados

Permite lhe informar o tempo de descanso informando apenas o número de minutos estudados ou por meio de formatação do tipo hh:mm:ss.

1. Exemplo de uso do programa informando tempo formatado, por meio do temrinal de comando:

INPUT

```
python run.py 01:34:45
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
python run.py 123
```

OUTPUT

```
Tempo estudado: 123 minutos
        Se optar por usar 1/5 do tempo de estudo, então seu tempo de descanso será 00:24:36!
        Se optar por usar 1/3 do tempo de estudo, então seu tempo de descanso será 00:40:35!
        Caso queira estender o tempo até 1/3 do tempo, então adicione 00:15:59 ao tempo de descanso!
```
