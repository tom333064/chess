import unittest, sys
sys.path.append('/Users/tombohlmann/Documents/programieren/python/Schach')
import Figures as F


class FiguresTest(unittest.TestCase):

    def test_Pawn(self):
        board = [
            [F.Pawn([0, 0], "white"), None, None, None, None, None, None, None],
            [None, None, None, None, None, F.Pawn([1, 5], "black"), F.Pawn([1, 6], "black"), F.Pawn([1, 7], "black")],
            [None, None, None, None, None, F.Pawn([2, 5], "black"),F.Pawn([2, 6], "white") , F.Pawn([2, 7], "white")],
            [None, None, None, None, F.Pawn([3, 4], "white"), None, F.Pawn([3, 6], "white"), None],
            [None, None, None, None, None, None, None, None],
            [F.Pawn([5, 0], "white"), F.Pawn([5, 1], "white"), None, None, None, None, None, None],
            [None, F.Pawn([6, 1], "black"), None, None, None, None, None, None],
            [None, F.Pawn([7, 1], "white"), None, None, None, None, None, F.Pawn([7, 7], "white")],
        ]

        self.assertListEqual(board[5][1].possible_positions(board), [[3, 1], [4, 1]]) # start step
        board[5][1].has_moved = True
        self.assertListEqual(board[5][1].possible_positions(board), [[4, 1]]) # no two step

        self.assertListEqual(board[7][1].possible_positions(board), []) # no move if Figure is infront
        self.assertListEqual(board[6][1].possible_positions(board), []) # no move if Figure is infront

        self.assertListEqual(board[0][0].possible_positions(board), []) # no move in corner of the opposite side
        self.assertListEqual(board[7][7].possible_positions(board), [[5, 7], [6, 7]]) # two moves on the side

        board[5][0].has_moved = True
        self.assertListEqual(board[5][0].possible_positions(board), [[4, 0]]) # one move on the side of the board

        self.assertListEqual(board[2][6].possible_positions(board), [[1, 7], [1, 5]]) # two hit options
        self.assertListEqual(board[1][6].possible_positions(board), [[2, 7]]) # one hit options, don´t hit one Figure

        self.assertListEqual(board[2][5].possible_positions(board), [[4, 5], [3, 5], [3, 6], [3, 4]]) # all options

    def test_Tower(self):
        board = [
            [F.Tower([0, 0], "white"), None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None,],
            [None, None, None, F.Tower([2, 3], "white"), None, None, None, None,],
            [None, F.Tower([3, 1], "white"), None, None, None, F.Tower([3, 5], "black"), None, None,],
            [None, None, None, None, None, None, None, None,],
            [None, None, None, None, F.Tower([5, 4], "white"), F.Tower([5, 5], "white"), F.Tower([5, 6], "black"), None,],
            [None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None,],
        ]
        # open field
        self.assertTrue([2, 0] in board[2][3].possible_positions(board)) # in left
        self.assertTrue([2, 2] in board[2][3].possible_positions(board)) # in left
        self.assertTrue([2, 4] in board[2][3].possible_positions(board)) # in right
        self.assertTrue([2, 7] in board[2][3].possible_positions(board)) # in right
        self.assertTrue([0, 3] in board[2][3].possible_positions(board)) # in up
        self.assertTrue([1, 3] in board[2][3].possible_positions(board)) # in up
        self.assertTrue([3, 3] in board[2][3].possible_positions(board)) # in down
        self.assertTrue([7, 3] in board[2][3].possible_positions(board)) # in down

        self.assertFalse([1, 2] in board[2][3].possible_positions(board)) # not in

        # in Corner
        self.assertTrue([0, 1] in board[0][0].possible_positions(board)) # in right
        self.assertTrue([0, 7] in board[0][0].possible_positions(board)) # in right
        self.assertTrue([1, 0] in board[0][0].possible_positions(board)) # in down
        self.assertTrue([7, 0] in board[0][0].possible_positions(board)) # in down

        self.assertFalse([1, 1] in board[0][0].possible_positions(board)) # not in

        # enemy in line
        self.assertTrue([3, 5] in board[3][1].possible_positions(board)) # hit enemy
        self.assertFalse([3, 6] in board[3][1].possible_positions(board)) # hit nothing behind

        # ally in line
        self.assertFalse([5, 5] in board[5][4].possible_positions(board)) # dont hit ally
        self.assertFalse([5, 6] in board[5][4].possible_positions(board)) # dont hit enemy behind ally
            
    def test_Bishop(self):
        board = [
            [F.Bishop([0, 0], "black"), None, None, None, None, None, None, None],
            [None, None, None, None, None, None, F.Bishop([1, 6], "white"), None],
            [None, None, None, F.Bishop([2, 3], "black"), None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, F.Bishop([4, 3], "white"), None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, F.Bishop([6, 1], "black"), None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]

        # open field
        self.assertTrue([3, 4] in board[2][3].possible_positions(board)) # right-down
        self.assertTrue([6, 7] in board[2][3].possible_positions(board)) # right-down
        self.assertTrue([1, 2] in board[2][3].possible_positions(board)) # left-up
        self.assertTrue([0, 1] in board[2][3].possible_positions(board)) # left-up
        self.assertTrue([3, 2] in board[2][3].possible_positions(board)) # left-down
        self.assertTrue([5, 0] in board[2][3].possible_positions(board)) # left-down
        self.assertTrue([1, 4] in board[2][3].possible_positions(board)) # right-up
        self.assertTrue([0, 5] in board[2][3].possible_positions(board)) # right-up

        # in corner
        self.assertListEqual([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]], board[0][0].possible_positions(board))

        # hit enemy
        self.assertTrue([5, 2] in board[4][3].possible_positions(board)) # possible to move 1 infront
        self.assertTrue([6, 1] in board[4][3].possible_positions(board)) # hit the enemy
        self.assertFalse([7, 0] in board[4][3].possible_positions(board)) # not possible to move behind

        # don´t hit ally
        self.assertTrue([2, 5] in board[4][3].possible_positions(board)) # possible to move 1 infront
        self.assertFalse([1, 6] in board[4][3].possible_positions(board)) # don´t hit the ally
        self.assertFalse([0, 7] in board[4][3].possible_positions(board)) # not possible to move behind

    def test_Knight(self):
        board = [
            [F.Knight([0, 0], "black"), None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, F.Knight([2, 2], "black"), None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, F.Knight([5, 4], "black"), None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, F.Knight([7, 3], "black"), None, F.Knight([7, 5], "white"), None, None],
        ]
        # up-right, up-left, down-right, down-left, right-down, right-up, left-down, left-up
        # order of possible_positions(board) for the knight
        # all 8 moves
        self.assertListEqual([[0, 3], [0, 1], [4, 3], [4, 1], [3, 4], [1, 4], [3, 0], [1, 0]], board[2][2].possible_positions(board))

        # in corner, two moves
        self.assertListEqual([[2, 1], [1, 2]], board[0][0].possible_positions(board))

        # hit enemy
        self.assertTrue([7, 5] in board[5][4].possible_positions(board))

        # don`t hit ally 
        self.assertFalse([7, 3] in board[5][4].possible_positions(board))

    def test_Queen(self):
        board = [
            [F.Queen([0, 0], "black"), None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, F.Queen([2, 3], "black"), None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]
        # open field
        # diagonal
        self.assertTrue([3, 4] in board[2][3].possible_positions(board)) # right-down, min
        self.assertTrue([6, 7] in board[2][3].possible_positions(board)) # right-down, max
        self.assertTrue([1, 2] in board[2][3].possible_positions(board)) # left-up, min
        self.assertTrue([0, 1] in board[2][3].possible_positions(board)) # left-up, max
        self.assertTrue([3, 2] in board[2][3].possible_positions(board)) # left-down, min
        self.assertTrue([5, 0] in board[2][3].possible_positions(board)) # left-down, max
        self.assertTrue([1, 4] in board[2][3].possible_positions(board)) # right-up, min
        self.assertTrue([0, 5] in board[2][3].possible_positions(board)) # right-up, max
        self.assertFalse([0, 6] in board[2][3].possible_positions(board)) # not in
        # vertical and horizontal
        self.assertTrue([2, 0] in board[2][3].possible_positions(board)) # in left, min
        self.assertTrue([2, 2] in board[2][3].possible_positions(board)) # in left, max
        self.assertTrue([2, 4] in board[2][3].possible_positions(board)) # in right, min
        self.assertTrue([2, 7] in board[2][3].possible_positions(board)) # in right, max
        self.assertTrue([1, 3] in board[2][3].possible_positions(board)) # in up, min
        self.assertTrue([0, 3] in board[2][3].possible_positions(board)) # in up, max
        self.assertTrue([3, 3] in board[2][3].possible_positions(board)) # in down, min
        self.assertTrue([7, 3] in board[2][3].possible_positions(board)) # in down, max
        self.assertFalse([7, 4] in board[2][3].possible_positions(board)) # not in


        # in corner
        # vertical and horizontal
        self.assertTrue([0, 1] in board[0][0].possible_positions(board)) # in right, min
        self.assertTrue([0, 7] in board[0][0].possible_positions(board)) # in right, max
        self.assertTrue([1, 0] in board[0][0].possible_positions(board)) # in down, min
        self.assertTrue([7, 0] in board[0][0].possible_positions(board)) # in down, max
        self.assertTrue([1, 1] in board[0][0].possible_positions(board)) # in right-down, min
        self.assertTrue([7, 7] in board[0][0].possible_positions(board)) # in right-down, max

        board = [
            [F.Queen([0, 0], "black"), None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, F.Queen([2, 3], "black"), None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, F.Queen([4, 5], "black"), F.Queen([4, 6], "black"), None],
            [None, None, None, None, F.Queen([5, 4], "white"), F.Queen([5, 5], "white"), None, None],
            [None, None, None, None, F.Queen([6, 4], "white"), None, None, None],
            [None, None, None, None, None, None, None, None],
        ]
        # hit enemy, but nothing behind
        self.assertTrue([4, 6] in board[5][5].possible_positions(board)) # diagonal, enemy
        self.assertFalse([3, 7] in board[5][5].possible_positions(board)) # diagonal, behind enemy
        self.assertTrue([4, 5] in board[5][5].possible_positions(board)) # vertical/horizontal, enemy
        self.assertFalse([3, 5] in board[5][5].possible_positions(board)) # vertical/horizontal, behind enemy

        # don´t hit ally and nothing behind
        self.assertFalse([6, 4] in board[5][5].possible_positions(board)) # diagonal, ally
        self.assertFalse([7, 3] in board[5][5].possible_positions(board)) # diagonal, behind ally
        self.assertFalse([5, 4] in board[5][5].possible_positions(board)) # vertical/horizontal, ally
        self.assertFalse([5, 3] in board[5][5].possible_positions(board)) # vertical/horizontal, behind ally

    def test_King(self):
        board = [
            [F.King([0, 0], "black"), None, None, None, F.King([0, 4], "black"), F.Tower([0, 5], "black"), None, F.Tower([0, 7], "black"),],
            [None, None, None, None, None, None, None, None,],
            [None, None, F.King([2, 2], "black"), None, None, None, None, None,],
            [None, None, None, None, None, None, None, None,],
            [None, None, None, F.King([4, 3], "white"), None, None, None, None,],
            [None, None, None, F.King([5, 3], "black"), F.King([5, 4], "black"), F.King([5, 5], "white"), None, None,],
            [None, None, None, F.King([6, 3], "black"), None, None, None, None,],
            [F.Tower([7, 0], "black"), None, None, None, F.King([7, 4], "black"), None, None, F.Tower([7, 7], "black"),],
        ]
        # open field
        self.assertEqual(8, len(board[2][2].possible_positions(board)))

        # corner
        self.assertEqual(3, len(board[0][0].possible_positions(board)))

        # hit enemy
        self.assertTrue([5, 5] in board[5][4].possible_positions(board)) # horizontal/vertical
        self.assertTrue([4, 3] in board[5][4].possible_positions(board)) # diagonal

        # don´t hit ally
        self.assertFalse([5, 3] in board[5][4].possible_positions(board)) # horizontal/vertical
        self.assertFalse([6, 3] in board[5][4].possible_positions(board)) # diagonal

        # Rochade 
        self.assertTrue([7, 2] in board[7][4].possible_positions(board)) # left
        self.assertTrue([7, 6] in board[7][4].possible_positions(board)) # right
        self.assertFalse([0, 2] in board[0][4].possible_positions(board)) # not possible if not tower
        self.assertFalse([0, 6] in board[0][4].possible_positions(board)) # not possible with figures in between
        board[7][0].has_moved = True
        self.assertFalse([7, 2] in board[7][4].possible_positions(board)) # not possible if tower has moved
        board[7][4].has_moved = True
        self.assertFalse([7, 6] in board[7][4].possible_positions(board))# not possible if king has moved
        board = [
            [None, None, None, None, F.Tower([0, 4], "white"), None, None, None,],
            [None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None,],
            [F.Tower([7, 0], "black"), None, None, None, F.King([7, 4], "black"), None, None, None,],
        ]
        board[7][4].has_moved = False
        self.assertFalse([7, 2] in board[7][4].possible_positions(board))# not possible if checked

    #def test_check(self):

if __name__ == '__main__':
    unittest.main()