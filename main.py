from aiohttp import web


async def demo(request):
    text = "Hello, Anonymous"
    return web.Response(text=text)


app = web.Application()
app.add_routes([
    web.get('/', demo),
])

if __name__ == '__main__':
    web.run_app(app)
