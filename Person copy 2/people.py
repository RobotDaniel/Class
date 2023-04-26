import main
class People():
    def __init__(self,name,deck):
        self.name=name
        self.deck=deck
        
    def getName(self):
        return self.name
    def getDeck(self):
        return self.deck
    def setName(self,x):
        self.name = x
    def setDeck(self,x):
        self.deck = x
    def removeCard(self,x):
        self.deck.remove[x]
    def addCard(self,x):
        self.deck.append(x)





