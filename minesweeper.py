## Importer les bibliotheques
import tkinter as tk        # Importation de la bibliotheque tkinter, utilisee pour creer l<interface graphique.
import random               # Importation de la bibliotheque random, utilisee pour generer des positions aleatoires pour les mines.

## Classe Minesweeper
class Minesweeper:          # Declaration de la classe Minesweeper qui contiendra toute la logique et l'interface du jeu.
    
    ## Initialisation    
    def __init__(self, master, size=10, mines=10):                  # Methode d'innitalisation de la classe, qui est appelee lorsqu'un objet de la classe est cree.
        self.master = master                                        # Reference a la fenetre principale tkinter.
        self.size = size                                            # Taille de la grille (par defaut 10x10).
        self.mines = mines                                          # Nombre de mines dans la grille (par defaut 10).
        self.grid = [[0 for _ in range(size)] for _ in range(size)]                     # Creation d'une grille de jeu 2d initialisee a 0.
        self.buttons = [[None for _ in range(size)] for _ in range(size)]               # Creation d<une grille de boutons tkinter initialisee a None.
        self.place_mines()                                                              # Appel de la methode place_mine pour placer les mines.
        self.create_widgets()                                                           # Appel de la methode create_widgets pour creer
    
    ## Placer les mines
    def place_mines(self):                                                          # Methode pour placer les mines dans la grille.
        count = 0                                                                   # Compteur de mines placees.
        while count < self.mines:                                                   # Boucle jusqu'a ce que toutes les mines soient placees.
            x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)   # Genere des coordonnees aleatoire dans la grille.
            if self.grid[x][y] != -1:                                               # Verifie si la cellule ne contient pas deja une mine.
                self.grid[x][y] = -1                                                # Place une mine dans la cellule (representee par -1)
                count +=1                                                           # Incremente le compteur de mines placees.
                self.update_numbers(x,y)                                            # Met a jour les numeros autour de la mine placee.

    ## Mettre a jour les numeros
    def update_numbers(self, x, y):                                 # Methode pour mettre a jour les numeros autour d'une mine
        for i in range(max(0, x-1), min(self.size, x+2)):           # Parcourt les lignes autour de la mine.
            for j in range(max(0, y-1), min(self.size, y+2)):       # Parcourt les colonnes autour de la mine.
                if self.grid[i][j] != -1:                           # Verifie que la cellule n'est pas une mine.
                    self.grid[i][j] += 1                            # Incremente le numer de la cellule pour indiquer une mine adjacente.
    
    ## Creer les widgets (boutons)
    def create_widgets(self):                                                                           # Methode pour creer les boutons de l'interface.
        for i in range(self.size):                                                                      # Parcourt les lignes de la grille.
            for j in range(self.size):                                                                  # Parcourt les colonnes de la grille.
                button = tk.Button(self.master, width=2, command=lambda x=i, y=j: self.click(x,y))      # Cree un bouton pour chaque cellule, avec une largeur de 2 et une commande pour gerer les clics.
                button.grid(row=i, column=j)                                                            # Place le bouton a la position (i,j) dans la grille.
                self.buttons[i][j] = button                                                             # Enregistre le bouton dans la grille de boutons.

    ## Gerer les clics
    def click(self, x, y):                                                              # Methode pour gerer les clics sur les boutons.
        if self.grid[x][y] == -1:                                                       # Verifie si la cellule cliquee contient une mine.
            self.buttons[x][y].config(text='M', bg='red')                               # Change le texte du bouton pour afficher 'M' et le fond en rouge pour indiquer une mine.
            print("Game Over")                                                          # Affiche "Game Over" dans la console.
        else:                                                                           # Si la cellule ne contient pas de mine.
            self.buttons[x][y].config(text=str(self.grid[x][y]),state="disabled")       # Change le texte du bouton pour afficher le numero de mines adjacentes et desactive le bouton.

## Creer la fenetre principale et demarrer le jeu
root = tk.Tk()                  # Cree la fenetre principale tkinter.
game = Minesweeper(root)        # Cree une instance du jeu de demineur.
root.mainloop()                 # Demarre la boucle principale de l'interface graphique.
