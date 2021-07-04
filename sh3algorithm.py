import hashlib
rawdata = "message"

sha256 = hashlib.sha3_256(str(rawdata).encode("utf-8")).hexdigest() #For Sha256 hash
print(sha256)
sha512 = hashlib.sha3_512(str(rawdata).encode("utf-8")).hexdigest() #For Sha512 hash
print(sha512)