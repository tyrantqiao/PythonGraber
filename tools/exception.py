class TextCannotWrite(Exception):
    def __str__(self):return "cannot write text"

class TextCannotRead(Exception):
    def __str__(self):return "cannot read text"

class NotAccurateUrl(Exception):
    def __str__(self):return "driver doesn't get the accurate url"

class ElementNotFound(Exception):
    def __str__(self):return "element not found"