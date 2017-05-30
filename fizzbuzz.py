def CodeFight(n):
    i =  0
    codefight_array= []
    #for i in range(0, len("codefights")): print("codefights"[i], i)
    for i in range(0, n+1):
        codefight_array[i] = "CodeFights"[1:int(i**4%5*4):int(10--i**6%7*5/6)] or str(i)
    for i in range(len(codefight_array)): print(codefight_array[i])
n = 100
CodeFight(n)
