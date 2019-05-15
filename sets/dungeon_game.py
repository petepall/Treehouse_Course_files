import random
import os


CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
         ]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_location():
    return random.sample(CELLS, 3)


def move_player(player, move):
    x, y = player
    if move == "LEFT":
        x -= 1
    elif move == "RIGHT":
        x += 1
    elif move == "UP":
        y -= 1
    elif move == "DOWN":
        y += 1

    return x, y


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]

    x, y = player
    if x == 0:
        moves.remove("LEFT")
    elif x == 4:
        moves.remove("RIGHT")
    elif y == 0:
        moves.remove("UP")
    elif y == 4:
        moves.remove("DOWN")

    return moves


def main():
    # TODO: draw grid
    # TODO: draw the player in the grid
    # TODO: check for win/loss
    # TODO: clear screen and redraw the gird

    monster, door, player = get_location()

    while True:
        clear_screen()
        valid_moves = get_moves(player)
        print("Welcome to the dungeon!")
        print(f"You're currently in room {player}")
        print(f"You can move {', '.join(valid_moves)}")

        move = input("> ").upper()

        if move == "QUIT":
            break
        if move in valid_moves:
            player = move_player(player, move)
        else:
            print("\n ** Walls are hard! Don't run into them! **\n")

        # TODO: Good move? Change the player position
        # TODO: Bad move? Don't change anything!
        # TODO: On the door? They win!
        # TODO: On the monster? They lose!
        # TODO: Otherwise, loop back around


if __name__ == "__main__":
    main()
