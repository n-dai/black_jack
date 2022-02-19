import pygame as game   
import sys
import time
import random
import math

from pygame.constants import ACTIVEEVENT

#Class to handle the gameplay of the game
class GamePlay:

    bg_colour = (3, 65, 11)
    
    screen_height = 851
    screen_width = 1392
    screen = game.display.set_mode((screen_width, screen_height))
    
    table = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\black_jack_table.png'

    # Cards

    card_width = 167
    card_height = 242

    ace_of_spades = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\ace_of_spades.png'
    ace_of_clubs = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\ace_of_clubs.png'
    ace_of_diamonds = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\ace_of_diamonds.png'
    ace_of_hearts = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\ace_of_hearts.png'

    king_of_spades = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\king_of_spades2.png'
    king_of_clubs = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\king_of_clubs2.png'
    king_of_diamonds = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\king_of_diamonds2.png'
    king_of_hearts = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\king_of_hearts2.png'

    queen_of_spades = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\queen_of_spades2.png'
    queen_of_clubs = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\queen_of_clubs2.png'
    queen_of_diamonds = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\queen_of_diamonds2.png'
    queen_of_hearts = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\queen_of_hearts2.png'

    jack_of_spades = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\jack_of_spades2.png'
    jack_of_clubs = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\jack_of_clubs2.png'
    jack_of_diamonds = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\jack_of_diamonds2.png'
    jack_of_hearts = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\jack_of_hearts2.png'

    ten_of_spades = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\10_of_spades.png'
    ten_of_clubs = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\10_of_clubs.png'
    ten_of_diamonds = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\10_of_diamonds.png'
    ten_of_hearts = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\10_of_hearts.png'

    nine_of_spades = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\9_of_spades.png'
    nine_of_clubs = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\9_of_clubs.png'
    nine_of_diamonds = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\9_of_diamonds.png'
    nine_of_hearts = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\9_of_hearts.png'

    eight_of_spades = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\8_of_spades.png'
    eight_of_clubs = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\8_of_clubs.png'
    eight_of_diamonds = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\8_of_diamonds.png'
    eight_of_hearts = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\8_of_hearts.png'

    seven_of_spades = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\7_of_spades.png'
    seven_of_clubs = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\7_of_clubs.png'
    seven_of_diamonds = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\7_of_diamonds.png'
    seven_of_hearts = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\7_of_hearts.png'

    six_of_spades = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\6_of_spades.png'
    six_of_clubs = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\6_of_clubs.png'
    six_of_diamonds = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\6_of_diamonds.png'
    six_of_hearts = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\6_of_hearts.png'

    five_of_spades = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\5_of_spades.png'
    five_of_clubs = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\5_of_clubs.png'
    five_of_diamonds = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\5_of_diamonds.png'
    five_of_hearts = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\5_of_hearts.png'

    four_of_spades = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\4_of_spades.png'
    four_of_clubs = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\4_of_clubs.png'
    four_of_diamonds = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\4_of_diamonds.png'
    four_of_hearts = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\4_of_hearts.png'

    three_of_spades = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\3_of_spades.png'
    three_of_clubs = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\3_of_clubs.png'
    three_of_diamonds = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\3_of_diamonds.png'
    three_of_hearts = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\3_of_hearts.png'

    two_of_spades = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\2_of_spades.png'
    two_of_clubs = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\2_of_clubs.png'
    two_of_diamonds = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\2_of_diamonds.png'
    two_of_hearts = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\2_of_hearts.png'

    back = r'C:\Users\Neal Dai\Documents\PYTHON_SNAKE\blackjack\PNG-cards-1.3\PNG-cards-1.3\back.png'


    table_img = game.image.load(table)  
    table_img = game.transform.scale(table_img, (screen_width, screen_height))

    ace_s = game.image.load(ace_of_spades)
    ace_c = game.image.load(ace_of_clubs)
    ace_d = game.image.load(ace_of_diamonds)
    ace_h = game.image.load(ace_of_hearts)

    king_s = game.image.load(king_of_spades)
    king_c = game.image.load(king_of_clubs)
    king_d = game.image.load(king_of_diamonds)
    king_h = game.image.load(king_of_hearts)

    queen_s = game.image.load(queen_of_spades)
    queen_c = game.image.load(queen_of_clubs)
    queen_d = game.image.load(queen_of_diamonds)
    queen_h = game.image.load(queen_of_hearts)

    jack_s = game.image.load(jack_of_spades)
    jack_c = game.image.load(jack_of_clubs)
    jack_d = game.image.load(jack_of_diamonds)
    jack_h = game.image.load(jack_of_hearts)

    ten_s = game.image.load(ten_of_spades)
    ten_c = game.image.load(ten_of_clubs)
    ten_d = game.image.load(ten_of_diamonds)
    ten_h = game.image.load(ten_of_hearts)

    nine_s = game.image.load(nine_of_spades)
    nine_c = game.image.load(nine_of_clubs)
    nine_d = game.image.load(nine_of_diamonds)
    nine_h = game.image.load(nine_of_hearts)

    eight_s = game.image.load(eight_of_spades)
    eight_c = game.image.load(eight_of_clubs)
    eight_d = game.image.load(eight_of_diamonds)
    eight_h = game.image.load(eight_of_hearts)

    seven_s = game.image.load(seven_of_spades)
    seven_c = game.image.load(seven_of_clubs)
    seven_d = game.image.load(seven_of_diamonds)
    seven_h = game.image.load(seven_of_hearts)

    six_s = game.image.load(six_of_spades)
    six_c = game.image.load(six_of_clubs)
    six_d = game.image.load(six_of_diamonds)
    six_h = game.image.load(six_of_hearts)

    five_s = game.image.load(five_of_spades)
    five_c = game.image.load(five_of_clubs)
    five_d = game.image.load(five_of_diamonds)
    five_h = game.image.load(five_of_hearts)

    four_s = game.image.load(four_of_spades)
    four_c = game.image.load(four_of_clubs)
    four_d = game.image.load(four_of_diamonds)
    four_h = game.image.load(four_of_hearts)

    three_s = game.image.load(three_of_spades)
    three_c = game.image.load(three_of_clubs)
    three_d = game.image.load(three_of_diamonds)
    three_h = game.image.load(three_of_hearts)

    two_s = game.image.load(two_of_spades)
    two_c = game.image.load(two_of_clubs)
    two_d = game.image.load(two_of_diamonds)
    two_h = game.image.load(two_of_hearts)

    back = game.image.load(back)

    # Card deck in array 
    deck = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3","2"]

    # Create game window 

    table_red = (112, 10, 10)
    boarder = (255, 192, 0)
    white = (255, 255, 255)

    balance_display_x_pos = 60
    balance_display_y_pos = 810
    balance_display_length = 180
    balance_display_width = 21

    initial_balance = 1000
    remainder = 0

    win_display_x_pos = 1200
    win_display_y_pos = 810
    win_display_length = 180
    win_display_width = 21

    win_value = 0

    bet_display_x_pos = win_display_x_pos
    bet_display_y_pos = win_display_y_pos - 30
    bet_display_length = win_display_length
    bet_display_width = win_display_width

    bet_value = 0

    count_display_x_pos = 1240
    count_display_y_pos = 615
    count_display_length = 100
    count_display_width = 30

    count_value = 1000

    player_value_display_x_pos = 500
    player_value_display_y_pos = 600
    player_value_display_length = 80
    player_value_display_width = 50

    dealer_value_display_x_pos = 500
    dealer_value_display_y_pos = 200
    dealer_value_display_length = 80
    dealer_value_display_width = 50

    initial_time = pow(10,99)
    inital_player_hand_time = pow(10,99)
    inital_dealer_hand_time = pow(10,99)
    time_flag = 0
    initial_player_hand_time_flag = 0
    initial_dealer_hand_time_flag = 0

    def pygame_init(self):
        game.init()
        game.font.init()
    
    def status_display(self):
        font = game.font.SysFont("calibri", 20)
        hand_font = game.font.SysFont("calibri", 40)

        # Bank Roll Display
        game.draw.rect(game_state.screen, (self.boarder), [self.balance_display_x_pos - 1, self.balance_display_y_pos - 1, self.balance_display_length + 2, self.balance_display_width + 2])
        game.draw.rect(game_state.screen, (self.table_red), [self.balance_display_x_pos, self.balance_display_y_pos, self.balance_display_length, self.balance_display_width])
        balance = font.render("Balance:          $" + str(self.initial_balance), True, self.white)
        self.screen.blit(balance, (self.balance_display_x_pos + 7, self.balance_display_y_pos + 2))

        # Win Display
        game.draw.rect(game_state.screen, (self.boarder), [self.win_display_x_pos - 1, self.win_display_y_pos - 1, self.win_display_length + 2, self.win_display_width + 2])
        game.draw.rect(game_state.screen, (self.table_red), [self.win_display_x_pos, self.win_display_y_pos, self.win_display_length, self.win_display_width])
        bet = font.render("Win:                $" + str(self.win_value), True, self.white)
        self.screen.blit(bet, (self.win_display_x_pos + 7, self.balance_display_y_pos + 2))

        # Bet Display

        game.draw.rect(game_state.screen, (self.boarder), [self.bet_display_x_pos - 1, self.bet_display_y_pos - 1, self.bet_display_length + 2, self.bet_display_width + 2])
        game.draw.rect(game_state.screen, (self.table_red), [self.bet_display_x_pos, self.bet_display_y_pos, self.bet_display_length, self.bet_display_width])
        bet = font.render("Bet:                 $" + str(self.bet_value), True, self.white)
        self.screen.blit(bet, (self.bet_display_x_pos + 6, self.bet_display_y_pos + 2))

        # Bet counter

        game.draw.rect(game_state.screen, (self.boarder), [self.count_display_x_pos - 1, self.count_display_y_pos - 1, self.count_display_length + 2, self.count_display_width + 2])
        game.draw.rect(game_state.screen, (self.table_red), [self.count_display_x_pos, self.count_display_y_pos, self.count_display_length, self.count_display_width])
        bet = font.render("Bet:  " + str(self.count_value), True, self.white)
        self.screen.blit(bet, (self.count_display_x_pos + 7, self.count_display_y_pos + 5))

        # Player value counter 
        game.draw.rect(game_state.screen, (self.boarder), [self.player_value_display_x_pos - 1, self.player_value_display_y_pos - 1, self.player_value_display_length + 2, self.player_value_display_width + 2])
        game.draw.rect(game_state.screen, (self.table_red), [self.player_value_display_x_pos, self.player_value_display_y_pos, self.player_value_display_length, self.player_value_display_width])
        counter = hand_font.render(str(player.player_hand_value), True, self.white)
        self.screen.blit(counter, (530, 605))

        if player.player_hand_value > 9:
            game.draw.rect(game_state.screen, (self.boarder), [self.player_value_display_x_pos - 1, self.player_value_display_y_pos - 1, self.player_value_display_length + 2, self.player_value_display_width + 2])
            game.draw.rect(game_state.screen, (self.table_red), [self.player_value_display_x_pos, self.player_value_display_y_pos, self.player_value_display_length, self.player_value_display_width])
            counter = hand_font.render(str(player.player_hand_value), True, self.white)
            self.screen.blit(counter, (520, 605))
        

        # Dealer value counter 
        game.draw.rect(game_state.screen, (self.boarder), [self.dealer_value_display_x_pos - 1, self.dealer_value_display_y_pos - 1, self.dealer_value_display_length + 2, self.dealer_value_display_width + 2])
        game.draw.rect(game_state.screen, (self.table_red), [self.dealer_value_display_x_pos, self.dealer_value_display_y_pos, self.dealer_value_display_length, self.dealer_value_display_width])
        counter = hand_font.render(str(dealer.dealer_hand_value), True, self.white)
        self.screen.blit(counter, (self.dealer_value_display_x_pos + 30, self.dealer_value_display_y_pos + 5))

        if dealer.dealer_hand_value > 9:
            game.draw.rect(game_state.screen, (self.boarder), [self.dealer_value_display_x_pos - 1, self.dealer_value_display_y_pos - 1, self.dealer_value_display_length + 2, self.dealer_value_display_width + 2])
            game.draw.rect(game_state.screen, (self.table_red), [self.dealer_value_display_x_pos, self.dealer_value_display_y_pos, self.dealer_value_display_length, self.dealer_value_display_width])
            counter = hand_font.render(str(dealer.dealer_hand_value), True, self.white)
            self.screen.blit(counter, (self.dealer_value_display_x_pos + 20, self.dealer_value_display_y_pos + 5))
    
    def face_value(self, card, entity):
        
        if card == 1 and entity == 1 and (player.player_hand_value < 11):
                return 11
        if card == 1 and entity == 1 and player.player_hand_value > 11:
                return 1
            
        if card == 1 and entity == 1 and dealer.dealer_hand_value + 11 > 21:
                return 1
        if card == 1 and entity == 1 and dealer.dealer_hand_value + 11 <= 21:
                return 11

        if card >= 10 and card <= 13:
            return 10
        else: 
            return card
    
    def card_display(self, card, suite):
    
        if card == 1:
            
            if suite == 1:
                return game_state.ace_s
            
            if suite == 2:
                return game_state.ace_c
            
            if suite == 3:
                return game_state.ace_d
            
            if suite == 4:
                return game_state.ace_h
        
        if card == 2:

            if suite == 1:
                return game_state.two_s
            
            if suite == 2:
                return game_state.two_c
            
            if suite == 3:
                return game_state.two_d
            
            if suite == 4:
                return game_state.two_h

            

        if card == 3:

            if suite == 1:
                return game_state.three_s
            
            if suite == 2:
                return game_state.three_c
            
            if suite == 3:
                return game_state.three_d
            
            if suite == 4:
                return game_state.three_h
            

        if card == 4:

            if suite == 1:
                return game_state.four_s
            
            if suite == 2:
                return game_state.four_c
            
            if suite == 3:
                return game_state.four_d
            
            if suite == 4:
                return game_state.four_h
            
            
        
        if card == 5:

            if suite == 1:
                return game_state.five_s
            
            if suite == 2:
                return game_state.five_c
            
            if suite == 3:
                return game_state.five_d
            
            if suite == 4:
                return game_state.five_h
            
            

        if card == 6:

            if suite == 1:
                return game_state.six_s
            
            if suite == 2:
                return game_state.six_c
            
            if suite == 3:
                return game_state.six_d
            
            if suite == 4:
                return game_state.six_h
            

        if card == 7:

            if suite == 1:
                return game_state.seven_s
            
            if suite == 2:
                return game_state.seven_c
            
            if suite == 3:
                return game_state.seven_d
            
            if suite == 4:
                return game_state.seven_h
            
            
        
        if card == 8:

            if suite == 1:
                return game_state.eight_s
            
            if suite == 2:
                return game_state.eight_c
            
            if suite == 3:
                return game_state.eight_d
            
            if suite == 4:
                return game_state.eight_h
            
            

        if card == 9:

            if suite == 1:
                return game_state.nine_s
            
            if suite == 2:
                return game_state.nine_c
            
            if suite == 3:
                return game_state.nine_d
            
            if suite == 4:
                return game_state.nine_h
            
            

        if card == 10:

            if suite == 1:
                return game_state.ten_s
            
            if suite == 2:
                return game_state.ten_c
            
            if suite == 3:
                return game_state.ten_d
            
            if suite == 4:
                return game_state.ten_h
            
            
        
        if card == 11:

            if suite == 1:
                return game_state.jack_s
            
            if suite == 2:
                return game_state.jack_c
            
            if suite == 3:
                return game_state.jack_d
            
            if suite == 4:
                return game_state.jack_h
            
            
        if card == 12:


            if suite == 1:
                return game_state.queen_s
            
            if suite == 2:
                return game_state.queen_c
            
            if suite == 3:
                return game_state.queen_d
            
            if suite == 4:
                return game_state.queen_h
            
        
        if card == 13:

            if suite == 1:
                return game_state.king_s
            
            if suite == 2:
                return game_state.king_c
            
            if suite == 3:
                return game_state.king_d
            
            if suite == 4:
                return game_state.king_h
    
    def win_check(self, player, dealer):

        # Checking for losses, a return of 0 means the player lost, 1 means the player won, 2 means the player got black jack and 3 means the dealer got black jack
        if player > 21:
            return 0

        
        if player < dealer:
            if player <= 21 and dealer <= 21:
                return 0
        
        if player == 21 and Player.hit_flag == 0: #Player.hit_flag == 0 and Player.stand_flag != 0 and :
    
            return 2
        

        if player <= 21 and dealer <= 21 and player > dealer: # and Player.player_second_card_flag != 0 and Player.player_hand_value != 21:
            return 1
        
        if player <= 21 and dealer > 21:
            return 1 

        if Dealer.dealer_hand_value == 21:
            return 3

        if player <= 21 and dealer <= 21:
            if player == dealer:
                return 4

    def round_result(self):

        # Conditions to signify that the round is over, either player or dealer gets blackjack or if the dealer exceeds 16
        if player.deal_flag != 0 and (d_card1 + d_card2 ) != 21 and player.player_hand_value == 21 and player.hit_flag == 0 and dealer.second_card_flag != 0:
            dealer.round_over_flag = 1
        
        if dealer.dealer_hand_value > 16 or (player.player_hand_value == 21 and player.hit_flag == 0 and (d_card1 > 1 and d_card1 < 10)):
                dealer.round_over_flag = 1

        if dealer.round_over_flag != 0:
    
            if self.win_check(player.player_hand_value, dealer.dealer_hand_value) == 1: 
                game_state.initial_balance = int(game_state.remainder + 2 * game_state.bet_value)
                game_state.win_value = int(2 * game_state.bet_value)

            if self.win_check(player.player_hand_value, dealer.dealer_hand_value) == 2: 
                game_state.initial_balance = int(game_state.remainder + 2.5 * game_state.bet_value)
                game_state.win_value = int(2.5 * game_state.bet_value)
            
            if self.win_check(player.player_hand_value, dealer.dealer_hand_value) == 4: 
                game_state.initial_balance = int(game_state.remainder + game_state.bet_value)
                game_state.win_value = 0
            
            
            if self.win_check(player.player_hand_value, dealer.dealer_hand_value) == 0:
                game_state.win_value = 0
                dealer.round_over_flag = 1     
    
    def new_round(self):

        if dealer.round_over_flag != 0:
            player.deal_flag = 0
            player.deal_btn_flag = 10
            player.hit_flag = 0
            player.stand_flag = 0
            dealer.second_card_flag = 0
            dealer.third_card_flag = 0
            dealer.fourth_card_flag = 0
            dealer.back_card_flag = 0
            game_state.inital_player_hand_time = time.time()
            game_state.initial_time = 999999999999999999
    
    # Test button 
    flag = 0
    card_1 = 0
    card_2 = 0
    def test_btn(self):
        
        if game.mouse.get_pos()[0] > 100 and game.mouse.get_pos()[0] < 200:
            if game.mouse.get_pos()[1] > 20 and game.mouse.get_pos()[1] <70:
                btn_colour = (70, 10, 10)
                game.draw.rect(game_state.screen, (btn_colour),[100, 20, 100, 50])
                for event in game.event.get():
                    if event.type == game.MOUSEBUTTONDOWN:
                        self.card_1 = random.randint(1, 2)
                        self.card_2 = random.randint(1, 2)
                        self.flag = 1
            
                        print("pressed")
        
        if self.flag == 1:

            self.screen.fill(self.bg_colour)
            self.screen.blit(self.table_img, (0, 0))
            self.status_display()
            player.buttons()
            game_state.screen.blit(game_state.card_display(self.card_1, 1), dealer.dealer_position_generator(0))
            game_state.screen.blit(game_state.card_display(self.card_2, 2), dealer.dealer_position_generator(1))
            game_state.screen.blit(game_state.card_display(self.card_1, 1), player.card_position_generator(0))
            game_state.screen.blit(game_state.card_display(self.card_2, 2), player.card_position_generator(1))
            print(self.flag)
            game.display.flip()
            

    def window_init(self):
        self.pygame_init()
        game.display.set_caption('Back Jack')
        self.screen.fill(self.bg_colour)
        self.screen.blit(self.table_img, (0, 0))
        self.status_display()
        game.display.flip()
    # Create card deck 


    # Create game loop

    # Creating Buttons


    def game_loop(self):

        running = True
        #player.card_generator()
        #dealer.dealer_card_generator()
        #player.card_value_handle()
        game_state.window_init()
        while running:
            #game.time.delay(2)
            #game_state.window_init()
            # game_state.status_display()
            # player.buttons()
            # player.dealt_cards()
            # dealer.dealer_cards()
            game_state.round_result()
            game_state.new_round()
            #game_state.test_btn()
            player.deal_display()
            print(game_state.initial_player_hand_time_flag)
            for event in game.event.get():

                if event.type == game.QUIT: 
                    running = False
                    game.quit()
                    sys.exit()


# Class to handle the rules of the player
class Player:

    # Flags to signify when certain buttons have been pressed  
    deal_flag = 0
    hit_flag = 0
    stand_flag = 0 
    
    # Array to store the randomly generated cards of the player
    player_card_arr = []

    # Function to generate random cards for the player
    def card_generator(self):
        global card1, suite1, card2, suite2 , card3, suite3, card4, suite4
        global card5, suite5, card6, suite6 , card7, suite7, card8, suite8

        card1 = random.randint(1, 13)
        suite1 = random.randint(1,4)

        card2 = random.randint(1, 13)
        suite2 = random.randint(1,4)

        card3 = random.randint(1, 13)
        suite3 = random.randint(1,4)

        card4 = random.randint(1, 13)
        suite4 = random.randint(1,4)

        card5 = random.randint(1, 13)
        suite5 = random.randint(1,4)

        card6 = random.randint(1, 13)
        suite6 = random.randint(1,4)

        card7 = random.randint(1, 13)
        suite7 = random.randint(1,4)

        card8 = random.randint(1, 13)
        suite8 = random.randint(1,4)

        self.player_card_arr = [card1, card2, card3, card4, card5, card6, card7, card8]
    # Action buttons
    game.font.init()
    font = game.font.SysFont("calibri", 20)

    # Actions of pressing the split button 
    split_x_pos = 350
    split_y_pos = 725

    split_x_len = 90
    split_y_len = 55
    def split_action(self):
        split = self.font.render("SPLIT", True, game_state.white)

        btn_colour = (70, 10, 10)
        game.draw.rect(game_state.screen, (btn_colour),[self.split_x_pos, self.split_y_pos, self.split_x_len, self.split_y_len])
        game_state.screen.blit(split, (self.split_x_pos + (0.27 * self.split_x_len), self.split_y_pos + (0.25 * self.split_y_len)))
        for event in game.event.get():
            if event.type == game.MOUSEBUTTONDOWN:
                print("SPLIT CLICKED")
                btn_colour = (112, 10, 10)
                game.draw.rect(game_state.screen, (btn_colour),[self.split_x_pos, self.split_y_pos, self.split_x_len, self.split_y_len])
                game_state.screen.blit(split, (self.split_x_pos + (0.27 * self.split_x_len), self.split_y_pos + (0.3 * self.split_y_len)))
    
    # Actions of pressing the hit button
    hit_x_pos = split_x_pos + 200
    hit_y_pos = split_y_pos

    hit_x_len = split_x_len
    hit_y_len = split_y_len
    def hit_action(self):

        hit = self.font.render("HIT", True, game_state.white)

        print("HIT CLICKED")

        game.draw.rect(game_state.screen, (game_state.table_red),[self.hit_x_pos, self.hit_y_pos, self.hit_x_len, self.hit_y_len])
        game_state.screen.blit(hit, (self.hit_x_pos + (0.35 * self.hit_x_len), self.hit_y_pos + (0.3 * self.hit_y_len)))
        self.hit_flag += 1
        print("hit flag is now: " + str(self.hit_flag))

    # Actions of pressing the stand button
    stand_x_pos = hit_x_pos + 200
    stand_y_pos = split_y_pos

    stand_x_len = split_x_len
    stand_y_len = split_y_len
    def stand_action(self):
        stand = self.font.render("STAND", True, game_state.white)
        print("STAND CLICKED")
        game.draw.rect(game_state.screen, (game_state.table_red),[self.stand_x_pos, self.stand_y_pos, self.stand_x_len, self.stand_y_len])
        game_state.screen.blit(stand, (self.stand_x_pos + 20, self.split_y_pos + (0.3 * self.split_y_len)))
        self.stand_flag += 1
        game_state.initial_time = time.time()


    def double_action(self):
        pass
    
    deal_x_pos = 1240
    deal_y_pos = 660
    deal_x_len = 100
    deal_y_len = 30

    # Actions of pressing the deal button
    def deal_action(self):
    
      
        deal = self.font.render("DEAL", True, game_state.white)
        btn_colour = (70, 10, 10)

        game.draw.rect(game_state.screen, (btn_colour),[self.deal_x_pos, self.deal_y_pos, self.deal_x_len, self.deal_y_len])
        game_state.screen.blit(deal, (self.deal_x_pos + 10, self.deal_y_pos + 6))
        self.deal_flag += 1
        game_state.bet_value = game_state.count_value
        game_state.remainder = game_state.initial_balance - game_state.count_value
        game_state.initial_balance = game_state.initial_balance - game_state.count_value
        player.player_hand_value = 0
        dealer.dealer_hand_value = 0
        game_state.initial_player_hand_time_flag = 0
        #self.hit_flag = 0
        #print("Hit flag is: " + str(self.hit_flag))
        print("The time flag is:" + str(game_state.initial_player_hand_time_flag))

        if game_state.initial_balance < 0:
            game_state.initial_balance = 0
        
        game_state.count_value = game_state.remainder
        
        game_state.inital_player_hand_time = time.time()
        game_state.initial_time = 999999999999999999
        print(self.deal_flag)


    sub_x_pos = GamePlay.bet_display_x_pos 
    sub_y_pos =  615

    sub_x_len = 30
    sub_y_len = 30
    
    def sub_action(self):
        sub = self.font.render("-", True, game_state.white)
        print("ADD CLICKED")
        game.draw.rect(game_state.screen, (game_state.table_red),[self.sub_x_pos, self.sub_y_pos, self.sub_x_len, self.sub_y_len])
        game_state.screen.blit(sub, (self.sub_x_pos + 10, self.sub_y_pos + 6))
        game_state.count_value -= 50

        if game_state.count_value < 0:
            game_state.count_value = 0
    
    add_x_pos = 1350
    add_y_pos =  sub_y_pos

    add_x_len = 30
    add_y_len = 30
    
    def add_action(self):
        add = self.font.render("-", True, game_state.white)
        game.draw.rect(game_state.screen, (game_state.table_red),[self.add_x_pos, self.add_y_pos, self.add_x_len, self.add_y_len])
        game_state.screen.blit(add, (self.add_x_pos + 10, self.add_y_pos + 6))
        game_state.count_value += 50

        if game_state.count_value > game_state.initial_balance:
            game_state.count_value = game_state.initial_balance

    hit_btn_time_init = 0
    hit_btn_flag = 0

    stand_btn_time_init = 0
    stand_btn_flag = 0

    deal_btn_time_init = 0
    deal_btn_flag = 0

    sub_btn_time_init = 0
    sub_btn_flag = 0

    add_btn_time_init = 0
    add_btn_flag = 0

    def buttons(self):
        font = game.font.SysFont("calibri", 20)

        font_x_pos = 20
        font_y_pos = 5

        btn_colour = (112, 10, 10)
        
        keys = game.key.get_pressed()
        # Split button
        split_x_pos = 350
        split_y_pos = 725

        split_x_len = 90
        split_y_len = 55
        split = font.render("SPLIT", True, game_state.white)
        game.draw.rect(game_state.screen, (game_state.boarder), [split_x_pos - 1, split_y_pos - 1, split_x_len + 2, split_y_len + 2])
        game.draw.rect(game_state.screen, (btn_colour),[split_x_pos, split_y_pos, split_x_len, split_y_len])
        game_state.screen.blit(split, (split_x_pos + (0.27 * split_x_len), split_y_pos + (0.3 * split_y_len)))

        if keys[game.K_PERIOD]:
            self.split_action()

        if game.mouse.get_pos()[0] > split_x_pos and game.mouse.get_pos()[0] < split_x_pos + split_x_len:
            if game.mouse.get_pos()[1] > split_y_pos and game.mouse.get_pos()[1] < split_y_pos + split_y_len:
                self.split_action()

        # Hit button 
        hit_x_pos = split_x_pos + 200
        hit_y_pos = split_y_pos

        hit_x_len = split_x_len
        hit_y_len = split_y_len
        hit = font.render("HIT", True, game_state.white)
        game.draw.rect(game_state.screen, (game_state.boarder), [hit_x_pos - 1, hit_y_pos - 1, hit_x_len + 2, hit_y_len + 2])
        game.draw.rect(game_state.screen, (game_state.table_red),[hit_x_pos, hit_y_pos, hit_x_len, hit_y_len])
        game_state.screen.blit(hit, (hit_x_pos + (0.35 * hit_x_len), split_y_pos + (0.3 * split_y_len)))

        if (time.time() - self.hit_btn_time_init) > 2:
            self.hit_btn_flag += 1
            self.hit_btn_time_init = time.time()

        if keys[game.K_h] and self.hit_btn_flag != 0 and self.deal_flag != 0:
            self.hit_action()
            self.hit_btn_flag = 0

        if game.mouse.get_pos()[0] > hit_x_pos and game.mouse.get_pos()[0] < hit_x_pos + hit_x_len:
            if game.mouse.get_pos()[1] > hit_y_pos and game.mouse.get_pos()[1] < hit_y_pos + hit_y_len:
                btn_colour = (70, 10, 10)
                game.draw.rect(game_state.screen, (btn_colour),[hit_x_pos, hit_y_pos, hit_x_len, hit_y_len])
                game_state.screen.blit(hit, (hit_x_pos + (0.35 * hit_x_len), hit_y_pos + (0.25 * hit_y_len)))
                for event in game.event.get():
                    if event.type == game.MOUSEBUTTONDOWN and self.deal_flag != 0:
                        self.hit_action()

        # Stand button 
        stand_x_pos = hit_x_pos + 200
        stand_y_pos = split_y_pos

        stand_x_len = split_x_len
        stand_y_len = split_y_len
        stand = font.render("STAND", True, game_state.white)

        game.draw.rect(game_state.screen, (game_state.boarder), [stand_x_pos - 1, stand_y_pos - 1, stand_x_len + 2, stand_y_len + 2])
        game.draw.rect(game_state.screen, (game_state.table_red),[stand_x_pos, stand_y_pos, stand_x_len, stand_y_len])
        game_state.screen.blit(stand, (stand_x_pos + font_x_pos, split_y_pos + (0.3 * split_y_len)))

        if (time.time() - self.stand_btn_time_init) > 1:
            self.stand_btn_flag += 1
            self.stand_btn_time_init = time.time()

        if keys[game.K_s] and self.stand_btn_flag != 0:
            self.stand_action()
            self.stand_btn_flag = 0

        if game.mouse.get_pos()[0] > stand_x_pos and game.mouse.get_pos()[0] < stand_x_pos + stand_x_len:
            if game.mouse.get_pos()[1] > stand_y_pos and game.mouse.get_pos()[1] < stand_y_pos + stand_y_len:
                btn_colour = (70, 10, 10)
                game.draw.rect(game_state.screen, (btn_colour),[stand_x_pos, stand_y_pos, stand_x_len, stand_y_len])
                game_state.screen.blit(stand, (stand_x_pos + font_x_pos, split_y_pos + (0.25 * split_y_len)))
                for event in game.event.get():
                    if event.type == game.MOUSEBUTTONDOWN and self.deal_flag != 0 or self.stand_flag !=0:
                        self.stand_action()

        # Double down button
        double_x_pos = stand_x_pos + 200
        double_y_pos = split_y_pos

        double_x_len = stand_x_len
        double_y_len = stand_y_len
        double = font.render("DOUBLE", True, game_state.white)
        game.draw.rect(game_state.screen, (game_state.boarder), [double_x_pos - 1, double_y_pos - 1, double_x_len + 2, double_y_len + 2])
        game.draw.rect(game_state.screen, (game_state.table_red),[double_x_pos, double_y_pos, double_x_len, stand_y_len])
        game_state.screen.blit(double, (double_x_pos + 12, split_y_pos + (0.3 * split_y_len)))

        if game.mouse.get_pos()[0] > double_x_pos and game.mouse.get_pos()[0] < double_x_pos + double_x_len:
            if game.mouse.get_pos()[1] > double_y_pos and game.mouse.get_pos()[1] < double_y_pos + double_y_len:
                btn_colour = (70, 10, 10)
                game.draw.rect(game_state.screen, (btn_colour),[double_x_pos, double_y_pos, double_x_len, double_y_len])
                game_state.screen.blit(double, (double_x_pos + 12, double_y_pos + (0.25 * double_y_len)))
                for event in game.event.get():
                    if event.type == game.MOUSEBUTTONDOWN:
                        print("DOUBLE CLICKED")
                        btn_colour = (112, 10, 10)
                        game.draw.rect(game_state.screen, (game_state.table_red),[double_x_pos, double_y_pos, double_x_len, stand_y_len])
                        game_state.screen.blit(double, (double_x_pos + 12, split_y_pos + (0.3 * split_y_len)))
        
        # Bet subtraction button 
        sub_x_pos = game_state.bet_display_x_pos 
        sub_y_pos =  615

        sub_x_len = 30
        sub_y_len = 30

        sub = font.render("-", True, game_state.white)
        game.draw.rect(game_state.screen, (game_state.boarder), [sub_x_pos - 1, sub_y_pos - 1, sub_x_len + 2, sub_y_len + 2])
        game.draw.rect(game_state.screen, (game_state.table_red),[sub_x_pos, sub_y_pos, sub_x_len, sub_y_len])

        game_state.screen.blit(sub, (sub_x_pos + 10, sub_y_pos + 6))

        if (time.time() - self.sub_btn_time_init) > 0.3:
            self.sub_btn_flag += 1
            self.sub_btn_time_init = time.time()

        if keys[game.K_LEFT] and self.sub_btn_flag != 0:
            self.sub_action()
            self.sub_btn_flag = 0
        
        if game.mouse.get_pos()[0] > sub_x_pos and game.mouse.get_pos()[0] < sub_x_pos + sub_x_len:
            if game.mouse.get_pos()[1] > sub_y_pos and game.mouse.get_pos()[1] < sub_y_pos + sub_y_len:
                btn_colour = (70, 10, 10)
                game.draw.rect(game_state.screen, (btn_colour),[sub_x_pos, sub_y_pos, sub_x_len, sub_y_len])
                game_state.screen.blit(sub, (sub_x_pos + 10, sub_y_pos + 4))
                for event in game.event.get():
                            if event.type == game.MOUSEBUTTONDOWN:
                                self.sub_action()
        

        # Bet add button 
        add_x_pos = 1350
        add_y_pos =  sub_y_pos

        add_x_len = 30
        add_y_len = 30

        add = font.render("+", True, game_state.white)
        game.draw.rect(game_state.screen, (game_state.boarder), [add_x_pos - 1, add_y_pos - 1, add_x_len + 2, add_y_len + 2])
        game.draw.rect(game_state.screen, (game_state.table_red),[add_x_pos, add_y_pos, add_x_len, add_y_len])

        game_state.screen.blit(add, (add_x_pos + 10, add_y_pos + 6))

        if (time.time() - self.add_btn_time_init) > 0.3:
            self.add_btn_flag += 1
            self.add_btn_time_init = time.time()

        if keys[game.K_RIGHT] and self.add_btn_flag != 0:
            self.add_action()
            self.add_btn_flag = 0
        
        if game.mouse.get_pos()[0] > add_x_pos and game.mouse.get_pos()[0] < add_x_pos + add_x_len:
            if game.mouse.get_pos()[1] > add_y_pos and game.mouse.get_pos()[1] < add_y_pos + add_y_len:
                btn_colour = (70, 10, 10)
                game.draw.rect(game_state.screen, (btn_colour),[add_x_pos, add_y_pos, add_x_len, add_y_len])
                game_state.screen.blit(add, (add_x_pos + 10, add_y_pos + 4))
                for event in game.event.get():
                            if event.type == game.MOUSEBUTTONDOWN:
                                self.add_action()

                    
        # Deal button                       

        deal_x_pos = 1240
        deal_y_pos = 660
        deal_x_len = 100
        deal_y_len = 30
        
        deal = font.render("DEAL", True, game_state.white)
        game.draw.rect(game_state.screen, (game_state.boarder), [deal_x_pos - 1, deal_y_pos - 1, deal_x_len + 2, deal_y_len + 2])
        game.draw.rect(game_state.screen, (game_state.table_red),[deal_x_pos, deal_y_pos, deal_x_len, deal_y_len])

        game_state.screen.blit(deal, (deal_x_pos + 27, deal_y_pos + 6))

        if (time.time() - self.deal_btn_time_init) > 1:
            self.deal_btn_flag += 1
            self.deal_btn_time_init = time.time()

        if keys[game.K_d] and self.deal_btn_flag > 0 and self.deal_btn_flag < 1000:
            player.card_generator()
            dealer.dealer_card_generator()
            self.deal_action()
            player.card_value_handle()
            
            dealer.round_over_flag = 0
            self.deal_btn_flag = 999999
        
        if game.mouse.get_pos()[0] > deal_x_pos and game.mouse.get_pos()[0] < deal_x_pos + deal_x_len:
            if game.mouse.get_pos()[1] > deal_y_pos and game.mouse.get_pos()[1] < deal_y_pos + deal_y_len:
                btn_colour = (70, 10, 10)
                game.draw.rect(game_state.screen, (btn_colour),[deal_x_pos, deal_y_pos, deal_x_len, deal_y_len])
                game_state.screen.blit(deal, (deal_x_pos + 10, deal_y_pos + 4))
                for event in game.event.get():
                            if event.type == game.MOUSEBUTTONDOWN:
                                player.card_generator()
                                dealer.dealer_card_generator()
                                self.deal_action()
                                player.card_value_handle()
                                btn_colour = (112, 10, 10)
                                game.draw.rect(game_state.screen, (game_state.table_red),[deal_x_pos, deal_y_pos, deal_x_len, deal_y_len])
                                game_state.screen.blit(deal, (deal_x_pos + 10, deal_y_pos + 6))


    # Card positions 
    initial_card_x = 630
    initial_card_y = 530
    x_mov = 40
    y_mov = 30

    def card_position_generator(self, position):

        return (self.initial_card_x + (position * self.x_mov), self.initial_card_y - (position * self.y_mov))

    hand_value = 0
    player_hand_value = 0

    # Player money 

    starting_value = 1000
    increment = 50

    # Card count
    card_value_total = 0

    def card_value_handle(self):
    
        if player.deal_flag != 0:
            for i in range(8):

                if self.player_card_arr[i] > 9:
                    self.player_card_arr[i] = 10
                
                if self.player_card_arr[i] == 1:
                    self.player_card_arr[i] = 11


            for i in range(8):

                if dealer.dealer_card_arr[i] > 9:
                    dealer.dealer_card_arr[i] =10
                
                if dealer.dealer_card_arr[i] == 1:
                    dealer.dealer_card_arr[i] = 11
        

    player_second_card_flag = 0
    def dealt_cards(self):

        if (time.time() - game_state.inital_player_hand_time) > 1:
            game_state.initial_player_hand_time_flag += 1
            game_state.inital_player_hand_time = time.time()
        
        if dealer.dealer_hand_value < 17:
            player.deal_flag += 0

        # First card dealt
        if self.deal_flag != 0 and game_state.initial_player_hand_time_flag == 1:
            game_state.screen.blit(game_state.card_display(card1, suite1), self.card_position_generator(0))
            
            self.player_hand_value = self.player_card_arr[0]

        # Second card dealt
        if self.deal_flag != 0 and game_state.initial_player_hand_time_flag > 2 and game_state.flag == 0:

            if dealer.back_card_flag == 0:
                game_state.screen.blit(game_state.card_display(card1, suite1), self.card_position_generator(0))
                game_state.screen.blit(game_state.card_display(card2, suite2), self.card_position_generator(1))
                game_state.screen.blit(game_state.card_display(d_card1, d_suite1), dealer.dealer_position_generator(0))
            
            if dealer.back_card_flag != 0:
                game_state.screen.blit(game_state.card_display(card1, suite1), self.card_position_generator(0))
                game_state.screen.blit(game_state.card_display(card2, suite2), self.card_position_generator(1))
                #game_state.screen.blit(game_state.card_display(d_card1, d_suite1), dealer.dealer_position_generator(0))

            if self.player_card_arr[0] == 11 and self.player_card_arr[1] == 11:
                self.player_card_arr[1] = 1

            self.player_second_card_flag += 1
            self.player_hand_value = self.player_card_arr[0] + self.player_card_arr[1]
        
        # Will increment after all cards are dealt
        if game_state.initial_player_hand_time_flag < 4:
            self.hit_flag = 0

        # Third card dealt
        if self.hit_flag > 0 and game_state.initial_player_hand_time_flag > 3:
            game_state.screen.blit(game_state.card_display(card1, suite1), self.card_position_generator(0))
            game_state.screen.blit(game_state.card_display(card2, suite2), self.card_position_generator(1))
            game_state.screen.blit(game_state.card_display(card3, suite3), self.card_position_generator(2))
            
            if self.player_hand_value > 10 and self.player_card_arr[2] == 11:
                self.player_card_arr[2] = 1

            
            self.player_hand_value = self.player_card_arr[0] + self.player_card_arr[1] + self.player_card_arr[2]
        
        # Fourth card 
        if self.hit_flag > 1 and game_state.initial_player_hand_time_flag > 3:
            game_state.screen.blit(game_state.card_display(card4, suite4), self.card_position_generator(3))

            if self.player_hand_value > 10 and self.player_card_arr[3] == 11:
                self.player_card_arr[3] = 1

            self.player_hand_value = self.player_card_arr[0] + self.player_card_arr[1] + self.player_card_arr[2] + self.player_card_arr[3]
            #self.player_hand_value = game_state.face_value(1, 1) + game_state.face_value(card2, 1) + game_state.face_value(card3, 1) + game_state.face_value(card4, 1)

        if self.hit_flag > 2 and game_state.initial_player_hand_time_flag > 3:

            game_state.screen.blit(game_state.card_display(card5, suite5), self.card_position_generator(4))
            if self.player_hand_value > 10 and self.player_card_arr[4] == 11:
                self.player_card_arr[4] = 1

            self.player_hand_value = self.player_card_arr[0] + self.player_card_arr[1] + self.player_card_arr[2] + self.player_card_arr[3] + self.player_card_arr[4]
            #self.player_hand_value = game_state.face_value(1, 1) + game_state.face_value(card2, 1) + game_state.face_value(card3, 1) + game_state.face_value(card4, 1) + game_state.face_value(card5, 1)
        game.display.flip()

    def deal_display(self):
        if player.deal_flag != 0:
            game_state.screen.fill(game_state.bg_colour)
            game_state.screen.blit(game_state.table_img, (0, 0))
        
        game_state.status_display()
        self.buttons()
        dealer.dealer_cards()
        self.dealt_cards()
     



# Class to handle the rules of the dealer
class Dealer:
    
    dealer_card_arr = []
    def dealer_card_generator(self):

        global d_card1, d_suite1, d_card2, d_suite2, d_card3, d_suite3, d_card4, d_suite4
        global d_card5, d_suite5, d_card6, d_suite6, d_card7, d_suite7, d_card8, d_suite8

        d_card1 = random.randint(1,13)
        d_suite1 = random.randint(1,4)

        d_card2 = random.randint(1,13)
        d_suite2 = random.randint(1,4)

        d_card3 = random.randint(1,13)
        d_suite3 = random.randint(1,4)

        d_card4 = random.randint(1,13)
        d_suite4 = random.randint(1,4)

        d_card5 = random.randint(1,13)
        d_suite5 = random.randint(1,4)

        d_card6 = random.randint(1,13)
        d_suite6 = random.randint(1,4)

        d_card7 = random.randint(1,13)
        d_suite7 = random.randint(1,4)

        d_card8 = random.randint(1,13)
        d_suite8 = random.randint(1,4)

        self.dealer_card_arr = [d_card1, d_card2, d_card3, d_card4,d_card5,d_card6,d_card7,d_card8]
    
    initial_dealer_card_x = 630
    initial_dealer_card_y = 200
    x_dealer_mov = 40
    y_dealer_mov = 30
    
    def dealer_position_generator(self, position): 
        
        return (self.initial_dealer_card_x + (position * self.x_dealer_mov), self.initial_dealer_card_y - (position * self.y_dealer_mov))
    
    dealer_hand_value = 0
    back_card_flag = 0
    second_card_flag = 0
    third_card_flag = 0
    fourth_card_flag = 0
    fifth_card_flag = 0

    round_over_flag = 0

    def dealer_cards(self):

        # Time checking was implemented to control the animation of the cards, 1 second was allocated for each card showing up on the screen
        
        #First dealer card
        if player.deal_flag != 0 and player.stand_flag == 0 and game_state.initial_player_hand_time_flag > 1 and game_state.initial_player_hand_time_flag < 3:

            game_state.screen.blit(game_state.card_display(d_card1, d_suite1), self.dealer_position_generator(0))
            game_state.screen.blit(game_state.card_display(card1, suite1), player.card_position_generator(0))

            self.dealer_hand_value = self.dealer_card_arr[0]
            game.display.flip()
        
        
        if player.deal_flag != 0 and player.stand_flag == 0 and game_state.initial_player_hand_time_flag > 3 and self.second_card_flag == 0: #$and game_state.flag == 0:
            
            self.back_card_flag += 1
            game_state.screen.blit(game_state.card_display(d_card1, d_suite1), self.dealer_position_generator(0))
            game_state.screen.blit(game_state.back, self.dealer_position_generator(1))
    
            game.display.flip()
        
        # Second card dealt
        # A flag for the third card getting dealt was implemented so the code wouldn't run the condition for 2 cards getting dealt which would overlay the current hand
        if player.deal_flag !=0 and player.stand_flag !=0 and self.third_card_flag == 0:
            game_state.screen.blit(game_state.card_display(d_card1, d_suite1), self.dealer_position_generator(0))
            game_state.screen.blit(game_state.card_display(d_card2, d_suite2), self.dealer_position_generator(1))
            self.second_card_flag += 1

            if self.dealer_card_arr[0] == 11 and self.dealer_card_arr[1] == 11:
                self.dealer_card_arr[1] = 1

            self.dealer_hand_value = self.dealer_card_arr[0] + self.dealer_card_arr[1]

        # Third card dealt
        if player.deal_flag !=0 and player.stand_flag !=0 and game_state.time_flag > 0 and self.dealer_hand_value < 17:
            game_state.screen.blit(game_state.card_display(d_card1, d_suite1), self.dealer_position_generator(0))
            game_state.screen.blit(game_state.card_display(d_card2, d_suite2), self.dealer_position_generator(1))
            game_state.screen.blit(game_state.card_display(d_card3, d_suite3), self.dealer_position_generator(2))

            if self.dealer_hand_value > 10 and self.dealer_card_arr[2] == 11:
                self.dealer_card_arr[2] = 1
            
            self.dealer_hand_value = self.dealer_card_arr[0] + self.dealer_card_arr[1] + self.dealer_card_arr[2]

            #self.dealer_hand_value = game_state.face_value(d_card1, 2) + game_state.face_value(d_card2, 2) + game_state.face_value(d_card3, 2)
            self.third_card_flag += 1
            game.display.flip()

        if (time.time() - game_state.initial_time) > 2:
            game_state.time_flag += 1
            game_state.initial_time = time.time()
        
        # Fourth card dealt
        if player.deal_flag !=0 and player.stand_flag !=0 and game_state.time_flag > 1 and self.dealer_hand_value < 17: 
                game_state.screen.blit(game_state.card_display(d_card1, d_suite1), self.dealer_position_generator(0))
                game_state.screen.blit(game_state.card_display(d_card2, d_suite2), self.dealer_position_generator(1))
                game_state.screen.blit(game_state.card_display(d_card3, d_suite3), self.dealer_position_generator(2))
                game_state.screen.blit(game_state.card_display(d_card4, d_suite4), self.dealer_position_generator(3))

                if self.dealer_hand_value > 10 and self.dealer_card_arr[3] == 11:
                    self.dealer_card_arr[3] = 1

                self.dealer_hand_value = self.dealer_card_arr[0] + self.dealer_card_arr[1] + self.dealer_card_arr[2] + self.dealer_card_arr[3]
                self.fourth_card_flag += 1
            
                game.display.flip()
        
        # Fifth card dealt
        if player.deal_flag !=0 and player.stand_flag !=0 and game_state.time_flag > 2 and self.dealer_hand_value < 17: 
                game_state.screen.blit(game_state.card_display(d_card1, d_suite1), self.dealer_position_generator(0))
                game_state.screen.blit(game_state.card_display(d_card2, d_suite2), self.dealer_position_generator(1))
                game_state.screen.blit(game_state.card_display(d_card3, d_suite3), self.dealer_position_generator(2))
                game_state.screen.blit(game_state.card_display(d_card4, d_suite4), self.dealer_position_generator(3))
                game_state.screen.blit(game_state.card_display(d_card5, d_suite5), self.dealer_position_generator(4))
                if self.dealer_hand_value > 10 and self.dealer_card_arr[4] == 11:
                    self.dealer_card_arr[4] = 1

                self.dealer_hand_value = self.dealer_card_arr[0] + self.dealer_card_arr[1] + self.dealer_card_arr[2] + self.dealer_card_arr[3] + self.dealer_card_arr[4]
                
                self.fifth_card_flag += 1

                game.display.flip()
        
        end_on_second_flag = 0
        if self.second_card_flag != 0 and self.third_card_flag == 0 and dealer.round_over_flag !=0:
            end_on_second_flag += 1

        if end_on_second_flag !=0:
            game_state.screen.blit(game_state.card_display(d_card1, d_suite1), self.dealer_position_generator(0))
            game_state.screen.blit(game_state.card_display(d_card2, d_suite2), self.dealer_position_generator(1))
        
        end_on_third_flag = 0
        if self.third_card_flag != 0 and self.fourth_card_flag == 0 and dealer.round_over_flag !=0:
            end_on_third_flag += 1

        if end_on_third_flag != 0:
            game_state.screen.blit(game_state.card_display(d_card1, d_suite1), self.dealer_position_generator(0))
            game_state.screen.blit(game_state.card_display(d_card2, d_suite2), self.dealer_position_generator(1))
            game_state.screen.blit(game_state.card_display(d_card3, d_suite3), self.dealer_position_generator(2))

        end_on_fourth_flag = 0
        if self.fourth_card_flag != 0 and self.fifth_card_flag == 0 and dealer.round_over_flag !=0:
            end_on_fourth_flag += 1

        if end_on_fourth_flag != 0:
            game_state.screen.blit(game_state.card_display(d_card1, d_suite1), self.dealer_position_generator(0))
            game_state.screen.blit(game_state.card_display(d_card2, d_suite2), self.dealer_position_generator(1))
            game_state.screen.blit(game_state.card_display(d_card3, d_suite3), self.dealer_position_generator(2))
            game_state.screen.blit(game_state.card_display(d_card4, d_suite4), self.dealer_position_generator(3))


game_state = GamePlay( )
player = Player()
dealer = Dealer()

game_state.game_loop()