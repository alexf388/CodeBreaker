import random


# generates random code, which is number_of_holes long in an array, with each number randomly from a set of
# 1 to number_of_pegs
# (e.g. if number_of_pegs is 6, and number_of_holes is 4, then a possible random_code could be: [1, 2, 5, 6])
def generate_random_code(number_of_holes, number_of_pegs):
    random_code = []

    for x in range(number_of_holes):
        random_code.append(str(random.randint(1, number_of_pegs)))

    return random_code


# checks the user_guess with random_code
# returns an array of same length of user_guess_str/random_code with values of the following set: Black, White, Empty
# Black means one of the guesses was correct (right number, right position)
# White means one of the guesses was half-correct (right number, wrong position)
# Empty means one of the guesses was incorrect (wrong number, wrong position)
# assumption: user_guess_str has already been validated
def check_guess_with_random_code(user_guess_split_array, random_code):
    result_array = []

    for i in range(len(user_guess_split_array)):
        right_number = False
        right_position = False

        for j in range(len(random_code)):
            if user_guess_split_array[i] == random_code[i]:
                right_number = True
                right_position = True
                break
            elif user_guess_split_array[i] == random_code[j] and i is not j:
                right_number = True
                right_position = False
                break

        if right_number and right_position:
            result_array.append("Black")
        elif right_number:
            result_array.append("White")
        else:
            result_array.append("Empty")

    # TODO: reorganize the result_array by custom sorting order: Black, White, Empty
    result_custom_sorted_array = sorted(result_array, key=custom_sorting_order)

    return result_custom_sorted_array


# this function will sort result_array into the following custom order: Black, White, Empty
# e.g. if the result_array is (White, Black, Black, White), the new order is (Black, Black, White, White)
# e.g. (2) if the result_array is (White, Empty, Empty, White), the new order is (White, White, Empty, Empty)
# the purpose of the function is to mask right numbers with wrong positions, ensuring users will get no further
# information where they can learn the positions of numbers by looking at the result_array
def custom_sorting_order(value):
    if value is "Black":
        return 1
    elif value is "White":
        return 2
    elif value is "Empty":
        return 3
