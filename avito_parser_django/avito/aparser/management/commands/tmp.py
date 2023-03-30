#Пакет `psiphon3` предоставляет возможность использования функций и
# создания соединения с помощью кода Python.
# Более подробно можно ознакомиться с документацией по ссылке
# https://github.com/Psiphon-Labs/psiphon-tunnel-core-python.
#Вот пример использования `psiphon3` в Python:

from psiphon3 import PsiphonTunnelCore

proxy_host = "&lt;адрес_прокси_сервера>"
proxy_port = "&lt;порт_прокси_сервера>"
app_id = "&lt;идентификатор_приложения>"
config = {
    "psiphon": {
        "upstream_proxy": "http://{}:{}".format(proxy_host, proxy_port),
        "app_id": app_id
    }
}

tunnel = PsiphonTunnelCore.create(config)

if tunnel.allocate():
    print("Connected to Psiphon server")
    # Use tunnel for requests
else:
    print("Connection unsuccessful")

