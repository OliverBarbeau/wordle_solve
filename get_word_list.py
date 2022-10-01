
import csv

#possible_words is the current universe of words
def get_word_list(word_list_filename="words_10", length_limit= 50000):
    words = []
    with open("word-lists\\" + str(word_list_filename) + '.csv', 'r') as word_list_file:
        reader = csv.reader(word_list_file)
        line_count = 0
        for row in reader:
            if line_count > length_limit:
                break
            if line_count != 0:
                words.append(row[0])
            line_count += 1
    return words