import asyncio
from aiofile import AIOFile, Reader, Writer

import markovify
from random import choice
import concurrent.futures
import sys

class Brain(object):
    """docstring for Brain."""

    def __init__(self, arg):
        self.path = arg

    def think(self,iteration=1, thread_number=1):
        result = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for i in range(thread_number):
                thread = executor.submit(self.worker, iteration)
                result.append(thread.result())
        new_list = []
        for i in result :
            if i not in new_list:
                new_list.append(i)
        return new_list

    def worker(self,i):
        list = []
        with open(self.path) as f:
            text = f.read()
        text_model = markovify.NewlineText(text)
        for i in range(i):
            a = text_model.make_short_sentence(100)
            list.append(a)
        return list


class Save(object):
    """docstring forSave."""

    def __init__(self, arg):
        self.path = arg

    def save(self,data):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.run(data))


    async def run(self,data):
        found  = False
        async with AIOFile(self.path, mode='r') as afp:
            reader = Reader(afp, chunk_size=8)
            async for chunk in reader:
                if data in str(chunk):
                    found = True
                    sys.stdout.write('data already exist\n')
        if found is False:
            async with AIOFile(self.path, mode='a') as afp:
                await afp.write(str(data))
                await afp.write('\n')
