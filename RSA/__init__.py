
from ..Util.number import findModInverse

def decrypt(c, d, N):
    """
    @param => int: `c`: ciphertext
    @param => int: `d`: findModInverse(e, phi)
    @param => int: `N`: p * q
    return int: decrypted `c`
    """
    return pow(c, d, N)

def encrypt(m, e, N):
    raise NotImplementedError

def Compute_phi(p, q):
    """
    @param => int: `p`: prime number
    @param => int: `q`: prime number
    return int
    """
    return (p - 1) * (q - 1)

def Compute_d(e, phi):
    """
    @param => int: `e`: public exposent
    @param => int: `phi`: (p - 1) * (q - 1)
    return int
    """
    return findModInverse(e, phi)