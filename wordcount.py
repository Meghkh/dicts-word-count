# put your code here.

def count_words(data_file):
    """ Prints the number of times a word appears in the file.

    """
    word_count = {}
    file_name = open(data_file)
    for line in file_name:
        line = line.rstrip().split(' ')
#        line = line.split(' ')
        for word in line:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    for key, value in word_count.iteritems():
        print key, value

count_words("twain.txt")
