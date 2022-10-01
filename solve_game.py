from get_word_list import get_word_list
from print_list import print_list
from filter_word_universe import filter_word_universe

def solve_game():
    possible_words = get_word_list()
    print('number of words is:', len(possible_words))

    # user loop to help with playing a round of the game, enter guess results they recieve from wordle.
    solve_loop = True
    guess_count = 0
    print("Grey -> 0\nGreen -> 1\nYellow -> 2\n")

    while solve_loop:
        
        print("Suggested guesses:")
        print_list(possible_words, 10)
        # USER MANUALLY ENTERS GUESS RESULT FROM WORDLE GAME
        guess_result = []
        letters_entered = 0

        
        correct_user_input = False
        while (not correct_user_input):
            guess_word = input("Enter the word you played:\n").lower()
            guess_result_codes = input("Enter the result codes of the word you played: (ex. '10200')\n")
            if guess_result_codes == 'q' or guess_word == 'q':
                correct_user_input = True
                solve_loop = False
                break
            try:
                guess_result = [(guess_word[i], int(guess_result_codes[i])) for i in range(5)]
                correct_user_input = True
            except Exception:
                print("Error: Incorrect user input")
        if guess_result_codes == "11111":
            print("Oh. you won!")
            solve_loop = False
            break  

        

        print("guess result is: ", guess_result)

        possible_words = filter_word_universe(possible_words, guess_result)

        guess_count += 1
        if guess_count > 6: solve_loop = False
solve_game()

