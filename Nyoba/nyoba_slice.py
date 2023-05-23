import base64
auth = "Basic SGFyeToxMjM0NTY3OA=="
print(auth[6:])
encode= (auth[6:])
print(encode.encode())
encode1=(base64.b64decode(encode)).decode()
print((encode1))
username=encode1.split(":")[0]
print(username)