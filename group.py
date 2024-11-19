# part 1
from typing import Optional


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

def command_line(file)->Optional[float]:  # takes in a list of the parameters in the configuration and
    try:
        open(file)
        for line in file:
            parts = line.split()
            try:
                for i in line:
                    float(line[i])
                print(sum(line))
            except ValueError:
                print("Error - missing value")
    except FileNotFoundError:
        exit()


if __name__ == '__main__':
    command_line(times)
