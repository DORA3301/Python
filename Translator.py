# Translation where vowels are changed with certain letter/s

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "Z"
            else:
                translation = translation + "z"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter your phrase: ")))

