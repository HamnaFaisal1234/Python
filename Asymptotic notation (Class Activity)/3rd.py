def Time(n):
    iteration=0
    for i in range(0,n):
      for j in range(0,n):
         print("*" , end = "" )
      iteration = iteration+3
      print("")
    print("when n is",n ,"Iteration = " , iteration , "\n" )
Time(3)
Time(5)
Time(7)