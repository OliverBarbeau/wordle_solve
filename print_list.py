# show that word list was imported correctly.
# print list object item by item on a new line for each item
def print_list(l, n=-1):
    i = n 
    for x in l:
        print(x)
        i -= 1
        if i == 0: break