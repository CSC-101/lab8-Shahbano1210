# part 1

def groups_of_3(nums:list[int])->list[list[int]]:
    newList = []
    remainders = []
    lB = 0
    uB = 2
    while uB<=len(nums)-1:
        subList = []
        subList.append(nums[lB])
        subList.append(nums[lB+1])
        subList.append(nums[uB])
        newList.append(subList)
        lB = lB + 3
        uB = uB +3
    if lB<=len(nums)-1:
        for i in range(lB,len(nums)):
            remainders.append(nums[i])
        newList.append(remainders)
    return newList

# part 2

def