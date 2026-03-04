#the hcc variable
#x^2 - dy^2 = 1
d = -7
p1 = (4, 5)
p2 = (7, 17)

#geometry
# def normaladd(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#
#     if x1 == x2 and y1 + y2 == 0:
#         return (1, 0)
#
#     if x1 == x2 and y1 == y2:
#         m = fraction(x1, (d * y1))
#     else:
#         m = fraction(y1 - y2, x1 - x2)
#     x = int(fraction(d * m**2 + 1, d * m**2 - 1))
#     y = int(m * x - m)
#
#     return (x, y)

#algebra
def normaladd(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    #no need to check inverse it will handle automatically
    x3 = (x1 * x2 + d * y1 * y2) 
    y3 = (x1 * y2 + x2 * y1) 

    return (x3, y3)

#example
print("\n-------------------------------------------\n") 
print("Normal Add")
print(f"d: {d}")
print(f"p1: {p1}, p2: {p2}")
print(normaladd(p1, p2)) 
print("\n-------------------------------------------\n") 

#the hcc variable
d = -7
modp = 19
p1 = (4, 5)
p2 = (7, 17)

def modadd(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    #no need to check inverse it will handle automatically
    x3 = (x1 * x2 + d * y1 * y2) % modp
    y3 = (x1 * y2 + x2 * y1) % modp

    return (x3, y3)

#example
print("\n-------------------------------------------\n") 
print("Mod Add")
print(f"d: {d}, modp: {modp}")
print(f"p1: {p1}, p2: {p2}")
print(modadd(p1, p2)) 
print("\n-------------------------------------------\n") 