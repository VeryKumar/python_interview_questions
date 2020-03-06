str = "ABCD"
rev_str = []
index = len(str)
while index > 0:
    rev_str += str[index - 1]
    index -= 1
print(rev_str)
