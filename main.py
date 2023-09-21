import asyncio
from aiohttp import web
import asyncio
from project.core.Config import Config
from project.core.Writer import Writer
from project.core.GETFactory import GETFactory

async def handle(request):
    global writer
    logRecord = GETFactory.build_from_url(request.path_qs)
    writer.write_record(logRecord)
    return web.Response(text="")

async def run_web_server():
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, Config.getHttpAddress(), Config.getHttpPort())
    await site.start()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    Config.load()
    writer = Writer()
    loop.run_until_complete(run_web_server())
    loop.run_forever()