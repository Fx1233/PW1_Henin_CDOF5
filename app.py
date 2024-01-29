import os
import time
import random

def create_grid(width, height):
    """Créer une nouvelle grille (tableau 2D) avec les dimensions données."""
    return [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]

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
