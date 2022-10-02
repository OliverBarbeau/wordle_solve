import re
# data structure for guess results
# list of tuples
# [(w,1), (o,2), (r,0), (s,0), (t,0)]
# [(LETTER, RESULT_CODE), ... (x, 0)]
# List is ordered by user guess result entry sequence

# result_codes_map = {0:"not in word.", 1: "correct.", 2: "in word, not in correct position." }

# Letter Result Codes:
# 0. Letter Not in Word.
# 1. Letter Correct.
# 2. Letter is in word, not in correct position.

# Result Code Actions:
# 0. remove words that contain this letter.
# 1. remove words that do not contain that letter in that position.
# 2. remove words that contain this letter in this position, AND
#    remove words that do not contain this letter.

# GIVE USER SAMPLE FIRST GUESS "audio"
# USER ENTERS FIRST GUESS
# sample_guess_result of "audio"
# sample_guess_result = [('d',2), ('o',1), ('w',0), ('r',0), ('y',0)]

def filter_word_universe(possible_words : list[str], guess_result : list[tuple]):
    letter_position = 0
    for letter, result_code in guess_result:
        # 0. letter not in word
        if result_code == 0:
            #print(letter, ": is not in word here\n")
            # check for multiple occurances
            if ((letter, 2) in guess_result):
                #print("but letter is in guess_result in an incorrect position somewhere")
                pattern = ((letter_position)*".") + letter + ((4-letter_position)*".")
                possible_words = [word for word in possible_words if (re.match(pattern, word) is None)]
            
            elif ((letter, 1) in guess_result):
                #print("but letter is in guess_result in correct position somewhere")
                other_letter_position = guess_result.index((letter, 1))
                pattern = ((other_letter_position)*("[^" + letter + "]")) + letter + ((4-other_letter_position)*("[^" + letter + "]"))
                #print(pattern)
                possible_words = [word for word in possible_words if (re.match(pattern, word) is not None)]
            #remove words that contain this letter
            else:
                possible_words = [word for word in possible_words if letter not in word]
        # 1. letter correct
        elif result_code == 1:
            if guess_result.count((letter,2)) >= 1:
                #print("There is more than one of this letter ")
                possible_words = [word for word in possible_words if word.count(letter) >= 2]
            # remove words that do not contain that letter in that position.
            #print(letter, ": is in word at position: ", letter_position)
            pattern = ((letter_position)*".") + letter + ((4-letter_position)*".")
            # add regex pattern matches
            possible_words = [word for word in possible_words if (re.match(pattern, word) is not None)]
        # 2. letter is in word, not correct position
        elif result_code == 2:
            #print(letter, ": is in word, not in position: ", letter_position)
            possible_words = [word for word in possible_words if letter in word]
            if guess_result.count((letter,2)) > 1:
                #print("There is more than one of this letter ")
                possible_words = [word for word in possible_words if (word.count(letter) >= 2)]
            # remove words that contain this letter in this position
            # remove words that do not contain this letter
            pattern = ((letter_position)*".") + letter + ((4-letter_position)*".")
            possible_words = [word for word in possible_words if (re.match(pattern, word) is None)]  
        letter_position += 1
        #print('number of words is:', len(possible_words))
    # if len(possible_words) > 0:
        
    #     print("top choices:")
    #     print_list(possible_words, 1)
    # else:
    #     print("No choices available")
    return possible_words