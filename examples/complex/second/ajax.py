import json
from dajaxice.core import dajaxice_functions


def complex_example1(request):
    return json.dumps({'message': 'hello world'})

dajaxice_functions.register(complex_example1)


def complex_example2(request):
    return json.dumps({'numbers': [1, 2, 3]})

dajaxice_functions.register(complex_example2)
