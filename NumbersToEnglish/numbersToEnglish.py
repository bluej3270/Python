

def numbersToEnglish(num):
    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
            'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    numsTeens = ['eleven', 'twelve', 'thirteen', 'fourteen',
                 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'ten']
    # Edge case: if the number is zero
    if num == 0:
        return 'zero'

    # convert num to char array
    arrNums = [int(a) for a in str(num)]
    if not len(arrNums) == 3:
        arrNums.insert(0, -1)
        if not len(arrNums) == 3:
            arrNums.insert(0, -1)

    hundreds = " "
    tens = " "
    ones = " "

    # TODO: fix for numbers with zeros as the last char
    if not arrNums[1] == 1 and not arrNums[2] == -1:
        ones = nums[arrNums[2] - 1]
        if arrNums[2] == 0:
            ones = " "
    if not arrNums[1] == 1 and not arrNums[1] == -1:
        tens = nums[arrNums[1] + 7] + " "
        if arrNums[1] == 0:
            tens = " "
    if arrNums[1] == 1 and not arrNums[1] == -1:
        tens = numsTeens[arrNums[2] - 1]
    if len(arrNums) >= 3 and not arrNums[0] == -1:
        hundreds = nums[arrNums[0] - 1] + ' hundred '

    return hundreds + tens + ones


print("Enter the number you would like to convert from 0 to 999 inclusive. Only integers.")
i = input()
print(numbersToEnglish(i))
