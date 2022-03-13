import pygame as p, sys
import Engine

# settings of the game
GAME_NAME = "chess"
BOARD_COLOR_1 = "white"
BOARD_COLOR_2 = "grey"
SELECTED_COLOR = "gold"
MOVES_COLOR = "green"
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15

FIGURE_IMAGES = {}




def main():
    # set up the screen and clock
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    p.display.set_caption(GAME_NAME)

    gs = Engine.GameState()
    load_images()

    # for saving the clicks the user made,
    # which are neccesary for this move.
    square_selected = ()
    player_clicks = []

    # the gameloop
    while True:

        # check for userinputs
        for event in p.event.get():

            # for quitting the game
            if event.type == p.QUIT:
                p.quit()
                sys.exit()

            # for moving the figures
            elif event.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE

                # ignore a click if it is the first and on an empty square
                if gs.board[row][col] == None and len(player_clicks) == 0:
                    continue
                # unselect a figure if clicked twice on the same square
                if square_selected == (row, col):
                    square_selected = ()
                    player_clicks = []
                    continue

                square_selected = (row, col)
                player_clicks.append(square_selected)

                # only choose figures from the color of the players turn
                if gs.players_move != gs.board[player_clicks[0][0]][player_clicks[0][1]].color:
                    square_selected = ()
                    player_clicks = []
                    continue

                # try to move the figure
                if len(player_clicks) == 2:
                    # dont go on figures of the players color
                    if gs.board[player_clicks[1][0]][player_clicks[1][1]] != None:
                        if gs.players_move == gs.board[player_clicks[1][0]][player_clicks[1][1]].color:
                            square_selected = ()
                            player_clicks = []
                            continue

                    # make a move
                    gs.move(player_clicks[0], player_clicks[1])
                    square_selected = ()
                    player_clicks = []
                
            
            # key input
            elif event.type == p.KEYDOWN:
                key_input(gs, event.key)


        draw_the_state(screen, gs, player_clicks)
        clock.tick(MAX_FPS)
        p.display.flip()



"""
Responsible for all key inputs.
"""
def key_input(gs, key):
    if gs.state == "start":
        # keyinput in start state
        start_key_input(gs, key)
    elif gs.state == "game":
        # keyinput in game state
        game_key_input(gs, key)
    elif gs.state == "final":
        # keyinput in final state
        final_key_input(gs, key)

"""
Responsible for all key inputs in start state.
"""
def start_key_input(gs, key):
    if key == p.K_SPACE:
        # start the game 
        gs.state = "game"

"""
Responsible for all key inputs in the game state.
"""
def game_key_input(gs, key):
    # print all made moves
    if key == p.K_SPACE:
        gs.print_movelog()
    # print all Figures
    elif key == p.K_f:
        gs.print_figures()
    # new game
    elif key == p.K_n:
        gs = Engine.GameState()
    # undo a move
    elif key == p.K_BACKSPACE:
        try: gs.undo_move()
        except Exception as exc:
            print(exc)

"""
Responsible for all key inputs in the final state.
"""
def final_key_input(gs, key):
    if key == p.K_SPACE:
        # start a new game
        gs.state = "game"
        gs.board = gs.movelog[0].board
        gs.players_move = "white"
        gs.movelog = []




"""
Decides which state should be drawn.
"""
def draw_the_state(screen, gs, player_clicks):
    if gs.state == "start":
        draw_start_state(screen)
    elif gs.state == "game":
        draw_game_state(screen, gs, player_clicks)
    elif gs.state == "final":
        draw_final_state(screen, gs)

"""
Draws the start state.
"""
def draw_start_state(screen):
    draw_board(screen)

"""
Draws the final state. Draws the Queen and the King
of the winnig color or both Kings if it is a remis.
"""
def draw_final_state(screen, gs):
    draw_board(screen)
    # position of the Figures
    row = 3
    left = 3
    right = 4
    if gs.players_move == "black":
        # white won
        screen.blit(FIGURE_IMAGES["white_King"], p.Rect(left * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        screen.blit(FIGURE_IMAGES["white_Queen"], p.Rect(right * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    elif gs.players_move == "white":
        # black won
        screen.blit(FIGURE_IMAGES["black_King"], p.Rect(left * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        screen.blit(FIGURE_IMAGES["black_Queen"], p.Rect(right * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    else:
        # nobody won
        screen.blit(FIGURE_IMAGES["black_King"], p.Rect(left * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        screen.blit(FIGURE_IMAGES["white_King"], p.Rect(right * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

"""
Is responsible for every drawing in this programm while the game is running.
It draws:
    - board
    - figures
"""
def draw_game_state(screen, gs, player_clicks):
    draw_board(screen)
    draw_helpers(screen, gs.board, player_clicks)
    draw_figures(screen, gs.board, player_clicks)

"""
Function to help while programming.
"""
def draw_helpers(screen, board, player_clicks):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            # mark selected field
            if len(player_clicks) >= 1:
                if (row, col) == player_clicks[0]:
                    p.draw.rect(screen, p.Color(SELECTED_COLOR), p.Rect(col * SQ_SIZE,row * SQ_SIZE, SQ_SIZE, SQ_SIZE), 3)
            # mark possible moves
            if len(player_clicks) >= 1:
                if (row, col) == player_clicks[0]:
                    for field in board[row][col].possible_positions(board):
                        p.draw.rect(screen, p.Color(MOVES_COLOR), p.Rect(field[1] * SQ_SIZE,field[0] * SQ_SIZE, SQ_SIZE, SQ_SIZE))

"""
Calculates which field should be white or grey, 
and draws rectangles.
"""
def draw_board(screen):
    colors = [p.Color(BOARD_COLOR_1), p.Color(BOARD_COLOR_2)]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col)% 2)]
            p.draw.rect(screen, color, p.Rect(col * SQ_SIZE,row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

"""
Draws every Figure at its position.
"""
def draw_figures(screen, board, player_clicks):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != None:
                screen.blit(FIGURE_IMAGES[piece.color + "_" + piece.name], p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))





"""
Function to load the images of every Figure in IMAGES.
Is only called ones.
"""
def load_images():
    figures = ["black_Bishop", "black_King", "black_Knight", "black_Pawn", "black_Queen", "black_Tower", "white_Bishop",
              "white_King", "white_Knight", "white_Pawn", "white_Queen", "white_Tower"]
    for figure in figures:
        FIGURE_IMAGES[figure] = p.transform.scale(p.image.load("images/" + figure + ".png"), (SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()