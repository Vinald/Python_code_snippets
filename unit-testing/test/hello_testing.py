from hello import hello


def hello_default():
    assert hello() == 'hello samuel'


def hello_argument():
    assert hello('vinald') == 'hello vinald'
