
with open('input.txt', 'r') as file:
    lines = file.readlines()

line = lines[0].strip()

memlength = sum((int(i) for i in line))

mempos = 0
result = 0

start = 0
end = len(line)-1
if end % 2 != 0:
    end -= 1

end_len = int(line[end])

while end >= start:
    if end == start:
        #print("end", end_len)
        while end_len > 0:
            #print(end//2, mempos, (end//2)*mempos)
            result+= (end//2)*mempos
            mempos += 1
            end_len -= 1
        break
    if start % 2 == 0:
        for _ in range(int(line[start])):
            #print(start//2, mempos, (start//2)*mempos)
            result += (start//2)*mempos
            mempos += 1
    else:
        for _ in range(int(line[start])):
            if end_len == 0:
                end -= 2
                end_len = int(line[end])
            #print(end//2, mempos, (end//2)*mempos)
            result+= (end//2)*mempos
            mempos += 1
            end_len -= 1
    start += 1

print(result)