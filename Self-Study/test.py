def sum(n):
    sum = 0
    for i in range(n):
        i += 1
        print(f"in i i = {i}")
        for j in range(i + 1, n):
            print(f"in j j = {j}")
            j += 1
            for k in range(j + 1, n):
                k += 1
                print(f"in k k = {k}")
                for l in range(k + 1, 10 + k):
                    print(f"in l l = {l}")
                    l += 1
                    sum += 1

print(sum(9))
