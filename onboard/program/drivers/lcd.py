import ssd1306
import time

X_MAX = 128
Y_MAX = 64
CHAR_HEIGHT = 10
CHAR_WIDTH = 8
COLUMNS = X_MAX // CHAR_WIDTH
ROWS = Y_MAX // CHAR_HEIGHT
X_OFFSET = (X_MAX - COLUMNS * CHAR_WIDTH) // 2
Y_OFFSET = (Y_MAX - ROWS * CHAR_HEIGHT) // 2
BLACK = 0


class LCD():
    def __init__(self, i2c):
        self.__i2c = i2c
        self.__display = ssd1306.SSD1306_I2C(X_MAX, Y_MAX, i2c)
        self.__X = 0
        self.__Y = 0

    def flush(self):
        while True:
            try:
                self.__display.show()
            except Exception as error:
                continue
            else:
                break

    def __convert(self, X, Y, length):
        x = X_OFFSET + X * CHAR_WIDTH
        y = Y_OFFSET + Y * CHAR_HEIGHT
        width = length * CHAR_WIDTH
        height = CHAR_HEIGHT
        return (x, y, width, height)

    def __clear_bg(self, X, Y, characters):
        (x, y, width, height) = self.__convert(X, Y, characters)
        self.__display.fill_rect(x, y, width, height, BLACK)

    def __scroll(self, rows=1):
        self.__display.scroll(0, - rows * CHAR_HEIGHT)
        self.__clear_bg(0, ROWS - 1, COLUMNS)

    def __raw_print(self, string, X, Y, clear_bg=True):
        (x, y, width, height) = self.__convert(X, Y, len(string))
        if clear_bg:
            self.__display.fill_rect(x, y, width, height, BLACK)
        self.__display.text(string, x, y)

    def gotoXY(self, X=None, Y=None):
        if X is not None:
            self.__X = X
        if Y is not None:
            self.__Y = Y

    def getXY(self):
        return (self.__X, self.__Y)

    def new_line(self):
        self.__X = 0
        self.__Y += 1
        if self.__Y == ROWS:
            self.__scroll()
            self.__Y -= 1

    def printXY(self, string, X=None, Y=None, scroll=True):
        self.gotoXY(X=X, Y=Y)
        remaining = len(string)
        count = 0
        while remaining:
            size = min(remaining, COLUMNS - self.__X)
            self.__raw_print(string[count:count + size], self.__X, self.__Y)
            count += size
            remaining -= size
            self.__X += size
            if (self.__X) == COLUMNS:
                self.__X = 0
                self.__Y += 1
                if self.__Y == ROWS:
                    if scroll:
                        self.__scroll()
                        self.__Y -= 1
                    else:
                        break

    def clear(self):
        self.__display.fill(0)
        self.flush()
        self.gotoXY(X=0, Y=0)
