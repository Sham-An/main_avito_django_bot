import base64
import chardet

import base64

def decode_f_param(f_param: str):
    f_param = 'ASgBAQECAUQ82gECQPKKDhSkgpQBgo4PFLib8QIBRcaaDBd7ImZyb20iOjIwMDAsInRvIjozMDAwfQ=='
    parts = f_param.split('-')
    result = []
    for part in parts:
        decoded_part = base64.b64decode(part.encode())[1:].decode('utf-8')
        result.append(decoded_part)
    print(result)
    return result
"""
encoded_f = 'ASgBAQECAUQ82gECQPKKDhSkgpQBgo4PFLib8QIBRcaaDBd7ImZyb20iOjIwMDAsInRvIjozMDAwfQ=='
#with open('file.txt', 'rb') as f:
data = encoded_f.encode() #encoded_f #f.read()
result = chardet.detect(data)
encoding = result['encoding']
decoded_data = data.decode(encoding)
print(decoded_data)

decoded_f = base64.b64decode(encoded_f).decode('latin-1')
decoded_f2 = base64.b64decode(encoded_f).decode('utf-8')
print(decoded_f2)
"""