from aiohttp import web
import asyncio
from core.Config import Config
from writers.Writer import Writer
from core.GETFactory import GETFactory
from core.POSTFactory import POSTFactory


async def handle_get(request):
    global writer
    log_record = GETFactory.build_from_url(request.path_qs)
    await writer.write_record(log_record)
    return web.Response(text="")


async def handle_post(request):
    global writer
    json_data = await request.json()
    log_record = POSTFactory.build_from_json(json_data)
    await writer.write_record(log_record)
    return web.Response(text="")


async def run_web_server():
    app = web.Application()
    app.add_routes([web.get('/', handle_get),
                    web.post('/', handle_post)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, Config.http_address(), Config.http_port())
    await site.start()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    Config.load()
    writer = Writer()
    loop.run_until_complete(run_web_server())
    loop.run_forever()