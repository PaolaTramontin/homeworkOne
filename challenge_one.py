def sum_to(n):
    total = []
    for i in range(n+1):
        total.append(i)
        finalTotal = sum(total)
    return finalTotal
           

print(sum_to(10))