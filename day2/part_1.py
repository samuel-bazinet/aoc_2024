
with open('input.txt', 'r') as file:
    lines = file.readlines()

safe_n = 0

for line in lines:
    numbers = [int(n) for n in line.strip().split()]

    safe = True
    for i, n in enumerate(numbers):
        if i == 0:
            continue
        first = numbers[i-1]
        second = n
        if i == 1:
            ascending = second > first
        if  abs(second - first) < 1 or abs(second - first) > 3:
            safe = False
            break
        if i >= 2:
            if (first < second and not ascending) or (first > second and ascending):
                safe = False
                break
    if safe:
        print(numbers, "safe")
        safe_n += 1

print(safe_n)
