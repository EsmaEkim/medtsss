import random

def roll():
    minValue=1
    maxValue=6
    roll=random.randint(minValue,maxValue)

    return roll

while True:
    players=input("Gib die Anzahl der Spieler ein (2 - 4):")
    if players.isdigit():
       players=int(players)
       if 2 <= players <= 4:
           break  
       else:
           print("Es müssen zwischen 2 und 4 Spieler sein.")
    else:
        print("Ungültig, versuche es erneut.")

maxScore=50
playerScors=[0 for _ in range(players)]

totalscore="Deine Gesamtpunktzahl ist:"

while max(playerScors)<maxScore:

 for playerIdx in range(players):
    print("\nDer Spieler",playerIdx +1, "ist gerade am Zug!")
    print(totalscore,playerScors[playerIdx],"\n")
    currentScore=0

    while True:
        shouldRoll= input("Möchtest du werfen (j)?")
        if shouldRoll.lower()=="j":
           break
    
        value=roll()
        if value==1:
           print("Du hast eine 1 geworfen! Zug beendet!")
           currentScore=0
           break
        else:
           currentScore += value
           print("Du hast eine geworfen:",value)
           print("Deine Punktzahl ist:",currentScore)

    playerScors[playerIdx] +=currentScore
    print("Deine Gesamtpunktzahl ist:",playerScors[playerIdx])
maxScore=max(playerScors)
winningIdx=playerScors.index(maxScore)
print("Die Spielerzahl",winningIdx + 1, "ist der Gewinner mit einer Punktzahl von:", maxScore)