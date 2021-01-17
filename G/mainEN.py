import spacy

nlp = spacy.load('en_core_web_sm')

sentence = input("Input sentence: ")

doc = nlp(sentence)

is_command = False
right_after_command = False
command = ""
obj = ""

for token in doc:
    print(token.text, token.pos_, token.tag_)
    if token.pos_ == "VERB" and token.tag_ == "VB":
        is_command = True
        command = command + token.text
        right_after_command = True

    elif right_after_command is True and token.pos_ == "ADP":
        command = command + " " + token.text
        right_after_command = False

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
