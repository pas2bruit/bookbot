def numberOfWords(text):
    words = text.split()
    totalWords = 0
    for i in words:
        totalWords += 1
    return totalWords


def numberOfEachCharacter(text):
    character_list = {}
    for i in text:
        i = i.lower()
        if i in character_list:
            character_list[i] += 1
        elif i.isalpha():
            character_list[i] = 1
    return character_list


def sort_on(dict):
    return dict["times"]


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        nWord = numberOfWords(file_contents)
        nChar = numberOfEachCharacter(file_contents)
        charList = []

        for i in nChar:
            charList.append({"letter": i, "times": nChar[i]})

        charList.sort(reverse=True, key=sort_on)

        print(f"--- Begin report of {f.name} ---")
        print(f"{nWord} words found in the document\n")

        for i in charList:
            print(f"The '{i["letter"]}' character was found {i["times"]} times")

        print("--- End report ---")


main()
