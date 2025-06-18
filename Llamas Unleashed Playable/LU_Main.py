deck = []
from PIL import Image
discard = []
hand_1 = []
hand_2 = []
field_1 = []
field_2 = []
chain = []
import os
os.system("cls")
import sqlite3
import random
conn = sqlite3.connect('.database/data_source.db')
c = conn.cursor()
for row in c.execute('SELECT id, amount FROM Actual_Card_List WHERE id > 12'):
    i = 0
    while i < int(row[1]):
        deck.append(row[0])
        i+=1
random.shuffle(deck)
print(deck)

def draw_hands():
    for i in range(5):
        hand_1.append(deck[0])
        deck.pop(0)
        hand_2.append(deck[0])
        deck.pop(0)
def print_hand(k):
    if k == 1:
        for i in hand_1:
            sql = "SELECT name FROM Actual_Card_List WHERE id = " + str(i)
            c.execute(sql)
            print(str(c.fetchone()))
    elif k == 2:
        for i in hand_2:
            sql = "SELECT name FROM Actual_Card_List WHERE id = " + str(i)
            c.execute(sql)
            print(str(c.fetchone()))

#im = Image.open(r"C:\Users\dexter\Desktop\myPWA\public\Llamas_unleashed_Cards\A Basic Catapult.png")
#im.show()


draw_hands()
print(deck)
print_hand(1)
