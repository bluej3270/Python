# https://edabit.com/challenge/6APNLL9DAKzsHJfCn
import numpy as np


def MemeSum(num1: int, num2: int):
    # Convert to list
    num1_arr = list(map(int, str(num1)))
    num2_arr = list(map(int, str(num2)))

    # Convert list to np array
    num1_arr = np.array(num1_arr)
    num2_arr = np.array(num2_arr)

    # make arrays equal length
    while num1_arr.size != num2_arr.size:
        if num1_arr.size < num2_arr.size:
            num1_arr = np.insert(num1_arr, 0, 0)  # Add a 0 to the start of num1_arr
        elif num2_arr.size < num1_arr.size:
            num2_arr = np.insert(num2_arr, 0, 0)  # Add a 0 to the start of num2_arr
        else:
            print("Array sizes are equal but the loop still ran, fix your loop.")

    # Add arrays and convert back to list
    sum_arr = num1_arr + num2_arr
    sum_arr = sum_arr.tolist()

    # Convert list to int
    sum_arr = map(str, sum_arr)
    meme_sum = ''.join(sum_arr)
    meme_sum = int(meme_sum)

    return meme_sum


print(MemeSum(2, 11))
print(MemeSum(0, 1))
print(MemeSum(0, 0))
print(MemeSum(16, 18))
print(MemeSum(26, 39))
print(MemeSum(122, 81))
print(MemeSum(1222, 30277))
print(MemeSum(38810, 1383))
print(MemeSum(1236, 30977))
print(MemeSum(49999, 49999))
