def bpe(how_many_elements, input_text):

    dictionary = {}
    bigrams = {}
    previous_chosen = list()

    for i in range(0, len(input_text)):
        bigram = input_text[i]
        value = dictionary.setdefault(bigram, 0)
        dictionary[bigram] = value + 1


    while len(dictionary) < int(how_many_elements):
        for e in dictionary:
            index = 0
            indexes = set()

            while index != -1:
                index = input_text.find(e, index)
                if index != -1:
                    indexes.add(index)
                    index = index + 1

            for i in indexes:
                if (i + len(e)) < len(input_text):
                    bigram = input_text[i:(i + len(e) + 1)]
                    value = bigrams.setdefault(bigram, 0)
                    bigrams[bigram] = value + 1

        left_index = len(input_text)
        max_value = max(bigrams.values())
        biggest_bigrams = list()

        while not biggest_bigrams:
            for key, value in bigrams.items():
                if value == max_value and key not in previous_chosen:
                    biggest_bigrams.append(key)
            if not biggest_bigrams:
                max_value = max_value - 1

        for key in biggest_bigrams:
            if key not in previous_chosen:
                if left_index > input_text.find(key):
                    left_index = input_text.find(key)
                    new_bigram = key
        dictionary[new_bigram] = max_value
        previous_chosen.append(new_bigram)

        bigrams.clear()

    return dictionary



how_many_elements = int(input("How many elements: "))
input_text = input("Put text: ")
print(bpe(how_many_elements, input_text))