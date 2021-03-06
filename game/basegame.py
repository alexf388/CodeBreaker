import util.utilityfunctions as util


class BaseGame:
    # number_of_pegs is the the set of numbers from 1 to N
    # number_of_holes is the number of pegs a player must guess
    # random_code calls generate_random_code() to generate a possible permutation
    # (e.g. if number_of_pegs is 6, and number_of_holes is 4, then a possible random_code could be: [1, 2, 5, 6])
    def __init__(self, number_of_pegs, number_of_holes):
        self.number_of_pegs = int(number_of_pegs)
        self.number_of_holes = int(number_of_holes)
        self.random_code = util.generate_random_code(self.number_of_holes, self.number_of_pegs)
        self.is_solved = False

    # play game function, acts sort of main function here
    def play_game(self):
        print("Guess should be entered with numbers separated by comma")
        print("e.g. for number_of_pegs = 1,2,3,4")

        while not self.is_solved:
            user_guess_str = str(input("Please input your guess: "))

            if self.validate_input(user_guess_str):
                # convert user_guess_str to array
                user_guess_split_array = user_guess_str.split(",")
                result_array = util.check_guess_with_random_code(user_guess_split_array, self.random_code)

                if util.validate_result_array(result_array):
                    self.is_solved = True
                    print("Congratulations! You broke the code!")
                else:
                    print("Following results: " + str(result_array))

            else:
                print("Please enter an appropriate guess")

    # validates input of user_guess_str
    def validate_input(self, user_guess_str):
        input_validated = True

        if user_guess_str:
            number_of_commas = user_guess_str.count(",", 0, len(user_guess_str))

            if number_of_commas is self.number_of_holes - 1:
                number_split_array = user_guess_str.split(",")

                for i in range(len(number_split_array)):
                    if 1 > int(number_split_array[i]):
                        input_validated = False
                        print("integer " + str(number_split_array[i]) + " at position " + str(i) + " was smaller than 1")
                    elif int(number_split_array[i]) > self.number_of_pegs:
                        input_validated = False
                        print("integer " + str(number_split_array[i]) + " at position " + str(i) + " was bigger than " + str(self.number_of_pegs))

            else:
                input_validated = False
                print("Only " + str(number_of_commas) + "commmas were found. This did not match with the expectation "
                                                        "of " + str(self.number_of_holes - 1) + " commas")

        else:
            input_validated = False
            print("Your guess was empty. Please enter an appropriate guess.")

        return input_validated
