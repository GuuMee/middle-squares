n = int(input("Please enter a four digit number: "))
already_seen = list()
while n not in already_seen:
    already_seen.append(n)
    n = int(str(n * n).zfill(8)[2:6])
    print(n)
print('periodicity = ', len(already_seen) - already_seen.index(n))