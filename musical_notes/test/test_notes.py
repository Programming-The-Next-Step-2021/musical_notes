import unittest
import unittest.mock

import tkinter


from musical_notes.notes_test import game_notes

 
class TestWidget(self):
    def test_entry_widget(self):
        widget=Widget('answer_box')
        self.assertEqual(widget.size(), (50, 50))

if __name__ == '__main__':
    unittest.main()
            

