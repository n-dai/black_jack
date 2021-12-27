import pygame as game   
import sys
import time
import random

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

    win_display_x_pos = 1200
    win_display_y_pos = 810
    win_display_length = 180
    win_display_width = 21

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


    def pygame_init(self):
        game.init()
        game.font.init()
    
    def status_display(self):
        font = game.font.SysFont("calibri", 20)

        # Bank Roll Display
        game.draw.rect(game_state.screen, (self.boarder), [self.balance_display_x_pos - 1, self.balance_display_y_pos - 1, self.balance_display_length + 2, self.balance_display_width + 2])
        game.draw.rect(game_state.screen, (self.table_red), [self.balance_display_x_pos, self.balance_display_y_pos, self.balance_display_length, self.balance_display_width])
        balance = font.render("Balance:          $" + str(self.initial_balance), True, self.white)
        self.screen.blit(balance, (self.balance_display_x_pos + 7, self.balance_display_y_pos + 2))

        # Win Display
        game.draw.rect(game_state.screen, (self.boarder), [self.win_display_x_pos - 1, self.win_display_y_pos - 1, self.win_display_length + 2, self.win_display_width + 2])
        game.draw.rect(game_state.screen, (self.table_red), [self.win_display_x_pos, self.win_display_y_pos, self.win_display_length, self.win_display_width])
        bet = font.render("Win                 $1000", True, self.white)
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
        player.card_generator()
        while running:
            game.time.delay(2)
            game_state.window_init()
            player.buttons()
            player.dealt_cards()
            #print(game.mouse.get_pos())
            for event in game.event.get():

                if event.type == game.QUIT: 
                    running = False
                    game.quit()
                    sys.exit()



# Class to handle the rules of the player
class Player:
    deal_flag = 0
    hit_flag = 0
    def card_generator(self):
        global card1, suite1, card2, suite2 , card3, suite3, card4, suite4
        card1 = random.randint(1, 13)
        suite1 = random.randint(1,4)

        card2 = random.randint(1, 13)
        suite2 = random.randint(1,4)

        card3 = random.randint(1, 13)
        suite3 = random.randint(1,4)

        card4 = random.randint(1, 13)
        suite4 = random.randint(1,4)

    # Action buttons

    def buttons(self):
        font = game.font.SysFont("calibri", 20)

        font_x_pos = 20
        font_y_pos = 5

        btn_colour = (112, 10, 10)
        

        # Split button
        split_x_pos = 350
        split_y_pos = 725

        split_x_len = 90
        split_y_len = 55
        split = font.render("SPLIT", True, game_state.white)
        game.draw.rect(game_state.screen, (game_state.boarder), [split_x_pos - 1, split_y_pos - 1, split_x_len + 2, split_y_len + 2])
        game.draw.rect(game_state.screen, (btn_colour),[split_x_pos, split_y_pos, split_x_len, split_y_len])
        game_state.screen.blit(split, (split_x_pos + (0.27 * split_x_len), split_y_pos + (0.3 * split_y_len)))

        if game.mouse.get_pos()[0] > split_x_pos and game.mouse.get_pos()[0] < split_x_pos + split_x_len:
            if game.mouse.get_pos()[1] > split_y_pos and game.mouse.get_pos()[1] < split_y_pos + split_y_len:
                btn_colour = (70, 10, 10)
                game.draw.rect(game_state.screen, (btn_colour),[split_x_pos, split_y_pos, split_x_len, split_y_len])
                game_state.screen.blit(split, (split_x_pos + (0.27 * split_x_len), split_y_pos + (0.25 * split_y_len)))
                for event in game.event.get():
                    if event.type == game.MOUSEBUTTONDOWN:
                        print("SPLIT CLICKED")
                        btn_colour = (112, 10, 10)
                        game.draw.rect(game_state.screen, (btn_colour),[split_x_pos, split_y_pos, split_x_len, split_y_len])
                        game_state.screen.blit(split, (split_x_pos + (0.27 * split_x_len), split_y_pos + (0.3 * split_y_len)))


        # Hit button 
        hit_x_pos = split_x_pos + 200
        hit_y_pos = split_y_pos

        hit_x_len = split_x_len
        hit_y_len = split_y_len
        hit = font.render("HIT", True, game_state.white)
        game.draw.rect(game_state.screen, (game_state.boarder), [hit_x_pos - 1, hit_y_pos - 1, hit_x_len + 2, hit_y_len + 2])
        game.draw.rect(game_state.screen, (game_state.table_red),[hit_x_pos, hit_y_pos, hit_x_len, hit_y_len])
        game_state.screen.blit(hit, (hit_x_pos + (0.35 * hit_x_len), split_y_pos + (0.3 * split_y_len)))

        if game.mouse.get_pos()[0] > hit_x_pos and game.mouse.get_pos()[0] < hit_x_pos + hit_x_len:
            if game.mouse.get_pos()[1] > hit_y_pos and game.mouse.get_pos()[1] < hit_y_pos + hit_y_len:
                btn_colour = (70, 10, 10)
                game.draw.rect(game_state.screen, (btn_colour),[hit_x_pos, hit_y_pos, hit_x_len, hit_y_len])
                game_state.screen.blit(hit, (hit_x_pos + (0.35 * hit_x_len), hit_y_pos + (0.25 * hit_y_len)))
                for event in game.event.get():
                    if event.type == game.MOUSEBUTTONDOWN:
                        print("HIT CLICKED")
                        btn_colour = (112, 10, 10)
                        game.draw.rect(game_state.screen, (game_state.table_red),[hit_x_pos, hit_y_pos, hit_x_len, hit_y_len])
                        game_state.screen.blit(hit, (hit_x_pos + (0.35 * hit_x_len), hit_y_pos + (0.3 * hit_y_len)))
                        self.hit_flag += 1

        # Stand button 
        stand_x_pos = hit_x_pos + 200
        stand_y_pos = split_y_pos

        stand_x_len = split_x_len
        stand_y_len = split_y_len
        stand = font.render("STAND", True, game_state.white)
        game.draw.rect(game_state.screen, (game_state.boarder), [stand_x_pos - 1, stand_y_pos - 1, stand_x_len + 2, stand_y_len + 2])
        game.draw.rect(game_state.screen, (game_state.table_red),[stand_x_pos, stand_y_pos, stand_x_len, stand_y_len])
        game_state.screen.blit(stand, (stand_x_pos + font_x_pos, split_y_pos + (0.3 * split_y_len)))

        if game.mouse.get_pos()[0] > stand_x_pos and game.mouse.get_pos()[0] < stand_x_pos + stand_x_len:
            if game.mouse.get_pos()[1] > stand_y_pos and game.mouse.get_pos()[1] < stand_y_pos + stand_y_len:
                btn_colour = (70, 10, 10)
                game.draw.rect(game_state.screen, (btn_colour),[stand_x_pos, stand_y_pos, stand_x_len, stand_y_len])
                game_state.screen.blit(stand, (stand_x_pos + font_x_pos, split_y_pos + (0.25 * split_y_len)))
                for event in game.event.get():
                    if event.type == game.MOUSEBUTTONDOWN:
                        print("STAND CLICKED")
                        btn_colour = (112, 10, 10)
                        game.draw.rect(game_state.screen, (game_state.table_red),[stand_x_pos, stand_y_pos, stand_x_len, stand_y_len])
                        game_state.screen.blit(stand, (stand_x_pos + font_x_pos, split_y_pos + (0.3 * split_y_len)))

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
        
        # Bet add button 
        sub_x_pos = game_state.bet_display_x_pos 
        sub_y_pos =  615

        sub_x_len = 30
        sub_y_len = 30

        sub = font.render("-", True, game_state.white)
        game.draw.rect(game_state.screen, (game_state.boarder), [sub_x_pos - 1, sub_y_pos - 1, sub_x_len + 2, sub_y_len + 2])
        game.draw.rect(game_state.screen, (game_state.table_red),[sub_x_pos, sub_y_pos, sub_x_len, sub_y_len])

        game_state.screen.blit(sub, (sub_x_pos + 10, sub_y_pos + 6))
        
        if game.mouse.get_pos()[0] > sub_x_pos and game.mouse.get_pos()[0] < sub_x_pos + sub_x_len:
            if game.mouse.get_pos()[1] > sub_y_pos and game.mouse.get_pos()[1] < sub_y_pos + sub_y_len:
                btn_colour = (70, 10, 10)
                game.draw.rect(game_state.screen, (btn_colour),[sub_x_pos, sub_y_pos, sub_x_len, sub_y_len])
                game_state.screen.blit(sub, (sub_x_pos + 10, sub_y_pos + 4))
            for event in game.event.get():
                        if event.type == game.MOUSEBUTTONDOWN:
                            print("ADD CLICKED")
                            btn_colour = (112, 10, 10)
                            game.draw.rect(game_state.screen, (game_state.table_red),[sub_x_pos, sub_y_pos, sub_x_len, sub_y_len])
                            game_state.screen.blit(sub, (sub_x_pos + 10, sub_y_pos + 6))
                            game_state.count_value -= 50

                            if game_state.count_value < 0:
                                game_state.count_value = 0
        

        # Bet subtract button 
        add_x_pos = 1350
        add_y_pos =  sub_y_pos

        add_x_len = 30
        add_y_len = 30

        add = font.render("+", True, game_state.white)
        game.draw.rect(game_state.screen, (game_state.boarder), [add_x_pos - 1, add_y_pos - 1, add_x_len + 2, add_y_len + 2])
        game.draw.rect(game_state.screen, (game_state.table_red),[add_x_pos, add_y_pos, add_x_len, add_y_len])

        game_state.screen.blit(add, (add_x_pos + 10, add_y_pos + 6))
        
        if game.mouse.get_pos()[0] > add_x_pos and game.mouse.get_pos()[0] < add_x_pos + add_x_len:
            if game.mouse.get_pos()[1] > add_y_pos and game.mouse.get_pos()[1] < add_y_pos + add_y_len:
                btn_colour = (70, 10, 10)
                game.draw.rect(game_state.screen, (btn_colour),[add_x_pos, add_y_pos, add_x_len, add_y_len])
                game_state.screen.blit(add, (add_x_pos + 10, add_y_pos + 4))
            for event in game.event.get():
                        if event.type == game.MOUSEBUTTONDOWN:
                            print("ADD CLICKED")
                            btn_colour = (112, 10, 10)
                            game.draw.rect(game_state.screen, (game_state.table_red),[add_x_pos, add_y_pos, add_x_len, add_y_len])
                            game_state.screen.blit(add, (add_x_pos + 10, add_y_pos + 6))
                            game_state.count_value += 50

                            if game_state.count_value > game_state.initial_balance:
                                game_state.count_value = game_state.initial_balance
        

        # Deal button

        deal_x_pos = 1240
        deal_y_pos = 660
        deal_x_len = 100
        deal_y_len = 30
        
        deal = font.render("DEAL", True, game_state.white)
        game.draw.rect(game_state.screen, (game_state.boarder), [deal_x_pos - 1, deal_y_pos - 1, deal_x_len + 2, deal_y_len + 2])
        game.draw.rect(game_state.screen, (game_state.table_red),[deal_x_pos, deal_y_pos, deal_x_len, deal_y_len])

        game_state.screen.blit(deal, (deal_x_pos + 10, deal_y_pos + 6))
        
        if game.mouse.get_pos()[0] > deal_x_pos and game.mouse.get_pos()[0] < deal_x_pos + deal_x_len:
            if game.mouse.get_pos()[1] > deal_y_pos and game.mouse.get_pos()[1] < deal_y_pos + deal_y_len:
                btn_colour = (70, 10, 10)
                game.draw.rect(game_state.screen, (btn_colour),[deal_x_pos, deal_y_pos, deal_x_len, deal_y_len])
                game_state.screen.blit(deal, (deal_x_pos + 10, deal_y_pos + 4))
            for event in game.event.get():
                        if event.type == game.MOUSEBUTTONDOWN:
                            print("DEAL CLICKED")
                            btn_colour = (112, 10, 10)
                            game.draw.rect(game_state.screen, (game_state.table_red),[deal_x_pos, deal_y_pos, deal_x_len, deal_y_len])
                            game_state.screen.blit(deal, (deal_x_pos + 10, deal_y_pos + 6))
                            self.deal_flag += 1



    # Card positions 
    initial_card_x = 630
    initial_card_y = 530
    x_mov = 40
    y_mov = 30

    def card_position_generator(self, position):

        return (self.initial_card_x + (position * self.x_mov), self.initial_card_y - (position * self.y_mov))

    card_value = 0
    player_hand_value = 0

    # Player money 

    starting_value = 1000
    increment = 50

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

            self.card_value = 2

        if card == 3:
            if suite == 1:
                return game_state.three_s
            
            if suite == 2:
                return game_state.three_c
            
            if suite == 3:
                return game_state.three_d
            
            if suite == 4:
                return game_state.three_h
            
            self.card_value = 3

        if card == 4:
            if suite == 1:
                return game_state.four_s
            
            if suite == 2:
                return game_state.four_c
            
            if suite == 3:
                return game_state.four_d
            
            if suite == 4:
                return game_state.four_h
            
            self.card_value = 4
        
        if card == 5:
            if suite == 1:
                return game_state.five_s
            
            if suite == 2:
                return game_state.five_c
            
            if suite == 3:
                return game_state.five_d
            
            if suite == 4:
                return game_state.five_h
            
            self.card_value = 5

        if card == 6:
            if suite == 1:
                return game_state.six_s
            
            if suite == 2:
                return game_state.six_c
            
            if suite == 3:
                return game_state.six_d
            
            if suite == 4:
                return game_state.six_h
            
            self.card_value = 6
        
        if card == 7:
            if suite == 1:
                return game_state.seven_s
            
            if suite == 2:
                return game_state.seven_c
            
            if suite == 3:
                return game_state.seven_d
            
            if suite == 4:
                return game_state.seven_h
            
            self.card_value = 7
        
        if card == 8:
            if suite == 1:
                return game_state.eight_s
            
            if suite == 2:
                return game_state.eight_c
            
            if suite == 3:
                return game_state.eight_d
            
            if suite == 4:
                return game_state.eight_h
            
            self.card_value = 8

        if card == 9:
            if suite == 1:
                return game_state.nine_s
            
            if suite == 2:
                return game_state.nine_c
            
            if suite == 3:
                return game_state.nine_d
            
            if suite == 4:
                return game_state.nine_h
            
            self.card_value = 9

        if card == 10:
            if suite == 1:
                return game_state.ten_s
            
            if suite == 2:
                return game_state.ten_c
            
            if suite == 3:
                return game_state.ten_d
            
            if suite == 4:
                return game_state.ten_h
            
            self.card_value = 10
        
        if card == 11:
            if suite == 1:
                return game_state.jack_s
            
            if suite == 2:
                return game_state.jack_c
            
            if suite == 3:
                return game_state.jack_d
            
            if suite == 4:
                return game_state.jack_h
            
            self.card_value = 10

        if card == 12:
            if suite == 1:
                return game_state.queen_s
            
            if suite == 2:
                return game_state.queen_c
            
            if suite == 3:
                return game_state.queen_d
            
            if suite == 4:
                return game_state.queen_h
            
            self.card_value = 10
        
        if card == 13:
            if suite == 1:
                return game_state.king_s
            
            if suite == 2:
                return game_state.king_c
            
            if suite == 3:
                return game_state.king_d
            
            if suite == 4:
                return game_state.king_h
            
            self.card_value = 10
        
    def dealt_cards(self):
        keys = game.key.get_pressed()

        # if draw == 1:
        #     card = game_state.ace_d
        # else: 
        #     card = game_state.king_c

        if self.deal_flag != 0:
            game_state.screen.blit(self.card_display(card1, suite1), self.card_position_generator(0))
            game_state.screen.blit(self.card_display(card2, suite2), self.card_position_generator(1))

        # if keys[game.K_d]:
        #     game_state.screen.blit(game_state.three_d, self.second_card_pos)

        if self.hit_flag > 0:
            game_state.screen.blit(self.card_display(card3, suite3), self.card_position_generator(2))
        
        if self.hit_flag > 1:
            game_state.screen.blit(self.card_display(card3, suite3), self.card_position_generator(2))
            game_state.screen.blit(self.card_display(card4, suite4), self.card_position_generator(3))
        
        game.display.flip()
        


# Class to handle the rules of the dealer
class Dealer:
    pass

game_state = GamePlay( )
player = Player()
dealer = Dealer()

game_state.game_loop()