import aiofiles
import aiohttp
import aiomysql
import asyncio
import time
import sys


async def store_address(address, pool):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("insert into Places(street_name) values('{address}');".format(address=address.replace("'", '')))
            await conn.commit()


async def geocode(address, pool, session):
    async with session.post('http://localhost:8000/', data=address) as resp:
        await store_address(address, pool)


async def read_addresses_from(file, pool, session):
    async with aiofiles.open(file, 'r') as addresses:
        async for address in addresses:
            await geocode(address, pool=pool, session=session)


async def main(file_name):
    session = aiohttp.ClientSession()
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='sa', password='caju3253',
                                      db='addresses', loop=asyncio.get_event_loop())

    print(f"started at {time.strftime('%X')}")
    await read_addresses_from(file_name, pool=pool, session=session)
    print(f"finish at {time.strftime('%X')}")
    pool.close()
    await session.close()

if __name__ == "__main__":
    pool = None
    file_name = sys.argv[1]
    asyncio.run(main(file_name))
