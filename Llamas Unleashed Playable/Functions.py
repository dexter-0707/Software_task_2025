from pygame.locals import * # type: ignore
import pygame
import random
import sqlite3
conn = sqlite3.connect('.database/data_source.db')
c = conn.cursor()
pygame.init()
font = pygame.font.SysFont('comicsans', 40)

def draw(k, n, hands, deck):
    for i in range(n):
        hands[k-1].append(deck[0])
        deck.pop(0)
def draw_hands(hand_1, hand_2, deck, sprites):
    for i in range(8):
        hand_1.append(deck[0])
        deck.pop(0)
        hand_2.append(deck[0])
        deck.pop(0)
    sprites.add(Card(pygame.Rect(50,150,130,180), 0, "is_deck"))
def print_hand(k, sprites, hand_1, hand_2, screen):
    for i in sprites:
        if i.type != "button" and i.type != "notice":
            if i.position == "hand":
                i.kill()
    position = 210
    spacing = 0
    if k == 1:
        if len(hand_1) > 4:
            spacing = (650)/(len(hand_1)-1)
        else:
            position += 650/(len(hand_1)+1)
            spacing = (650)/(5)
        for i in hand_1:
            sprites.add(Card(pygame.Rect(int(position),500,210,300), str(i), "hand"))
            position += spacing
        position = 210
        if len(hand_2) > 4:
            spacing = (650)/(len(hand_2)-1)
        else:
            position += 650/(len(hand_2)+1)
            spacing = (650)/(5)
        for i in hand_2:
            a = pygame.image.load('public/Llamas_unleashed_Cards/Z_Card_Back.png')
            a = pygame.transform.smoothscale(a, (210,300))
            screen.blit(a,(position,-250))
            position += spacing
    elif k == 2:
        if len(hand_2) > 4:
            spacing = (650)/(len(hand_2)-1)
        else:
            position += 650/(len(hand_2)+1)
            spacing = (650)/(5)
        for i in hand_2:
            sprites.add(Card(pygame.Rect(int(position),500,210,300), str(i), "hand"))
            position += spacing
        position = 210
        if len(hand_1) > 4:
            spacing = (650)/(len(hand_1)-1)
        else:
            position += 650/(len(hand_1)+1)
            spacing = (650)/(5)
        for i in hand_1:
            a = pygame.image.load('public/Llamas_unleashed_Cards/Z_Card_Back.png')
            a = pygame.transform.smoothscale(a, (210,300))
            screen.blit(a,(position,-250))
            position += spacing
    sprites.draw(screen) 
def reprint_hand(k, n, sprites, screen, hand_1, hand_2):
    position = 210
    spacing = 0
    sprites.draw(screen)
    screen.fill("purple")
    if n:
        gy_change(n, screen)
    if k == 1:
        if len(hand_2) > 4:
            spacing = (650)/(len(hand_2)-1)
        else:
            position += 650/(len(hand_2)+1)
            spacing = (650)/(5)
        for i in hand_2:
            a = pygame.image.load('public/Llamas_unleashed_Cards/Z_Card_Back.png')
            a = pygame.transform.smoothscale(a, (210,300))
            screen.blit(a,(position,-250))
            position += spacing
    elif k == 2:
        if len(hand_1) > 4:
            spacing = (650)/(len(hand_1)-1)
        else:
            position += 650/(len(hand_1)+1)
            spacing = (650)/(5)
        for i in hand_1:
            a = pygame.image.load('public/Llamas_unleashed_Cards/Z_Card_Back.png')
            a = pygame.transform.smoothscale(a, (210,300))
            screen.blit(a,(position,-250))
            position += spacing
def card_change(k, screen):
    a = int(k)
    while a >= 1000:
        a -= 1000
    sql = "SELECT image FROM Actual_Card_List WHERE id = " + str(a)
    c.execute(sql)
    card = str(c.fetchone())
    image = pygame.image.load('public/'+ str(card[2:-3]))
    image = pygame.transform.smoothscale(image, (260,360))
    screen.blit(image,(1000,90))
def gy_change(k, screen):
    a = int(k)
    while a >= 1000:
        a -= 1000
    sql = "SELECT image FROM Actual_Card_List WHERE id = " + str(a)
    c.execute(sql)
    card = str(c.fetchone())
    image = pygame.image.load('public/'+ str(card[2:-3]))
    image = pygame.transform.smoothscale(image, (130,180))
    screen.blit(image,(50,400))
def print_chain(sprites, chain, screen):
    for i in sprites:
        if i.type != "notice":
            if i.position == "chain":
                i.kill()
    position = 210
    spacing = 0
    if len(chain) > 4:
        spacing = (650)/(len(chain)-1)
    else:
        position += 650/(len(chain)+1)
        spacing = (650)/(5)
    for i in chain:
        sprites.add(Card(pygame.Rect(int(position),120,210,300), str(i), "chain"))
        position += spacing
    sprites.draw(screen)
def print_field(k, sprites, fields, screen):
    if k == 0:
        a = 1
    else:
        a = 0
    win_1 = 0
    win_2 = 0
    for i in sprites:
        if i.type != "button" and i.type != "notice":
            if i.position == "field":
                i.kill()
    position = 270 + 610/(len(fields[k])+1)
    spacing = (610)/(len(fields[k])+1)
    for i in fields[k]:
            sprites.add(Card(pygame.Rect(int(position),350,70,100), str(i), "field"))
            position += spacing
    position = 270 + 610/(len(fields[a])+1)
    spacing = (610)/(len(fields[a])+1)
    for i in fields[a]:
        sprites.add(Card(pygame.Rect(int(position),70,70,100), str(i), "field",True))
        position += spacing
    sprites.draw(screen)
    for i in sprites:
        if i.type != "notice":
            if i.type[2:-3] == "animal" and i.position == "field":
                if i.flip == False:
                    win_1 += 1
                else:
                    win_2 += 1
    if win_1 >=7:
        return "turn win"
    elif win_2 >= 7:
        return "other win"
    else:
        return ""
def animal_played(k):
    to_return = "a"
    while k > 1000:
        k-=1000
    if k in [17, 18, 19, 20, 24, 25, 26, 30, 31, 33, 34, 35, 36, 38, 40, 41, 42, 43, 44, 45, 46, 91, 94, 95, 96, 97, 99, 102, 104, 105]:
        to_return = "b"
    return to_return
def make_choice(sprites, player_choice):
    if player_choice == False:
        sprites.add(Button("blue", "yellow", pygame.Rect(435,240,150,100),"yes", "Yes", "black"))
        sprites.add(Button("blue", "yellow", pygame.Rect(635,240,150,100),"no", "No", "black"))
        sprites.add (Button("blue", "blue", pygame.Rect(410,100,400,100), "none", "Use Card Effect?", "black"))
    else: 
        sprites.add(Button("blue", "yellow", pygame.Rect(435,240,150,100),"you", "You", "black"))
        sprites.add(Button("blue", "yellow", pygame.Rect(635,240,150,100),"opponent", "Opponent", "black"))
        sprites.add (Button("blue", "blue", pygame.Rect(410,100,400,100), "none", "Choose a player", "black"))


def animal_effects(k,t, hands, gy, deck, fields,sprites,screen, hand_1, hand_2, top):
    to_return = "a"
    while k > 1000:
        k-=1000
    if k == 17:
        draw(t,1, hands, deck)
    elif k == 18:
        for n in hands[t-1]:  
            gy.append(n)
            global top_of_gy
            top_of_gy = n
        for n in range(len(hands[t-1])):
            hands[t-1].pop(0)            
        draw(t,3, hands, deck)
    elif k == 19:
        pass
    elif k == 20:
        to_return = ["play", "alpaca", "hand"]
    elif k == 25:
        to_return = ["play", "goat", "hand"]
    elif k == 31: 
        draw(t,3, hands, deck)
        try: 
            draw(t-1,1, hands, deck)
        except:
            draw(t+1,1, hands, deck)
    elif k == 33:
        to_return = ["play", "llama", "hand"]
    elif k == 41: 
        to_return = ["discard", "self", "any"]
    elif k == 44:
        to_return = ["play", "ram", "hand"]
    elif k == 95:
        a = random.randint(1,12)
        while (a in fields[0]) or (a in fields[1]):
            a += 1000
        fields[t-1].append(a)
        print_field(t-1,sprites,fields,screen)
        reprint_hand(t, top, sprites, screen, hand_1, hand_2)
    elif k == 105:
        to_return = ["discard", "target", "all"]
    return to_return
def magic_effects(k, t, hands, gy, deck, fields,sprites,screen, hand_1, hand_2, top):
    to_return = "a"
    while k > 1000:
        k-=1000
    if k == 66:
        a = False
        if gy:
            if len(gy) >= 2:
                for i in sprites:
                    if i.type != "notice":
                        if i.position == "field" and i.flip == False and i.animal_type[2:-3] == "goat":
                            a = True
            if a == True:
                hands[t-1].append(gy[-1])
                gy.pop()
            hands[t-1].append(gy[-1])
            gy.pop()
            global top_of_gy
            top_of_gy = gy[-1]
    return to_return
def begin_turn_effects(k):
    pass
def optional_effects(k,t, hands, gy, deck):
    if k == 18:
        for i in hands[t-1]:  
            gy.append(i)
            global top_of_gy
            top_of_gy = i
        for i in range(len(hands[t-1])):
            hands[t-1].pop(0)            
        draw(t,3, hands, deck)

class Card(pygame.sprite.Sprite):
    def __init__(self, rect, id, position, flip =False, type = "", animal_type = "", outline = "yellow"):
        super().__init__()
        self.outline = outline
        self.id = id
        self.position = position
        self.flip = flip
        self.type = type
        self.animal_type = animal_type
        self.image = pygame.Surface(rect.size)
        tmp_rect = pygame.Rect(0, 0, *rect.size)
        a = int(self.id)
        while a >= 1000:
            a -= 1000
        self.targ = self._create_image(tmp_rect, self.outline, a)
        self.org = self._create_image(tmp_rect, "none", a)
        self.image = self.org
        self.rect = rect
    def _create_image(self, rect, outline, a ):
        img = pygame.Surface(rect.size)
        if a != 0:
            sql = "SELECT type FROM Actual_Card_List WHERE id = " + str(a)
            c.execute(sql)
            self.type = str(c.fetchone())
            if (self.type[2:-3]) == "animal":
                sql = "SELECT animal_type FROM Actual_Card_List WHERE id = " + str(a)
                c.execute(sql)
                self.animal_type = str(c.fetchone())
            sql = "SELECT image FROM Actual_Card_List WHERE id = " + str(a)
            c.execute(sql)
            card = str(c.fetchone())
            a = pygame.image.load('public/'+ str(card[2:-3]))
            if self.position == "field":
                a = pygame.transform.smoothscale(a, (70,100)) 
                if self.flip == True:
                    a = pygame.transform.flip(a,1,1)
            else:
                a = pygame.transform.smoothscale(a, (210,300))
        else: 
            a = pygame.image.load('public/Llamas_unleashed_Cards/Z_Card_Back.png')
            a = pygame.transform.smoothscale(a, (130,180))
        if outline != "none": 
            img = pygame.Surface(rect.inflate(10, 10).size)
            img.fill(outline)
            img.blit(a, (5,5))
        else: 
            img.blit(a, (0,0))
        

        return img
    def update(self, events, discard, play, type_check): # type: ignore
        pos = pygame.mouse.get_pos()
        hit = self.rect.collidepoint(pos)
        i = 1
        if self.animal_type[2:-3] in type_check and self.position == "hand" and self.type[2:-3] == "animal":
            self.image = self.targ
        else:
            self.image = self.org
        if type_check != "none":
            for event in events:
                if i == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN and hit:
                        if self.position == "hand":
                            if (self.type[2:-3]) == "animal":
                                if type_check in (self.animal_type[2:-3]):
                                    return "into_play"
                            else:
                                return self.id
                    elif hit:
                        return self.id
                    i += 1
        elif discard == True:
            for event in events:
                if i == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN and hit:
                        if self.position == "hand":
                            return "discard"
                        else: 
                            return self.id
                    elif hit:
                        return self.id
                    i+=1
        elif play == True:
            for event in events:
                if i == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN and hit:
                        if self.position == "hand":
                            if (self.type[2:-3]) != "instant":
                                return "play"
                            else:
                                return "instant"
                        elif self.position == "is_deck":
                            return "draw_action"
                        else:
                            return self.id
                    elif hit:
                        return self.id
                    i+=1
        else:
            if hit:
                return self.id
#    def targetable(self, ):
#        self.image = self.targ if hit else self.org
class Button(pygame.sprite.Sprite):
    def __init__(self, color, color_hover, rect, callback, text='', outline=None, type = "button"):
        super().__init__()
        self.text = text
        tmp_rect = pygame.Rect(0, 0, *rect.size)
        self.org = self._create_image(color, outline, text, tmp_rect)
        self.hov = self._create_image(color_hover, outline, text, tmp_rect)
        self.image = self.org
        self.rect = rect
        self.callback = callback
        self.type = type

    def _create_image(self, color, outline, text, rect):
        img = pygame.Surface(rect.size)
        if outline:
            img.fill(outline)
            img.fill(color, rect.inflate(-4, -3))
        else:
            img.fill(color)

        if text != '':
            if text == "Opponent":
                font = pygame.font.SysFont('comicsans', 30)
            else: 
                font = pygame.font.SysFont('comicsans', 40)
            text_surf = font.render(text, 1, pygame.Color('black'))
            text_rect = text_surf.get_rect(center=rect.center)
            img.blit(text_surf, text_rect)
        return img

    def update(self, events, a, b, c):
        pos = pygame.mouse.get_pos()
        hit = self.rect.collidepoint(pos)
        self.image = self.hov if hit else self.org
        i = 1
        if self.callback != "none":
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and hit:
                    if i == 1:
#                        print(self.callback)
                        i += 1
                        return self.callback
class Notice(pygame.sprite.Sprite):
    def __init__(self, color, rect, text='', outline=None, type = "notice"):
        super().__init__()
        self.text = text
        tmp_rect = pygame.Rect(0, 0, *rect.size)
        self.org = self._create_image(color, outline, text, tmp_rect)
        self.image = self.org
        self.rect = rect
        self.type = type

    def _create_image(self, color, outline, text, rect):
        img = pygame.Surface(rect.size)
        
        if outline:
            img.fill(outline)
            img.fill(color, rect.inflate(-4, -3))
        else:
            img.fill(color)

        if text != '':
            font = pygame.font.SysFont('comicsans', 35)
            text_surf = font.render(text, 1, pygame.Color('black'))
            text_rect = text_surf.get_rect(center=rect.center)
            img.blit(text_surf, text_rect)
        return img
