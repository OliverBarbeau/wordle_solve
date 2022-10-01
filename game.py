from random import randint
from get_word_list import get_word_list
from compare_guess_to_answer import compare_guess_to_answer
from filter_word_universe import filter_word_universe
from print_list import print_list
from solve_on_answer import solve_on_answer
from sys import argv
# 0 -> no debug
# 1 -> reveal number of words left in solution universe
# 2 -> reveal suggetions + 1
# 3 -> reveal answer word + 2

def main():
    inpMsg = "# 0 -> no debug\n# 1 -> letter bank\n# 2 -> reveal number of words left in solution universe + 1\n# 3 -> reveal suggetions + 2\n# 4 -> reveal answer word + 3\nEnter debug level 0-3: "
    DB = 0
    DB = input(inpMsg)
    while(not DB.isnumeric() and (len(DB) != 0)):
        DB = input(inpMsg)
        DB = int(DB)
    if len(DB) == 0:
        DB = 0
    DB = int(DB)
    topOfWordList = 5000
    answerWord = None
    if DB: print(f"Debug mode level: {DB}")
    word_list_filename = "words_10"
    game_loop = True
    while(game_loop):
        gameBoard = []
        lettersOut = set([])
        lettersIn = set([])
        letters = {'a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k' ,'l' ,'m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        guess_count = 0
        userWon = False
        print("Starting Game.")
        wordList = get_word_list(word_list_filename=word_list_filename)
        wordUniverse = wordList
        
        if answerWord is None:
            print("Selecting random Answer Word...")

            print(f"Selecting from top {topOfWordList} of the word list (excluding words ending in 's')")
            answerWord = wordList[randint(0, topOfWordList)]
            
            while (answerWord[4] == 's'):
                answerWord = wordList[randint(0, topOfWordList)]

        if DB > 3: print(f"Answer Word is: {answerWord.upper()}")
        print("...Answer Word selected.")
        while guess_count < 6 and not userWon:
            if DB > 1: print(f"There are {len(wordUniverse)} possible words left.")
            if DB > 2: print(f"Suggested guesses: {wordUniverse[:5]}")
            if DB: 
                if len(lettersIn) > 0:
                    print(f"Letters in the solution: {lettersIn}")
                if len(lettersOut) > 0:
                    print(f"Letters not in the solution: {lettersOut}")
                if len(letters) > 0:
                    print(f"Letters available: {letters}")
            if len(gameBoard): 
                print("")
                print_list(gameBoard)
                print("")   
            userGuess = input(f"\nEnter your word for guess number {guess_count+1}: ").lower()
            if userGuess in wordList:
                gameBoard.append([userGuess[0].upper(), userGuess[1].upper(), userGuess[2].upper(), userGuess[3].upper(), userGuess[4].upper()])
                result = compare_guess_to_answer(userGuess, answerWord)
                gameBoard.append(result)
                guess_result = [(userGuess[i], int(result[i])) for i in range(5)]
                for i, r in guess_result:
                    if r == 0:
                        lettersOut.add(i)
                    else:
                        lettersIn.add(i)
                    try: 
                        letters.remove(i)
                    except KeyError:
                        pass
                wordUniverse = filter_word_universe(wordUniverse, guess_result)
                if result == ['1','1','1','1','1']:
                    userWon = True
                guess_count += 1
            elif userGuess == "q":
                break
            else:
                print("That word is not in the word list")
            if guess_count == 6 or userWon:
                if len(gameBoard): 
                    print("")
                    print_list(gameBoard)
                    print("")
            if userWon:
                print(f"You won in {guess_count} guesses!")
        botGuesses = solve_on_answer(answer=answerWord)
        print(f"I can complete this trial on [{answerWord.upper()}] in {len(botGuesses)} guesses: {botGuesses}")
        game_loop = (input("type 'q' to quit, enter to continue\n") != 'q')
        answerWord = None



if __name__ == '__main__':
    # main(answerWord=answerWord.lower())
    
    main()