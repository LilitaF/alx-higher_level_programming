#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    #first two elements from each tuple
    a = tuple_a[0] if len(tuple_a) > 0 else 0
    b = tuple_a[1] if len(tuple_a) > 1 else 0
    c = tuple_b[0] if len(tuple_b) > 0 else 0
    d = tuple_b[1] if len(tuple_b) > 1 else 0
    
    #adding for new elements
    e = a + c
    f = b + d

    #create new tuple
    tuple_c = (e, f)

    return (tuple_c)
