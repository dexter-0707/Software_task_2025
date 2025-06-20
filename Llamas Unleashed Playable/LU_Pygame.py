import pygame
# pygame setup
pygame.init()

from Variables import inits
inits()

from Variables import *
from Functions import *
from pygame.locals import * # type: ignore
import os
os.system("cls")
running = True



while running:
    if game_start == False:
        screen.fill("purple")
        draw_hands(hand_1, hand_2, deck, sprites)
#        hand_1.append(17) # adorable alpaca
#        hand_1.append(18) # alpacacopter
#        hand_1.append(20) # magical alpacacorn
#        hand_1.append(25) # magical goaticorn
#        hand_1.append(31) # dalai llama
#        hand_1.append(33) # magical llamacorn
#        hand_1.append(34) # prehistoric llamadon
#        hand_1.append(39) # henry the huarizo
        hand_1.append(41) # gin-rammy
        hand_1.append(44) # magical ramicorn
#        hand_1.append(95) # mother goat
#        hand_1.append(105) # woolly rammoth
#        hand_2.append(66) # garbage buffet
#        hand_2.append(70) # llama bomb
#        hand_2.append(111) # animal adoption
#        hand_2.append(118) # fannypaca
        game_start = True
        for i in fields:
            i.append(random.randint(1,12))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and type_check != "none" and selected_cards != [] and lock == False:
                type_check = "none"
                fields[turn-1].append(selected_cards[0])
                win = print_field(turn-1, sprites, fields, screen)
                if win == "turn win":
                    running = False
                    print("Player",turn,"wins")
                elif win == "other win":
                    running = False
                    if turn == 1:
                        print("Player",2,"wins")
                    else:
                        print("Player",1,"wins")
                hands[turn-1].pop(hands[turn-1].index(int(selected_cards[0])))
                reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy)
                print_hand(turn, sprites, hand_1, hand_2, screen)
                card = int(selected_cards[0])
                selected_cards = []
                a = animal_played(card)
                if a == "b":
                    for i in sprites:
                        if i.type == "notice":
                            i.kill()
                    reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy)
                    sprites.add(Notice("blue", pygame.Rect(5,20,200,80),("Action Step"),"black"))

                    make_choice(sprites,player_choice,target,discard,type_check)
                    lock = True
                else: 
                    action_step = True
            elif discard == True and action_step == False:
                    number = len(selected_cards)
                    for i in selected_cards:
                        gy.append(i)
                        top_of_gy = i
                        hands[turn-1].pop(hands[turn-1].index(int(i)))    
                    draw(turn, number, hands, deck)
                    reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy)
                    print_hand(turn, sprites, hand_1, hand_2, screen)
                    selected_cards = []
                    discard = False
                    action_step = True
                    play = False
            elif event.key == pygame.K_SPACE:
                lock = True
                if chain == []:
                    n = 7
                    if 118 in fields[turn-1]:
                        n+=2
                    if 34 in fields[turn-1]:
                        n -=5
                    if discard == True and len(hands[turn-1])-len(selected_cards) == n:
                        for i in selected_cards:
                            gy.append(i)
                            top_of_gy = i
                            hands[turn-1].pop(hands[turn-1].index(int(i)))    
                        reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy) 
                        print_hand(turn, sprites, hand_1, hand_2, screen)
                        selected_cards = []
                        lock = False
                    elif play == True and selected_cards:
                        chain.append(selected_cards[0])
                        hands[turn-1].pop(hands[turn-1].index(int(selected_cards[0])))
                        reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy) 
                        print_hand(turn, sprites, hand_1, hand_2, screen)
                        print_chain(sprites, chain, screen)
                        selected_cards = []
                else:
                    if len(chain)>1:
                        pass
                    else:
                        lock = False
                        card = int(chain[0])
                        for i in sprites:
                            if i.type != "notice":
                                if i.position == "chain":
                                    if i.type[2:-3] == "magic":
                                        effect = magic_effects(card, turn, hands, gy, deck, fields, sprites, screen, hand_1, hand_2, top_of_gy)
                                        print_hand(turn, sprites, hand_1, hand_2, screen)
                                        top_of_gy = card
                                        gy.append(card)
                                        if effect == "turn win":
                                            running = False
                                            print("Player",turn,"wins")
                                        elif effect == "other win":
                                            running = False
                                            if turn == 1:
                                                print("Player",2,"wins")
                                            else:
                                                print("Player",1,"wins")
                                        try:
                                            if effect[1] == "target":
                                                target = True 
                                                make_choice(sprites,player_choice,target,discard,type_check)
                                                lock = True
                                        except: pass
                                    elif i.type[2:-3] == "animal":
                                        fields[turn-1].append(card)
                                        win = print_field(turn-1, sprites, fields, screen)
                                        if win == "turn win":
                                            running = False
                                            print("Player",turn,"wins")
                                        elif win == "other win":
                                            running = False
                                            if turn == 1:
                                                print("Player",2,"wins")
                                            else:
                                                print("Player",1,"wins")
                                        a = animal_played(card)
                                        if a == "b":
                                            make_choice(sprites, player_choice,target,discard,type_check)
                                            lock = True
                                    elif i.type[2:-3] == "upgrade":
                                        fields[turn-1].append(card)
                                        upgrade_effects(card, turn, hands, gy, deck, fields, sprites, screen, hand_1, hand_2, top_of_gy)
                                        print_field(turn-1, sprites, fields, screen)
                                    elif i.type[2:-3] == "downgrade":
                                        try:
                                            fields[turn].append(card)
                                        except:
                                            fields[turn-2].append(card)
                                        print_field(turn-1, sprites, fields, screen)
                                    i.kill()
                                    reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy)
                                    sprites.draw(screen)
                                    
                                    play = False
                                    if lock == False:
                                        action_step = True
                    chain = []
    
    if beginning_of_turn == False:
        sprites.add(Notice("blue", pygame.Rect(5,20,200,80),("Beginning"),"black"))
        print_field(turn-1, sprites, fields, screen)
        reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy)
        print_hand(turn, sprites, hand_1, hand_2, screen)
        beginning_of_turn = True
    elif draw_step == False:
        for i in sprites: 
            if i.type == "notice":
                i.kill()
        sprites.add(Notice("blue", pygame.Rect(5,20,200,80),("Draw Step"),"black"))
        draw(turn,1, hands, deck)
        print_hand(turn, sprites, hand_1, hand_2, screen)
        draw_step = True
        z = 0
    elif action_step == False:
        if z == 0: # type: ignore
            for i in sprites: 
                if i.type == "notice":
                    i.kill()
            sprites.add(Notice("blue", pygame.Rect(5,20,200,80),("Action Step"),"black"))
            play = True
            z+=1 # type: ignore
    elif End_of_turn_step == False:
        n = 7
        if 118 in fields[turn-1]:
            n += 2
        if 34 in fields[turn-1]:
            n -=5
        if len(hands[turn-1]) > n:
            if discard == False:
                for i in sprites: 
                    if i.type == "notice":
                        i.kill()
                reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy)
                a =  str(len(hands[turn-1])-n)
                if a != "1":
                    sprites.add(Notice("blue", pygame.Rect(410,200,400,100),("Discard "+a+" cards"),"black"))
                else:
                    sprites.add(Notice("blue", pygame.Rect(410,200,400,100),("Discard "+a+" card"),"black"))
                sprites.add(Notice("blue", pygame.Rect(5,20,200,80),("End Step"),"black"))
                discard = True
        else:
            for i in sprites: 
                if i.type == "notice":
                    i.kill()
            reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy)
            End_of_turn_step = True
            if turn == 1:
                turn = 2
            else: 
                turn = 1
            reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy)
            lock = False
            beginning_of_turn = False
            draw_step = False
            action_step = False
            End_of_turn_step = False
            discard = False
    
    if choice == True and type_check == "none": 
        lock = False
        choice = False
        effect = animal_effects(card,turn, hands, gy, deck, fields, sprites, screen, hand_1, hand_2, top_of_gy)
        print_hand(turn, sprites, hand_1, hand_2, screen)
        if effect[0] == "play":
            type_check = effect[1]
            make_choice(sprites, player_choice, target, discard, type_check)
        elif effect[0] == "discard":
            if effect[1] == "self":
                discard = True
                play = False
                into_play = False
            elif effect[1] == "target":
                play = False
                player_choice = True
                lock = True
            make_choice(sprites, player_choice,target,discard,type_check)
        else: 
            action_step = True
            play = False
    if target_player != 3:
        lock = False
        player_choice = False
        a = len(hands[target_player])
        for i in hands[target_player]:
            gy.append(i)
            top_of_gy = i
        for i in range(a):
            hands[target_player].pop(0)
        draw(target_player+1,a,hands,deck)
        reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy) 
        print_hand(turn, sprites, hand_1, hand_2, screen)
        action_step = True
        target_player = 3
#        if i.type != "notice":

    a = ""
    b = 0
    select = False
    for i in sprites:
        if b == 0:
            try: 
                if i.animal_type[2:-3] in type_check and i.position == "hand" and i.type[2:-3] == "animal":
                    b +=1
            except: pass                
        if i.update(events, discard, play, type_check, target, effect): 
            a = i.update(events, discard, play, type_check, target, effect)
            if a == "discard": 
                select = True
                a = i.id
            elif a == "play":
                select = True
                a = i.id
            elif a == "draw_action":
                draw(turn,1, hands, deck)
                selected_cards = []
                reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy)
                print_hand(turn, sprites, hand_1, hand_2, screen)
                play = False
                action_step = True
                a = ""
            elif a == "instant":
                a = ""
            elif a == "into_play":
                select = True
                into_play = True
                a = i.id
            elif a == "yes":
                for i in sprites:
                    if i.type == "button":
                        i.kill()
                reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy)
                a = ""
                choice = True
            elif a == "no":
                for i in sprites:
                    if i.type == "button":
                        i.kill()
                reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy)
                a = ""
                choice = False
                play = False
                action_step = True
                lock = False
                type_check = "none"
            elif a == "you":
                a = ""
                for i in sprites:
                    if i.type == "button":
                        i.kill()
                reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy)
                target_player = turn-1
            elif a == "opponent":
                a = ""
                for i in sprites:
                    if i.type == "button":
                        i.kill()
                reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy)
                if turn == 2:
                    target_player = turn-2
                else: 
                    target_player = turn
            elif a == "target":
                a = i.id
                for i in sprites:
                    if i.type == "button":
                        i.kill()
                select = True
            else: 
                into_play = False
    if b == 0 and type_check !="none":
        choice = False
        play = False
        action_step = True
        lock = False
        type_check = "none"
    b = ""
    if a != "" and a: 
        card_change(a, screen)
        if select == True and lock == False:
            if play == True or into_play == True:
                if a in selected_cards:
                    for i in range(len(selected_cards)):
                        try:
                            if selected_cards[i] == a:
                                selected_cards.pop(i)
                        except:
                            pass
                else:
                    if selected_cards:
                        b = True
                        down_card = selected_cards[0]
                    selected_cards.append(a)
                for i in sprites:
                    if i.type != "notice":
                        if i.id == a:
                            if i.rect.y == 500:
                                i.rect.y += -50
                            elif i.rect.y == 450:
                                i.rect.y += 50
                if b == True:
                    for i in sprites:
                        if i.type != "notice":
                            if i.id == down_card: # type: ignore
                                if i.rect.y == 450:
                                    i.rect.y += 50
                    selected_cards.pop(0)
                    b = False
            elif discard == True:
                if a in selected_cards:
                    for i in range(len(selected_cards)):
                        try:
                            if selected_cards[i] == a:
                                selected_cards.pop(i)
                        except:
                            pass
                else:
                    n = 7
                    if 118 in fields[turn-1]:
                        n +=2
                    if 34 in fields[turn-1]:
                        n -=5
                    if len(hands[turn-1])-len(selected_cards) == n and action_step == True:
                        b = True
                        down_card = selected_cards[0]
                    selected_cards.append(a)
                for i in sprites:
                    if i.type != "notice":
                        if i.id == a:
                            if i.rect.y == 500:
                                i.rect.y += -50
                            elif i.rect.y == 450:
                                i.rect.y += 50
                if b == True:
                    for i in sprites:
                        if i.type != "notice":
                            if i.id == down_card: # type: ignore
                                if i.rect.y == 450:
                                    i.rect.y += 50
                    selected_cards.pop(0)
                    b = False
            reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy)
        elif select == True:
            if target == True:
                if effect[0] == "destroy": # type: ignore
                    try:
                        fields[turn].pop(fields[turn].index(int(a)))
                    except:
                        fields[turn-2].pop(fields[turn-2].index(int(a)))
                    top_of_gy = a
                    gy.append(int(a))
                    print_field(turn-1, sprites, fields, screen)
                    reprint_hand(turn, top_of_gy, sprites, screen, hand_1, hand_2, gy)
                    lock = False
                    action_step = True
                    target = False
                    select = False
    sprites.draw(screen)
    
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
