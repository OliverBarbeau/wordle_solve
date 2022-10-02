import csv
# parse csv file from local directory, where first column is all 5-letter words
def get_word_list(word_list_filename : str ="sorted_5_letter_words", length_limit : int = 50000):
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