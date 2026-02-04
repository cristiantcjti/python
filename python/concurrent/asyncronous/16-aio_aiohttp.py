

import asyncio
import aiofiles
import aiohttp
from bs4 import BeautifulSoup


async def take_links():
    links = []
    async with aiofiles.open('16_links.txt', mode='r') as file:
        async for line in file:
            links.append(line.strip())
    return links


async def take_html(link):
    print(f"Downloading {link}...")
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            response.raise_for_status()
            
            return await response.text()


def take_title(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('title')
    title = title.text.split('|')[0].strip()
    return title


async def print_title():
    links = await take_links()
    
    tasks = []
    for link in links:
        tasks.append(asyncio.create_task(take_html(link)))

    for task in tasks:
        html = await task
        title = take_title(html)
        print("Title: ", title)


def main():
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(print_title())
    asyncio.run(print_title())


if __name__ == '__main__':
    main()