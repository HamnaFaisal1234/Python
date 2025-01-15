list=[65 , 5, 32 , 9 , 20]
def order(lst):
    for i in range (len(lst)-1):
        for j in range (i +1,len(lst)):
            if lst [i] > lst [j]:
                lst [i] , lst [j] = lst [j] , lst [i]
                return lst
sorted=order(list)
print("ascending_order",sorted)
