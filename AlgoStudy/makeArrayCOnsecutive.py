#this is a sorting question.
#If we have the array = [6,2,3,8], first we need to sort it
#then also return the numbers that are missing: 4,5 and 7.

array = [6,2,3,8,1,8,9,7,9,0,1]

def solution(array):
    #first sort it
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    #print(array)
    # now calculate the missing ones
    i=0
    while i < len(array) -1:
        difference = array[i+1] - array[i]
        if difference > 1: #if there is a gap
            item_to_insert = array[i] + 1
            array.insert(i+1, item_to_insert)

        else:
            i+=1
        print(array)
    print(array)
solution(array)