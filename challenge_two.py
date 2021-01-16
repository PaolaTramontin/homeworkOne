def largest(list):
    nums = []
    numsMax = []
    for i in list:
        nums.append(i)
    numsMax.append(max(nums))
    print(numsMax)           
        

largest([10, 4, 2, 231, 500, 54])