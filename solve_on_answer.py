from get_word_list import get_word_list
from print_list import print_list
from filter_word_universe import filter_word_universe
from compare_guess_to_answer import compare_guess_to_answer


# guess = "label"
# answer = "smalt"

# print(compare_guess_to_answer(guess, answer))

# sample = "thhis is a string"
# sample = sample.replace("h", "", 1)
# print(sample.find("x"))
def solve_on_answer(word_list_version="words_10", answer="crane", opening_guess=None):

    word_test_loop = True
    guess_count = 0
    guesses = []
    possible_words = get_word_list(word_list_version)
    while word_test_loop:
        #print("guesses made: ", guess_count)
        #print("making a new guess...")
        guess_result = []
        letters_entered = 0

        #get the guess
        try:
            guess_word = possible_words[0]
            guesses += [guess_word]
        except IndexError:
            print("guesses:", guess_count)
            print("Index Error, out of possible words perhaps.")
            break
        if opening_guess is None:
            opening_guess = possible_words[0]
        if guess_count == 0:
            guess_word = opening_guess
        #print(" guess word is: ", guess_word)
        #get result of word based on 
        guess_result_codes = compare_guess_to_answer(guess_word, answer)
        guess_result = [(guess_word[i], int(guess_result_codes[i])) for i in range(5)]
        guess_result_string = "".join(guess_result_codes)
        #print("result code is: ", guess_result_string)
        if guess_result_string == "11111" or len(possible_words) == 0:
            guess_count += 1

            if guess_count > 6:
                guess_count = "X"
            word_test_loop = False
            break

        #print("guess result is: ", guess_result)

        possible_words = filter_word_universe(possible_words, guess_result)

        guess_count += 1
        if guess_count > 6: word_test_loop = False
    return guesses


# def main():
#     word_list_version = "10"
#     word_list_version = "words_"+str(word_list_version)
#     opening_guess = "about"
#     print("word list v.", word_list_version)
#     answer = input("\nEnter Answer word: ")
#     main_loop = True
#     while main_loop:
#         guess_score = test_on_answer(word_list_version, opening_guess, answer)
#         print("Test Complete in  ", guess_score, "  guesses.")
#         answer = input("Enter another word: ")
#         if answer == "":
#             break
# main()