# Asteroids

## About

This is a simple clone of the classic "Asteroids" arcade game, implemented in Python using the pygame library. The purpose of this project is to demonstrate basic game development concepts such as sprite management, collision detection, and simple physics in a 2D environment.

## Requirements

-   [Python 3](https://www.python.org/)
-   [pygame](https://www.pygame.org/) (see [requirements.txt](requirements.txt))

## How to play

### 1. Clone the repository

```sh
git clone <repository-url>
cd asteroids
```

### 2. Set up the environment

It is recommended to use a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Run the game

Linux

```sh
python3 main.py
```

Windows

```sh
python main.py
```

### 5. Controls

-   **W**: Move forward
-   **S**: Move backward
-   **A**: Rotate left
-   **D**: Rotate right
-   **Space**: Shoot

Avoid colliding with asteroids. Shoot them to split or destroy them. The game ends when your ship collides with an asteroid.

Enjoy!
