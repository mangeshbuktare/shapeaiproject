# hash with SHA-2 (SHA-256 & SHA-512)
import hashlib
rawdata = "message"

sha256 = hashlib.sha256(str(rawdata).encode("utf-8")).hexdigest() #For Sha256 hash
print(sha256)
sha512 = hashlib.sha512(str(rawdata).encode("utf-8")).hexdigest() #For Sha512 hash
print(sha512)