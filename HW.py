
def pf(num):
    l1=list(num)
    m=1
    for a in l1:
        m=m*a
    return m


n=(7,2,3)
print("TUPLE:",n)

print("PRODUCT:",pf(n))