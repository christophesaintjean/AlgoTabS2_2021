"""
Algorithm:
Create a list of all walls, and create a set for each cell, each containing just that one cell.
For each wall, in some random order:
    If the cells divided by this wall belong to distinct sets:
    Remove the current wall.
    Join the sets of the formerly divided cells.
    Test end of generation.
"""
import random
import itertools as it
from turtle import *
from my_set import *

def draw_walls(walls, N, scale):
    # A faire

def find_set(cells, ij):
    # A faire
    

if __name__ == "__main__":
    N = 50
    walls = [(i,j,o) for i, j, o in it.product(range(N), range(N), [0, 1])]
    cells = [[(i,j)] for i, j in it.product(range(N), range(N))]
    start = (0, 0)
    end = (N-1, N-1)
    
    while walls:
        i_wall = random.randint(0, len(walls)-1)
        i, j, o = walls[i_wall]
        i_set1 = find_set(cells, (i, j))
        if o == 0 and i < N -1:
            i_set2 = find_set(cells, (i+1,j))
        elif o == 1 and j < N -1:
            i_set2 = find_set(cells, (i,j+1))
        else:
            continue
        if cells[i_set1][0] != cells[i_set2][0]:
            # A faire:
            # Reunir set1 et set2 
            # MAJ cells
            # MAJ wallsunion = set_union(cells[i_set1], cells[i_set2])
            # Faire ici terminer le while si nécessaire
    print(walls)
    draw_walls(walls, N, scale=5)
        
        