def pre_emptive():
    return True

def sort(array):
    array = sorted(array, key=lambda k: k.time)
    array.reverse()
    return array