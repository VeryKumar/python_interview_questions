# So an important aspect of data science, ML and LLMS is data purity

#We wanna make sure our model is getting valid datapoints
# HOw weould we go about data cleaning? If we used the example that you had, it would look something like this

# Object,Username,Password,Status
# Object 1,ayo,Family,Good
# Object 2,str8,up,Bad
# Object 3,forreal,Yessir,Good

# Object 1 should not appear in the final output since its missing the password field.
# Another more advanced step that you could take is if the data isn't within certain parameters, but that would be more like a challenge mode

# Alternativly how would you handle extra fields? Like if the CSV was malformed, and looked like this

# Object 1,ayo,Family,Good,Bad
# Object 2, str8,up,Bad
# Object 3, fooreal, Yessir, Good
# Here the Object 1 would be excluded because it has 5 fields instead of 4.

# ANSWER: It seems like the challenge is to deal with data that does not match our initial Object structure (as defined in the column titles). This sounds like it could be solved by adding a data validation step.

# This step could either be added
#   - before creating our datafield object.
#   - during the creation of our datafield object. 
#   - after the creation of our datafield object.

# Here are some pros and cons of doing each:
#   - before creating our datafield object.
#       + discrete step would be easier to debug (decoupled from our object creation)
#       + no undoing of work that has already been done
#       - may add duplicate code
#   - during the creation of our datafield object.
#       + could utilize majority of already written code
#       + seems like better time / space complexity could be achieved. (Have variables tracking structure + loops that interact with that structure)
#       - more tightly coupled
#   - after the creation of our datafield object.
#       + simplest to implement
#       - least time / space / work done efficient

# I think I'd like to try and implement doing a discrete step beforehand, that can be run once on the data to validate its shape and content.

# TEST DATA:
# Object,Username,Password,Status
# Object 1,ayo,Family,Good,Bad
# Object 2, str8,up,Bad
# Object 3, fooreal, Yessir, Good

def join_characters_into_words(string) -> list:
    # Object 1,ayo,Family,Good => 'O','b','j','e','c','t'
    words = []
    current_word = ''
    for char in string:
        if char != ',' and char != '\n':
            current_word += char
        else:
            words.append(current_word)
            current_word = ''
    if current_word:
        words.append(current_word)
    print(31,words)
    return words

def split_words_into_characters(arr) -> str:
    characters = ''
    for word in arr[:-2]:
        # print(word)
        # print(type(word))
        characters += ','
    characters += arr[-1]
    characters += '\n'
    return characters

def CSV_cleaner(csv_path: 'str') -> 'csv':
    csv = open(csv_path)
    cleaned_csv_array = []
    valid_num_cols = 0
    for idx, line in enumerate(csv):
        if idx == 0:
            column_titles = join_characters_into_words(line)
            valid_num_cols = len(column_titles)
            cleaned_csv_array.append(column_titles)
        else:
            object_list = join_characters_into_words(line)
            if(len(object_list)) == valid_num_cols:
                print(84,object_list)
                cleaned_csv_array.append(object_list)
    with open('test_objects_cleaned', "w") as file:
        for row in cleaned_csv_array:
            csv_row = ','.join([str(element) for element in row])
            file.write(csv_row + '\n')
    print("cleaning done")
CSV_cleaner('test_objects_2.csv')

# Questions:
# if we are thinking of dealing with an extremely long CSV, we should consider the limit of space inside of python objects such as array / dict. The max size of a python array is 536,870,912
# if we need speed, writing to disk can be quite slow. Instead building up an in memory data structure and writing once would be much faster. This affects the size of the in memory structure we wish to build before we write. 

# Python lessons: 
#   Does ''.split() split arrays of string? no. 