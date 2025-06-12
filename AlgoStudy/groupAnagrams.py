strw = ["eat", "tea", "tan", "ate", "nat", "bat"]

def solution(strs):
    anagrams = {}
    result = []
    for word in strs:
        sorted_word = ''.join(sorted(word)) #'' will join each char. The sorted will return as a list ["a", "e", "t"]
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())

    #anagrams = {}
    #for i in range(len(strs)-1):
        #for j in range(len(strs)-1):
print(solution(strw))