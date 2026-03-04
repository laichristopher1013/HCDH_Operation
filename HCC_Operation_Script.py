#x^2 - dy^2 = 1
#HCC (hyperbolic curve operation)
    #check (check p is on the hcc or not) 
    #findinverse (find the inverse of the given point)
    #findcoord (find the coordinates of giving x on the curve)
    #recordNcoord (record all N coordinates)
    #recordncoord (record all n coordinates)
    #add (modadd) 
    #mul (montgomary ladder) 
#example
from Crypto.Util.number import isPrime

class HCC:
    def __init__(self, d, p):
        self.zero = (1, 0)
        self.d = d
        self.p = p
        #to check d is perfect square or not if yes curve will degrade
        if pow(d, (p - 1) // 2, p) == 1 or not isPrime(p):
            raise ValueError("The Curve has Defects")

        self.countN, self.containerN = self.recordNcoord()

    def check(self, p):
        if p == self.zero:
            return True

        x, y = p

        if not (0 <= x < self.p and 0 <= y < self.p) or \
        not (x**2 - self.d * y**2 - 1) % self.p == 0:
            raise ValueError("Invalid point")
        return True

    def findinverse(self, p):
        self.check(p)
        x, y = p
        return(x, -y % self.p)

    def findcoord(self, x):
        if x < self.p:
            #y^2 = (x^2 - 1) / d
            y = (x**2 - 1) * pow(self.d, -1, self.p) % self.p

            for i in range(0, self.p):
                if i**2 % self.p == y:
                    return((x, i), (x, -i % self.p))
            raise ValueError("Not found")
        else:
            raise ValueError("Out of range")
    
    def recordNcoord(self):
        #the 1 point means the point at infinity 
        containerN = {self.zero}
        
        #to brute force in order to find the total point 
        for x in range(self.p):
            try:
                p1, p2 = self.findcoord(x)
                #if given x produce 2 same points + 1
                if p1 == p2:
                    containerN.add(p1)
                #if given x produce 2 different points + 2
                else:
                    containerN.add(p1)
                    containerN.add(p2)
            except Exception:
                pass
        return len(containerN), containerN

    def recordncoord(self, g):
        self.check(g)
        containern = []
        current = g

        for i in range(1, self.countN + 1):
            #n will always be a cycle so when n reach infinite point it means n is found
            #to keep letting g adding it self until it reach infinite point
            containern.append(current)
            if current == self.zero:
                return i, containern
            current = self.add(current, g)
        raise ValueError("Invalid order") 

    #hcc addition
    def add(self, p1, p2):
        self.check(p1)
        self.check(p2)
        #to check p1 / p2 is infinite point or not
        if p1 == self.zero:
            return p2
        elif p2 == self.zero:
            return p1

        x1, y1 = p1
        x2, y2 = p2

        #no need to check inverse it will handle automatically
        x3 = (x1 * x2 + self.d * y1 * y2) % self.p
        y3 = (x1 * y2 + x2 * y1) % self.p

        return (x3, y3)

    #hcc multiplication
    def mul(self, g, n): 
        self.check(g)
        #montgomery ladder
        r0 = self.zero
        r1 = g

        for i in bin(n)[2:]:
            if i == "1":
                r0 = self.add(r0, r1)
                r1 = self.add(r1, r1)
            else:
                r1 = self.add(r1, r0)
                r0 = self.add(r0, r0)
        
        return r0

#example
if __name__ == "__main__":
    g = (4, 5)
    k = 5
    d, p = -7, 19
    x, y = g
    hcc = HCC(d=d, p=p) 
    print("-------------------------------------------\n") 

    countN, containerN = hcc.countN, hcc.containerN
    print(f"HCC: x^2 - {d}y^2 mod({p}) = 1")
    print(f"N: {countN}") 
    print(f"Ncoorinates: {containerN}\n")
    
    countn, containern = hcc.recordncoord(g)
    print(f"G: {g}" )
    print(f"G Inverse: {hcc.findinverse(g)}") 
    print(f"Coordinates x = {x}: {hcc.findcoord(x)}") 
    print(f"n: {countn}") 
    print(f"ncoordinates: {containern}")
#h 一定是整數：拉格朗日定理
    print(f"h: {countN//countn}")
    print(f"{k}G: {hcc.mul(g, k)}") 
    print("\n-------------------------------------------") 
