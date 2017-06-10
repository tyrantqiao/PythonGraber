class TextCannotWrite(Exception):
    def __str__(self):return "cannot write text"

class TextCannotRead(Exception):
    def __str__(self):return "cannot read text"