def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


import hashlib

data = read_file("data.txt")[0]

hash = hashlib.md5(data.encode())

i = 282749

while True:
    if hashlib.md5((data + str(i)).encode()).hexdigest()[:6] == "000000":
        print(i)
        break
    i += 1
