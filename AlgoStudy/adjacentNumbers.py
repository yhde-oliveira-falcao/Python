#returns the highest product of the adjacent numbers
#example input: [3,6,-2,-5,7,3]; output: 21

ArrayInput = [3, 6, -2, -5, 7, 3]
#print(len(ArrayInput))

def solution(ArrayInput):
    highest = float('-inf')
    for i in range(len(ArrayInput) - 1):
        var = ArrayInput[i] * ArrayInput[i + 1]
        if var > highest:
            highest = var

    return highest

print(solution(ArrayInput))