# Concert Seats from edabit
# The function should decide weather each person can "see" by decideing wether eacb number is smaller than the numbes in front of it

def concertSeats(seats):
    j = 0  # to iterate through colums insted of rows, we must set j for the loop
    prevSeat = 0  # no one is infront of the front seat, therefore 0
    for i in range(len(seats[j])):
        for j in range(len(seats)):
            if j == 0:
                prevSeat = 0  # Don't compare the front seat of one row to the back seat of another
            if seats[j][i] < prevSeat:  # ? replace < with <= if instinces like 2, 3, 3 should be false
                return False
            prevSeat = seats[j][i]  # set prevSeat to the previus seat
    return True


print(concertSeats([[1, 2, 3],
                    [6, 5, 8],
                    [7, 8, 9]]))
