git@github.com:fransay/ShanyCodex.git

def numberSum(n:int):
    count, summ = 0 , 0
    while count < n:
        count += 1
        summ += count
    return "sum ==> ",summ

print(numberSum(5))