
from sys import modules
from typing import Text
import PySimpleGUI as sgui
import cardCounting


layout = [ 
            [sgui.Text("Card Counting Demonstration", justification="center")],
            [sgui.Text("Default Mode: Zen Count", size=(25, 1), key="currModeText")],
            [sgui.Button("Zen Count"), sgui.Button("Hi Lo"), sgui.Button("KO")],
            [sgui.HorizontalSeparator(pad=(10,25))], 
            [sgui.Text("Card Values", pad=((0,0), (0,10)) )],
            [sgui.Button("2", size=(3,1)), sgui.Button("3", size=(3,1)), sgui.Button("4", size=(3,1)), sgui.Button("5", size=(3,1)), sgui.Button("6", size=(3,1))],
            [sgui.Button("7", size=(3,1)), sgui.Button("8", size=(3,1)), sgui.Button("9", size=(3,1)), sgui.Button("10", size=(3,1))],
            [sgui.Button("J", size=(3,1)), sgui.Button("Q", size=(3,1)), sgui.Button("K", size=(3,1)), sgui.Button("A", size=(3,1))],
            [sgui.Text("Current Value: 0", size=(20,1), pad=((0,0), (10,0)), key="_total_")],
            [sgui.Text("Change in Sum: 0", size=(20,1), key="_changeInSum_")],
            [sgui.Button("Reset Sum", pad=(10,10)) ]
        ]

 

def sguiTest():

    mode = "zen"
    cardSum = 0
    oldSum = 0

    window = sgui.Window("Card Counting", layout, size=(400,400))
    
    while True:
        event, values = window.read()

        if event == "Exit" or event == sgui.WIN_CLOSED:
            break
        
        elif event == "Zen Count":
            mode = "zen"
            window["currModeText"].Update(value="Current Mode: Zen Count" )

        elif event == "Hi Lo":
            mode = "HiLo"
            window["currModeText"].Update("Current Mode: Hi Lo Count")
        elif event == "KO":
            mode = "ko"
            window["currModeText"].Update("Current Mode: KO Count")


        elif event =="Reset Sum":
            cardSum = 0
            window.Element("_total_").Update("Current Sum: 0")
            window.Element("_changeInSum_").Update("Change in Sum: 0")


        elif event == "2":
            oldSum = cardSum
            cardSum = cardCounting.getCountMethod("2", mode, cardSum)
            window.Element("_total_").Update("Current Sum: " + str(cardSum))
            window.Element("_changeInSum_").Update("Change in Sum: " + str( cardSum-oldSum ) )

        elif event == "3":
            oldSum = cardSum
            cardSum = cardCounting.getCountMethod("3", mode, cardSum)
            window.Element("_total_").Update("Current Sum: " + str(cardSum))
            window.Element("_changeInSum_").Update("Change in Sum: " + str( cardSum-oldSum ) )

        elif event == "4":
            oldSum = cardSum
            cardSum = cardCounting.getCountMethod("4", mode, cardSum)
            window.Element("_total_").Update("Current Sum: " + str(cardSum))
            window.Element("_changeInSum_").Update("Change in Sum: " + str( cardSum-oldSum ) )

        elif event == "5":
            oldSum = cardSum
            cardSum = cardCounting.getCountMethod("5", mode, cardSum)
            window.Element("_total_").Update("Current Sum: " + str(cardSum))
            window.Element("_changeInSum_").Update("Change in Sum: " + str( cardSum-oldSum ) )

        elif event == "6":
            oldSum = cardSum
            cardSum = cardCounting.getCountMethod("6", mode, cardSum)
            window.Element("_total_").Update("Current Sum: " + str(cardSum))
            window.Element("_changeInSum_").Update("Change in Sum: " + str( cardSum-oldSum ) )

        elif event == "7":
            oldSum = cardSum
            cardSum = cardCounting.getCountMethod("7", mode, cardSum)
            window.Element("_total_").Update("Current Sum: " + str(cardSum))
            window.Element("_changeInSum_").Update("Change in Sum: " + str( cardSum-oldSum ) )

        elif event == "8":
            oldSum = cardSum
            cardSum = cardCounting.getCountMethod("8", mode, cardSum)
            window.Element("_total_").Update("Current Sum: " + str(cardSum))
            window.Element("_changeInSum_").Update("Change in Sum: " + str( cardSum-oldSum ) )

        elif event == "9":
            oldSum = cardSum
            cardSum = cardCounting.getCountMethod("9", mode, cardSum)
            window.Element("_total_").Update("Current Sum: " + str(cardSum))
            window.Element("_changeInSum_").Update("Change in Sum: " + str( cardSum-oldSum ) )
        
        elif event == "10":
            oldSum = cardSum
            cardSum = cardCounting.getCountMethod("10", mode, cardSum)
            window.Element("_total_").Update("Current Sum: " + str(cardSum))
            window.Element("_changeInSum_").Update("Change in Sum: " + str( cardSum-oldSum ) )

        elif event == "K":
            oldSum = cardSum
            cardSum = cardCounting.getCountMethod("k", mode, cardSum)
            window.Element("_total_").Update("Current Sum: " + str(cardSum))
            window.Element("_changeInSum_").Update("Change in Sum: " + str( cardSum-oldSum ) )

        elif event == "A":
            oldSum = cardSum
            cardSum = cardCounting.getCountMethod("a", mode, cardSum)
            window.Element("_total_").Update("Current Sum: " + str(cardSum))
            window.Element("_changeInSum_").Update("Change in Sum: " + str( cardSum-oldSum ) )

        elif event == "J":
            oldSum = cardSum
            cardSum = cardCounting.getCountMethod("j", mode, cardSum)
            window.Element("_total_").Update("Current Sum: " + str(cardSum))
            window.Element("_changeInSum_").Update("Change in Sum: " + str( cardSum-oldSum ) )

        elif event == "Q":
            oldSum = cardSum
            cardSum = cardCounting.getCountMethod("q", mode, cardSum)
            window.Element("_total_").Update("Current Sum: " + str(cardSum))
            window.Element("_changeInSum_").Update("Change in Sum: " + str( cardSum-oldSum ) )

    window.close()
    return (mode, cardSum)



def main():

    m_mode, cardSum = sguiTest()
    print("mode: " + m_mode)
    print("Card Sum: " + str(cardSum)) 

    quit()
        
   
if __name__ == "__main__":
    main()