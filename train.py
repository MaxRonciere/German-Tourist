from ThickBrain import Brain, Save






if __name__ == '__main__':
    save = Save("database\sentences.txt")
    number = 50
    thread = 50
    a = Brain("database\dict.txt")
    result = a.think(number,thread)
    for i in result:
        for j in i:
            save.save(str(j))

            
