def get_password(a):
    result = ''
    div = []
    for i in range(2, a + 1):
        if a % i == 0:
            div.append(i)
    for d in div:
        for first in range(1, d // 2 + 1):
            if first == d - first:
                continue
            result += f'{first}{d - first}'
    return result

for number in range(3, 21):
    print(f'{number}: {get_password(number)}')
