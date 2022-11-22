"""Custom Exception Classes"""


class OnlyOneValue(Exception):
    def __int__(self, message="Cannot Perform Operation On Only One Value"):
        self.message = message
        super().__init__(self.message)
