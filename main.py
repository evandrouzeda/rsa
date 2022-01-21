#apt install gcc
#apt install libgmp3-dev
#pip install miller-rabin
from usecase.createKeys import CreateKeys


keys = CreateKeys.execute(1, 30)
print("N: ", keys.n)
print("E: ", keys.e)
print("D: ", keys.d)

m = 12
print("Original Message: ", m)
c = keys.encrypt(m)
print("Encrypted Message: ", c)
d = keys.decrypt(c)
print("Decrypted Message: ", d)