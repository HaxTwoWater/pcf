#DEBUT

#On admet la fonction random qui retourne un nombre aléatoire entre deux nombres donner en parametre
import random
#On admet la fonction input qui prend en paramètre les entrées utilisateurs que nous pouvons assigner a des variables




#On initialise highScore de valeur 0
# highScore = 0

#Definir la fonction gameIntro
def gameIntro():
    #Afficher "Bienvenue sur le Pierre Feuille Ciseau"
    print("Bienvenue sur le Pierre Feuille Ciseau")
    #Afficher "Tapez 1 pour voir les règles | tapez 2 pour choisir le mode de jeu et la difficulté"
    print("Tapez 1 pour voir les règles | tapez 2 pour choisir le mode de jeu et la difficulté")
    # print("Meilleur score actuel est de : " + str(highScore) + " !")
    #Assigner a x la valeur input
    x = int(input())
    #Switch de x
    #cas de x est égal a 1
    if x == 1:
        #Alors retour de l'execution de la fonction gameRule
        gameRule()
    #cas de x est égal a 2
    elif x == 2:
        #Alors retour de l'execution de la fonction gameMode
        gameMode()
    #autre cas
    else:
        #Alors 
        #Afficher "Mauvais chiffre n'oubliez pas 1 ou 2, retour à l'introduction"
        print("Mauvais chiffre n'oubliez pas 1 ou 2, retour à l'introduction")
        #Retour de l'execution de la fonction intro

#Definir la fonction gameRule
def gameRule():
    #Afficher "--------------Règles du jeu--------------"
    print("--------------Règles du jeu--------------")
    #Afficher "Dans le jeu du pierre feuille ciseau vous avez donc 3 options à chaque round pour jouer :"
    print("Dans le jeu du pierre feuille ciseau vous avez donc 3 options à chaque round pour jouer :")
    #Afficher "La pierre battant le ciseau, le ciseau battant la feuille et la feuille battand donc la pierre"
    print("La pierre battant le ciseau, le ciseau battant la feuille et la feuille battand donc la pierre")
    #Afficher "Cela est pour le mode normal, mais dans notre jeu nous avons ajouter le mode puit, ou l'option du puit est ajouter"
    print("Cela est pour le mode normal, mais dans notre jeu nous avons ajouter le mode puit, ou l'option du puit est ajouter")
    #Afficher "Le puit bat la pierre et le ciseau mais est battue par la feuille. Voila c'est tout pour les règles une fois celles ci bien comprises"
    print("Le puit bat la pierre et le ciseau mais est battue par la feuille. Voila c'est tout pour les règles une fois celles ci bien comprises")
    #Afficher "Tu peux retourner retourner au menu d'introduction en entrant 1 puis dans les modes de jeux pour commencer à jouer ! Bon jeu :p "
    print("Tu peux retourner retourner au menu d'introduction en entrant 1 puis dans les modes de jeux pour commencer à jouer ! Bon jeu :p ")
    #Assigner a x la valeur input
    x = int(input())
    if x == 1:
    #Si x est égal à 1
        gameIntro()
        #Alors retour de l'execution de la fonction gameIntro
    #Sinon
    else:
        #Alors
        #Afficher "Hop hop hop c'est 1 qui faut mettre pas un autre chiffre"
        print("Hop hop hop c'est 1 qui faut mettre pas un autre chiffre")
        #Alors retour de l'execution de la fonction gameRule
        gameRule()

#Definir la fonction printMode
def printMode():
    #On initialise a la liste modeTab et on y assigne la valeur "1-Normal" à l'index 0, la valeur "2-Le jeu du Puit" à l'index 1, la valeur "3-Multijoueur" à l'index 2 et la valeur "4-Multijoueur X Puit" à l'index 3
    modeTab = ["1-Normal", "2-Le jeu du Puit(Soon)", "3-Multijoueur", "4-Multijoueur X Puit(Soon)"]
    #Assigner a i la valeur 0
    i = 0
    #Tant que i est inférieur au retour de l'execution de la fonction len avec pour parametre modeTab
    while i < len(modeTab):
        #Alors
        #Afficher modeTab d'index i
        print(modeTab[i])
        #Incrementer i de 1
        i = i + 1

#Definir la fonction printDiff
def printDiff():
    #On initialise a la liste diffTab et on y assigne la valeur "1-Facile" à l'index 0, la valeur "2-Impossible"
    diffTab = ["1-Facile", "2-Normal", "3-Impossible"]
    #Assigner a i la valeur 0
    i = 0
    #Tant que i est inférieur au retour de l'execution de la fonction len avec pour parametre diffTab
    while i < len(diffTab):
        #Alors
        #Afficher diffTab d'index i
        print(diffTab[i])
        #Incrementer i de 1 
        i = i + 1

#Definir la fonction gameMode
def gameMode():
    #Afficher "---------------Mode de jeu---------------"
    print("---------------Mode de jeu---------------")
    #Afficher "Il est vrai qu'habituellement le pierre feuille ciseau ne contient qu'un mode de jeu"
    print("Il est vrai qu'habituellement le pierre feuille ciseau ne contient qu'un mode de jeu")
    #Afficher "mais le notre en possède plusieurs ainsi que plusieurs difficulté"
    print("mais le notre en possède plusieurs ainsi que plusieurs difficulté")
    #Afficher "Pour les modes de jeu :"
    print("Pour les modes de jeu :")
    #Retour de l'execution de la fonction printMode
    printMode()
    #Afficher "Veuillez mainentant renseigner votre choix"
    print("Veuillez mainentant renseigner votre choix vous pouvez aussi revenir au menu en entrant 0")
    #Assigner a gameModeChoice la valeur input
    gameModeChoice = int(input())
    #Si gameModeChoice est égal a 1 ou 2
    if gameModeChoice == 1 or gameModeChoice == 2:
        #Alors retour de l'execution de la fonction match avec comme parametre x
        match(gameModeChoice)
    #SI sinon x est égal a 3 ou 4
    elif gameModeChoice == 3 or gameModeChoice == 4:
        #Alors retour de l'execution de la fonction matchMulti avec comme parametre x
        matchMulti(gameModeChoice)
    elif gameModeChoice == 0:
        gameIntro()
    #Sinon
    else:
        #Alors 
        #Afficher "Mauvais nombre lisez bien les options"
        print("Mauvais chiffre lisez bien les options")
        #Retour de l'execution de la fonction gameMode
        gameMode()

#Definir la fonction match avec comme parametre x
def match(x):
    #Afficher "Votre match commence sous peu veuillez choisir la difficulté de l'IA"
    print("Votre match commence sous peu veuillez choisir la difficulté de l'IA")
    #Retour de l'execution de la fonction printDiff
    printDiff()
    #Afficher "Choisissez la difficulté souhaité :"
    print("Choisissez la difficulté souhaité :")
    #Assigner a diffChoice input
    diffChoice = int(input())
    #On initalise playerLife de valeur 3
    playerLife = 3
    #On initialise playerScore de valeur 0
    playerScore = 0
    #Tant que playerLife > 1
    while playerLife >= 1:
        #Alors
        #Afficher "Score actuel " et playerScore
        print("Score actuel " + str(playerScore))
        print("Quel coup voulez-vous jouer ? (1-Pierre 2-Feuille 3-Ciseau)")
        moveChoice = int(input())
        iaMove = iaDiff(diffChoice, moveChoice)
        if iaMove == 1:
            if moveChoice == 1:
                print("Vous avez tout les deux joué pierre, il y a donc égalité tu ne perds pas de vie mais tu ne gagnes pas de points")
            elif moveChoice == 2:
                print("Tu as joué feuille et l'ordinateur pierre, tu as donc gagné")
                playerScore = playerScore + 1
            elif moveChoice == 3:
                playerLife = playerLife - 1
                print("Tu as joué ciseau et l'ordinateur pierre, tu as donc perdue une vie plus que " + str(playerLife) + " !")
            else:
                print("Mauvaise valeur retour au match")
                match(x)
        elif iaMove == 2:
            if moveChoice == 1:
                playerLife = playerLife - 1
                print("Tu as joué pierre et l'ordinateur feuille, tu as donc perdue une vie plus que " + str(playerLife) + " !")
            elif moveChoice == 2:
                print("Vous avez tout les deux joué feuille, il y a donc égalité tu ne perds pas de vie mais tu ne gagnes pas de points")
            elif moveChoice == 3:
                print("Tu as joué ciseau et l'ordinateur feuille, tu as donc gagné")
                playerScore = playerScore + 1
            else:
                print("Mauvaise valeur retour au match")
                match(x)
        elif iaMove == 3:    
            if moveChoice == 1:
                print("Tu as joué pierre et l'ordinateur ciseau, tu as donc gagné")
                playerScore = playerScore + 1
            elif moveChoice == 2:
                playerLife = playerLife - 1
                print("Tu as joué feuille et l'ordinateur ciseau, tu as donc perdue une vie plus que " + str(playerLife) + " !")
            elif moveChoice == 3:
                print("Vous avez tout les deux joué ciseau, il y a donc égalité tu ne perds pas de vie mais tu ne gagnes pas de points")
            else:
                print("Mauvaise valeur retour au match")
                match(x)
    print("Très beau match !")
    # if playerScore > highScore:
    #     print("Vous avez carrément dépasser le record depuis que le jeu est lancé qui était de " + str(highScore) + " avec un score de " + str(playerScore) + " !")
    #     highScore = playerScore
    # else:
    #     notEnough = highScore - playerScore
    #     print("Vous n'avez pas dépasser le record actuel qui est de " + str(highScore) + " retentez votre chance la prochaine fois il ne vous manquez que " + str(notEnough) + " !")
    restart = int(input("Voulez-rejouer? si oui entrez 1 et vous serrez renvoyer au menu sinon entrer n'importe quoi d'autre et le jeu s'arrêtera"))
    if restart == 1:
        gameIntro()
    else:
        print("Merci d'avoir jouer à notre jeu !")

            

#Definir la fonction matchMulti avec comme parametre x
def matchMulti(playerChoice):
    print("COming soon")
    gameIntro()
    # if playerChoice == 3:
    #     print("")
    # else:
    #     print("Soon")
    #     gameMode()

#Definir la fonction iaDiff(diffValue, playerMove)
def iaDiff(diffValue, playerMove):
    if diffValue == 1:
        #Assigner a choice le retour de l'execution de la fonction random de parametre 1, 10
        iaChoice = random.randint(1,10)
        if iaChoice > 8:
            return 3
        elif iaChoice > 6:
            return 2
        else:
            return 1
    elif diffValue == 2:
        diffValue = random.randint(1,2)
        if diffValue == 1:
            diffValue = 1
            iaDiff(diffValue,playerMove)
        else:
            diffValue = 3
            iaDiff(diffValue,playerMove)
    elif diffValue == 3:
        if playerMove == 1:
            return 2
        elif playerMove == 2:
            return 3
        else: 
            return 1
            

#Retour de l'execution de la fonction gameIntro
gameIntro()
#FIN