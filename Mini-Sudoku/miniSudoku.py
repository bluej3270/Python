def miniSudoku(grid):
    nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    iter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print("loop")
            if not 0 < grid[i][j] <= 9:
                print(nums)
                return False
            else:
                if nums[grid[i][j] - 1] == 1:
                    print(grid)
                    return False
                else:
                    nums[iter] = 1
            iter += 1
    for k in range(len(nums)):
        if not nums[k] == 1:
            print(nums)
            return False
    print(nums)
    return True


print(miniSudoku([[1, 1, 2], [9, 7, 8], [4, 5, 6]]))
