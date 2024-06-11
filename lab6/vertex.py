class Vertex:
    def __init__(self, pos_x, pos_y, num):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.num = num

class Edge:
    def __init__(self, weight, start_vertex, end_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.next = None