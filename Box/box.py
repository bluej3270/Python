run = True

while run == True:

    print ('Enter Side Length or exit to exit')

    #unfiltered input
    size = input()

    # *filtering
    if size == exit:
        SystemExit
    #make size into an int
    size = int(size)
    #force size to be greater than or equal to 1
    if size < 1:
        size = 1

    box = [[]]
    for i in range(size):
        box.append([])
        for j in range(size):
            if i == 0 or i == size-1:
                box[i].append("#")
                continue
            elif j == 0 or j == size - 1:
                box[i].append("#")
            else:
                box[i].append(" ")


    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
          for row in box]))
