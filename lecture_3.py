# 1

text = input('Enter the text: ')

new_text = ''

for i in range(0, len(text) - 1, 2):
    new_text += text[i + 1] + text[i]

print(new_text)


# 2

text = input('Enter the text for end to end encryption: ')

alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

for i in range(len(text)):
    letter = text[i]
    if letter in alphabet:
        if letter == 'z':
            text[i] = 'a'
        elif letter == 'Z':
            text[i] = 'A'
        else:
            index = alphabet.index(text[i])
            text[i] = alphabet[index + 1]
text = ''.join(text)

print(text)


# 3 (Homework)

# 1

text1 = input('Enter the first text: ')
text2 = input('Enter the second text: ')

to = max(len(text1), len(text2))

new_text = ''
for i in range(to):
    if i < len(text1) and i < len(text2):
        new_text += text1[i] + text2[i]
    elif i < len(text1):
        new_text += '*' + text1[i]
    elif i < len(text2):
        new_text += text2[i] + '*'

print(new_text)

# 2

text = input('Enter the arabian text: ')

new_text = ''

text = text.split(' ')
print(text)

for i in text:
    word = list(i)
    word.reverse()
    new_text += ''.join(word) + ' '

print(new_text)