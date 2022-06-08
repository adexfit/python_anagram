# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from xmlrpc.client import boolean


def find_anagram(word, anagram):
    # [assignment] Add your code here
    mybool_list1 = []
    mybool_list2 = []
    answer = False
    word1 = []
    word2 = []

    for x in word:
        if x != " ":
            word1.append(x)
    for x in anagram:
        if x != " ":
            word2.append(x)

    if len(word1) != len(word2):
        answer = False

    elif len(word1) == len(word2):
        for x in word1:
            if x in word2 and x.isalpha():
                mybool_list1.append(True)
            else:
                mybool_list1.append(False)
        for x in word2:
            if x in word1 and x.isalpha():
                mybool_list2.append(True)
            else:
                mybool_list2.append(False)
        if False in mybool_list1 or False in mybool_list2:
            answer = False
        else:
            answer = True

    return answer


word = input("Enter first word: ")
anagram = input("Enter second word: ")

find_anagram(word, anagram)

print("The answer has been returned by the function. I would have printed this but we were only asked to return it")
