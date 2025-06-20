import pygame
def inits():
    global hand_1 
    hand_1 = []
    global hand_2
    hand_2 = []
    global hands
    hands = [hand_1, hand_2]
    global field_1
    field_1 = []
    global field_2
    field_2 = []
    global fields 
    fields = [field_1, field_2]
    global deck
    deck = []
    global deck_amount
    import sqlite3
    import random
    global c
    conn = sqlite3.connect('.database/data_source.db')
    c = conn.cursor()
    for row in c.execute('SELECT id, amount FROM Actual_Card_List WHERE id > 12'):
        i = 0
        while i < int(row[1]):
            card_id = row[0]
            deck_amount = len(deck)
            while deck_amount == len(deck):
                if card_id in deck:
                    card_id += 1000
                else:
                    deck.append(card_id)
            i+=1
    random.shuffle(deck)
    global gy
    gy = []
    global chain
    chain = []
    global selected_cards
    selected_cards = []
    global top_of_gy
    top_of_gy = ""
    global turn
    turn = 1
    global game_start
    game_start = False
    global discard
    discard = False
    global play
    play = False
    global beginning_of_turn
    beginning_of_turn = False
    global draw_step
    draw_step = False
    global action_step
    action_step = False
    global End_of_turn_step
    End_of_turn_step = False
    global choice
    choice = False
    global a
    a = ""
    global b
    b = ""
    global sprites
    sprites = pygame.sprite.Group()
    global screen
    screen = pygame.display.set_mode((1280, 720))
    global clock
    clock = pygame.time.Clock()
    global font
    font = pygame.font.SysFont('comicsans', 40)
    global lock 
    lock = False
    global into_play
    into_play = False
    global type_check
    type_check = "none"
    global card 
    card = 0
    global player_choice
    player_choice = False
    global target_player
    target_player = 3
    global target
    target = False
    global effect
    effect = []
