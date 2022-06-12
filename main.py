def get_hui(n, kc, kf):
    return [round((4897/(kc[i]/0.058 + kf[i]))**(1/n[i]), 5) for i in range(len(n))]

n = "1,1 0,7 0,2 0,9 0,4 0,3 0,5 0,5 0,7 0,13 0,11 0,2 0,15 1,6 1,6"
kc = "0,95 5,27 2,56 52,53 11,42 2,79 0,77 13,19 16,03 12,7 1,84 16,43 1,52 4,37 2,49"
kf = "1528,43 1515,04 43,12 1127,97 808,96 141,11 51,91 692,15 1262,53 1555,95 103,27 1724,69 119,6 196,72 245,9"

lmbd_cool = lambda x: ''.join([i if i != ',' else '.' for i in x])
lmbd_cool_too = lambda x: [float(i) for i in x.split()]

n = lmbd_cool_too(lmbd_cool(n))
kc = lmbd_cool_too((lmbd_cool(kc)))
kf = lmbd_cool_too(lmbd_cool(kf))

print(get_hui(n, kc, kf))