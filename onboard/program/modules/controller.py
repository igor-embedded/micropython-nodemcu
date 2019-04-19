from program.modules.displaycontroller import DisplayController
from program.modules.motioncontroller import MotionController


class Controller():
    def __init__(self, board):
        self.board = board
        self.__motioncontroller = MotionController(self)
        self.__displaycontroller = DisplayController(self)

    def test(self):
#        self.__board.lcd.test()
#        self.__displaycontroller.test()
#        pass
#        self.__motioncontroller.test()
        form1 = self.__displaycontroller.add_form(active=True, X=2, Y=2, width=5, height=3)
        form1.add_entry(label="X", value="0")
        form1.add_entry(label="YY", value="1234567")
        form1.add_entry(label="Z", value="2")
        form1.add_entry(label="W", value="3")
        form1.show()
        form1.__lcd.flush()
