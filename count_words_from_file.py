count_words_file = open('/Users/shanthipriya/Desktop/learn/example-01.txt', 'r').read()


def word_count(count_words_file):
    set_content = count_words_file.lower().split()  # split the words
    set_dict = {}
    for count_of_the_total_words in set_content:
        set_dict[count_of_the_total_words] = set_content.count(count_of_the_total_words)
    print(set_dict)


word_count(count_words_file)
