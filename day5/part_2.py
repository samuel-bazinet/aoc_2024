
with open('input.txt', 'r') as file:
    lines = file.readlines()

order: dict[int, list[int]] = dict()

adding_rules = True

to_fix = []

result = 0

def check_update(update) -> bool:
    for i, num in enumerate(update):
        if i == len(update) - 1:
            break
        if num in order.keys():
            for j, rest in enumerate(update[i+1:]):
                if j == len(update[i+1:])-1:
                    continue
                if rest in order[num]:
                    if rest in order.keys():
                        if num in order[rest]:
                            return False
                    else:
                        return False
                else:
                    return False
        else:
            return False
    return True

for line in lines:
    if line == '\n':
        adding_rules = False
        continue
    if adding_rules:
        pair = line.strip().split('|')
        if int(pair[0]) in order.keys():
            order[int(pair[0])].append(int(pair[1]))
        else:
            order[int(pair[0])] = [int(pair[1])]
    else:
        update = [int(n) for n in line.strip().split(',')]
        if not check_update(update):
            to_fix.append(update)

for update in to_fix:
    valid_order_counts = dict()
    for i, num in enumerate(update):
        valid_order_counts[num] = 0
        for j, o in enumerate(update):
            if num != o:
                if num in order.keys():
                    if o in order[num]:
                        valid_order_counts[num] += 1
                else:
                    valid_order_counts[num] = 0
    counts = valid_order_counts.items()
    counts = sorted(counts, key = lambda x: x[1])
    result += counts[len(counts)//2][0]
        

print(result)
