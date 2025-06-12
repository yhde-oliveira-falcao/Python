matrix = [[0,1,1,2],
          [0,5,0,0],
          [2,0,3,3]] #the output should be 9

#return the total value of the fields where they are NOT under a field that is zero.

def solution(matrix):
    for col in matrix:
        for row in col:

