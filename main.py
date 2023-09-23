import asyncio
from aiohttp import web
import asyncio
from project.core.Config import Config
from project.core.Writer import Writer
from project.core.GETFactory import GETFactory
from project.core.POSTFactory import POSTFactory

async def handle_get(request):
    global writer
    logRecord = GETFactory.build_from_url(request.path_qs)
    writer.write_record(logRecord)
    return web.Response(text="")

async def handle_post(request):
    global writer
    jsonData = await request.json()
    logRecord = POSTFactory.build_from_json(jsonData)
    writer.write_record(logRecord)
    return web.Response(text="")

async def run_web_server():
    app = web.Application()
    app.add_routes([web.get('/', handle_get),
                    web.post('/', handle_post)])
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