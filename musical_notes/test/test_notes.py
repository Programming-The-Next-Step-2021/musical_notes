import unittest
import unittest.mock

import tkinter


from musical_notes.notes_test import game_notes, imagegen

 

class TestRandomNote(unittest.TestCase):
    def test_notepick(self):
        self.note1 = imagegen(6, ['C_test', 'C1_test', 'D_test', 'D1_test', 'E_test', 'E1_test', 'F_test', 'F1_test', 'G_test', 'G1_test', 'A_test', 'A1_test', 'B_test', 'B1_test'])
        self.note2 = imagegen(10, ['C_test', 'C1_test', 'D_test', 'D1_test', 'E_test', 'E1_test', 'F_test', 'F1_test', 'G_test', 'G1_test', 'A_test', 'A1_test', 'B_test', 'B1_test'])
        self.note3 = imagegen(2, ['C_test', 'C1_test', 'D_test', 'D1_test', 'E_test', 'E1_test', 'F_test', 'F1_test', 'G_test', 'G1_test', 'A_test', 'A1_test', 'B_test', 'B1_test'])

        self.assertEqual(self.note1, "musical_notes/musicalnotes/F_test.png")
        self.assertEqual(self.note2, "musical_notes/musicalnotes/A_test.png")
        self.assertEqual(self.note3, "musical_notes/musicalnotes/D_test.png")

if __name__ == '__main__':
    unittest.main()
            

