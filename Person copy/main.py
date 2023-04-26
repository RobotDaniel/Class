import random 
import cards
import people
deck=[]
def WriteCards():
    
    for i in range(13):
            
            deck.append(cards.Cards("Spades",str(i)))
            deck.append(cards.Cards("Hearts",str(i)))
            deck.append(cards.Cards("Clubs",str(i)))
            deck.append(cards.Cards("Diamonds",str(i)))
def makeCards():
    CardsList=[]
    for i in range(5):
        x = deck[random.randint(0,len(deck))]
        CardsList.append(x)
        deck.remove(x)
        
    return CardsList
WriteCards()
print(makeCards())
print(len(deck))

Daniel=people.People("Daniel",makeCards())
Michael=people.People("Michael",makeCards())



