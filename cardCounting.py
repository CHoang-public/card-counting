

def getCountMethod(cVal, mode, currSum):
    
    returnValue = currSum
    
    if mode == "zen":
        returnValue = zenCount(cVal, currSum)
        #print("rv: " + str(returnValue))
        return returnValue

    elif mode == "HiLo":
        returnValue = hiLo(cVal, currSum)
        #print("rv: " + str(returnValue))
        return returnValue

    elif mode == "ko":
        returnValue = koCount(cVal, currSum)
        #print("rv: " + str(returnValue))
        return returnValue

    #print("rv: " + str(return_value))
    



def zenCount( cVal, cardSum ):
    
    card = cVal
    retVal = cardSum
     #print(card.isalpha())

    if card.isalpha() == False:
        card = int(card)   
        
        if card < 4 or card == 7:
            retVal = retVal + 1
            #print("Card sum/count: " + str(cardSum))
        elif card >= 4 and card <= 6:
            retVal = retVal + 2
            #print("Card sum/count: " + str(cardSum))
        elif card == 10:
            retVal = retVal - 2
            #print("Card sum/count: " + str(cardSum))
        elif card == 8 or card == 9: 
            retVal = retVal + 0
            #print("Card sum/count: " + str(cardSum))
        
    elif card == "a":
        retVal = retVal - 1
        #print("Card sum/count: " + str(cardSum))
    elif card == "j" or card == "k" or card == "q":
        retVal = retVal - 2
        #print("Card sum/count: " + str(cardSum))
    
    
    #print("zen rv: " + str(retVal))
    return retVal

    """""""""""""""""""""""""""""""""
    2  3  4  5  6  7  8  9  10,j,k,q    A
    1, 1, 2, 2, 2, 1, 0 ,0     -2       -1
    """""""""""""""""""""""""""""""""



def hiLo( cVal, cardSum ):
    
    card = cVal
    
    retVal = cardSum
    
        #print(card.isalpha())
    if card.isalpha() == False:
        card = int(card)
            
        if card < 7:
            retVal += 1
            #print("Card sum/count: " + str(cardSum))
        elif card < 10 and card > 6:
            retVal += 0
            #print("Card sum/count: " + str(cardSum))
        elif card == 10:
            retVal += -1
            #print("Card sum/count: " + str(cardSum))
       
    elif card == "a" or card == "j" or card == "k" or card == "q":
        retVal += -1
        #print("Card sum/count: " + str(cardSum))
    
    
    return retVal
    """""""""""""""""""""""""""""""""
    2  3  4  5  6  7  8  9  10,j,k,q, A
    1, 1, 1, 1, 1, 0, 0 ,0     -1
    """""""""""""""""""""""""""""""""


def koCount( cVal, cardSum ):
    card = cVal
    
    retVal = cardSum
    
        #print(card.isalpha())
    if card.isalpha() == False:
        card = int(card)
            
        if card <= 7:
            retVal += 1
            #print("Card sum/count: " + str(cardSum))
        elif card == 10:
            retVal += -1
            #print("Card sum/count: " + str(cardSum))
       
    elif card == "a" or card == "j" or card == "k" or card == "q":
        retVal += -1
        #print("Card sum/count: " + str(cardSum))
    
    
    return retVal


"""""""""""""""""""""""""""""""""
    2  3  4  5  6  7  8  9  10,j,k,q, A
    1, 1, 1, 1, 1, 0, 0 ,0     -1
    """""""""""""""""""""""""""""""""



def main():

    testcardSum = 0
    testcardSum += getCountMethod("2", "HiLo", testcardSum)
    #print("Final: " + str(testcardSum))

        
   
if __name__ == "__main__":
    main()
