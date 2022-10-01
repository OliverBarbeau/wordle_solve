from solve_on_answer import solve_on_answer
from get_word_list import get_word_list
answers_to_test_version = "wordle_solution_history"
opening_guess = "crane"
possible_words_list_version = "words_10"
answer_list = get_word_list(answers_to_test_version)
score_sum = 0
guess_scores = []
losses = 0
for answer in answer_list:
    #print("puzzle answer is :", answer)
    guess_score = len(solve_on_answer(possible_words_list_version, opening_guess, answer))
    try:
        guess_score = int(guess_score)
        guess_scores.append(guess_score)
        score_sum += guess_score
    except ValueError:
        pass
    #if int(guess_score) guess_scores.append(guess_score)
    if guess_score == "X" or guess_score >= 7:
        losses += 1
    print(answer, guess_score)
mean_score = score_sum / len(guess_scores)
print("Mean Score:", mean_score)
print("Losses:", losses)
