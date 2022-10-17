import hashlib

pwd = input("Input word to hash: ")
hpwd = hashlib.md5(pwd.encode('utf-8')).hexdigest()
print(hpwd)