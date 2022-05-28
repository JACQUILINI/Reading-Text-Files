# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



def read_file_content(filename):

    # [assignment] Add your code here 

    with open(filename) as t:
        content = t.readline()
    
    return content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    splited = text.split()
    print(splited)

    for i in set(splited):
        print("{} : {}" .format ( i,   splited.count(i)))

count_words()
# I do not feel satisfied with this task and i hope i could get correction on how best it can be. Thanks