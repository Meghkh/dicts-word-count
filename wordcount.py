# put your code here.

def count_words(data_file):
    """ Prints the number of times a word appears in the file.

    """
    word_count = {}
    file_name = open(data_file)

    for line in file_name:
        line = line.rstrip().split(' ')
        for word in line:
            if word == "I":
                word_count[word] = word_count.get(word, 0) + 1
            else:
                word_count[word.lower()] = word_count.get(word, 0) + 1

    for key, value in word_count.iteritems():
        print key, value

count_words("test.txt")
