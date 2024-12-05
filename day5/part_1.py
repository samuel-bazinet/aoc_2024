
with open('input.txt', 'r') as file:
    lines = file.readlines()

order: dict[int, list[int]] = dict()

adding_rules = True

result = 0

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
        valid = True
        for i, num in enumerate(update):
            if i == len(update) - 1 or not valid:
                break
            if num in order.keys():
                for j, rest in enumerate(update[i+1:]):
                    if j == len(update[i+1:])-1:
                        continue
                    if rest in order[num]:
                        if rest in order.keys():
                            if num in order[rest]:
                                print(update, "num in order")
                                valid = False
                                break
                        else:
                            print(update, "rest not in order keys", rest)
                            valid = False
                            break
                    else:
                        print(update, "rest not in order")
                        valid = False
                        break
            else:
                print(update, "num not in keys")
                valid = False
                break
        if valid:
            result += update[len(update)//2]

print(result)
