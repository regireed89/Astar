'''a* game'''



def astar(start, end):
    '''astar algorithm'''
    openlist = []
    closedlist = []
    camefrom = []
    openlist.append(start)
    start.g = 0
    while len(openlist) != 0:
        openlist.sort(key=lambda x: x.f)
        current = openlist[0]
        openlist.remove(current)
        closedlist.append(current)
        if current == end:
            camefrom = retrace(start, end)
            return camefrom
        for node in current.adjacents:
            if node in closedlist:
                continue
            set_gscore(current, node)
            tentative_g = current.g + set_gscore(current, node)
            if node not in openlist:
                openlist.append(node)
            elif tentative_g >= node.g:
                continue
            node.parent = current
            node.g = tentative_g
            node.h = Manhattan(node, end)
            node.f = node.g + node.h



def Manhattan(start, end):
    '''calculate manhattan distance'''
    xtotal = abs(end.posx - start.posx)
    ytotal = abs(end.posy - start.posy)
    return (xtotal + ytotal) * 10


def set_gscore(current, adjacent):
    '''sets gscore for node'''
    return 10 if adjacent.posx == current.posx or adjacent.posy == current.posy else 14


def retrace(start, end):
    '''retraces the path'''
    path = []
    i = end
    while i is not start:
        path.append(i)
        i = i.parent
    return path
