import random 
class Cards:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def getSuit(self):
        return self.suit
    def getRank(self):
        return self.rank

deck=[]
def WriteCards():
    
    for i in range(13):
            deck.append("Spades"+","+str(i)+"\n")
            deck.append("Hearts"+","+str(i)+"\n")
            deck.append("Clubs"+","+str(i)+"\n")
            deck.append("Diamonds"+","+str(i)+"\n")
def makeCards():
    random.randint(1,52)
    
    

