class Validation():
    def val_integer2(self, text):
        if text == '': return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 < value < 100


    def val_age(self, text):
        if text == '': return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 < value < 120