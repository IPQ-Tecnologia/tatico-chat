import sys
import inspect

class PORT:
    ISO_639_1 = 'pt'
    ISO_639 = 'por'
    ENGLISH_NAME = 'Portuguese'

def get_language_classes():
    return inspect.getmembers(sys.modules[__name__], inspect.isclass)

