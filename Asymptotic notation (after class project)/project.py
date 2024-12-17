def myfunction(n):
    
    if n < 0:
        print("Please provide a positive integer.")
        return

    for x in range(0, n+1):  
        print("First loop")
        j = 1
        while j <= n+1:  
            print("Second loop", j)
            j = j * 2
            for y in range(0, 100):  
                print("Third loop")


myfunction(1)
