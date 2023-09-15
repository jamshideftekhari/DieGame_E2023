import json

class Player():

    def __init__(self, name):
        self.name = name
        self.result = 0
        self.score = 0

    def getName(self):
        return self.name

    def getResult(self):
        return self.result
    
    def getScore(self):
        return self.score

    def rollDie(self, die1, die2):
        die1.Roll()
        die2.Roll()
        self.result = die1.GetFaceValue() + die2.GetFaceValue()
        if self.result == 7:
            self.score += 1
        

# Test the class
if __name__ == "__main__":

    x = {"name": "John", "age": 30, "city": "New York"}
    print(x)
    print(x["name"])
    print(x["age"])
    print(x["city"])    


    scoreList = []
    scoreList.append({"name": "John", "faceValue": 1})
    scoreList.append({"name": "poul", "faceValue": 2})
    scoreList.append({"name": "kim", "faceValue": 3})
    scoreList.append({"name": "anders", "faceValue": 4})
    scoreList.append({"name": "sam", "faceValue": 5})

    print(scoreList)

    # score list of player objects
    from Die import Die
    playerList = []
    playerList.append(Player("John"))
    playerList.append(Player("Poul"))
    playerList.append(Player("Kim"))

    print(playerList)
    print(playerList[0].getName())
    print(json.dumps(playerList[0].__dict__))
    print(playerList[0].__dict__)
    print("****")
    print(json.dumps([ob.__dict__ for ob in playerList]))


    
   