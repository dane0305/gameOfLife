import unittest
import gameOfLife

class TestGameOfLife(unittest.TestCase):
    def test_nextGeneration(self):
        self.assertEqual(gameOfLife.nextGeneration([["."]*7]*7), ([["."]*7]*7, False))
        self.assertEqual(gameOfLife.nextGeneration([["#"]*4]*4), ([["#",".",".","#"],
                                                                   [".",".",".","."],
                                                                   [".",".",".","."],
                                                                   ["#",".",".","#"]], True))
        self.assertEqual(gameOfLife.nextGeneration([["#","#",".","#"],
                                                    [".","#",".","#"],
                                                    [".",".","#","."],
                                                    ["#","#","#","#"]]),([["#","#",".","."],
                                                                          ["#","#",".","#"],
                                                                          ["#",".",".","."],
                                                                          [".","#","#","#"]], True))
    def test_initializeGrid(self):
        self.assertEqual(gameOfLife.initializeGrid("glider", {"patterns": {"glider": [["#", ".", ".", "."],
                                                                                      [".", "#", "#", "."],
                                                                                      ["#", "#", ".", "."],
                                                                                      [".", ".", ".", "."]]}}, 5, 5), [["#", ".", ".", ".", "."],
                                                                                                                       [".", "#", "#", ".", "."],
                                                                                                                       ["#", "#", ".", ".", "."],
                                                                                                                       [".", ".", ".", ".", "."],
                                                                                                                       ["."]*5])
        self.assertRaises(ValueError, gameOfLife.initializeGrid, "notStablishedPattern", {"patterns": {"notThatPattern": "nope"}}, 5, 5)
    def test_continueGame(self):
        self.assertEqual((gameOfLife.continueGame([["."]*4,
                                                  [".", "#", "#", "."],
                                                  [".", "#", ".", "."],
                                                  ["."]*4], 1, 2)), 2)
        self.assertEqual((gameOfLife.continueGame([["."]*4,
                                                  [".", "#", "#", "."],
                                                  [".", "#", ".", "."],
                                                  ["."]*4], 1, 3)), 2)
                        
if __name__ == '__main__':
    unittest.main()