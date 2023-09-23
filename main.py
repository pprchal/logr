from aiohttp import web
import asyncio
from core.Config import Config
from writers.Writer import Writer
from core.GETFactory import GETFactory
from core.POSTFactory import POSTFactory


async def handle_get(request):
    """
    Handles GET request.
    1) create LogRecord structure
    2) write to writer
    TODO: maybe only store to mem?
    :param request:
    :return:
    """
    global writer
    log_record = GETFactory.build_from_url(request.path_qs)
    await writer.write_record(log_record)
    return web.Response(text="")


async def handle_post(request):
    """
    Handles POST request.
    1) create LogRecord structure
    2) write to writer
    TODO: maybe only store to mem?
    :param request:
    :return:
    """
    global writer
    json_data = await request.json()
    log_record = POSTFactory.build_from_json(json_data)
    await writer.write_record(log_record)
    return web.Response(text="")


async def run_web_server():
    """
    Setup http mappings
    :return:
    """
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
    writer = Writer("MainWriter")
    writer.print_config()
    loop.run_until_complete(run_web_server())
    loop.run_forever()
