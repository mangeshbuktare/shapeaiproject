import hashlib
rawdata = "HELLO" #input string data
sha = hashlib.sha256(str(rawdata).encode("utf-8")).hexdigest() #For Sha256 hash
print(sha)
#If you need byte type output, use digest() instead of hexdigest()
mdpass = hashlib.md5(str(sha).encode("utf-8")).hexdigest() #For MD5 hash
print(mdpass)