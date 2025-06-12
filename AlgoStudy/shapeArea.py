#This is a polygon making question...
#the idea: an interesting polygon is a polygon with a side of length 1 and area n.
#Imagine a squares matrix, where a polygon n=1 is a one square in the matrix
#a polygon n=2 is that polygon n=1 and added a square for each of it's rim (top, bottom, left and right)
#the n=3 polygon will add squares to the sides so each side has 3 in total and from center to top (inclusive center) it has 3 squares
#same logic for other polygons
#so the solution for n=3 is 13, the solution for n=2 is 5, and the solution for n=4 is 25
#so solution(n=1)=1, solution(n=2)=5, solution(n=3)=13, solution(n=4)=25
#constraints:1<=n<=10000

def solution(n):
    total = n*n+(n-1)*(n-1)
    print(total)
solution(5)