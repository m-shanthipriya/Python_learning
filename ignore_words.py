count_words = open('/Users/shanthipriya/Desktop/learn/example-01.txt', 'r').read()
# count_words = "Print print the original amber string and the count of words"
words_to_ignore = ["of", "the", "was", "amber", "and"]


def word_count(count_words):
    # This method find the occurrence of words by storing in Dictionary
    set_content = count_words.lower().split()
    set_dict = {}
    for count_of_the_total_words in set_content:
        if count_of_the_total_words not in words_to_ignore:
            set_dict[count_of_the_total_words] = set_content.count(count_of_the_total_words)
    print(set_dict)


word_count(count_words)
