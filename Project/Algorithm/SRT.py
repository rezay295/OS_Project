def pre_emptive():
    return False

def sort(array):
    for i in array:
        i.remaining=(i.time - i.pass_time)

    array = sorted(array, key=lambda  k:k.remaining)

    return array