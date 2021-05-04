
def zenCount():
    card = input("Press/input anything to start (type 'end' to quit): ")
    cardSum = 0
    
    print("Allowed values: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A")
    while card != 'end':
        card = input("Insert card num or first letter or name: ")
        card = card.lower()
        card = card.replace(" ", "")
        
        #print(card.isalpha())
        if card.isalpha() == False:
            card = int(card)
            
            if card < 4 or card == 7:
                cardSum += 1
                print("Card sum/count: " + str(cardSum))
            elif card >= 4 and card <= 6:
                cardSum += 2
                print("Card sum/count: " + str(cardSum))
            elif card == 10:
                cardSum += -2
                print("Card sum/count: " + str(cardSum))
            elif card == 8 or card == 9: 
                cardSum += 0
                print("Card sum/count: " + str(cardSum))
            else:
                print("Improper input, nonreal card")
            print("")
        
        else:
            if card == "end" or card=="quit":
                print("Card sum/count: " + str(cardSum))
                return
            if card == "a":
                cardSum += -1
                print("Card sum/count: " + str(cardSum))
            elif card == "j" or card == "k" or card == "q":
                cardSum += -2
                print("Card sum/count: " + str(cardSum))
            else:
                print("Improper input, nonreal card")
            print("")
            
    """""""""""""""""""""""""""""""""
    2  3  4  5  6  7  8  9  10,j,k,q    A
    1, 1, 2, 2, 2, 1, 0 ,0     -2       -1
    """""""""""""""""""""""""""""""""

def hiLo():
    card = input("Press/input anything to start (type 'end' to quit): ")
    cardSum = 0
    
    print("Allowed values: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A")
    while card != 'end':
        card = input("Insert card num or first letter or name: ")
        card = card.lower()
        card = card.replace(" ", "")
        
        #print(card.isalpha())
        if card.isalpha() == False:
            card = int(card)
            
            if card < 7:
                cardSum += 1
                print("Card sum/count: " + str(cardSum))
            elif card < 10 and card > 6:
                cardSum += 0
                print("Card sum/count: " + str(cardSum))
            elif card == 10:
                cardSum += -1
                print("Card sum/count: " + str(cardSum))
            else:
                print("Improper input, nonreal card")
            print("")
        
        else:
            if card == "end" or card =="quit":
                print("Card sum/count: " + str(cardSum))
                return
            if card == "a" or card == "j" or card == "k" or card == "q":
                cardSum += -1
                print("Card sum/count: " + str(cardSum))
            else:
                print("Improper input, nonreal card")
            print("")
    """""""""""""""""""""""""""""""""
    2  3  4  5  6  7  8  9  10,j,k,q, A
    1, 1, 1, 1, 1, 0, 0 ,0     -1
    """""""""""""""""""""""""""""""""

def main():
    print("Select card strategy: ")
    print("    1) Hi-Lo")
    print("    2) Zen Count")
    strategy = input("Type the number: ")
    
    strategy = strategy.replace(" ", "") #remove whitespace
 
    
    while strategy != "end":
        if strategy == "1":
            print("starting hiLo")
            hiLo()
        elif strategy == "2":
            print("starting zenCount")
            zenCount()
        
        strategy = input("Use again or end (type 'end' to end): ")
        strategy = strategy.replace(" ", "")
        strategy = strategy.lower()
    
    quit()
        
   
if __name__ == "__main__":
    main()