def right_prop(x):
    """
    right propagate right most set bit in x
    i.e. turns (01010000)2 into (10101111)2
    type x: int
    rtype: binary word
    """

    return x | x-1

def pow_mod_2(x,p):
    """
    returns the value of x mod p where p is a power of 2
    type x: int
    type p: int
    rtype: mod
    """
    MASK = p-1
    return x & MASK


def isPow2(x):
    """
    returns whether x is power of 2
    type x: int
    rtype: bool
    """
    return  True if x & x-1 == 0 else False

def main():
    print("test for right prop")
    print("01010000 ",bin(right_prop(0b01010000)))
    print("10101111 ",bin(right_prop(0b10101111)))
    print("10000000 ",bin(right_prop(0b10000000)))
    print("test for mod power of 2")
    print("77,64 ",str(int(pow_mod_2(77,16))))
    print("2342143,128", str(int(pow_mod_2(2342143,128))))

    print("test for whether power of 2")
    print("64 ",isPow2(64))
    print("128 ",isPow2(128))
    print("35 ",isPow2(35))
main()
