def pre_emptive():
    return True

def sort(array):
    array = sorted(array, key=lambda k: k.time)
    return array