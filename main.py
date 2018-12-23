# importing libraries
import sys

# importing custom libraries
from game.basegame import BaseGame
from game.testalgorithmgame import TestAlgorithmGame


# main function
def main():
    print("Hello World! from main function")

    # play mode
    if len(sys.argv) == 3:
        print("Play Mode")
        number_of_pegs = sys.argv[1]
        number_of_holes = sys.argv[2]

        # set up game
        base_game = BaseGame(number_of_pegs, number_of_holes)
        print(base_game.random_code)
        base_game.play_game()

    # testing algorithm mode
    elif len(sys.argv) == 4:
        print("Testing Algorithm Mode")
        number_of_pegs = sys.argv[1]
        number_of_holes = sys.argv[2]
        algorithm_to_use = sys.argv[3]

        # set up game
        base_game = BaseGame(number_of_pegs, number_of_holes)
        print(base_game.random_code)

    else:
        print("This program runs with either 2 program arguments:  [number_of_pegs] [number_of_holes] for playing"
              "or "
              "3 program arguments: [number_of_pegs] [number_of_holes] [algorithm_to_use] for testing algorithms")
        raise ValueError("Invalid arguments. Please refer to the message above.")


if __name__ == "__main__":
    main()
