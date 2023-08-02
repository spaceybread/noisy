import random

def noise(amp, step, count, x_init, y_init):
    i = 0

    x_val = [0]
    y_val = [0]

    x = x_init
    y = y_init

    while i < count:
        x = x + step
        y = y + random.randint(-amp, amp)
        x_val.append(x)
        y_val.append(y)
        i = i + 1

    out = [x_val, y_val]

    return out
