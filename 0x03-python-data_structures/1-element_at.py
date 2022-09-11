#!/usr/bin/python3
def element_at(my_list, indx):
    if indx < 0:
        return (None)

    length = len(my_list)

    if indx > length - 1:
        return (None)

    return(my_list[indx])
