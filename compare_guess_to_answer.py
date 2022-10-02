
def compare_guess_to_answer(guess: str,  answer : str):

    result_code = ['','','','','']
    # first check for correct letters
    # take those letters out of the answer string
    # next check for letters in the guess that are in the word
    #   taking into account that repeat letter may be in the answer word
    for i in range(5):
        if answer[i] == guess[i]:
            # print("found the letter here")
            # print(answer)
            result_code[i] = '1'
            answer = answer.replace(answer[i], " ", 1)
        # print(result_code)
    i = 0
    for i in range(5):
        letter = guess[i]
        # print("letter is:  ", letter)
        if result_code[i] == "1":
            pass
        elif letter in answer:
            result_code[i] = '2'
            # print("its in the word NOT HERE")
        else:
            result_code[i] = '0'
            # print("its NOT in the word")
        if result_code[i] != '1': 
            answer = answer.replace(letter, " ", 1)
        # print("answer is currently: ", answer)
        # print("result code is currently: ", result_code)
        i += 1
    return result_code

# def main():
#     answer = input("enter answer")
#     guess = input("enter guess")
#     print(compare_guess_to_answer(guess=guess, answer=answer))
        
# main()