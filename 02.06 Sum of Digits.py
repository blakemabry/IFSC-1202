def getSum(n):
     
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)
   
n = 14
print(getSum(n))