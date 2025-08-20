def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist


def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos :
        node = node["next"]
        searchpos += 1
    return node["info"] 

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp