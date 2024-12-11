
with open('input.txt', 'r') as file:
    lines = file.readlines()

stones = lines[0].strip().split()

# rules:
# 0 -> 1
# even digits -> split 2
# multiply by 2024

def apply_rules(stone: str) -> list[str]:
    if stone == '0':
        return ['1']
    if len(stone) % 2 == 0:
        return [stone[:len(stone)//2], str(int(stone[len(stone)//2:]))]
    return [str(int(stone)*2024)]

for i in range(25):
    new_stones = []
    for stone in stones:
        new_stones.extend(apply_rules(stone))
    print(len(stones), len(new_stones))
    stones = new_stones

print(len(stones))