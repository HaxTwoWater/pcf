#DEBUT

#On admet la fonction random qui retourne un nombre aléatoire entre deux nombres donner en parametre
#On admet la fonction input qui prend en paramètre les entrées utilisateurs que nous pouvons assigner a des variables

#Definir la classe pfcGame

    #Definir la fonction gameIntro
        #Afficher "Bienvenue sur le Pierre Feuille Ciseau"
        #Afficher "Tapez 1 pour voir les règles | tapez 2 pour choisir le mode de jeu et la difficulté"
        #Assigner a x la valeur input
        #Essaie de la structure conditonelle suivante
            #Switch de x
                #cas de x est égal a 1
                    #Alors retour de l'execution de la fonction gameRule
                #cas de x est égal a 2
                    #Alors retour de l'execution de la fonction gameMode
                #autre cas
                    #Alors 
                    #Afficher "Mauvais chiffre n'oubliez pas 1 ou 2, retour à l'introduction"
                    #Retour de l'execution de la fonction intro
        #Exception en cas d'erreur de l'essaie
            #Afficher "Erreur mauvais type de valeur rentrer"
            #Retour de l'execution de la fonction gameIntro

    #Definir la fonction gameRule
        #Afficher "--------------Règles du jeu--------------"
        #Afficher "Dans le jeu du pierre feuille ciseau vous avez donc 3 options à chaque round pour jouer :"
        #Afficher "La pierre battant le ciseau, le ciseau battant la feuille et la feuille battand donc la pierre"
        #Afficher "Cela est pour le mode normal, mais dans notre jeu nous avons ajouter le mode puit, ou l'option du puit est ajouter"
        #Afficher "Le puit bat la pierre et le ciseau mais est battue par la feuille. Voila c'est tout pour les règles une fois celles ci bien comprises"
        #Afficher "Tu peux retourner retourner au menu d'introduction en entrant 1 puis dans les modes de jeux pour commencer à jouer ! Bon jeu :p "
        #Assigner a x la valeur input
        #Essaie de la structure conditonelle suivante
            #Si x est égal à 1
                #Alors retour de l'execution de la fonction gameIntro
            #Sinon
                #Alors
                #Afficher "Hop hop hop c'est 1 qui faut mettre pas un autre chiffre"
                #Alors retour de l'execution de la fonction gameRule
        #Exception en cas d'erreur de l'essaie
            #Afficher "Erreur mauvais type de valeur rentrer"
            #Retour de l'execution de la fonction gameRule

    #Definir la fonction printMode
        #On initialise a la liste modeTab et on y assigne la valeur "1-Normal" à l'index 0, la valeur "2-Le jeu du Puit" à l'index 1, la valeur "3-Multijoueur" à l'index 2 et la valeur "4-Multijoueur X Puit" à l'index 3
        #Assigner a i la valeur 0
        #Tant que i n'est pas supérieur au retour de l'execution de la fonction len avec pour parametre modeTab
            #Alors
            #Afficher modeTap d'index i
            #Incrementer i de 1

    #Definir la fonction printDiff
        #On initialise a la liste diffTab et on y assigne la valeur "1-Facile" à l'index 0, la valeur "2-Impossible"
        #Tant que i n'est pas supérieur au retour de l'execution de la fonction len avec pour parametre diffTab
            #Alors
            #Afficher diffTap d'index i, j
            #Incrementer i et j de 1 

    #Definir la fonction gameMode
        #Afficher "---------------Mode de jeu---------------"
        #Afficher "Il est vrai qu'habituellement le pierre feuille ciseau ne contient qu'un mode de jeu"
        #Afficher "mais le notre en possède plusieurs ainsi que plusieurs difficulté"
        #Afficher "Pour les modes de jeu :"
        #Retour de l'execution de la fonction printMode
        #Afficher "Et pour les difficultés :"
        #Retour de l'execution de la fonction printDiff
        #Afficher "Veuillez mainentant renseigner votre choix"
        #Assigner a x la valeur input
        #Essaie de la structure conditonelle suivante
            #Si x est égal a 1 ou 2
                #Alors retour de l'execution de la fonction match avec comme parametre x
            #SI sinon x est égal a 3 ou 4
                #Alors retour de l'execution de la fonction matchMulti avec comme parametre x
            #Sinon
                #Alors 
                #Afficher "Mauvais nombre lisez bien les options"
                #Retour de l'execution de la fonction gameMode
        #Exception en cas d'erreur de l'essaie
            #Afficher "Erreur mauvais type de valeur rentrer"
            #Retour de l'execution de la fonction gameMode

    #Definir la fonction match avec comme parametre x
        #Afficher "Votre match commence sous peu veuillez choisir la difficulté de l'IA"
        #Retour de l'execution de la fonction printDiff
        #Assigner a x input
        #On initalise playerLife de valeur 3
        #Assigner 
        #Essaue de la structure conditionelle suivante
            #Tant que playerLife > 1
                #Alors
                #Retour de l'execution de la fonction round avec pour parametre playerChoice

    #Definir la fonction matchMulti avec comme parametre y

    #Definir la fonction gameStart avec comme parametre z quelconque 

#FIN

#Definir la fonction round de parametre playerChoice et player1Winner
    #On initialise la variable player1Score avec la valeur 0
    #On initialise la variable player2Score avec la valeur 0

    #Switch player1Choice
        #cas 1
            #Assigner a player2Choice le retour de la fonction iaDiff de parametre player1Choice
            #Switch player2Choice
                #cas 1
                    #Afficher "Vous avez tout les deux joué pierre, il y a donc égalité"
                    #Incrementer player1Score et player2Score d'un
                #cas 2
                    #Afficher "Tu as joué pierre et l'ordinateur feuille, tu as donc perdue"
                    #Incrementer player2score d'un
                #cas 3
                    #Afficher "Tu as joué pierre et l'ordinateur ciseau, tu as donc gagné"
                    #Incrementer player1Score d'un
        #cas 2
            #Assigner a player2Choice le retour de la fonction iaDiff de parametre player1Choice
            #Switch player2Choice
                #cas 1
                    #Afficher "Tu as joué feuille et l'ordinateur pierre, tu as donc gagné"
                    #Incrementer player1score d'un
                #cas 2
                    #Afficher "Vous avez tout les deux joué feuille, il y a donc égalité"
                    #Incrementer player1Score et player2Score d'un
                #cas 3
                    #Afficher "Tu as joué feuille et l'ordinateur ciseau, tu as donc perdue"
                    #Incrementer player2Score d'un
        #cas 3
            #Assigner a player2Choice le retour de la fonction iaDiff de parametre player1Choice
            #Switch player2Choice
                #cas 1
                    #Afficher "Tu as joué ciseau et l'ordinateur pierre, tu as donc perdue"
                    #Incrementer player2score d'un
                #cas 2
                    #Afficher "Tu as joué ciseau et l'ordinateur feuille, tu as donc gagné"
                    #Incrementer player1score d'un
                #cas 3
                    #Afficher "Vous avez tout les deux joué ciseau, il y a donc égalité"
                    #Incrementer player1Score et player2Score d'un
    
    #Si player1Score > player2Score
        #Alors player1Winner est égal a True
    #Sinon
        #Alors player1winner est égal a False
    
    #Retourner player1Winner


#Definir la fonction iaDiff
    #Assigner a choice le retour de la fonction random de parametre 1, 10
    #Si
