# UT4-TE2: Objetos y clases

### TAREA EVALUABLE

<img src="https://github.com/sdelquin/pro/blob/main/ut4/te2/images/poker.svg">

## Objetivo

Escriba un programa en Python que permita simular el comportamiento de una partida de cartas de poker modalidad **TEXAS HOLDEM** utilizando técnicas de programación orientada a objetos.

## Propuestas de datos y responsabilidades

### Game

- Datos:
  - Deck
  - Players
  - Dealer
- Responsabilidades:
  - Crear un mazo
  - Crear los jugadores
  - Crear el dealer
  - Comenzar la partida (repartir cartas, buscar mejor combinación)
  - Finalizar la partida (mostrar el ganador y su mano)

### Dealer

- Datos:
  - Mazo
  - Jugadores
- Responsabilidades:
  - Dar cartas a los jugadores
  - Destapar cartas comunes

### Player

- Datos:
  - Nombre
  - 2 cartas propias
  - 5 cartas comunes
- Responsabilidades:
  - Encontrar su mejor combinación de cartas

### Card

- Datos:
  - Número de la carta
  - Palo de la carta
- Responsabilidades:
  - Saber si una carta es menor que otra
  - Representar la carta

### Deck

- Datos:
  - 52 cartas
- Responsabilidades:
  - Dar una carta aleatoria
  - Dar la carta de "arriba"
  - Dar la carta de "abajo"
  - Barajar
  - Ver una carta aleatoria
  - Ver la carta de "arriba"
  - Ver la carta de "abajo"

### Hand

- Datos:
  - 5 cartas
- Responsabilidades:
  - Descubrir la categoría de la mano
  - Asignar una puntuación a la categoría
  - Saber si una mano es mejor que otra (ranking)

## Propuesta de módulos

Propuesta de módulos y clases por módulo:

```
├── main.py
├── game.py
│   └── Game
├── cards.py
│   ├── Card
│   ├── Deck
│   └── Hand
└── roles.py
    ├── Dealer
    └── Player
```

### Módulo helpers

El fichero [helpers.py](./helpers.py) contiene funciones de apoyo al desarrollo del proyecto.

## Referencias

https://en.wikipedia.org/wiki/List_of_poker_hands
