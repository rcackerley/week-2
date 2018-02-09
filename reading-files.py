file_name = raw_input('What file do you want to read? ')
# file = open(file_name, 'r')

# for line in file:
#     print line

# new_contents = raw_input('What do you want to put into the file? ')

# file = open(file_name, 'a')
# file.write(new_contents)
# file.close()

file = open(file_name, 'r')
letter_histogram = {}
word_histogram = {}
for line in file:
    for letter in line:
        if letter in letter_histogram:
            #print letter
            letter_histogram[letter] += 1
        else:
            letter_histogram[letter] = 1
        if word in word_histogram:
            word_histogram[word] += 1
        else:
            word_histogram[word] = 1

print letter_histogram
print word_histogram
