n = int(input())

for i in range(n):
    str_1, str_2 = input().split(maxsplit=2)
    new_str = []

    j = 0
    while len(new_str) < (len(str_1) + len(str_2)):
        if j < len(str_1):
            new_str.append(str_1[j])
        if j < len(str_2):
            new_str.append(str_2[j])
        j += 1

    print(''.join(new_str))
