with open('input.txt') as f:
    lines = f.read().strip()

ranges = lines.split(',')
sum = 0 

for r in ranges:
    start_str, end_str = r.split('-')
    start = int(start_str)
    end = int(end_str)

    for n in range(start, end + 1):
        s = str(n)
        if(len(s) % 2 == 0):
            left = s[:len(s)//2]
            right = s[len(s)//2:]
            if left == right:
                sum += int(n)

print(sum)
