from usecase.createKeys import xgcd
from entity.crypto import Crypto

class GenerateKeysFromPublic:
    def __init__(self) -> None:
        pass

    def execute(p, q, e, n):
        t = (p-1)*(q-1)

        g, x, y = xgcd(e, t)
        if(x < 0):
            d = x + t
        else: 
            d = x

        return Crypto(n, e, d)