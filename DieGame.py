from Die import Die
from Player import Player

class DieGame():
    def __init__(self):
        self.players = []
        self.die1 = Die()
        self.die2 = Die()
        self.playList = []

    def addPlayer(self, name):
        self.players.append(Player(name))

    def getPlayers(self):
        return self.players
    
    def getPlayList(self):
        return self.playList
        
    def play(self):
        for player in self.players:
            player.rollDie(self.die1, self.die2)
            self.playList.append({"name": player.getName(), "faceValue": player.getResult()})

    # get højeste score


    # sort list by 
    
    # test the class
if __name__ == "__main__":
    game = DieGame()
    game.addPlayer("John")
    game.addPlayer("Poul")
    game.addPlayer("Kim")
    game.addPlayer("Anders")
    game.addPlayer("Sam")
    game.play()
    print(game.getPlayList())
    game.play()
    game.play()
    game.play()
    game.play()
    print(game.getPlayList())
    print("player Score")
    for player in game.getPlayers():
       print(player.getName(), player.getScore())
    print("Play List")   
    for item in game.getPlayList():
        print(item["name"], item["faceValue"])
        print(item.values())   # print values of dictionary dictionary method values()
    # print(game.getPlayers())
    # print(game.getPlayList())