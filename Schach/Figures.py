
"""
a Blueprint of a Figure.
"""
class Figure:
    """
    create a Figure at a specific position.
    It has a color and has a specific value.
    """
    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.name = str(type(self))[16:-2] # cut the type so its just the name of the class
        self.has_moved = False

    """
    Print all attributes of this figure.
    """
    def print(self):
        print("Position: ", self.position, ", Color: ", self.color, ", Figure: ", self.name, ", moved: ", self.has_moved)

"""
Can move up, down, left, right.
Endless range.
"""
class Tower(Figure):
    """
    Return all possible positions, the figure can stand on, after this move.
    It can only move to positions, which are available by its moveset
    and empty or from the other color.
    """
    def possible_positions(self, board):
        positions = [] # a list of all possible moves
        """
        A tower can move up, down, left, rights until he
        touches a wall or a figure.
        So to get all his possible positions, the method has to check
        all moves until facing an distraction.
        """
        # right
        for x in range(1, 8):
            # if out of board
            if self.position[1] + x > 7:
                break
            # if a figure is found
            elif board[self.position[0]][self.position[1] + x] != None:
                if board[self.position[0]][self.position[1] + x].color == self.color: # if it is the same color
                    break
                elif board[self.position[0]][self.position[1] + x].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0], self.position[1] + x])
                    break   
            # if no Figure is found append the move to positions
            positions.append([self.position[0], self.position[1] + x])
        
        # left
        for x in range(1, 8):
            # if out of board
            if self.position[1] - x < 0:
                break
            # if a figure is found
            elif board[self.position[0]][self.position[1] - x] != None:
                if board[self.position[0]][self.position[1] - x].color == self.color: # if it is the same color
                    break
                elif board[self.position[0]][self.position[1] - x].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0], self.position[1] - x])
                    break
            # if no Figure is found append the move to positions
            positions.append([self.position[0], self.position[1] - x])
        
        # down
        for y in range(1, 8):
            # if out of board
            if self.position[0] + y > 7:
                break
            # if a figure is found
            elif board[self.position[0] + y][self.position[1]] != None:
                if board[self.position[0] + y][self.position[1]].color == self.color: # if it is the same color
                    break
                elif board[self.position[0] + y][self.position[1]].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0] + y, self.position[1]])
                    break
            # if no Figure is found append the move to positions
            positions.append([self.position[0] + y, self.position[1]])
        
        # up
        for y in range(1, 8):
            # if out of board
            if self.position[0] - y < 0:
                break
            # if a figure is found
            elif board[self.position[0] - y][self.position[1]] != None:
                if board[self.position[0] - y][self.position[1]].color == self.color: # if it is the same color
                    break
                elif board[self.position[0] - y][self.position[1]].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0] - y, self.position[1]])
                    break
            # if no Figure is found append the move to positions
            positions.append([self.position[0] - y, self.position[1]])

        return positions

"""
Can move diagonal in every direction.
Endless range.
"""
class Bishop(Figure):
    """
    Return all possible positions, the figure can stand on, after this move.
    It can only move to positions, which are available by its moveset
    and empty or from the other color.
    """
    def possible_positions(self, board):
        positions = [] # a list of all possible moves
        """
        A Bishop can move up-right, up-left, down-right, down-left until he
        touches a wall or a figure.
        So to get all his possible positions, the method has to check
        all moves until facing an distraction.
        """
        # down-right
        for i in range(1, 8):
            # if out of board
            if self.position[0] + i > 7 or self.position[1] + i > 7:
                break
            # if a figure is found
            elif board[self.position[0] + i][self.position[1] + i] != None:
                if board[self.position[0] + i][self.position[1] + i].color == self.color: # if it is the same color
                    break
                elif board[self.position[0] + i][self.position[1] + i].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0] + i, self.position[1] + i])
                    break
            # if no Figure is found append the move to positions
            positions.append([self.position[0] + i, self.position[1] + i])

        # down-left
        for i in range(1, 8):
            # if out of board
            if self.position[0] + i > 7 or self.position[1] - i < 0:
                break
            # if a figure is found
            elif board[self.position[0] + i][self.position[1] - i] != None:
                if board[self.position[0] + i][self.position[1] - i].color == self.color: # if it is the same color
                    break
                elif board[self.position[0] + i][self.position[1] - i].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0] + i, self.position[1] - i])
                    break
            # if no Figure is found append the move to positions
            positions.append([self.position[0] + i, self.position[1] - i])

        # up-right
        for i in range(1, 8):
            # if out of board
            if self.position[0] - i < 0 or self.position[1] + i > 7:
                break
            # if a figure is found
            elif board[self.position[0] - i][self.position[1] + i] != None:
                if board[self.position[0] - i][self.position[1] + i].color == self.color: # if it is the same color
                    break
                elif board[self.position[0] - i][self.position[1] + i].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0] - i, self.position[1] + i])
                    break
            # if no Figure is found append the move to positions
            positions.append([self.position[0] - i, self.position[1] + i])

        # up-left
        for i in range(1, 8):
            # if out of board
            if self.position[0] - i < 0 or self.position[1] - i < 0:
                break
            # if a figure is found
            elif board[self.position[0] - i][self.position[1] - i] != None:
                if board[self.position[0] - i][self.position[1] - i].color == self.color: # if it is the same color
                    break
                elif board[self.position[0] - i][self.position[1] - i].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0] - i, self.position[1] - i])
                    break
            # if no Figure is found append the move to positions
            positions.append([self.position[0] - i, self.position[1] - i])

        return positions
    
"""
Can move 2 (up, down, left, right) and one to the side (relative to the 2 step move).
Can jump over other Figures.
"""
class Knight(Figure):
    """
    Return all possible positions, the figure can stand on, after this move.
    It can only move to positions, which are available by its moveset
    and empty or from the other color.
    """
    def possible_positions(self, board):
        positions = [] # a list of all possible moves
        # up-right, up-left, down-right, down-left, right-down, right-up, left-down, left-up
        knight_moves = [[-2, 1], [-2, -1], [2, 1], [2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

        for move in knight_moves:
            # continue if the move ends outside the board
            if self.position[0] + move[0] > 7 or self.position[0] + move[0] < 0 or self.position[1] + move[1] > 7 or self.position[1] + move[1] < 0:
                continue
            # continue if the move ends on a Figure of the same color
            if board[self.position[0] + move[0]][self.position[1] + move[1]] != None:
                if board[self.position[0] + move[0]][self.position[1] + move[1]].color == self.color:
                    continue
            
            positions.append([self.position[0] + move[0], self.position[1] + move[1]])

        return positions
"""
Can move 1 forward. If not moved before 2.
Can hit by moving one left up or right up.
"""
class Pawn(Figure):
    """
    Return all possible positions, the figure can stand on, after this move.
    It can only move to positions, which are available by its moveset
    and empty or from the other color.
    """
    def possible_positions(self, board):
        positions = [] # a list of all possible moves

        if self.color == "black":
            # check for two forward
            if self.position[0] + 2 <= 7:
                if not self.has_moved:
                    if board[self.position[0] + 2][self.position[1]] == None and board[self.position[0] + 1][self.position[1]] == None:
                        positions.append([self.position[0] + 2, self.position[1]])
            # check for one forward
            if self.position[0] + 1 <= 7:
                if board[self.position[0] + 1][self.position[1]] == None:
                    positions.append([self.position[0] + 1, self.position[1]])
                # check for hiting
                if self.position[1] + 1 <= 7: # right slash
                    if board[self.position[0] + 1][self.position[1] + 1] != None:
                        if board[self.position[0] + 1][self.position[1] + 1].color != self.color:
                            positions.append([self.position[0] + 1, self.position[1] + 1])
    
                if self.position[1] - 1 >= 0: # left slash
                    if board[self.position[0] + 1][self.position[1] - 1] != None:
                        if board[self.position[0] + 1][self.position[1] - 1].color != self.color:
                            positions.append([self.position[0] + 1, self.position[1] - 1])
                    
            
        if self.color == "white":
            # check for two forward
            if self.position[0] - 2 >= 0: 
                if not self.has_moved:
                    if board[self.position[0] - 2][self.position[1]] == None and board[self.position[0] - 1][self.position[1]] == None:
                        positions.append([self.position[0] - 2, self.position[1]])

            # check for one forward
            if self.position[0] - 1 >= 0:
                if board[self.position[0] - 1][self.position[1]] == None:
                    positions.append([self.position[0] - 1, self.position[1]])
                # check for hiting
                if self.position[1] + 1 <= 7: # right slash
                    if board[self.position[0] - 1][self.position[1] + 1] != None:
                        if board[self.position[0] - 1][self.position[1] + 1].color != self.color:
                            positions.append([self.position[0] - 1, self.position[1] + 1])
                    
                if self.position[1] - 1 >= 0: # left slash
                    if board[self.position[0] - 1][self.position[1] - 1] != None:
                        if board[self.position[0] - 1][self.position[1] - 1].color != self.color:
                            positions.append([self.position[0] - 1, self.position[1] - 1])
                    
        return positions

"""
Can move in all directions.
Endless range.
"""
class Queen(Figure):
    """
    Return all possible positions, the figure can stand on, after this move.
    It can only move to positions, which are available by its moveset
    and empty or from the other color.
    """
    def possible_positions(self, board):
        positions = [] # a list of all possible moves
        """
        A Quen can move up, down, left, right, up-left, up-right, down-left, down-right until she
        touches a wall or a figure.
        So to get all her possible positions, the method has to check
        all moves until facing an distraction.
        """
        # right
        for x in range(1, 8):
            # if out of board
            if self.position[1] + x > 7:
                break
            # if a figure is found
            elif board[self.position[0]][self.position[1] + x] != None:
                if board[self.position[0]][self.position[1] + x].color == self.color: # if it is the same color
                    break
                elif board[self.position[0]][self.position[1] + x].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0], self.position[1] + x])
                    break
            # if no Figure is found append the move to positions
            positions.append([self.position[0], self.position[1] + x])
        
        # left
        for x in range(1, 8):
            # if out of board
            if self.position[1] - x < 0:
                break
            # if a figure is found
            elif board[self.position[0]][self.position[1] - x] != None:
                if board[self.position[0]][self.position[1] - x].color == self.color: # if it is the same color
                    break
                elif board[self.position[0]][self.position[1] - x].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0], self.position[1] - x])
                    break
            # if no Figure is found append the move to positions
            positions.append([self.position[0], self.position[1] - x])
        
        # down
        for y in range(1, 8):
            # if out of board
            if self.position[0] + y > 7:
                break
            # if a figure is found
            elif board[self.position[0] + y][self.position[1]] != None:
                if board[self.position[0] + y][self.position[1]].color == self.color: # if it is the same color
                    break
                elif board[self.position[0] + y][self.position[1]].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0] + y, self.position[1]])
                    break
            # if no Figure is found append the move to positions
            positions.append([self.position[0] + y, self.position[1]])
        
        # up
        for y in range(1, 8):
            # if out of board
            if self.position[0] - y < 0:
                break
            # if a figure is found
            elif board[self.position[0] - y][self.position[1]] != None:
                if board[self.position[0] - y][self.position[1]].color == self.color: # if it is the same color
                    break
                elif board[self.position[0] - y][self.position[1]].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0] - y, self.position[1]])
                    break
            # if no Figure is found append the move to positions
            positions.append([self.position[0] - y, self.position[1]])

        # down-right
        for i in range(1, 8):
            # if out of board
            if self.position[0] + i > 7 or self.position[1] + i > 7:
                break
            # if a figure is found
            elif board[self.position[0] + i][self.position[1] + i] != None:
                if board[self.position[0] + i][self.position[1] + i].color == self.color: # if it is the same color
                    break
                elif board[self.position[0] + i][self.position[1] + i].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0] + i, self.position[1] + i])
                    break
            # if no Figure is found append the move to positions
            positions.append([self.position[0] + i, self.position[1] + i])
        
        # down-left
        for i in range(1, 8):
            # if out of board
            if self.position[0] + i > 7 or self.position[1] - i < 0:
                break
            # if a figure is found
            elif board[self.position[0] + i][self.position[1] - i] != None:
                if board[self.position[0] + i][self.position[1] - i].color == self.color: # if it is the same color
                    break
                elif board[self.position[0] + i][self.position[1] - i].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0] + i, self.position[1] - i])
                    break
            # if no Figure is found append the move to positions
            positions.append([self.position[0] + i, self.position[1] - i])
        
        # up-right
        for i in range(1, 8):
            # if out of board
            if self.position[0] - i < 0 or self.position[1] + i > 7:
                break
            # if a figure is found
            elif board[self.position[0] - i][self.position[1] + i] != None:
                if board[self.position[0] - i][self.position[1] + i].color == self.color: # if it is the same color
                    break
                elif board[self.position[0] - i][self.position[1] + i].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0] - i, self.position[1] + i])
                    break
            # if no Figure is found append the move to positions
            positions.append([self.position[0] - i, self.position[1] + i])
        
        # up-left
        for i in range(1, 8):
            # if out of board
            if self.position[0] - i < 0 or self.position[1] - i < 0:
                break
            # if a figure is found
            elif board[self.position[0] - i][self.position[1] - i] != None:
                if board[self.position[0] - i][self.position[1] - i].color == self.color: # if it is the same color
                    break
                elif board[self.position[0] - i][self.position[1] - i].color != self.color: # if it is the other color, append the last move
                    positions.append([self.position[0] - i, self.position[1] - i])
                    break
            # if no Figure is found append the move to positions
            positions.append([self.position[0] - i, self.position[1] - i])

        return positions

"""
Can move in all directions 1.
If he is killed the game is over.
"""
class King(Figure):

    """
    True if King is checked.
    """
    def check (self, board):
        for row in range(8):
            for col in range(8):
                if board[row][col] != None:
                    if board[row][col].color != self.color and board[row][col].name != "King":
                        if self.position in board[row][col].possible_positions(board):
                            return True # if at least one Figure of the opposite color can hit the king
        return False

    """
    Return all possible positions, the figure can stand on, after this move.
    It can only move to positions, which are available by its moveset
    and empty or from the other color.
    """
    def possible_positions(self, board):
        positions = [] # a list of all possible moves

        # normal moves
        for row in range(-1, 2):
            for col in range(-1, 2):
                # continue if th emove ends outside the board
                if self.position[0] + row > 7 or self.position[0] + row < 0 or self.position[1] + col > 7 or self.position[1] + col < 0:
                    continue
                # continue if the move ends on a Figure of the same color
                elif board[self.position[0] + row][self.position[1] + col] != None:
                    if board[self.position[0] + row][self.position[1] + col].color == self.color:
                        continue
                
                positions.append([self.position[0] + row, self.position[1] + col])

        # Rochade
        """
        A Rochade is possible if the king and the tower did not move 
        and the king is not checked. Furthermore there is no Figure 
        between the two.
        """
        if not self.has_moved and not self.check(board):
            # left
            if board[self.position[0]][0] != None:
                if not board[self.position[0]][0].has_moved and board[self.position[0]][0].name == "Tower":
                    if board[self.position[0]][1] == None and board[self.position[0]][2] == None and board[self.position[0]][3] == None:
                        positions.append([self.position[0], self.position[1] - 2])
            # right
            if board[self.position[0]][7] != None:
                if not board[self.position[0]][7].has_moved and board[self.position[0]][7].name == "Tower":
                    if board[self.position[0]][5] == None and board[self.position[0]][6] == None:
                        positions.append([self.position[0], self.position[1] + 2])

        return positions


