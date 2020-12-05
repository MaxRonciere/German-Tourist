import asyncio

import markovify
import sys

class Brain(object):
    """docstring for Brain."""

    def __init__(self, arg):
        self.path = arg


    def think(self,i):
        list = []
        with open(self.path) as f:
            text = f.read()
        text_model = markovify.Text(text, retain_original=False)
        text_model.compile(inplace = True)
        for i in range(i):
            a = text_model.make_short_sentence(280)
            list.append(a)
        return list


class Save(object):
    """docstring forSave."""

    def __init__(self, arg):
        self.path = arg

    def save(self,data):
        with open(self.path,'r') as f:
            for piece in self.read_in_chunks(f):
                if data in piece:
                    return
        with open(self.path,'a') as f:
            f.write(data)
            f.write('\n')
            f.close()
    
    def read_in_chunks(self,file_object, chunk_size=1024):
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data




