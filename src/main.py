import asyncio
from game import *

async def main():
    game=Game()
    while game.running:
        game.handle_events()
        game.update()
        game.render()
        await asyncio.sleep(0)

    game.shutdown()

asyncio.run(main())