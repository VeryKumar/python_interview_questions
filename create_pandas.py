# For this particular question we can assume that the data is structured in a file like so:

# Object 1: attribute1, attribute2
# Object 2: attribute

# So each object could have any number of attributes, but we can assume that every object in the CSV file is guaranteed to be in identical structure.

# The objects are guaranteed to have the same structure, but could have any number of attributes


# Create a parent object, with the right children
# df = {Object1:
    #   {Object: Object1, Username: ayo, Password: Family, Status: Good}
    # }

# df[Object1][Username] ## ayo
# df[Object1] ## {Object: Object1}

def join_characters_into_words(string):
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


csv = open("test_objects.csv")

df = {}
object_structure = {}
for idx, line in enumerate(csv):
    # print('line',line)
    word = ''
    if idx == 0:
        for char in line:
            if char.isalnum():
                word += char
                # print('30',word)
            else:
                object_structure[word] = None
                word = ''
    else:
        words = join_characters_into_words(line)
        if words:
            object_title = words[0]
            df[object_title]=object_structure.copy()
            column_titles=list(object_structure.keys())
            for i, word in enumerate(words):
                df[object_title][column_titles[i]] = word
print(df["Object 1"]["Username"]) # gives ayo
print(df["Object 2"]) # gives {'Object': 'Object 2', 'Username': 'str8', 'Password': 'up', 'Status': 'Bad'}
print(df['Object 3']) # gives {'Object': 'Object 3', 'Username': 'forreal', 'Password': 'Yessir', 'Status': 'Good'}



