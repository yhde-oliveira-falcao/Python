def solution(matrix):
    total = 0
    rows = len(matrix)
    cols = len(matrix[0])
    
    for col in range(cols):
        for row in range(rows):
            if matrix[row][col] == 0:
                break  # stop counting in this column
            total += matrix[row][col]
    
    return total

# Example usage:
matrix = [[0,1,1,2],
          [0,5,0,0],
          [2,0,3,3]]

print(solution(matrix))  # Output: 9
