import spacy

nlp = spacy.load('pl_core_news_sm')

sentence = input("Input sentence: ")

doc = nlp(sentence)

is_command = False
command = ""
obj = ""

for token in doc:
    print(token.text, token.pos_, token.tag_)
    if token.pos_ == "VERB" and token.tag_ == "IMPT":
        is_command = True
        command = command + token.text

    elif is_command is True:
        if obj == "":
            obj = obj + token.text
        else:
            obj = obj + " " + token.text


if command == "":
    print("END")
else:
    print("Operation: " + command)
    print("Object: " + obj)
