import hashlib
rawdata = "message"

blake2c = hashlib.blake2s(str(rawdata).encode("utf-8")).hexdigest() #For blake2c hash
print(blake2c)
blake2b = hashlib.blake2b(str(rawdata).encode("utf-8")).hexdigest() #For blake2b hash
print(blake2b)