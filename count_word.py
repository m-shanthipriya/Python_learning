count_words = "Print print the original string and the count of words"


def word_count(count_words):
    set_content = count_words.lower().split()
    set_dict = {}
    for count_of_the_total_words in set_content:
        set_dict[count_of_the_total_words] = set_content.count(count_of_the_total_words)
    print(set_dict)


word_count(count_words)