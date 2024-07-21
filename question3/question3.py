#Hi, I wrote this code by python lang

txt = input('enter your text pls : ')

words = []
txt_without_char = ''
characters = []
char_index = []

for i in txt :

    if ord(i) < 65 or 90 < ord(i) < 97 or ord(i) > 122 :            # Separate non-alphabetic characters and their indices
        characters.append(i)
        char_index.append(txt.index(i))


# Split text by non-alphabetic characters and reverse alphabetic parts
for i in range(len(characters)) :
    new = txt.split(characters[i])
    words.append(new[0])

    if i==len(characters)-1 :
        words.append(new[1])

    txt = new[1]


for i in range(len(words)) :            # Concatenate all parts to form words
    for j in words[i] :
        txt_without_char += j


reversed_txt = txt_without_char[::-1]           # Reverse the entire concatenated string

list_of_alphabetic = []         # Prepare a list for final output


for i in reversed_txt :
    list_of_alphabetic.append(i)


for i in range(len(characters)) :           # Insert non-alphabetic characters back into their original positions
    list_of_alphabetic.insert(char_index[i] , characters[i])

final_result = ''

for i in list_of_alphabetic :           # Convert the list to a final string
    final_result+= i

print(final_result)

