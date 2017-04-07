'''a* game'''
import drawablenode as DN


def astar(start, end, graph):
    '''astar algorithm'''
    openlist = []
    closedlist = []
    camefrom = []
    openlist.append(start)
    start.g = 0
    openlist.sort(key=lambda x: x.f)
    while len(openlist) != 0:
        current = openlist[0]
        openlist.remove(current)
        closedlist.append(current)
        if current == end:
            camefrom = retrace(start, end)
            return camefrom
        neighbors = DN.get_neighbors(current, graph)
        for node in neighbors:
            if node in closedlist or not node.walkable:
                continue
            tentative_g = current.g + set_gscore(current, node)
            if node not in openlist:
                openlist.append(node)
            elif tentative_g >= node.g:
                continue
            node.parent = current
            node.g = tentative_g
            node.h = manhattan(node, end)
            node.f = node.g + node.h
    return camefrom


def manhattan(start, end):
    '''calculate manhattan distance'''
    xtotal = abs(end.pos[0] - start.pos[0])
    ytotal = abs(end.pos[1] - start.pos[1])
    return (xtotal + ytotal) * 10


def set_gscore(current, adjacent):
    '''sets gscore for node'''
    return 10 if adjacent.pos[0] == current.pos[0] or adjacent.pos[1] == current.pos[1] else 14


def retrace(start, end):
    '''retraces the path'''
    path = []
    i = end
    while i is not start:
        path.append(i)
        i = i.parent
    path.append(i)
    return path
