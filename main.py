#DEBUT

#On admet la fonction random qui retourne un nombre aléatoire entre 1 et 2
#On admet la fonction input qui prend en paramètre les entrées utilisateurs que nous pouvons assigner a des variables

#Definir la classe pfcGame

    #Definir la fonction gameIntro
        #Afficher le retour de l'execution de la fonction print avec pour parametre "Bienvenue sur le Pierre Feuille Ciseau"
        #Afficher le retour de l'execution de la fonction print avec pour parametre "Tapez 1 pour voir les règles | tapez 2 pour choisir le mode de jeu et la difficulté"
        #Assigner a x la valeur input
        #Essaie de la structure conditonelle suivante
            #Switch de x
                #cas de x est égal a 1
                    #Alors retour de l'execution de la fonction gameRule
                #cas de x est égal a 2
                    #Alors retour de l'execution de la fonction gameMode
                #autre cas
                    #Alors 
                    #Afficher le retour de l'execution de la fonction print avec pour parametre "Mauvais chiffre n'oubliez pas 1 ou 2, retour à l'introduction"
                    #Retour de l'execution de la fonction intro
        #Exception en cas d'erreur de l'essaie
            #Afficher le retour de l'execution de la fonction print avec pour parametre "Erreur mauvais type de valeur rentrer"
            #Retour de l'execution de la fonction gameIntro

    #Definir la fonction gameRule
        #Afficher le retour de l'execution de la fonction print avec pour parametre "--------------Règles du jeu--------------"
        #Afficher le retour de l'execution de la fonction print avec pour parametre "Dans le jeu du pierre feuille ciseau vous avez donc 3 options à chaque round pour jouer :"
        #Afficher le retour de l'execution de la fonction print avec pour parametre "La pierre battant le ciseau, le ciseau battant la feuille et la feuille battand donc la pierre"
        #Afficher le retour de l'execution de la fonction print avec pour parametre "Cela est pour le mode normal, mais dans notre jeu nous avons ajouter le mode puit, ou l'option du puit est ajouter"
        #Afficher le retour de l'execution de la fonction print avec pour parametre "Le puit bat la pierre et le ciseau mais est battue par la feuille. Voila c'est tout pour les règles une fois celles ci bien comprises"
        #Afficher le retour de l'execution de la fonction print avec pour parametre "Tu peux retourner retourner au menu d'introduction en entrant 1 puis dans les modes de jeux pour commencer à jouer ! Bon jeu :p "
        #Assigner a x la valeur input
        #Essaie de la structure conditonelle suivante
            #Si x est égal à 1
                #Alors retour de l'execution de la fonction gameIntro
            #Sinon
                #Alors
                #Afficher le retour de l'execution de la fonction print avec pour prametre "Hop hop hop c'est 1 qui faut mettre pas un autre chiffre"
                #Alors retour de l'execution de la fonction gameRule
        #Exception en cas d'erreur de l'essaie
            #Afficher le retour de l'execution de la fonction print avec pour parametre "Erreur mauvais type de valeur rentrer"
            #Retour de l'execution de la fonction gameRule

    #Definir la fonction printMode
        #Assigner à la variable modeTab une liste à deux entrées avec 
            # --------------tableau----------------
            #--------------------------------------
            #--------------------------------------
        # A VOIR AVEC ALEXANDRE /!\ <---------------

        #Assigner a i et a j la valeur 0
        #Tant que i n'est pas supérieur au retour de l'execution de la fonction len avec pour parametre modeTab
            #Alors
            #Afficher le retour de l'execution de la fonction print avec pour parametre modeTap d'index i, j
            #Incrementer i et j de 1
        #Retourner la liste modeTab

    #Definir la fonction printDiff
        # MEME CHOSE QU'AU DESSUS

        #Assigner a i et a j la valeur 0
        #Tant que i n'est pas supérieur au retour de l'execution de la fonction len avec pour parametre diffTab
            #Alors
            #Afficher le retour de l'execution de la fonction print avec pour parametre diffTap d'index i, j
            #Incrementer i et j de 1
        #Retourner la liste diffTab

    #Definir la fonction gameMode
        #Afficher le retour de l'execution de la fonction print avec pour parametre "---------------Mode de jeu---------------"
        #Afficher le retour de l'execution de la fonction print avec pour parametre "Il est vrai qu'habituellement le pierre feuille ciseau ne contient qu'un mode de jeu"
        #Afficher le retour de l'execution de la fonction print avec pour parametre "mais le notre en possède plusieurs ainsi que plusieurs difficulté"
        #Afficher le retour de l'execution de la fonction print avec pour parametre "Pour les modes de jeu :"
        #Retour de l'execution de la fonction printMode
        #Afficher le retour de l'execution de la fonction print avec pour parametre "Et pour les difficultés :"
        #Retour de l'execution de la fonction printDiff

    #Definir la fonction gameStart avec comme parametre x quelconque 

#FIN