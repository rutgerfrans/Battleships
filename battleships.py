#Zeeslag
#Windows OS
#Rutger de Groen
################


import turtle
import random
import sys

#Lijsten
#Lijst voor de letters en cijfers rondom het grid.
Letterlijst = [0, 'A','B','C','D','E','F','G','H','I','J']
Cijferlijst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#lijst met boten van de speler.
schip1 = [0,0,0,0,0]
schip2 = [0,0,0,0]
schip3 = [0,0,0]
schip4 = [0,0,0]
schip5 = [0,0]

#Lijsten van de boten met de coordinaten van bot1.
botschip1 = [(2,4),(2,5),(2,6),(2,7),(2,8)]
botschip2 = [(4,4),(4,5),(4,6),(4,7)]
botschip3 = [(6,8),(7,8),(8,8)]
botschip4 = [(9,2),(9,3),(9,4)]
botschip5 = [(6,2),(7,2)]
#Lijsten van de boten met de coordinaten van bot2.
bot2schip1 = [(2,2),(3,2),(4,2),(5,2),(6,2)]
bot2schip2 = [(9,5),(9,6),(9,7),(9,8)]
bot2schip3 = [(6,5),(6,6),(6,7)]
bot2schip4 = [(3,9),(4,9),(5,9)]
bot2schip5 = [(2,6),(3,6)]
#Lijsten van de boten met de coordinaten van bot3.
bot3schip1 = [(10,3),(10,4),(10,5),(10,6),(10,7)]
bot3schip2 = [(4,6),(4,7),(4,8),(4,9)]
bot3schip3 = [(1,1),(1,2),(1,3)]
bot3schip4 = [(6,8),(7,8),(8,8)]
bot3schip5 = [(5,2),(6,2)]
#Lijsten van de boten met de coordinaten van bot4.
bot4schip1 = [(6,3),(6,4),(6,5),(6,6),(6,7)]
bot4schip2 = [(2,2),(2,3),(2,4),(2,5)]
bot4schip3 = [(8,4),(9,4),(10,4)]
bot4schip4 = [(7,10),(8,10),(9,10)]
bot4schip5 = [(1,10),(2,10)]
#Lijsten van de boten met de coordinaten van bot5.
bot5schip1 = [(6,5),(7,5),(8,5),(9,5),(10,5)]
bot5schip2 = [(7,7),(7,8),(7,9),(7,10)]
bot5schip3 = [(9,8),(9,9),(9,10)]
bot5schip4 = [(3,7),(4,7),(5,7)]
bot5schip5 = [(2,2),(3,2)]
#Lijsten van de boten met de coordinaten van bot6.
bot6schip1 = [(3,10),(4,10),(5,10),(6,10),(7,10)]
bot6schip2 = [(4,2),(4,3),(4,4),(4,5)]
bot6schip3 = [(1,7),(2,7),(3,7)]
bot6schip4 = [(6,3),(7,3),(8,3)]
bot6schip5 = [(9,10),(10,10)]

#Dit zijn de lijsten om bij te houden of er een boot is gezonken of of er een helevloot is gezonken.
#Dit door de index van de nested lists te veranderen tot ze gelijk staan aan het laatste getalletje bijv 5 4 3 2.
#Als de eerste index van de laatste nested list gelijk is aan de tweede index dan is de vloot gezonken.
vlootstatus = [[0,0,0,0,0,0,5],[0,0,0,0,0,4],[0,0,0,0,3],[0,0,0,0,3],[0,0,0,2],[0,5]]
vlootbotstatus = [[0,0,0,0,0,0,5],[0,0,0,0,0,4],[0,0,0,0,3],[0,0,0,0,3],[0,0,0,2],[0,5]]

#In deze lijst komen de coordinaten rondom de geplaatste boot zodat de aankomende boten niet naast elkaar komen te liggen.
vlootcontour = []

#Dit zijn de lijsten waar de schepen/vlooten van de bot in 1 lijst worden gezet.
#Hier gaat een randomnater overheen die dan een vastgestelde vloot uitkiest waar de speler tegen moet spelen.
vloot = [schip1,schip2,schip3,schip4,schip5]
vlootbot = [botschip1,botschip2,botschip3,botschip4,botschip5]
vlootbot2 = [bot2schip1,bot2schip2,bot2schip3,bot2schip4,bot2schip5]
vlootbot3 = [bot3schip1,bot3schip2,bot3schip3,bot3schip4,bot3schip5]
vlootbot4 = [bot4schip1,bot4schip2,bot4schip3,bot4schip4,bot4schip5]
vlootbot5 = [bot5schip1,bot5schip2,bot5schip3,bot5schip4,bot5schip5]
vlootbot6 = [bot6schip1,bot6schip2,bot6schip3,bot6schip4,bot6schip5]
vlootbotlijst = [vlootbot,vlootbot2,vlootbot3,vlootbot4,vlootbot5,vlootbot6]

#Dit is een lijst die aangeeft ingame welke boot je moet plaatsen met welke lengte.
Printschepen = ['maak boot 1 (5 lang)','maak boot 2 (4 lang)','maak boot 3 (3 lang)','maak boot 4 (3 lang)','maak boot 5 (2 lang)']

#Listcor is een lijst di samenwerkt met smartcorlist. dit zijn twee lijsten waar coordinaten inkomen te staan als de bot een boot raakt. dit is om de bot slimmmer te maken.
listcor = []
smartcorlist = []

#Dit is een list waar een tijdelijke boot inkomt te staan als de bot een schip heeft geraakt. ook dit heeft als doel de bot slimmer te maken.
boot = []

#variables
endclick = False
bootgemaakt = False
corokay = False
foundoncontourvloot = False
PlayerClick = True
zelfdecor = False
BotenGeplaatst = False
Letter = 1
Cijfer = 0
vlootteller = 0
Sectry = 0
Rx = 0
Ry = 0
B = 1
dirn2 = 'reset'
minr = 0
maxr = 0
level = 0
gamemode = 0
Schipteller = 0
raakteller = 0
Gamestatus = 'reset'
HitStatus = 'Niet Geraakt'
BootGeraakt = False
RnG = random.randint(0,5)

#turtle setup
turtle.setup(1500,800)
window = turtle.Screen()
window.title('Battleships')
window.bgcolor('white')
pen1 = turtle.getturtle()
pen2 = turtle.getturtle()
pen3 = turtle.getturtle()
text = turtle.getturtle()
turtle.hideturtle()
pen1.speed(0)

#Dit zijn posities voor de bot, om de pen op de juiste plek te zetten voordat turtle de grids gaat printen.
def positie1():
    pen1.penup()
    pen1.setposition(-700, -300)
    pen1.pendown()

def positie2():
    pen2.penup()
    pen2.forward(54)
    pen2.pendown()

def positie3():
    pen2.penup()
    pen2.setposition(0, 0)
    pen2.pendown()

def positie4():
    pen2.penup()
    pen2.setposition(-646, 246)
    pen2.pendown()

def positie5():
    pen2.penup()
    pen2.setposition(-675, 210)

def positie6():
    pen2.right(90)
    pen2.penup()
    pen2.setposition(-620 , 265)
    
#Dit zijn posities voor de speler, om de pen op de juiste plek te zetten voordat turtle de grids gaat printen.
def positie7():
    pen2.penup()
    pen1.setposition(100, -300)
    pen1.pendown()

def positie8():
    pen2.penup()
    pen2.setposition(154, 246)
    pen2.pendown()

def positie9():
    pen2.penup()
    pen2.setposition(125, 210)

def positie10():
    pen2.right(90)
    pen2.penup()
    pen2.setposition(180 , 265)

def PlaatsBotenText():
    text.setposition(-550,310)
    text.write(Printschepen[vlootteller], font=("Arial", 45, "normal"))

#Dit zijn twee functie om de hokjes in te kleren tijdens het spelen.
def CollorCellBotGrey(Ty, Tx):
    D = 54.6
    Gy = 246 - (Ty-1) * D
    Gx = -700 + Tx * D
    ColorCellGrey(Gx, Gy)

def CollorCellBotRed(Ty, Tx):
    D = 54.6
    Gy = 246 - (Ty-1) * D
    Gx = -700 + Tx * D
    ColorCellRed(Gx, Gy)


#HitorSunk is een fucntie die controleert of de boten zijn gezonken of dat de hele vloot is gezonken.
#Dit doet hij doormiddel van de lijsten 'vlootstatus' en 'vlootbotstatus'.
def HitOrSunk(Ty, Tx, vloot, vlootstatus):
    global gevonden
    global HitStatus
    vlootteller = 0
    schipteller = 0
    gevonden = False
    HitStatus = 'Reset'
    while vlootteller < len(vloot) and gevonden != True:
        while schipteller < len(vloot[vlootteller]) and gevonden != True:
            #Raak?
            if vloot[vlootteller][schipteller] == (Ty, Tx):
                gevonden = True
                #Niet eerder geraakt?
                if vlootstatus[vlootteller][schipteller] == 0:
                    vlootstatus[vlootteller][schipteller] = 1
                    vlootstatus[vlootteller][-2] += 1
                    if vlootstatus[vlootteller][-2] == vlootstatus[vlootteller][-1]:
                        HitStatus = 'Boot gezonken!'
                        vlootstatus[-1][0] += 1
                        if vlootstatus[-1][0] == vlootstatus[-1][1]:
                            HitStatus = 'Vloot gezonken!'
                else:
                    HitStatus = 'Coördinaat al geraakt, raak een nieuw coördinaat!'
            schipteller += 1
        vlootteller += 1
        schipteller = 0
    return HitStatus

#Dit is een functie waarin er gecheckt wordt of de nieuw geplaatste boot niet naast de laast geplaatste boot geplaatst word.
#Inprincipe wordt er gecontroleerd of de boten niet naast elkaar liggen maar netjes met een blokje afstand.
def checkoncontour(vlootcontour, Ty, Tx):
    global foundoncontourvloot
    foundoncontourvloot = False
    for teller in range(0,len(vlootcontour)):
        if vlootcontour[teller] == (Ty, Tx):
            foundoncontourvloot = True
    return foundoncontourvloot

#In deze functie worden de omliggende coordinaten van de geplaatste boot in een lijst gezet. Zodat deze coordinaten naderhand gecontroleerd kunnen worden in de funcitie 'checkoncontour'.
#Als een boot in het midden ligt van het speel veld, zijn er geen uitzonderingen. Want alle omiggende coordinaten worden netjes in een lijst gezet.
#Als de boot tegen de border aanligt kunnen niet alle coordinaten toegevoegd worden. dus daar moesten een paar checks op gemaakt worden.
#Die checks worden gecontroleerd met 'maxi' en 'mini'. Als een cordinaat tegen de border aanligt met een x van 10, dan kan er niet een coordinaat met een x van 11 toegevoed worden in de lijst.
#Zo geld dat ook voor de kant met een x van 1, de kant met de letter A en de kant met de letter J.
def maakvlootcontour(schip, richting, dirn):
    mini =10
    maxi =1
    for teller in range(0,(len(schip))):
        if richting == 'hor':
            if schip[teller][1] < mini:
                mini = schip[teller][1]
            elif schip[teller][1] > maxi:
                maxi = schip[teller][1]
            if dirn == 1:
                vlootcontour.append((dirn+1,schip[teller][1]))
            elif dirn == 10:
                vlootcontour.append((dirn-1,schip[teller][1]))
            elif dirn != 10 and dirn != 1:
                vlootcontour.append((dirn+1,schip[teller][1]))
                vlootcontour.append((dirn-1,schip[teller][1]))             
        if richting == 'ver':
            if schip[teller][0] < mini:
                mini = schip[teller][0]
            elif schip[teller][0] > maxi:
                maxi = schip[teller][0]
            if dirn == 1:
                vlootcontour.append((schip[teller][0], dirn+1))
            elif dirn == 10:
                vlootcontour.append((schip[teller][0], dirn-1))
            elif dirn != 1 and dirn != 10:
                vlootcontour.append((schip[teller][0], dirn+1))
                vlootcontour.append((schip[teller][0], dirn-1))   
    if richting == 'hor':
        if mini == 1:
            vlootcontour.append((dirn, maxi+1))
        elif maxi == 10:
            vlootcontour.append((dirn, mini-1))
        elif mini != 1 and mini != 10:
            vlootcontour.append((dirn, mini-1))
            vlootcontour.append((dirn, maxi+1))
    elif richting == 'ver':
        if mini == 1:
            vlootcontour.append((maxi+1, dirn))
        elif maxi == 10:
            vlootcontour.append((mini-1, dirn))
        elif mini != 1 and mini != 10:
            vlootcontour.append((mini-1, dirn))
            vlootcontour.append((maxi+1, dirn))

#Dit is een functie waar de geklikte coordinaten, om een boot te maken, worden geregistreed in een lijst.
#Voor dat deze coordinaten echter toegevoegd worden aan een lijst moeten ze eerst een check doorstaan. Dat wordt gedaan met de functie 'Checkcor', die de variabele 'corokay' terug stuurt met een True of False.
#Als corokay True is dan kan de coordinaat toegevoegd worden. Zodra corokay False is houdt dat in dat de gekikte coordinaat fout geplaatst is en wordt de coordinaat niet toegevoegd.
#Meer uitleg over de functie 'checkcor' bij de functie zelf.
#In deze functie wordt de functie 'maakvlootcontour' aangeroepen. Nadat er een boot is geplaatst gaat de boot die functie in. Dan worden de contour coordinaten aangemaakt zodat de aankomende boot met een blokje afstand ernaast kan komen te liggen.    
def maakboot(schip, Ty, Tx, Gx, Gy):
    global Schipteller
    global vlootteller
    global corokay
    global richting
    global dirn
    global BotenGeplaatst
    if Schipteller != len(schip):
        corokay = Checkcor(Tx, Ty, schip, Schipteller, corokay)
        foundoncontourvloot = checkoncontour(vlootcontour, Ty, Tx)
        if corokay == True and foundoncontourvloot == False:
            schip[Schipteller] = Ty, Tx
            Schipteller += 1
            ColorCell(Gx, Gy)
            if Schipteller == len(schip):
                if vlootteller == len(Printschepen)-1:
                    maakvlootcontour(schip5, richting, dirn)
                    kleurwit()
                    text.setposition(-125,310)
                    text.write('Begin met spelen!', font=("Arial", 25, "normal"))
                    text.setposition(-465,310)
                    text.color('green')
                    text.write('Your Fleet', font=("Arial", 25, "normal"))
                    text.setposition(350,310)
                    text.color('red')
                    text.write('Enemies fleet', font=("Arial", 25, "normal"))
                    text.color('black')
                    BotenGeplaatst = True
                    richting = 'reset'
                    dirn = 0
                    Schipteller = 0
                else:
                    vlootteller += 1
                    if vlootteller == 1:
                        kleurwit()
                        text.setposition(-550,310)
                        text.write(Printschepen[vlootteller], font=("Arial", 25, "normal"))
                        maakvlootcontour(schip1, richting, dirn)
                    elif vlootteller == 2:
                        kleurwit()
                        text.setposition(-550,310)
                        text.write(Printschepen[vlootteller], font=("Arial", 25, "normal"))
                        maakvlootcontour(schip2, richting, dirn)
                    elif vlootteller == 3:
                        kleurwit()
                        text.setposition(-550,310)
                        text.write(Printschepen[vlootteller], font=("Arial", 25, "normal"))
                        maakvlootcontour(schip3, richting, dirn)
                    elif vlootteller == 4:
                        kleurwit() 
                        text.setposition(-550,310)
                        text.write(Printschepen[vlootteller], font=("Arial", 25, "normal"))
                        maakvlootcontour(schip4, richting, dirn)
                    richting = 'reset'
                    dirn = 0
                    Schipteller = 0
    return


#Deze functie gebruk is slechts om de woordjes ingame te kunnen vervangen met nieuwe woordjes. door het oude woordje in te kleuren met de backgroundcolor kan er een nieuw woord overheen geschreven worden.
def kleurwit():
    pen2.setposition(-560,360)
    pen2.penup()
    pen2.fillcolor('white')
    pen2.begin_fill()
    for i in range(2):
        pen2.forward(300)
        pen2.right(90)
        pen2.forward(60)
        pen2.right(90)
    pen2.end_fill()
    pen2.fillcolor('black')

#deze functie is om de cellen rood te kleuren als de klik raak was.
def ColorCellRed(Gx, Gy):
    Gx += 2
    Gy -= 2
    pen2.setposition(Gx, Gy)
    pen2.penup()
    pen2.fillcolor('Red')
    pen2.begin_fill()
    for i in range(4):
        pen2.forward(50.6)
        pen2.right(90)
    pen2.end_fill()

#deze funcite is om de cellen grijs te kleuren als de klik mis was.
def ColorCellGrey(Gx, Gy):
    Gx += 2
    Gy -= 2
    pen2.setposition(Gx, Gy)
    pen2.penup()
    pen2.fillcolor('Grey')
    pen2.begin_fill()
    for i in range(4):
        pen2.forward(50.6)
        pen2.right(90)
    pen2.end_fill()

#deze functie is om de cellen zwart te kleuren voor bij het plaatsen van de boten.
def ColorCell(Gx, Gy):
    Gx += 2
    Gy -= 2
    pen2.penup()
    pen2.setposition(Gx, Gy)
    pen2.begin_fill()
    for i in range(4):
        pen2.forward(50.6)
        pen2.right(90)
    pen2.end_fill()

#Deze functie is om te controleren of de schepen netjes geplaatst worden.
#Bijvoorbeeld worden de blokjes van de schepen netjes aan elkaar geplaatst.
#En de check of het schip horizontaal of verticaal geplaatst word.
    #Dit door na de tweede klik te checken of de y of de x coordinaat veranderd is.
#Als de geklikte cootdinaten kloppen dan wordt 'corokay' gereturnded met True.
def Checkcor(Tx, Ty, schip, Schipteller, corokay):
    global dirn
    global richting
    if len(schip) > 0:
        if Schipteller == 0:
            corokay = True
            richting = 'unknown'
        elif Schipteller == 1:
            if Ty - schip[Schipteller-1][0] > 1 or Ty - schip[Schipteller-1][0] < -1:
                corokay = False
            elif Tx - schip[Schipteller-1][1] > 1 or Tx - schip[Schipteller-1][1] < -1:
                    corokay = False
            else:
                corokay = True
                #y horizontaal
                if schip[0][0] == Ty:
                    dirn = Ty
                    richting = 'hor'
                #x verticaal
                elif schip[0][1] == Tx:
                    dirn = Tx
                    richting = 'ver'
        elif Schipteller > 1:
            if richting == 'hor':
                if Tx - schip[Schipteller-1][1] > 1 or Tx - schip[Schipteller-1][1] < -1:
                    corokay = False
                elif Ty != dirn:
                    corokay = False
                else:
                    corokay = True
            elif richting == 'ver':
                if Ty - schip[Schipteller-1][0] > 1 or Ty - schip[Schipteller-1][0] < -1 :
                    corokay = False
                elif Tx != dirn:
                    corokay = False
                else:
                    corokay = True
    return corokay

#Deze functie houdt bij welke boot je aan het plaatsen bent.
#Hij roept de functie 'maakboot aan' waarin de boot gemaakt wordt.
#Als de boot dan geplaatst is dan word de variabele 'vlootteller' met 1 opgehoogd. zoweet deze functie dat je met een nieuwe boot bezig bent.
def maakvlootPlayer(Gx, Gy):
    if vlootteller == 0:
        maakboot(schip1, Ty, Tx, Gx, Gy)
    elif vlootteller == 1:
        maakboot(schip2, Ty, Tx, Gx, Gy)
    elif vlootteller == 2:
        maakboot(schip3, Ty, Tx, Gx, Gy)
    elif vlootteller == 3:
        maakboot(schip4, Ty, Tx, Gx, Gy)
    elif vlootteller == 4:
        maakboot(schip5, Ty, Tx, Gx, Gy)


#Deze functie registreerd de klikken op het linker grid (Grid met player fleet).
#Dit doet hij door rij voor rij te kijken of de geklikte x en y coordinaten binnen een cell valt.
#zoja dan registreerd hij de cell.
#Zoniet dan zoekt hij verder.
def InCellLeftGrid(x, y):
    global InCellFound
    global Ty
    global Tx
    global Gx
    global Gy
    InCellFound = False
    Gx = -646
    Gy = 246
    D = 54.6
    Tx = 1
    Ty = 1
    found = False
    while found == False and Ty < 11:
        while found == False and Tx < 11:
            if x >= Gx and x < (Gx + D) and y > (Gy - D) and y <= Gy:
                found = True
            if found == False:
                Tx += 1
                Gx += D
        if found == True:
            InCellFound =True
        else:
            found = False
            Ty += 1
            Gy -= D
            Gx = -646
            Tx = 1
    return InCellFound

#Deze functie registreerd de klikken op het rechter grid (Grid met enemie fleet).
#Dit doet hij door rij voor rij te kijken of de geklikte x en y coordinaten binnen een cell valt.
#zoja dan registreerd hij de cell.
#Zoniet dan zoekt hij verder.
def InCellRightGrid(x, y):
    global InCellFound
    global Ty
    global Tx
    global Gx
    global Gy
    InCellFound = False
    Gx = 154.6
    Gy = 246
    D = 54.6
    Tx = 1
    Ty = 1
    found = False
    while found == False and Ty < 11:
        while found == False and Tx < 11:
            if x >= Gx and x < (Gx + D) and y > (Gy - D) and y <= Gy:
                found = True
            if found == False:
                Tx += 1
                Gx += D
        if found == True:
            InCellFound =True
        else:
            found = False
            Ty += 1
            Gy -= D
            Gx = 154.6
            Tx = 1
    return InCellFound

#Deze functie vult de lijst listcor met alle coordinaten op het speelveld. Deze lijst word later gebruikt om de gebruikte kliks van de boot uit deze lijst te halen
#zodat de bot niet twee keer dezelfde coordinaat kiest.
def CreateGrid(listcor):
    for i in range(1,11):
        for j in range(1,11):
            listcor.append((i,j))

#deze functie wordt gekeken welke coordinaat de bot kiest. vervolgens wordt deze coordinaat verwijderd zodat hij niet nog een keer kan worden uitgekozen.
def SmartClick(listcordinates, flag):
    global Ty
    global Tx
    maxteller = len(listcordinates)-1
    teller = random.randint(0,maxteller)
    Ty = listcordinates[teller][0]
    Tx = listcordinates[teller][1]
    del listcordinates[teller]
    if flag == 1:
       RemoveTuple(Ty, Tx, listcor)

#Deze functie wordt aangeroepen in de functie 'SmartClick'.
#Deze fucntie verwijderd het gekozen coordinaat.
def RemoveTuple(Ty, Tx, listcor):
    gevondenx = False
    tellery = 0
    while gevondenx == False and tellery < len(listcor):
        if listcor[tellery] == (Ty,Tx):
            gevondenx = True
        else:
            tellery += 1
    if gevondenx == True:
        del listcor[tellery]

#Deze functie maakt de lijst smartcorlist leeg. eigenlijk is het een reset zodat de bot bij de volgende boot zich op andere coordinaten richt.
def Emptycorlist(listcor):
    for x in range(len(listcor)):
        del listcor[0]

#In deze functie wordt een lijst aangemaakt om de bot zo slim mogelijk te maken.
#Als de bot een boot raakt is de bot nog een keer aan de beurt.
#Een mens zou als hij een boot raakt, om dit coordinaat heen gaan schieten om te kijken of de boot horizontaal ligt of verticaal.
#Dat is precies wat ik de bot hiet ook laat doen. zodra hij dan de richting heeft gevonden, worden er twee coordinaten toegevoegd aan de lijst 'smartcorlist'.
#Als de boot zou zijn: A3,A4,A5. en de boot raakt A4, en daarna raakt hij gelijk A5. dan weet de bot dat de boot horizontaal is.
#De coordinaten A3 en A6 worden in een lijst gezet. de boot gaat dan bij zijn volgende beurt alleen deze twee coordinaten proberen.
#Als de bot A6 zou kiezen mist hij. Dan wordt dit coordinaat verwijderd uit de lijst, waardoor alleen A3 nog overblijft.
#bij de volgende beurt kiest de bot A3 en zinkt de boot.
def CreateSmartlist(Ty, Tx, boot, smartcorlist):
    global dirn2
    global level
    global minr
    global maxr
    if len(boot) == 0:
        boot.append((Ty, Tx))
        if len(smartcorlist) > 0:
            Emptycorlist(smartcorlist)
        #bepaal smartlist 
        if Tx > 1:
            if tupleinlist(Ty, (Tx-1), listcor) == True:
                smartcorlist.append((Ty, (Tx-1)))#linkercor
        if Ty > 1:
            if tupleinlist((Ty-1), Tx, listcor) == True:
                smartcorlist.append(((Ty-1), Tx))#bovencor
        if Tx < 10:
            if tupleinlist(Ty, (Tx+1), listcor) == True:
                smartcorlist.append((Ty,(Tx+1)))#rechtercor
        if Ty < 10:
            if tupleinlist((Ty+1), Tx, listcor) == True:
                smartcorlist.append(((Ty+1),Tx))#ondercor
    elif len(boot) == 1:
        Emptycorlist(smartcorlist)
        boot.append((Ty, Tx))
        #bepaal orientatie en level en min range en max range
        if boot[0][0] == boot[1][0]:
            dirn2 = 'hor'
            level = boot[0][0]
            if boot[0][1] < boot[1][1]:
                maxr = boot[1][1]
                minr = boot[0][1]
            else:
                minr = boot[1][1]
                maxr = boot[0][1]
        else:
            #bepaal smartlist 
            dirn2 = 'ver'
            level = boot[0][1]
            if boot[0][0] < boot[1][0]:
                maxr = boot[1][0]
                minr = boot[0][0]
            else:
                minr = boot[1][0]
                maxr = boot[0][0]
        if dirn2 == 'hor':
            if minr > 1:
                if tupleinlist(level, (minr-1), listcor) == True:
                    smartcorlist.append((level, (minr-1)))#linkercor
            if maxr < 10:
                if tupleinlist(level, (maxr+1), listcor) == True:
                    smartcorlist.append((level, (maxr+1)))#rechtercor
        if dirn2 == 'ver':
            if minr > 1:
                if tupleinlist((minr-1), level, listcor) == True:
                    smartcorlist.append(((minr-1), level))#bovencor
            if maxr < 10:
                if tupleinlist((maxr+1), level, listcor) == True:
                    smartcorlist.append(((maxr+1), level))#ondercor
    elif len(boot) > 1:
        boot.append((Ty, Tx))
        #bepaal smartlist
        if dirn2 == 'hor':
            if Tx < minr:
                minr = Tx
                if Tx > 1:
                    if tupleinlist(level, (Tx-1), listcor) == True:
                        smartcorlist.append((level, (Tx-1)))
            elif Tx > maxr:
                maxr = Tx
                if Tx < 10:
                    if tupleinlist(level, (Tx+1), listcor) == True:
                        smartcorlist.append((level, (Tx+1)))
        if dirn2 == 'ver':
            if Ty < minr:
                minr = Ty
                if Ty > 1:
                    if tupleinlist((Ty-1), level, listcor) == True:
                        smartcorlist.append(((Ty-1), level))
            elif Ty > maxr:
                maxr = Ty
                if Ty < 10:
                    if tupleinlist((Ty+1), level, listcor) == True:
                        smartcorlist.append(((Ty+1), level))

#Met deze kleine functie word er gecheckt of de coordinaat voor de lijst 'smartcorlist' aanwezig is in de cor list. 
#zo niet dan is de coordinaat al gebruikt en hoeft hij niet meer gecheckt te worden.
def tupleinlist(Ty, Tx, inlist):
    tellerx = 0
    gevondenz = False
    while gevondenz == False and tellerx < len(inlist):
        if inlist[tellerx] == (Ty, Tx):
            gevondenz = True
        else:
            tellerx += 1
    return gevondenz

#Deze Functie is eigenlijk de stam van alle andere functies.
#Als eerste checkt deze functie of je op 'spelen' duwt of op 'stoppen'.
#Bij stoppen sluit het programma.
#Bij spelen ga je het spel spelen.
#Nadat er op spelen is geduwt kun je je boten plaatsen.
#Als alle boten zijn geplaatst wordt de variabele 'BotenGeplaatst' op True gezet.
#Dit houdt in dat het spel is begonnen en dat de speler aan de beurt is met klikken.
#Als de speler raakt is de speler nog een keer aan de beurt tot de speler mist.
#Als de speler mist is de bot aan de beurt.
#Voor de bot geld het zelfde zolang de bot raakt mag de bot nog een keer, als hij mist is de speler weer aan de beurt.
#Tussendoor worden er checks uitgevoerd om te kijken of de vloot al gezonken is.
#Als de vloot van de bot is gezonken dan krijgt de speler een scherm met de melding dat hij gewonnen heeft.
#Als de vloot van de speler is gozonken dan krijgt de speler een scherm met de melding dat hij verloren heeft.
def ZeeSlag(x, y):
    global gevonden
    global zelfdecor
    global raakteller
    global Rx 
    global Ry
    global BootGeraakt
    global HitStatus
    global gamemode
    global RnG
    found = False
    if x<=-200 and x>=-300 and y<=0 and y>=-80 and gamemode == 0:
        gamemode = 1
        pen2.clear()
        if gamemode == 1:    
            CreateGrid(listcor)    
            GridBuildPlayer()
            GridBuildBot()
            text.setposition(-550,310)
            text.write(Printschepen[vlootteller], font=("Arial", 25, "normal"))
            turtle.onscreenclick(none)
    elif x<=400 and x>=300 and y<=0 and y>=-80 and gamemode == 0:
        turtle.bye()
        exit
    InCellLeftGrid(x, y)
    if BotenGeplaatst == False:
        maakvlootPlayer(Gx, Gy)
    else:
        #speler speelt
        InCellRightGrid(x, y)
        HitOrSunk(Ty, Tx, vlootbotlijst[RnG], vlootbotstatus)
        if gevonden == True:
            ColorCellRed(Gx, Gy)
        if HitStatus == 'Vloot gezonken!':
            turtle.clearscreen()
            text.setposition(-200,0)
            text.color('green')
            text.write('Gewonnen! :)', font=("Arial", 50, "normal"))
            text.setposition(-140,-200)
            text.color('black')
            text.write('klik om te stoppen', font=("Arial", 25, "normal"))
            turtle.exitonclick()
        #Bot speelt
        if gevonden == False:
            ColorCellGrey(Gx, Gy)
            #in the case a boat has not been hit already
            if BootGeraakt == False :
                SmartClick(listcor,0)
                HitOrSunk(Ty, Tx, vloot, vlootstatus)
                if gevonden == True:
                    CollorCellBotRed(Ty, Tx)
                    BootGeraakt = True
                else:
                   CollorCellBotGrey(Ty, Tx)
            if BootGeraakt == True :
                while True:
                    if gevonden == True :
                        CreateSmartlist(Ty, Tx, boot, smartcorlist)
                    SmartClick(smartcorlist,1)
                    HitOrSunk(Ty, Tx, vloot, vlootstatus)
                    if gevonden == True:
                        CollorCellBotRed(Ty, Tx)
                        if HitStatus == 'Vloot gezonken!':
                            turtle.clearscreen()
                            text.setposition(-200,0)
                            text.color('red')
                            text.write('Verloren! :(', font=("Arial", 50, "normal"))
                            text.setposition(-140,-200)
                            text.color('black')
                            text.write('klik om te stoppen', font=("Arial", 25, "normal"))
                            turtle.exitonclick()
                        elif HitStatus == 'Boot gezonken!':
                            Emptycorlist(boot)
                            SmartClick(listcor,0)
                            HitOrSunk(Ty, Tx, vloot, vlootstatus)
                            if gevonden == False:
                                CollorCellBotGrey(Ty, Tx)
                                BootGeraakt = False
                                break
                            else:
                                CollorCellBotRed(Ty, Tx)
                                BootGeraakt = True
                    else:
                        CollorCellBotGrey(Ty, Tx)
                        break

#Dit is een functie met de commands om het hoofdmenu te tekenen.
#Het hoofdmenu bevat twee simpele vierkantjes met een tekst erboven. Spelen en Stoppen.
def MainMenuBuild():
    pen2.penup()
    pen2.setposition(300,0)
    pen2.pendown()
    for i in range(4):
        pen2.forward(100)
        pen2.right(90)
    pen2.penup()
    pen2.setposition(-300,0)
    pen2.pendown()
    for i in range(4):
        pen2.forward(100)
        pen2.right(90)
    pen2.penup()
    text.setposition(-300,20)
    pen2.pendown()
    text.write('Spelen', font=("Arial", 25, "normal"))
    pen2.penup()
    text.setposition(300,20)
    pen2.pendown()
    text.write('Stoppen', font=("Arial", 25, "normal"))

#Deze functie bouwt simpelweg het speelveld van de speler.
#Een grid van 10 bij 10 met de bijbehorende letters en cijfers voor de coordinaten aanduiding.
def GridBuildPlayer():
    global Letter
    global Cijfer
    positie1()
    for i in range(4):
        pen1.forward(600)
        pen1.left(90)

    positie2()
    for i in range(4):
        pen2.forward(546)
        pen2.left(90)

    positie4()
    for i in range(5):
        pen2.forward(54.6)
        pen2.right(90)
        pen2.forward(546)
        pen2.left(90)
        pen2.forward(54.6)
        pen2.left(90)
        pen2.forward(546)
        pen2.right(90)
    for i in range(5):
        pen2.right(90)
        pen2.forward(54.6)
        pen2.right(90)
        pen2.forward(546)
        pen2.left(90)
        pen2.forward(54.6)
        pen2.left(90)
        pen2.forward(546)
    pen2.left(90)
    positie5()
    for i in range(10):
        pen2.write(Letterlijst[Letter])
        pen2.backward(54.6)
        Letter += 1
    positie6()
    for i in range(10):
        pen2.write(Cijferlijst[Cijfer])
        pen2.forward(54.6)
        Cijfer += 1

#Deze functie bouwt simpelweg het speelveld van de bot.
#Een grid van 10 bij 10 met de bijbehorende letters en cijfers voor de coordinaten aanduiding.
def GridBuildBot():
    positie7()
    for i in range(4):
        pen1.forward(600)
        pen1.left(90)
        
    positie2()
    for i in range(4):
        pen2.forward(546)
        pen2.left(90)

    positie8()
    for i in range(5):
        pen2.forward(54.6)
        pen2.right(90)
        pen2.forward(546)
        pen2.left(90)
        pen2.forward(54.6)
        pen2.left(90)
        pen2.forward(546)
        pen2.right(90)
    for i in range(5):
        pen2.right(90)
        pen2.forward(54.6)
        pen2.right(90)
        pen2.forward(546)
        pen2.left(90)
        pen2.forward(54.6)
        pen2.left(90)
        pen2.forward(546)

    pen2.left(90)

    positie9()
    Letter = 1
    for i in range(10):
        pen2.write(Letterlijst[Letter])
        pen2.backward(54.6)
        Letter += 1

    positie10()
    Cijfer = 0
    for i in range(10):
        pen2.write(Cijferlijst[Cijfer])
        pen2.forward(54.6)
        Cijfer += 1
        
#Deze Aanroep tekent het hoofdmenu.
MainMenuBuild()

#Dit is de klik die de Functie 'ZeeSlag' triggered.
turtle.onscreenclick(ZeeSlag)

#Dit is de cheatcode die in idle de coordinaten van de schepen print.
print('\n=========================\nCheatCode\n=========================\nSchip 1 (5 lang):',vlootbotlijst[RnG][0],'\nSchip 2 (4 lang):',vlootbotlijst[RnG][1],'\nSchip 3 (3 lang):',vlootbotlijst[RnG][2], '\nSchip 4 (3 lang):',vlootbotlijst[RnG][3],'\nSchip 5 (2 lang):',vlootbotlijst[RnG][4])
