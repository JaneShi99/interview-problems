def count_bits(x):
    """
    this counts the number of bits that are needed to represent the integer x
    """

    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


def parity(x):
    """
    THE BRUTE FORCE ALGORITHM
    this computes the parity of a binary word, where the parity is defined as the number of 1s in its
    binary expansion modulo 2
    """
    answer = 0
    while x:
        answer ^= x & 1
        x >>= 1
    return answer


def parity1(x):
    """
    THE ALGORITHM THAT CUTS DOWN IN CHUNKS
    this uses the trick that drops non-zero bits one at a time
    """
    result = 0
    while x:
        result ^= 1
        x &= x - 1 # it drops the lowest non-zero bit from x, a.k.a it accumulates 1 mod 2 whenever encounters nonzero bit
       
    return result

def parity2(x):
    """
    this uses a bitmask that just extracts the wanted digits and does operation accordingly
    each pair of bits in the string of length 8
    """
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return(PRECOMPUTED_PARITY [x >> (3 * MASK_SIEZZ)] ^ 
           PRECOMPUTED_PARITY [(x >> (2 * MASK_SIZE)) & BIT_MASK] ^ 
           PRECOMPUTED_PARITY [(x >> MASK_SIZE) & BIT_MASK] ^ 
           PRECOMPUTED_PARITY [x & BIT_MASK])


def parity3(x):
    """
    this method just does bitwise xor for the binary words's first half and second half
    """
   x ^= x >> 32
   x ^= x >> 16
   x ^= x >> 8
   x ^= x >> 4
   x ^= x >> 2
   x ^= x >> 1

   return x & 0x1
