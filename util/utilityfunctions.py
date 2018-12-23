import random


# generates random code, which is number_of_holes long in an array, with each number randomly from a set of
# 1 to number_of_pegs
# (e.g. if number_of_pegs is 6, and number_of_holes is 4, then a possible random_code could be: [1, 2, 5, 6])
def generate_random_code(number_of_holes, number_of_pegs):
    random_code = []

    for x in range(number_of_holes):
        random_code.append(random.randint(1, number_of_pegs))

    return random_code


# checks the user_guess with random_code
# returns an array of same length of user_guess_str and random_code containing values of the following set: Black, White, Empty
# Black means one of the guesses was correct (right number, right position)
# White means one of the guesses was half-correct (right number, wrong position)
# Empty means one of the guesses was incorrect (wrong number, wrong position)
# assumption: user_guess_str has already been validated
def check_guess_with_random_code(user_guess_str, random_code):
    result_array = []

    for i in range(len(user_guess_str)):
        right_number = False
        right_position = False

        for j in range(len(random_code)):
            if user_guess_str[i] is random_code[i]:
                right_number = True
                right_position = True
                break
            elif user_guess_str[i] is random_code[j] and i is not j:
                right_number = True
                right_position = False
                break

        if right_number and right_position:
            result_array.append("Black")
        elif right_number:
            result_array.append("White")
        else:
            result_array.append("Empty")

    #TODO: reorganize the result_array by custom sorting order: Black, White, Empty

    return result_array
