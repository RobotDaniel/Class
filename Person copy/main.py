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

        


     
WriteCards()    
def makeCards(x):
    CardsList=[]
    for i in range(x):
        p1 = deck[random.randint(0,len(deck))]
        CardsList.append(p1)
        deck.remove(p1)
        
        
    return CardsList

Daniel=people.PeopleClass("Daniel",makeCards(5))
Michael=people.PeopleClass("Michael",makeCards(5))



print(len(deck))
#print(Daniel.getDeck())

currentCard=makeCards(1)
print("this Is the Current Card:")
print(currentCard[0].getRank(),currentCard[0].getSuit())

print("please choose you card")
num=1
for i in Daniel.getDeck():
    print(num,".",i.getRank(),i.getSuit())
    num+=1
chooseCard=input("choose a card")
try:
    chooseCard=int(chooseCard)
except:
    print("")
chooseCard-=1
if (Daniel.getDeck()[chooseCard]).getRank() == currentCard[0].getRank():
    print("match")
    currentCard=Daniel.getDeck()[chooseCard]
    Daniel.removeCard(Daniel.getDeck()[chooseCard])
    
else:
    print("you pick up a card")






