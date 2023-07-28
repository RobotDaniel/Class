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
        p1 = deck[random.randint(0,len(deck)-1)] 
        CardsList.append(p1)
        deck.remove(p1)
        
        
    return CardsList




#print(len(deck))
#print(Daniel.getDeck())

def play(Player,card):
    num=1
    print(card[0].getRank(),",",card[0].getSuit())
    
    print(Player.getName(),"is playing")
    for i in Player.getDeck():
        
        print(num,".",i.getRank(),i.getSuit())
        
        num+=1
    print("6 . skip go")
    chooseCard=input("choose a card")
    try:
        chooseCard=int(chooseCard)
    except:
        print("")
        play(Player,card)
    checkCard(Player,card,chooseCard)
    
    

    
    
    
    
def checkCard(Player,card,chooseCard):
    if chooseCard == 6:
        #play(Player,card)
        checkWin(Player,card)
    elif (Player.getDeck()[chooseCard-1]).getRank() == card[0].getRank():
        print("match")
        card=Player.getDeck()[chooseCard-1]
        Player.removeCard(Player.getDeck()[chooseCard-1])
        
    else:
        print("you pick up a card")
        Player.addCard(makeCards(1))
        #play(Player,card)
    checkWin(Player,card)
def checkWin(Player,card):
    if len(Player.getDeck()) == 0:
        return True,card
    else:
        return False,card    
def main(): 
    Daniel=people.PeopleClass("Daniel",makeCards(5))
    Michael=people.PeopleClass("Michael",makeCards(5))
    startingCard=makeCards(1)
    win,card = play(Daniel,startingCard)
    while win == False:
        win, card = play(Michael,card)
        if win == True:
            break
        win, card = play(Daniel,card)
        if win == True:
            break 
main()





