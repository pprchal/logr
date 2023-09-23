import asyncio
from servers.HttpServer import HttpServer
from core.Config import Config
from writers.Writer import Writer

if __name__ == '__main__':
    props = {'a': 'AAA'}
    key = "ad"

    x = props[key] if key in props else "nene"

    # read config
    Config.load()

    # main writer
    writer = Writer("MainWriter")
    writer.print_config()

    # start async loop
    loop = asyncio.get_event_loop()
    http_server = HttpServer(writer)
    loop.run_until_complete(http_server.run())
    loop.run_forever()
