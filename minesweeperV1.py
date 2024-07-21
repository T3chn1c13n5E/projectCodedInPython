## Importer les bibliotheques
import pygame   # Importation de la bibliotheque 'pygame' pour crer des jeux en Python.
import random   # Importation de la bibliotheque 'random' pour generer des positions aleatoire pour les mines.

## Initialisation de Pygame
pygame.init()   # Initialise tous les modules de Pygame.

## Parametres du jeu
SIZE = 10                           # Definit la taille de la grille de jeu a 10x10.
MINES = 10                          # Definit le nombre de mines a placer sur la grille.
CELL_SIZE = 40                      # Definit la taille de chaque cellule en pixels.
SCREEN_SIZE = SIZE * CELL_SIZE      # Calcule l taille totale de l'ecran en pixels.

## Couleurs
# Definition des couleurs utilisees dans le jeu sous forme de tubles RGB.
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

## Initialisation de l'ecran
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))    # Cree la fenetre de jeu avec les dimensions definies.
pygame.display.set_caption('Minesweeper V1')                    # Definit le titre de la fenetre de jeu.

## Police pour le texte
font = pygame.font.SysFont(None, 36)    # Definit la police et la taille du texte a afficher.

## Creation de la grille de jeu
grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]              # Cree une grille de jeu 2D initalisee a 0.
revealed = [[False for _ in range(SIZE)] for _ in range(SIZE)]      # Cree une grille 2D pour suivre quelles cellules sont revelees, initialisee a 'False'.

## Placement des mines
def place_mines():                                                          # Definition de la fonction pour placer les mines.
    count = 0                                                               # Initialise un compteur pour les mins placees.
    while count < MINES:                                                    # Boucle jusqu'a ce que toutes les mines soient placees.
        x, y = random.randint(0, SIZE - 1), random.randint(0, SIZE -1)      # Genere des coordonnees aleatoires dans la grille.
        if grid[x][y] != -1:                                                # Verifie si la cellule ne contient pas deja une mines.
            grid[x][y] = -1                                                 # Place une mine dans la cellule (representee par -1).
            count += 1                                                      # Incremente le compteur de mines placees.
            update_numbers(x, y)                                            # Appelle la fonction 'update_numbers' pour mettre a jour les numeros autour de la mine placee.

## Mise a jour des numeros
def update_numbers(x, y):                                   # Definition de la fonction pour mettre a jour les numeros autour d'une mine.
    for i in range(max(0, x -1), min(SIZE, x + 2)):         # Parcour les lignes autour de la mine.
        for j in range(max(0, y -1), min(SIZE, y + 2)):     # Parcourt les colonnes autour de la mine.
            if grid[i][j] != -1:                            # Verifie que la cellule n'est pas une mine.
                grid[i][j] += 1                             # Incremente le numero de la cellule pour indiquer une mine adjacente.

## Dessiner la grille
def draw_grid():                                                                                            # Definition de la fonction pour dessiner la grille de jeu.
    for i in range(SIZE):                                                                                   # Parcourt les lignes de la grille.
        for j in range(SIZE):                                                                               # Parcourt les colonnes de la grille.
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)                          # Cree un rectangle pour chaque cellule.
            pygame.draw.rect(screen, WHITE, rect)                                                           # Dessine chaque cellule en blanc.
            pygame.draw.rect(screen, BLACK, rect, 1)                                                        # Dessine les contours des cellules en noir.
            if revealed[i][j]:                                                                              # Si la cellule est revelee
                if grid[i][j] == -1:                                                                        # Si c'est une mine, dessine un cercle rouge.
                    pygame.draw.circle(screen, RED, rect.center, CELL_SIZE // 3)
                else:                                                                                       # Sinon, dessine le numero de mines adjacentes.
                    text = font.render(str(grid[i][j]), True, BLACK)
                    screen.blit(text, (j * CELL_SIZE + CELL_SIZE // 4, i * CELL_SIZE + CELL_SIZE // 4))

## Reveler une cellule
def reveal_cell(x, y):                                                      # Definition de la fonction pour reveler une cellule.
    if not revealed[x][y]:                                                  # Si la cellule n<est pas deja revelee. 
        revealed[x][y] = True                                               # Marque la cellule comme revelee.
        if grid[x][y] == -1:                                                # Si c'est la une mine, retoune 'False'.
            return False
        elif grid[x][y] == 0:                                               # Si c'est une cellule vide, revele recursivement les cellules adjacentes.
            for i in range(max(0, x -1), min(SIZE, x + 2)):
                for j in range(max(0, y - 1), min(SIZE, y + 2)):
                    reveal_cell(i, j)
    return True                                                             # Retourne 'True' si la cellule n'est pas une mine.

## Verification de la victoire
def check_victory():                                            # Definition de la fonction pour verifier la victoire.
    for i in range(SIZE):                                       # Parcourt les lignes de la grille.
        for j in range(SIZE):                                   # Parcourt les colonnes de la grille. 
            if grid[i][j] != -1 and not revealed[i][j]:         # Si une cellule non minee n<est pas revelee, retourne 'False'.
                return False
    return True                                                 # Si toutes les cellules non minees sont revelees, retourne 'True'.

## Placer les mines sur la grille
place_mines()                           # Appelle de la fonction pour placer les mines sur la grille.

## Boucle principale du jeu
running = True                                                              # Indique si le jeu est en cours d'execution.
game_over = False                                                           # Indique si le jeu est termine.
while running:                                                              # Boucle principale du jeu.
    for event in pygame.event.get():                                        # Parcourt tous les evenements.
        if event.type == pygame.QUIT:                                       # Si l'utilisateur ferme la fenetre, arrete le jeu.
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:        # Si l'utilisateur clique et que le jeu n'est pas termine.
            x, y = event.pos                                                # Recupere la position du clic.
            x //= CELL_SIZE                                                 # Convertit la position en coordonnees de la grille.
            y //= CELL_SIZE                                                 # Convertit la position en coordonnees de la gilles.
            if not reveal_cell(y, x):                                       # Revele la cellule cliquee et verifie si c'est une mine.
                game_over = True                                            # Si c'est une mine, Partie terminee.

## Dessiner la grille et verifier la victoire
    screen.fill(GRAY)                           # Remplit l'ecran de la couleur grise.
    draw_grid()                                 # Dessine la grille de jeu.

    if check_victory() and not game_over:       # Si le joueur a gagne et que le jeu n'est pas termine.
        game_over = True                        # Partie terminee.
        print("You Win!")                       # Affiche "You Win!" dans la console.
    pygame.display.flip()                       # Met a jour l'affichage de l'ecran.

## Quiter le jeu
pygame.quit()               # Ferme proprement Pygame.