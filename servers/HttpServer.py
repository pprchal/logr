from aiohttp import web
from writers.AbstractWriter import AbstractWriter
from core.Config import Config
from servers.HttpParser import HttpParser


class HttpServer:
    def __init__(self, writer: AbstractWriter):
        """
        Constructor
        :param writer:
        """
        self.writer = writer

    async def handle_get(self, request):
        """
        Handles GET request.
        1) create LogRecord structure
        2) write to writer
        :param request:
        :return:
        """
        log_record = HttpParser.parse_from_url(request.path_qs)
        await self.writer.write_record(log_record)
        return web.Response(text="")

    async def handle_post(self, request):
        """
        Handles POST request.
        1) create LogRecord structure
        2) write to writer
        :param request:
        :return:
        """
        json_data = await request.json()
        log_record = HttpParser.parse_from_json(json_data)
        await self.writer.write_record(log_record)
        return web.Response(text="")

    async def run(self):
        """
        Setup http mappings
        :return:
        """
        app = web.Application()
        app.add_routes([web.get('/', self.handle_get),
                        web.post('/', self.handle_post)])
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, Config.Http.address(), Config.Http.port())
        await site.start()
