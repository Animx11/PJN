
def load_dictionary():
    file = open("PoliMorf-0.6.7.tab", "r", encoding='utf-8')
    dictionary = set()

    for line in file:
        t = line.split("\t")
        dictionary.add(t[0])

    file.close()

    return dictionary

def max_match(sentence, dictionary, list):
    sentence = sentence.lower()
    if sentence == "":
        return list
    for i in range(len(sentence), 1, -1):
        firstword = sentence[0:i]
        remainder = sentence[i:]
        if firstword in dictionary:
            list.append(firstword)
            return max_match(remainder, dictionary, list)

    firstword = sentence[0]
    remainder = sentence[1:]
    list.append(firstword)
    return max_match(remainder, dictionary, list)


dictionary = load_dictionary()
list = []
sentence = input()
list = max_match(sentence, dictionary, list)
print(list)
