def generate_password(n):
    pairs = []
    for i in range(1, n):
        for j in range(i+1, n+1):
            if i + j == n:
                pairs.append((i, j))

    password = ''.join(str(pair[0]) +str(pair[1]) for pair in pairs)
    return password

n = int(input("Введите число от 3 до 20: "))
result = generate_password(n)
print(result)
