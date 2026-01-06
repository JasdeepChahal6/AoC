with open("input.txt") as f:
        lines = f.read().splitlines()

    
amount_of_zero = 0
point = 50
for line in lines:
    direction = line[0]
    amount = int(line[1:])

    if direction == "L":
            point = (point + amount) % 100
    elif direction == "R":
            point = (point - amount) % 100
    if point == 0:
        amount_of_zero += 1

print(amount_of_zero)