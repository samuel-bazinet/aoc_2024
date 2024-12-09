
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

files: list[tuple[int, int, int]] = []
free_spaces: list[tuple[int, int]] = []
final_mem: list[tuple[int, int]] = [-1 for _ in range(memlength)]

offset = 0
for i in range(0, end+1):
    if i % 2 == 0:
        files.append((i//2, int(line[i]), offset))
        offset += int(line[i])
    else:
        free_spaces.append((offset, int(line[i])))
        offset += int(line[i])

#print(files)
#print(free_spaces)

files.reverse()

''' need to inverse
for i, free_space in enumerate(free_spaces):
    #print(free_space[0])
    size = free_space[1]
    offset = 0
    deleted = 0
    if len(files) > 0:
        file = files.pop()
        for l in range(file[1]):
            final_mem[l + file[2]] = file[0]
    else:
        break
    c_files = files.copy()
    for j, file in enumerate(c_files):
        if file[1] <= size and file[2] > (free_space[0]+offset):
            size -= file[1]
            files.pop(j-deleted)
            for l in range(file[1]):
                final_mem[offset + free_space[0] + l] = file[0]
            offset += file[1]
            deleted += 1
'''

for i, (idx, size, offset) in enumerate(files):
    moved = False
    for j, (b_off, b_size) in enumerate(free_spaces):
        if b_size >= size and offset > b_off:
            moved = True
            free_spaces[j] = (b_off+size, b_size-size)
            for s in range(size):
                final_mem[b_off+s] = idx
            break
    if not moved:
        for s in range(size):
            final_mem[offset+s] = idx


for i in final_mem:
    print(f'{i}' if i != -1 else '.', end='')
print()

result = 0
for i, e in enumerate(final_mem):
    result += i*e if e > 0 else 0
print(result)
