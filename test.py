import unittest
from board import *

#Test for border class
class TestBorder(unittest.TestCase):
    def test_rightcolumn(self):
        Board1 = Board(10, 12)
        Board2 = Board(10, 13 )
        self.assertEqual(Board1.cols, 10)
        self.assertEqual( Board2.cols, 10)

    def test_rightrow(self):
       Board3=Board(10,12)
       Board4=Board(10,13)
       self.assertEqual(Board3.rows,12)
       self.assertEqual(Board4.rows,13)

    def test_wrongrow(self):
        Board3 = Board(10, 12)
        Board4 = Board(10, 13)
        self.assertNotEqual(Board3.rows, 9)
        self.assertNotEqual(Board4.rows, 4)

    def test_wrongcols(self):
        Board3 = Board(10, 12)
        Board4 = Board(10, 13)
        self.assertNotEqual(Board3.cols, 15)
        self.assertNotEqual(Board4.cols, 16)

#All these Tests should be passed
#Test for Bishop class
class TestNewBishop(unittest.TestCase):
    def test_Bishopcolor(self):
        Bishop1=Bishop(3,4,"WHITE")
        Bishop2=Bishop(6,7,"Black")
        self.assertEqual(Bishop1.color,"WHITE")
        self.assertEqual(Bishop2.color,"Black")
    def test_Bishoprow(self):
        Bishop1=Bishop(3,4,"WHITE")
        Bishop2=Bishop(6,7,"Black")
        self.assertEqual(Bishop1.row,4)
        self.assertEqual(Bishop2.col,6)
#Test for Knight class
class TestNewKnight(unittest.TestCase):
    def test_Knight(self):
        Knight1=Knight(3,4,"White")
        self.assertEqual(Knight1.col,3)

 #Test for king class
class TestNewKing(unittest.TestCase):
    def test_King(self):
        King1=King(10,11,"black")
        self.assertEqual(King1.col,10)




if __name__ == '__main__':
    unittest.main()
