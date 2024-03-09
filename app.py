import os
import time
import random

def create_grid(width, height, mode='random', custom_cells=[]):
    """Créer une nouvelle grille (tableau 2D) avec les dimensions données."""
    grid = [[0 for _ in range(width)] for _ in range(height)]
    
    if mode == 'random':
        return [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]
    elif mode == 'custom':
        for cell in custom_cells:
            if 0 <= cell[0] < height and 0 <= cell[1] < width:
                grid[cell[0]][cell[1]] = 1
        return grid

def print_grid(grid):
    """Imprimer la grille dans la console avec des carrés."""
    border = "+" + "--" * len(grid[0]) + "+"
    print(border)
    for row in grid:
        print('|' + ''.join(['██' if cell else '  ' for cell in row]) + '|')
    print(border)
    print("\n")

def count_neighbors(grid, x, y):
    """Compter le nombre de voisins vivants autour d'une cellule donnée."""
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]):
                count += grid[x + i][y + j]
    return count

def get_custom_cells():
    """Permettre à l'utilisateur de définir des cellules vivantes."""
    cells = []
    print("Entrez les coordonnées des cellules vivantes sous la forme 'x,y'. Tapez 'fin' pour terminer.")
    while True:
        input_str = input()
        if input_str.lower() == 'fin':
            break
        try:
            x, y = map(int, input_str.split(','))
            cells.append((x, y))
        except ValueError:
            print("Format invalide. Veuillez entrer les coordonnées sous la forme 'x,y'.")
    return cells
    
def update_grid(grid):
    """Mettre à jour la grille pour la génération suivante."""
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            neighbors = count_neighbors(grid, i, j)
            if cell:
                if neighbors in [2, 3]:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid

def main():
    width, height = 20, 10  # Taille de la grille
    mode = input("Choisissez le mode de démarrage ('random' ou 'custom'): ")
    if mode == 'custom':
        custom_cells = get_custom_cells()
        grid = create_grid(width, height, mode, custom_cells)
    else:
        grid = create_grid(width, height)

    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_grid(grid)
            grid = update_grid(grid)
            time.sleep(0.5)  # Ajustez ceci pour contrôler la vitesse de la simulation
    except KeyboardInterrupt:
        print("Simulation du Jeu de la Vie terminée.")

if __name__ == "__main__":
    main()
