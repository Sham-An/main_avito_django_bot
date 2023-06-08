
import ssl
import httpx
from lxml import html
# create an ssl context
ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)#+PROTOCOL_TLS_CLIENT) #PROTOCOL_TLS)#
ssl_context = httpx.create_ssl_context()
# ssl.PROTOCOL_TLS - Selects the highest protocol version that both the client and server support.
# Despite the name, this option can select both "SSL" and "TLS" protocols.

# set protocol to use
ssl_context.set_alpn_protocols(["h2"])

CIPHERS = 'ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES'

# set ciphers
ssl_context.set_ciphers(CIPHERS)

# httpx verify param lets you pass a standard library ssl.SSLContext
url = 'https://example.com'
url = 'https://www.avito.ru/tarasovskiy/mototsikly_i_mototehnika?cd=1&radius=50&searchRadius=50'


response = httpx.get(url, verify=ssl_context)
#

print(response.http_version)
#print(response.text[:10000])
print(response.text)
# outputs HTTP/2
#Вместо использования ssl.SSLContext
# вы также можете использовать
# httpx.create_ssl_context() для установки контекста ssl.