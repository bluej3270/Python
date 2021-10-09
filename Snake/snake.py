
def snake(side):
    tiles = side * side
    length = 1
    fruits = 0
    while length < tiles:
        length *= 2
        fruits += 1
    return fruits - 1

print(snake(3))
print(snake(6))
print(snake(24))