from Setup_deal import *
import winner

def pair_ties(players_points, player, table_cards, indexOfScores):
    #this will be the winners circle
    winners_circle = []
#keys will be players and value will be the card with pair
    high_pair = {}
    #list of all the pairs
    list = []
    for i in range(len(indexOfScores)):
        #call pair function with player[indexOfScores[i]] because indexOfScores[i] is the 
        #player with the pair
        pair_indicator1 = winner.pair(table_cards, player[indexOfScores[i]])
        #set key at player number and value at the first index of the card pair. Should 
        #only contain 1 thing in list because there's only one pair
        high_pair[indexOfScores[i]] = pair_indicator1[1][0]
        #append the values with pairs
        list.append(pair_indicator1[1][0])
    #quicksort the list
    winner.quickSort(list, 0, len(list)-1)
    #highest pair is last index of list because we quick sorted it
    maxPair = list[-1]
    #players with the high pairs
    playersOfHigh = []
    #for each key/player, if the value/pair is maxPair, append the player into playersOfHigh
    for i in high_pair:
        if high_pair[i] == maxPair:
            playersOfHigh.append(i)
    #if there is only one player with max pair, he has the high pair so he wins
    #de quanitfiy maxPair so it outputs a string of face card
    if maxPair == 13: maxPair="King"
    elif maxPair == 12: maxPair="Queen"
    elif maxPair == 11: maxPair="Jack"
    elif maxPair == 14: maxPair="Ace"
    if len(playersOfHigh)==1:
        print("Player "+str(playersOfHigh[0])+" wins with a high pair of "+str(maxPair))
        winners_circle.append(playersOfHigh[0])
        return winners_circle
    else:
        #else, make a information list. This will be used to append the information of the players
        #with the identical high card. This will indicate who wins through a high card
        information_card = []
        for i in range(len(playersOfHigh)):
            #call winner pair with the players that have the high pair. This is from playersOfHigh
                pair_indicator1 = winner.pair(table_cards, player[playersOfHigh[i]])
                #append the player number into pair_indicator1 so we know how to distinguish the information
                pair_indicator1.append(playersOfHigh[i])
                #append the information into information_card list
                information_card.append(pair_indicator1)
        length = len(information_card)
        #iterates through ith high card
        for i in range(3): 
            #the high cards of all players
            high_card = []
            #for each players high, append it to high_card. This should go from highest high cards to lowest high card
            for j in range(len(information_card)): 
                high_card.append(information_card[j][2][i])
            #store max card to indicate who wins
            max_card = max(high_card)
            #this iterates through each players high cards. Starts with their highest card at index 0 to players lowest
            #high card which is index 2. This outside for loop will go inside the for loop iff one of the ith cards of each
            #player is not the high card
            for x in range(len(high_card)):
                if high_card[x] != max_card:
                    #we have the ith high card of each player. We then get the max number among the ith high card.
                    #We then iterate through the ith high card, and if its not the max number, we delete it from information card because
                    #it cant not be the high card. If there is a tie, we then do nothing and move on through the iterations
                    #to the next ith card with the remaining players. If there is one player remaining, we know this player
                    #is has the highest ith card which indicate they have the high card. 
                    acc = 0 
                    y=0
                    length = len(information_card)
                    #this iterates through the ith high card in information card. If it does not contain the max card
                    #delete from information_card
                    for acc in range(length):
                        if information_card[y][2][i] != max_card:
                            #remove all cases of highcard[x]
                            #print(information_card[y][2][i])
                            information_card.remove(information_card[y])
                        else:
                            #we only accumulate y sometimes because when we remove from a list,
                            #we shift the elements one to the left so the shifting in a way iterates
                            #for us
                            y=y+1
            #if there is only one information card left, we know only one remains which means they have the high card
            if len(information_card) == 1:
                if max_card == 13: max_card="King"
                elif max_card == 12: max_card="Queen"
                elif max_card == 11: max_card="Jack"
                elif max_card == 14: max_card="Ace"
                print("Winner is player "+str(information_card[0][3]) + " with a pair of " +str(maxPair) +" with a high card of "+ str(max_card))
                winners_circle.append(information_card[0][3])
                return winners_circle
        #this means information_card still remains with more than one player, which means it must have been a tie!
        players_tied = []
        sent= "Players "
        for i in range(len(information_card)):
            winners_circle.append(information_card[i][3])
            sent = sent+ str(information_card[i][3])
            if i != len(information_card)-1:
                sent=sent+" and "
        sent=sent + " tied!"
        print(sent)
        return winners_circle

def two_pair_tie(players_points, player, table_cards, indexOfScores):
    #this will be the winners circle
    winners_circle = []
    #keys will be players and value will be the card with first pair
    high_pair = {}
    #keys will be players and value will be the card with second pair
    high_pair2 = {}
    #list of all second pairs
    list2 = []
    maxPair1= 0
    maxPair2 = 0
    for i in range(len(indexOfScores)):
        #call pair function with player[indexOfScores[i]] because indexOfScores[i] is the 
        #player with the pair
        pair_indicator1 = winner.pair(table_cards, player[indexOfScores[i]])
        #set key as player and the card pair as value. high_pair will contain the highest pair for
        #the player, and high_pair2 will contain the second highsst pair for the player
        high_pair[indexOfScores[i]] = pair_indicator1[1][1]
        high_pair2[indexOfScores[i]] = pair_indicator1[1][0]
        #finds the highest first and second pair out of all players
        if pair_indicator1[1][1]>maxPair1:
            maxPair1=pair_indicator1[1][1]
        if pair_indicator1[1][0]>maxPair2:
            maxPair2=pair_indicator1[1][0]
    #players with the high pairs
    playersOfHigh = []
    #for each key/player, if the value/pair is maxPair, append the player into playersOfHigh
    for i in high_pair:
        if high_pair[i] == maxPair1:
            playersOfHigh.append(i)
    if maxPair1 == 13: maxPair="King"
    elif maxPair1 == 12: maxPair="Queen"
    elif maxPair1 == 11: maxPair="Jack"
    elif maxPair1 == 14: maxPair="Ace"
    #if there is only one player in playersOfhigh, this means a single player has the max pair, which 
    #means they have the strongest hand
    if len(playersOfHigh)==1:
        print("Player "+str(playersOfHigh[0])+" wins with a high pair of "+str(maxPair))
        winners_circle.append(playersOfHigh[0])
        return winners_circle
    else:
        #list for highest second pair
        playersOfHigh2 = []
        #for each second pair, if the player has the second max Pair, and
        #also has the first highest pair, append it to players of High. This is an indicator that
        #the player has the first and second max pairs among the players
        for i in high_pair2:
            if high_pair2[i] == maxPair2 and i in playersOfHigh:
                playersOfHigh2.append(i)
        #if only one person has the second highest pair, then this player has the strongest hand
        if len(playersOfHigh2)==1:
            print("Player "+str(playersOfHigh2[0])+" wins with a high pair of "+str(maxPair2))
            winners_circle.append(playersOfHigh2[0])
            return winners_circle
        else:
            #if the player has the two highest pairs, we must check for the high card.
            player_info = []
            high_card = 0
            #this finds the high card out of the remaining players and appends all the remaining players'
            #information into player_info
            for i in range(len(playersOfHigh2)):
                info = winner.pair(table_cards, player[playersOfHigh2[i]])
                info.append(playersOfHigh2[i])
                player_info.append(info)
                if info[2][0]>high_card:
                    high_card = info[2][0]
            x=0
            #removes all the players that doesn't contain the high card
            for i in range(len(player_info)):
                if player_info[x][2][0] != high_card:
                    player_info.remove(player_info[x])
                else:
                    x=x+1
            #if player_info only has one player, then this person is the last remaining player
            #which means they must contain the high card which means they are the winners
            if len(player_info)== 1:
                if high_card == 13: high_card="King"
                elif high_card == 12: high_card="Queen"
                elif high_card == 11: high_card="Jack"
                elif high_card == 14: high_card="Ace"
                print("Player "+str(player_info[0][3])+" wins with a high card of "+str(high_card))
                winners_circle.append(player_info[0][3])
                return winners_circle
            else:
                #if there are more than one person in player_info, they have the same high pairs and
                #high card so they must have tied
                sent = "Players "
                for i in range(len(player_info)):
                    winners_circle.append(player_info[i][3])
                    sent = sent+ str(player_info[i][3])
                    if i != len(player_info)-1:
                        sent=sent+" and "
                sent=sent + " tied!"
                print(sent)
                return winners_circle


def three_tie(players_points, player, table_cards, indexOfScores):
    #this will be the winners circle
    winners_circle = []
    #keys will be players and value will be the card with three of a kind
    high_three = {}
    #highest three of a kind
    maxThree= 0
    for i in range(len(indexOfScores)):
        #call three function with player[indexOfScores[i]] because indexOfScores[i] is the 
        #player with the three of a kind
        three_indicator1 = winner.three(table_cards, player[indexOfScores[i]])
        #set key as player and the three of a kind card as value
        high_three[indexOfScores[i]] = three_indicator1[1][0]
        #finds the highest three of a kind out of all players
        if three_indicator1[1][0]>maxThree:
            maxThree=three_indicator1[1][0]
    #players with the high three of a kind
    playersOfHigh = []
    #for each key/player, if the value/three of a kind contains a maxThree, append the player into playersOfHigh
    for i in high_three:
        if high_three[i] == maxThree:
            playersOfHigh.append(i)
    if maxThree == 13: maxThree="King"
    elif maxThree == 12: maxThree="Queen"
    elif maxThree == 11: maxThree="Jack"
    elif maxThree == 14: maxThree="Ace"
    #if there is only one player in playersOfhigh, this means a single player has the max three, which 
    #means they have the strongest hand
    if len(playersOfHigh)==1:
        print("Player "+str(playersOfHigh[0])+" wins with a higher three of kind "+str(maxThree))
        winners_circle.append(playersOfHigh[0])
        return winners_circle
    else:
        #if both players have the same three of a kind we enter this else statment
        player_info = []
        high_card = 0
        high_card2 = 0
        #this finds the high card out of the remaining players and appends all the remaining players'
        #information into player_info
        for i in range(len(playersOfHigh)):
            info = winner.three(table_cards, player[playersOfHigh[i]])
            info.append(playersOfHigh[i])
            player_info.append(info)
            if info[2][0]>high_card:
                high_card = info[2][0]
            if info[2][1]>high_card2:
                high_card2 = info[2][1]
        x=0
        #removes all the players that doesn't contain the high card
        for i in range(len(player_info)):
            if player_info[x][2][0] != high_card:
                player_info.remove(player_info[x])
            else:
                x=x+1
        #if player_info only has one player, then this person is the last remaining player
        #which means they must contain the high card which means they are the winners
        if len(player_info)== 1:
            if high_card == 13: high_card="King"
            elif high_card == 12: high_card="Queen"
            elif high_card == 11: high_card="Jack"
            elif high_card == 14: high_card="Ace"
            print("Player "+str(player_info[0][3])+" wins with a high card of "+str(high_card))
            winners_circle.append(player_info[0][3])
            return winners_circle
        
        #this will take account for the fact if two players have the same first high card, see which
        #has the higher second card
        y=0
        if len(player_info) != 1:
            for i in range(len(player_info)):
                if player_info[y][2][1] != high_card2:
                    player_info.remove(player_info[y])
                else:
                    y=y+1
        if len(player_info)== 1:
            if high_card2 == 13: high_card2="King"
            elif high_card2 == 12: high_card2="Queen"
            elif high_card2 == 11: high_card2="Jack"
            elif high_card2 == 14: high_card2="Ace"
            print("Player "+str(player_info[0][3])+" wins with a second high card of "+str(high_card2))
            winners_circle.append(player_info[0][3])
            return winners_circle
        
        else:
            #if there are more than one person in player_info, they have the same three of a kind and
            #high card so they must have tied
            sent = "Players "
            for i in range(len(player_info)):
                winners_circle.append(player_info[i][3])
                sent = sent+ str(player_info[i][3])
                if i != len(player_info)-1:
                    sent=sent+" and "
            sent=sent + " tied!"
            print(sent)
            return winners_circle


def straight_ties(players_points, player, table_cards, indexOfScores):
    winners_circle = []
    info= []
    high_straight = 0
    #stores player information into info and finds the highest straight card
    for i in range(len(indexOfScores)):
        straight_indicator = winner.straight(table_cards, player[indexOfScores[i]])
        straight_indicator.append(indexOfScores[i])
        info.append(straight_indicator)
        if straight_indicator[1]>high_straight:
            high_straight = straight_indicator[1]
    x= 0 
    #removes all players if they dont have the high straight
    for i in range(len(indexOfScores)):
        if info[x][1]!=high_straight:
            info.remove(info[x])
        else:
            x=x+1
    #if there is only one player in info, this is the only person with the high straight card
    #so the player must be the sole winner
    if len(info)==1:
        if high_straight == 13: high_straight="King"
        elif high_straight == 12: high_straight="Queen"
        elif high_straight == 11: high_straight="Jack"
        elif high_straight == 14: high_straight="Ace"
        print("Player "+str(info[0][2])+" wins with a higher straight of "+str(high_straight))
        winners_circle.append(info[0][2])
        return winners_circle
    else:
        #if there are more than one person in info, they have the same strightand
        #so they must have tied
        sent = "Players "
        for i in range(len(info)):
            winners_circle.append(info[i][2])
            sent = sent+ str(info[i][2])
            if i != len(info)-1:
                sent=sent+" and "
        sent=sent + " tied!"
        print(sent)
        return winners_circle


def flush_ties(players_points, player, table_cards, indexOfScores):
    winners_circle = []
    info = []
    #puts all flush information of players into a list called info
    for i in range(len(indexOfScores)):
        flush_indicator = winner.flush(table_cards, player[indexOfScores[i]])
        flush_indicator.append(indexOfScores[i])
        info.append(flush_indicator)
    print(info)
    #for each card of the flush, and for each player, compare the ith high card of the flush
    #from player to player, and whoever has the highest flush card does not get removed
    #we keep iterating to the next ith card if two players have the high card. 
    for i in range(1, 6):
        max = 0 
        for j in range(len(info)):
            if info[j][1][-i] >max:
                max = info[j][1][-i]
        acc = 0 
        for k in range(len(info)) :
            if info[acc][1][-i] != max:
                info.remove(info[acc])
            else:
                acc = acc+1
        if len(info)==1:
            break
    #if there is only one person in info, must be the winner
    if len(info) !=1:
        sent = "Players "
        for i in range(len(info)):
            winners_circle.append(info[i][2])
            sent = sent+ str(info[i][2])
            if i != len(info)-1:
                sent=sent+" and "
        sent=sent + " tied!"
        print(sent)
        return winners_circle
    #quantify face card and return the max high flush
    else:
        if max == 13: max="King"
        elif max == 12: max="Queen"
        elif max== 11: max="Jack"
        elif max == 14: max="Ace"
        print("Player "+str(info[0][2])+" wins with a higher flush of "+str(max))
        winners_circle.append(info[0][2])
        print(winners_circle)
        return winners_circle


def fullhouse_ties(players_points, player, table_cards, indexOfScores):
    #0th index is three of a kind, first is the pair. If there are two three of a kinds, 
    #take the higher three of a kind as the 0th index, and the lower three of a kind as 
    #the 1st index
    info = []
    #this will find the highest three of a kind amongst player
    high_three = 0
    high_pair = 0
    winners_circle =[]
    for i in range(len(indexOfScores)):
        #find the three of a kinds of each player
        three_indicator = winner.three(table_cards, player[indexOfScores[i]])
        #if there are two three of a kinds, find the max three of a kind and append it 
        #as the 0th index. The other three of a kind can be the 1st index and be the 
        # "pair"
        if len(three_indicator[1])>1:
            maxThree = max(three_indicator[1])
            if three_indicator[1][0] == maxThree:
                minThree = three_indicator[1][1]
            else:
                minThree = three_indicator[1][0]
            info.append([maxThree, minThree, indexOfScores[i]])
        else:
            #else, use the other pairs as the "kicker"
            pair_indicator = winner.pair(table_cards, player[indexOfScores[i]])
            #if there are the two pairs, you need to use the higher pair
            if len(pair_indicator[1])>1:
                maxThree = three_indicator[1][0]
                maxPair = max(pair_indicator[1])
                info.append([maxThree, maxPair, indexOfScores[i]])
            #else, just use the the only pair as the "kicker"
            else:
                maxThree = three_indicator[1][0]
                maxPair = pair_indicator[1][0]
                info.append([maxThree, maxPair, indexOfScores[i]])
        #this finds the highest three of a kind amongst players
        if maxThree>high_three:
            high_three = maxThree
    #removes any player without the high three of a kind
    acc = 0
    for i in range(len(info)):
        if info[acc][0]!=high_three:
            info.remove(info[acc])
        else:
            acc = acc+1
    #returns with the player with the highest three of a kind
    if len(info)==1:
        if info[0][0] == 13: info[0][0]="King"
        elif info[0][0] == 12: info[0][0]="Queen"
        elif info[0][0] == 11: info[0][0]="Jack"
        elif info[0][0] == 14: info[0][0]="Ace"
        print("Player "+str(info[0][2])+" wins with a full house with a higher three of a kind of "+str(info[0][0]))
        winners_circle.append(info[0][2])
        print(winners_circle)
        return winners_circle
    #if two people have the same high three of a kind, compare the pairs
    else:
        #finds high pair amongst remaining players
        high_pair = 0
        for i in range(len(info)):
            if info[i][1]>high_pair:
                high_pair = info[i][1]
    acc = 0
    #deletes all those without the high pair
    for i in range(len(info)):
        if info[acc][1]!=high_pair:
            info.remove(info[acc])
        else:
            acc = acc+1
    #returns player with the highest pair
    if len(info)==1:
        if info[0][1] == 13: info[0][1]="King"
        elif info[0][1] == 12: info[0][1]="Queen"
        elif info[0][1] == 11: info[0][1]="Jack"
        elif info[0][1] == 14: info[0][1]="Ace"
        print("Player "+str(info[0][2])+" wins with a full house with a higher pair of "+str(info[0][1]))
        winners_circle.append(info[0][2])
        print(winners_circle)
        return winners_circle
    #else its a tie so return all tied folks!
    else:
        if len(info) !=1:
            sent = "Players "
            for i in range(len(info)):
                winners_circle.append(info[i][2])
                sent = sent+ str(info[i][2])
                if i != len(info)-1:
                    sent=sent+" and "
            sent=sent + " tied!"
            print(sent)
            return winners_circle





        


















        
                
