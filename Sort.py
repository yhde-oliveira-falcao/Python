
def sort(lst):

    less = []
    equal = []
    greater = []

    if len(lst) > 1:
        pivot = lst[0]
        for x in lst:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater) 
    else:  
        return lst

lst = [7,9,8,5,3,12,100,0]
print(sort(lst))

lst = list(input("Enter some numbers (seperate with comma): ").split(","))
lst = [int(x) for x in lst]
print(sort(lst))


