n = int(input('N?'))
t0 = 0
t1 = 1
print('{}->{}'.format(t0, t1), end='')
index = 2
while index <= n:
    t2 = t1 + t0
    print('->{}'.format(t2), end='')
    t0 = t1
    t1 = t2
    index += 1
