class Form():
    def __init__(self, lcd, active=False, X=0, Y=0, width=None, height=None):
        self.__lcd = lcd
        self.__entries = []
        self.__label_len = 0
        self.__X = X
        self.__Y = Y
        self.__width = width
        self.__height = height
        self.__active = active

    def add_entry(self, label, value=""):
        self.__entries.append([label, value])
        self.__label_len = max(self.__label_len, len(label))

    def set_entry(self, label, value):
        for entry in self.__entries:
            if entry[0] == label:
                entry[1] = value
                break

    def show(self):
        if not self.__active:
            pass
        x = self.__X
        y = self.__Y
        self.__lcd.gotoXY(x, y)
        for entry in self.__entries:
            x = self.__X
            self.__lcd.printXY(entry[0], X=x, Y=y, scroll=False)
            x += self.__label_len + 1
            ln = self.__width - (self.__label_len + 1)
            self.__lcd.printXY(entry[1][:ln], X=x, Y=y,
                               scroll=False)
            y += 1
            if y == self.__Y + self.__height:
                break


class DisplayController():
    def __init__(self, controller):
        self.controller = controller
        self.__forms = []

    def add_form(self, active, X, Y, width, height):
        form = Form(self.controller.board.lcd, active=active, X=X, Y=Y,
                    width=width, height=height)
        self.__forms.append(form)
        return form
    
    def show(self):
        for form in self.__forms:
            form.show()
