from functools import cache

# @cache
def blink_with_steps(s, steps):
    if steps == 0:
        return 1
    
    new_el = blink(s)
    result = 0
    for i in range(len(new_el)):
        result += blink_with_steps(new_el[i], steps-1)

    return result

def blink(s):
    n = len(s)

    if s == '0':
        return ['1']
    elif n%2 == 0:
        left_part = str(int(s[:n//2]))
        right_part = str(int(s[n//2:]))
        return [left_part, right_part]
    else:
        return [str(int(s) * 2024)]


input = []
with open('input.txt') as f:
    input = f.readline().strip().split(' ')

result = 0
steps = 75
for j in range(len(input)):
    result += blink_with_steps(input[j], steps)

print(result)