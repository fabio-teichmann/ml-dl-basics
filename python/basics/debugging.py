# Tips for debugging:
#
# 1) linting: in-built functionality of identifying errors (by IDE)
#
# 2) use IDE / editor
#
# 3) read errors and understand their meaning
#
# 4) pdb module (Python Debugging): can step through code
import pdb


def add(num1, num2):
    pdb.set_trace()
    return num1 + num2


add(1, 'asd')
