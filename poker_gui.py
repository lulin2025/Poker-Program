from operator import truediv
from os import environ
from re import L
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from Setup_deal import *
import winners_circle
import probability
import copy
import time
import sys
import os


def rect(screen):
    #both cards bottom middle
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(505, 660, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(605, 660, 90, 115),5) 
    #both cards in bottom left
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(150, 575, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(250, 575, 90, 115),5) 
    #both cards middle left
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(0, 342, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(100, 342, 90, 115),5) 
    #both cards top middle
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(505, 0, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(605, 0, 90, 115),5) 
    #both cards top left
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(150, 100, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(250, 100, 90, 115),5) 
    #both cards in bottom right
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(960, 575, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(860, 575, 90, 115),5) 
    #both cards middle right
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(1110, 342, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(1010, 342, 90, 115),5) 
    #both cards in bottom right
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(960, 100, 90, 115), 5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(860, 100, 90, 115),5) 
    #cards on the board
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(365, 330, 90, 115),5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(460, 330, 90, 115),5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(555, 330, 90, 115),5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(650, 330, 90, 115),5) 
    pygame.draw.rect(screen, [0, 0, 0], pygame.Rect(745, 330, 90, 115),5) 

def addplayer():
    #make a dictionary with all needed information for all add player buttons
    player = {}
    font = pygame.font.SysFont('Arial', 15, bold = True)
    surf = font.render('Add Player +', True, 'white')
    addplayer1 = pygame.Rect(197, 710, 94, 20)
    addplayer2 = pygame.Rect(47, 477, 94, 20)
    addplayer3 = pygame.Rect(552, 135, 94, 20)
    addplayer4 = pygame.Rect(197, 235, 94, 20)
    addplayer5 = pygame.Rect(907, 710, 94, 20)
    addplayer6 = pygame.Rect(1055, 477, 94, 20)
    addplayer7 = pygame.Rect(907, 235, 94, 20)
    player["player2"]= [font, surf, addplayer1]
    player["player3"] = [font, surf, addplayer2]
    player["player5"] = [font, surf, addplayer3]
    player["player4"] = [font, surf, addplayer4]
    player["player8"] = [font, surf, addplayer5]
    player["player7"] = [font, surf, addplayer6]
    player["player6"] = [font, surf, addplayer7]
    return player

def init_addcard():
    #make a dictinoary with all needed information to make a button that displays
    #and adds cards for player 1 and the board
    add_card = {}
    font = pygame.font.SysFont('Arial', 15, bold = True)
    surf = font.render('', True, 'white')
    user_button1 = pygame.Rect(510, 665, 80, 105)
    user_button2 = pygame.Rect(610, 665, 80, 105)
    board_card1 = pygame.Rect(370, 335, 80, 105)
    board_card2 = pygame.Rect(465, 335, 80, 105)
    board_card3 = pygame.Rect(560, 335, 80, 105)
    board_card4 = pygame.Rect(655, 335, 80, 105)
    board_card5 = pygame.Rect(750, 335, 80, 105)
    add_card["user1"]= [font, surf, user_button1]
    add_card["user2"]= [font, surf, user_button2]
    add_card["board1"]= [font, surf, board_card1]
    add_card["board2"]= [font, surf, board_card2]
    add_card["board3"]= [font, surf, board_card3]
    add_card["board4"]= [font, surf, board_card4]
    add_card["board5"]= [font, surf, board_card5]
    return add_card

def addcard(player_info):
    #this will take in the info of the add player button. it will see which outlined cards need
    #to be added to add_card dictionary. 
    if player_info[2].x ==197 and player_info[2].y == 710:
        card1 = pygame.Rect(155, 580, 80, 105)
        card2 =  pygame.Rect(255, 580, 80, 105)
    elif player_info[2].x ==47:
        card1 = pygame.Rect(5, 347, 80, 105)
        card2 =  pygame.Rect(105, 347, 80, 105)
    elif player_info[2].x ==552:
        card1 = pygame.Rect(510, 5, 80, 105)
        card2 =  pygame.Rect(610, 5, 80, 105)
    elif player_info[2].x ==197:
        card1 = pygame.Rect(155, 105, 80, 105)
        card2 =  pygame.Rect(255, 105, 80, 105)
    elif player_info[2].x ==907 and player_info[2].y ==710:
        card1 = pygame.Rect(965, 580, 80, 105)
        card2 =  pygame.Rect(865, 580, 80, 105)

    elif player_info[2].x ==1055:
        card1 = pygame.Rect(1115, 347, 80, 105)
        card2 =  pygame.Rect(1015, 347, 80, 105)

    elif player_info[2].x ==907:
        card1 = pygame.Rect(965, 105, 80, 105)
        card2 =  pygame.Rect(865, 105, 80, 105)
    list = []
    list.append(card1)
    list.append(card2)
    return list


def main():
    #this will be used to display cards in ascending order in interface
    value_cards=["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", 'default']
    FPS_CLOCK = pygame.time.Clock()
    #intializing the game
    pygame.init()
    #setting dimensions of display
    screen = pygame.display.set_mode((1200, 775))
    #name
    pygame.display.set_caption("Poker")
    #displays green background
    screen.fill([0,128,0])
    running = True
    #unsorted cards will be the png files in unsorted order
    unsorted_cards = []
    #this will iterate through the file and append the file names in unsorted_cards
    rect(screen)
    directory = 'cards'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        unsorted_cards.append(f)
    #intiailzing sorted_cards. This will append the png files from Ace-King in image form for pygame
    sorted_cards=[]
    #this will be used later to indicate which card has been chosen
    listOfcards = []
    #value cards go in ascending order, so we append to sorted_cards from smallest to biggest
    #font and surf for the add_card
    font = pygame.font.SysFont('Arial', 15, bold = True)
    surf = font.render('', True, 'white')
    for i in range(len(value_cards)):
        for j in range(len(unsorted_cards)):
            if value_cards[i] in unsorted_cards[j]:
                sorted_cards.append(pygame.image.load(unsorted_cards[j]))
                listOfcards.append(unsorted_cards[j])
    #returns a dictionaries of all things needed to make a add player button
    player = addplayer()
    
    #add_card will contain all available add card buttons. We are intiliazing in 
    #the line below
    add_card = init_addcard()
    #this will be used to indicate which number player has been added
    add_player_num = 1
    show_cards=False
    #this will contain the player in which the user picks the card for
    card_player =[]
    remove = []
    temp = []
    removal=0
    while running:    #checks each event and see if it should quit
        screen.fill([0,128,0])
        rect(screen)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    running = False
            elif (event.type == pygame.QUIT):
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                #iterate through each add player button if we press down on the mouse
                for i in player:
                    #if we pressed down on the mouse and it happens to colllide with one of the players, 
                    #go in the if statement
                    if player[i][2].collidepoint(event.pos) and show_cards==False:
                        #update the player number
                        add_player_num = add_player_num +1
                        #these are the keys of each player and their cards
                        player_num1 = "Player"+str(add_player_num)+"first_card"
                        player_num2 = "Player"+str(add_player_num)+"second_card"
                        #when we call addcards, it takes in the information of the add_player button we have just selected
                        #we then figure out the coordinates of both the card positions for the player and append it in a list
                        list = addcard(player[i])
                        #adding the key and value into the add_card dictionary because we want this person's card slot to be 
                        #a button now
                        add_card[player_num1] = [font, surf, list[0]]
                        add_card[player_num2] = [font, surf, list[1]]
                        #we add this into a list called remove because these are all keys that we want to remvoe from player
                        remove.append(i)

                #finds the indice of the card picked when the cards are popped up. indice should range from 0,0 - 10,3
                #anything else is not valid
                if event.type == pygame.MOUSEBUTTONDOWN and show_cards == True:
                    pos = pygame.mouse.get_pos()
                    indiceX = (pos[0]-180)//60
                    indiceY = (pos[1]-200)//90
                    
                    #if the indices youve chosen is an indice where a card is located, then go in this if statement
                    #it should display the card for the proper player, get rid of the button option for card, and get rid
                    #of the card from the display
                    if indiceX >= 0 and indiceX<14 and indiceY >=0 and indiceY<4:
                        #finds the one dimenesional indice for the card
                        base = indiceY*13
                        indice = base + indiceX +indiceY
                        sorted_cards.pop(indice)
                        show_cards = False

                #remove contains all player add buttons that have been clicked. We dont need these buttons
                #anymore because we just clicked them
                elif show_cards ==False:
                    for i in remove:
                        #i[2] contains player numbers
                        temp.append([player[i][2], add_player_num])
                        player.pop(i)
                        remove=[]
                    #if we click a add_card button, turn show_cards to true and append the key
                    #card player
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for i in add_card:
                            if add_card[i][2].collidepoint(event.pos):
                                show_cards =True
                                card_player.append(i)
                                removal = i
                                removal2 = add_card[i][2]
                                

        a,b = pygame.mouse.get_pos()
        #loops through player which is information for each button, and if mouse is on top of any 
        #of the add player buttons, highlight
        if show_cards == False:
            for i in player:
                if player[i][2].x<= a <player[i][2].x+94 and player[i][2].y <= b <= player[i][2].y+20:
                    pygame.draw.rect(screen, (180, 180, 180), player[i][2])
                else:
                    pygame.draw.rect(screen, (0,128,0), player[i][2])
            #loops over players and displays all the buttons
            for i in player:
                screen.blit(player[i][1],(player[i][2].x, player[i][2].y))
            #displays face down card
            #screen.blit(pygame.transform.scale(sorted_cards[52], (90, 115)), (270, 330))

            #for each add_card button, if cursor is over it, highlight it 
            for i in add_card:
                if add_card[i][2].x<= a <add_card[i][2].x+90 and add_card[i][2].y <= b <= add_card[i][2].y+115:
                    pygame.draw.rect(screen, (180, 180, 180), add_card[i][2])
                else:
                    pygame.draw.rect(screen, (0,128,0), add_card[i][2])
                screen.blit(add_card[i][1],(add_card[i][2].x, add_card[i][2].y))
            #displays all the player numbers that have been added
            for i in temp:
                surf2 = font.render('     Player '+str(i[1]), True, 'white')
                screen.blit(surf2,(i[0].x, i[0].y))
        #if true, display the cards
        if show_cards == True:
            pygame.draw.rect(screen, (0,128,0), removal2)
            x=180
            y=200
            for i in range(len(sorted_cards)):
                screen.blit(pygame.transform.scale(sorted_cards[i], (60, 90)), (x, y))
                x=x+60
                if i ==13 or i == 27 or i == 41:
                    y=y+90
                    x=180
            if removal !=0:
                add_card.pop(removal)
            removal=0

            #IMPLEMENT A WAY SO THAT WHEN USER CLICKS ON A CARD, IT PICKS THE CARD AND PUTS IT IN HIS HAND
        
        pygame.display.update()
main()