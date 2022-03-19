print("This is Text to morse code converter")

morsecode_list = ['· –', '– · · ·', '– · – ·', '– · ·', '·', '· · – ·', '– – ·', '· · · ·', '· ·', '· – – –', '– · –',
                  '· – · ·', '– –', '– ·', '– – –', '· – – ·', '– – · –', '	· – ·', '· · ·', '–', '	· · –', '· · · –',
                  '· – –', '– · · –', '– · – –', '– – · ·', '· – · – · –', '– – · · – –']
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', '.', ',']
converted_string = ""

# print(len(morsecode_list))
# print(len(letter_list))
def text_to_morse(text):
    global converted_string
    for letter in text:
        if letter == ' ':
            converted_string += letter
        else:
            index = letter_list.index(letter)
            morsecode = morsecode_list[index]
            converted_string += morsecode
    print(converted_string)


text = input("enter the text to convert \n").lower()
text_to_morse(text)
# def morse_to_text(text):
#     global converted_string
#     for code in text:
#         if code == ' ':
#             converted_string += code
#         else:
#             index = morsecode_list.index(code)
#             code = letter_list[index]
#             converted_string += code
#     print(converted_string)


# conversiontype = input("choose your conversion type. texttomorse / morsetotext ").lower()

# if conversiontype == 'texttomorse':
#     text = input("enter the text to convert \n").lower()
#     text_to_morse(text)
# else:
#     text = input("enter the text to convert \n").lower()
#     morse_to_text(text)




