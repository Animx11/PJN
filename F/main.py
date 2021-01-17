forms_count = {}


def search_for_word(word):
    file = open("PoliMorf-0.6.7.tab", "r", encoding='utf-8')
    search_result = []

    for line in file:
        t = line.split("\t")
        if t[0] == word:
            search_result.append(t)

        form = t[2].split(":")
        value = forms_count.setdefault(form[0], 0)
        forms_count[form[0]] = value + 1

    file.close()
    return search_result


word = input("Wpisz słowo do wyszukania: ")
search_result = search_for_word(word)

result = []
count = 0
for i in search_result:
    if count == 0:
        result = i
        count = forms_count[i[2].split(":")[0]]
    if count < forms_count[i[2].split(":")[0]]:
        result = i

print()
if(result == []):
    print("Nie znaleziono wyrazu w słowniku")
else:
    print(result[1])
    print(result[2])