import re


# https://www.tutorialspoint.com/python3/python_reg_expressions.htm
# example: return re.match(r'my-expression', s)
class Hieroglyph(object):
    def __init__(self):
        return

    @staticmethod
    def worship_sacred_cats(s):
        return re.match(r'.*cat.*', s)

    @staticmethod
    def alphanumeric_glyph(s):
        return re.match(r'[a-z]{3}d\d+', s)

    @staticmethod
    def steal_crystal_skull(s):
        return s.replace('skull', 'idol')

    @staticmethod
    def symbolic_glyph(s):
        # FIXME!
        return True

    @staticmethod
    def nile_crocodile(s):
        # FIXME!
        return True
