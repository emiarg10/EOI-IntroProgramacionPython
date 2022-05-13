import asyncio

async def saludo():
    print('Hola ...')
    await asyncio.sleep(4)
    print(' ... world')

asyncio.run(saludo())
print('Fin del programa')