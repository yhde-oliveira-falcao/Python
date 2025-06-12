from itertools import count

sequence = [1,3,2,1]
#this question needs to return if, by dropping one of the elements of the array, the array becomes strictly increasing. (In this case it should drop 2 elements, so returns false)

def solution(sequence):
    counter = 0
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i-1]:
            counter +=1
            if counter > 1:
                return  False
            if i > 1 and i + 1 < len(sequence):
                if sequence[i] <= sequence[i - 2] and sequence[i + 1] <= sequence[i - 1]:
                    return False

        return True
        #new_sequence = sequence[:i] + sequence[i+1:]



print(solution(sequence))
