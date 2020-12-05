from ThickBrain import Brain, Save
import requests






if __name__ == '__main__':
    url = 'https://etherpad.opendev.org/p/dridri/export/txt'
    r = requests.get(url, allow_redirects=True)

    path = "database/dict.txt"
    open(path, 'wb').write(r.content)


    save = Save("database/sentences.txt")
    number = 50000
    for i_ in range(500):
        a = Brain(path)
        result = a.think(number)
        for i in result:
            save.save(str(i))
