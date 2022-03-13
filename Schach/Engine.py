import Figures as F
import copy
import pygame as p

MAX_MOVES_BEFORE_REMIS = 50
# sound effects
PAWN_PROMOTION_SOUND = 'sounds/Pawn_Promotion.wav'
INVALID_MOVE_SOUND = 'sounds/invalid_move.wav'
WINNER = 'sounds/winner.wav'
NO_WINNER = 'sounds/no_winner.wav'
HIT = 'sounds/hit.wav'

"""
A game of chess.
Stores the location of all Figures in this Game. 
"""
class GameState():
    """
    Initialize the startstate of chess.
    Whites perspective.
    """
    def __init__(self):
        
        self.board = [
            [F.Tower([0, 0], "black"), F.Knight([0, 1], "black"), F.Bishop([0, 2], "black"), F.Queen([0, 3], "black"), F.King([0, 4], "black"), F.Bishop([0, 5], "black"), F.Knight([0, 6], "black"), F.Tower([0, 7], "black")],
            [F.Pawn([1, 0], "black"), F.Pawn([1, 1], "black"), F.Pawn([1, 2], "black"), F.Pawn([1, 3], "black"), F.Pawn([1, 4], "black"),F.Pawn([1, 5], "black"), F.Pawn([1, 6], "black"), F.Pawn([1, 7], "black")],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [F.Pawn([6, 0], "white"), F.Pawn([6, 1], "white"), F.Pawn([6, 2], "white"), F.Pawn([6, 3], "white"), F.Pawn([6, 4], "white"),F.Pawn([6 ,5], "white"), F.Pawn([6, 6], "white"), F.Pawn([6, 7], "white")],
            [F.Tower([7, 0], "white"), F.Knight([7, 1], "white"), F.Bishop([7, 2], "white"), F.Queen([7, 3], "white"), F.King([7, 4], "white"), F.Bishop([7, 5], "white"), F.Knight([7, 6], "white"), F.Tower([7, 7], "white")],
        ]
        
        self.players_move = "white"
        self.movelog = []
        self.state = "start"

    """
    Make a move and append it to the movelog.
    """
    def move(self, start_position, goal_position):
        try:
            # try to make a move
            m = Move(start_position, goal_position, self.board)
            self.movelog.append(copy.deepcopy(m))
            m.make_move(self.players_move)
            self.players_move = "white" if (self.players_move == "black") else "black"

            # check for final state
            if self.is_checkmate(copy.deepcopy(self.board)):
                self.state = "final"
                p.mixer.music.load(WINNER)
                p.mixer.music.play(0, 0.0)
            if self.is_remis():
                self.state = "final"
                p.mixer.music.load(NO_WINNER)
                p.mixer.music.play(0, 0.0)

        except Exception as e:
            print(e)
            p.mixer.music.load(INVALID_MOVE_SOUND)
            p.mixer.music.play(0, 0.0)
            self.movelog.pop(-1) # dont save the last move

    """
    Undos the last move made.
    Raises Exception if no move was made.
    """
    def undo_move(self):
        try :
            self.board = self.movelog.pop(-1).board 
            self.players_move = "white" if (self.players_move == "black") else "black"

        except Exception as exc:
            raise Exception("Make a First move!!")

    """
    print all made moves.
    """
    def print_movelog(self):
        # get the right chess notation
        ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
        rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
        files_to_cols = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        cols_to_files = {v: k for k, v in files_to_cols.items()}

        print("Movelog:")
        for move in self.movelog:
            print("start: " + cols_to_files[move.start_col] + rows_to_ranks[move.start_row] + " goal: " + cols_to_files[move.goal_col] + rows_to_ranks[move.goal_row])

    """
    print all Figures in this game.
    """
    def print_figures(self):
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != None:
                    self.board[x][y].print()

    """
    Return the amount of Figures in the game
    """
    def count_Figures(self, copied_board):
        count = 0
        for x in range(8):
            for y in range(8):
                if copied_board[x][y] != None:
                    count += 1
        return count

    """
    Returns True if the King of the active player is in checkmate.
    Works on a copy of the board.
    """
    def is_checkmate(self, copied_board):

        for row in range(8):
            for col in range(8):
                # go through every Figure of the color of the activ player, who is possible check-mate
                if copied_board[row][col] != None and copied_board[row][col].color == self.players_move:
                    for goal_position in copied_board[row][col].possible_positions(copied_board):
                        # go through every move of this Figure
                        try:
                            m = Move([row, col], goal_position, copied_board)   
                            m.make_alibi_move(self.players_move)
                            # false if there is a possible move, which unchecks the king
                            return False
                        except Exception as e:
                            continue
        return True

    """
    Returns true if in the last MAX_MOVES_BEFORE_REMIS moves no Figure was killed.
    """
    def is_remis(self):
        if len(self.movelog) >= MAX_MOVES_BEFORE_REMIS and self.count_Figures(self.movelog[-1].board) == self.count_Figures(self.movelog[-MAX_MOVES_BEFORE_REMIS].board):
            self.players_move = None
            return True
        return False



"""
A move has a start -and goalposition on a specific board.
"""
class Move():
    
    def __init__(self, start_position, goal_position, board):
        self.start_col = start_position[1]
        self.start_row = start_position[0]
        self.goal_col = goal_position[1]
        self.goal_row = goal_position[0]
        self.board = board

    """
    Moves the figure at startposition to goalposition.
    The startposition is now empty.
    Raises Exception if not possible.
    """
    def make_move(self, players_move):
        positions = self.board[self.start_row][self.start_col].possible_positions(self.board)
        goal_position = [self.goal_row, self.goal_col]

        # try to make a move if the goal_position is a valid move
        if goal_position in positions:

            self.check_for_Rochade()
            goal_field = self.board[self.goal_row][self.goal_col] # safe the figure of the goal position
            
            # sound effect for hitting
            if not goal_field == None:
                p.mixer.music.load(HIT)
                p.mixer.music.play(0, 0.0)

            # change values of the moved figures
            self.board[self.goal_row][self.goal_col] = self.board[self.start_row][self.start_col]
            self.board[self.start_row][self.start_col] = None
            self.board[self.goal_row][self.goal_col].position = [self.goal_row, self.goal_col]
            self.board[self.goal_row][self.goal_col].has_moved = True
            
            self.check_for_check(goal_field, players_move) # potentially undo the move
            self.check_for_pawn_promotion()

            return 

        raise Exception("Invalid move!")

    """
    Makes a move on a board just to check if the king is not checked after this move.
    """
    def make_alibi_move(self, players_move):
        goal_field = self.board[self.goal_row][self.goal_col] # safe the figure of the goal position
        
        # change values of the moved figures
        self.board[self.goal_row][self.goal_col] = self.board[self.start_row][self.start_col]
        self.board[self.start_row][self.start_col] = None
        self.board[self.goal_row][self.goal_col].position = [self.goal_row, self.goal_col]
        self.board[self.goal_row][self.goal_col].has_moved = True

        self.check_for_check(goal_field, players_move) # potentially undo the move

    """
    Change thr the Pawn to another Figure accepted the King,
    if promoted.
    """
    def check_for_pawn_promotion(self):
        if self.board[self.goal_row][self.goal_col].name == "Pawn":
            if self.goal_row == 0 or self.goal_row == 7:

                # loop until the user decided which Figure he wants
                looping = True
                while looping:
                    for event in p.event.get():
                        if event.type == p.KEYDOWN:
                            if event.key == p.K_q: # Queen
                                self.board[self.goal_row][self.goal_col] = F.Queen([self.goal_row, self.goal_col], self.board[self.goal_row][self.goal_col].color)
                                looping = False
                                break
                            elif event.key == p.K_k: # Knight
                                self.board[self.goal_row][self.goal_col] = F.Knight([self.goal_row, self.goal_col], self.board[self.goal_row][self.goal_col].color)
                                looping = False
                                break
                            elif event.key == p.K_t: # Tower
                                self.board[self.goal_row][self.goal_col] = F.Tower([self.goal_row, self.goal_col], self.board[self.goal_row][self.goal_col].color)
                                looping = False
                                break
                            elif event.key == p.K_b: # Bishop
                                self.board[self.goal_row][self.goal_col] = F.Bishop([self.goal_row, self.goal_col], self.board[self.goal_row][self.goal_col].color)
                                looping = False
                                break
                
                p.mixer.music.load(PAWN_PROMOTION_SOUND)
                p.mixer.music.play(0, 0.0)

    """
    Raises an Exception if the King of the player in action is checked after the move.
    Undos the move.
    """
    def check_for_check(self, goal_field, players_move):
        for row in range(8):
            for col in range(8):
                if self.board[row][col] != None:

                    # find the king and check for check
                    if self.board[row][col].name == "King" and self.board[row][col].color == players_move:
                        if self.board[row][col].check(self.board):
                            # if king is checked undo the move
                            self.board[self.start_row][self.start_col] = self.board[self.goal_row][self.goal_col]
                            self.board[self.goal_row][self.goal_col] = goal_field
                            self.board[self.start_row][self.start_col].position = [self.start_row, self.start_col]
                            self.board[self.start_row][self.start_col].has_moved = False

                            raise Exception("Your King is checked!")
                        break
        return
            
    """
    Checks if a Rochade was made and also moves the Tower if so.
    """
    def check_for_Rochade(self):
        # check for Rochade
        if self.board[self.start_row][self.start_col].name == "King":
            # right Rochade, if so move the tower
            if self.goal_col == self.start_col + 2:
                self.board[self.start_row][5] = self.board[self.start_row][7]
                self.board[self.start_row][7] = None
                self.board[self.start_row][5].has_moved = True
                self.board[self.start_row][5].position = [self.start_row, 5]
            # left Rochade, if so move the tower
            elif self.goal_col == self.start_col - 2:
                self.board[self.start_row][3] = self.board[self.start_row][0]
                self.board[self.start_row][0] = None
                self.board[self.start_row][3].has_moved = True
                self.board[self.start_row][3].position = [self.start_row, 3]

        return
