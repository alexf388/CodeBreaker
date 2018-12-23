import util.utilityfunctions as util


class TestAlgorithmGame:
    # number_of_pegs is the the set of numbers from 1 to N
    # number_of_holes is the number of pegs a player must guess
    # random_code calls generate_random_code() to generate a possible permutation
    # (e.g. if number_of_pegs is 6, and number_of_holes is 4, then a possible random_code could be: [1, 2, 5, 6])
    def __init__(self, number_of_pegs, number_of_holes):
        self.number_of_pegs = int(number_of_pegs)
        self.number_of_holes = int(number_of_holes)
        self.random_code = util.generate_random_code(self.number_of_holes, self.number_of_pegs)
        self.is_solved = False
