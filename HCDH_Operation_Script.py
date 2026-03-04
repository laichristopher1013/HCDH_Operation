#import HCC 
#HCDH (Hyperbolic curve diffie hellman operation) 
    #gen (generate private key & public key) 
#example

from HCC_Operation_Script import HCC 
import random 

class DH:
    #to initialize variable
    def __init__(self, hcc, g):
        self.hcc = hcc 
        self.g = g 
        countn, containern = hcc.recordncoord(g)
        self.n = countn
    
    #to generate the public key & private key
    def gen(self): 
        #private key = random number between 1 to n
        pri_k = random.randint(1, self.n - 1) 
        #public key = the point that produce by g * private key
        pub_k = self.hcc.mul(self.g, pri_k) 
        return (pri_k, pub_k)

#example
if __name__ == "__main__":
    g = (4, 5)
    d, p = -7, 19
    hcc = HCC(d=d, p=p)
    countN, containerN = hcc.countN, hcc.containerN
    countn, containern = hcc.recordncoord(g)
    N, n = countN, countn
    h = N / n
    dh = DH(hcc=hcc, g=g)

    print("-------------------------------------------\n") 
    #generate pri_k, pub_k
    #client 1
    pri_k1, pub_k1 = dh.gen()
    print(f"client 1\n pri_k1: {pri_k1}, pub_k1: {pub_k1}\n")

    #client 2
    pri_k2, pub_k2 = dh.gen()
    print(f"client 2\n pri_k2: {pri_k2}, pub_k2: {pub_k2}\n")

    #deliver pub_k to generate shared key
    #client 1 
    shared_k1 = hcc.mul(pub_k2, pri_k1)
    print(f"client 1: {pub_k2} * {pri_k1}\n shared_k: {shared_k1}\n")

    #client 2
    shared_k2 = hcc.mul(pub_k1, pri_k2)
    print(f"client 2: {pub_k1} * {pri_k2}\n shared_k: {shared_k2}")
    print("\n-------------------------------------------") 