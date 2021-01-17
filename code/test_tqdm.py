# tqdm a installer
#from tqdm import tqdm                   # programme python classique
#from tqdm.notebook import tqdm           # dans un notebook
from tqdm.gui import tqdm               # pour thonny
from time import sleep
from random import randint

for i in tqdm(range(5), desc='Boucle sur i'):
    for j in tqdm(range(3), desc=f'Boucle sur j', leave=False):
        duree_sommeil = randint(1, 2)
        sleep(duree_sommeil)