#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    else:
        a1, a2, b1, b2 = 0, 0, 0, 0
        if len(tuple_a) == 0:
            a1, a2 = 0, 0
        elif len(tuple_a) == 1:
            a2 = 0
            a1 = tuple_a[0]
        else:
            a1 = tuple_a[0]
            a2 = tuple_a[1]

        if len(tuple_b) ==0:
            b1, b2 = 0, 0
        elif len(tuple_b) == 1:
            b2 = 0
            b1 = tuple_b[0]
        else:
            b1 = tuple_b[0]
            b2 = tuple_b[1]

        return (a1 + b1, a2 + b2)
