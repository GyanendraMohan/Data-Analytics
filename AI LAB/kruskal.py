class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        
    def add_edges(self, u , v, w):
        self.graph.append([u,v,w])
        
    '''graph compression'''   
    def find(self, parent , ele):
        if ele != parent[ele]:
            parent[ele] = self.find(parent, parent[ele])
        return parent[ele]
    
    def union(self, parent, rank , x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
            
    def kruskal(self):
        mst = []
        
        ''' sort all edges '''  
        self.graph = sorted(self.graph , key = lambda item:item[2])
        
        parent = []
        rank = []
        
        '''create subsets'''
        for v in range(self.V):
            parent.append(v)
            rank.append(0)
            
        e = 0
        i = 0
        while e < self.V-1:
            '''select the smallest edge'''
            u,v,w = self.graph[i]
            i = i+1
            
            x = self.find(parent, u)
            y = self.find(parent , v)
            
            #including edge if its not making cycle
            if x!= y:
                mst.append([u,v,w])
                e = e+1
                self.union(parent , rank , x, y)

        min_cost = 0
        for u, v, w in mst:
            min_cost += w
            print("%d -- %d : %d" % (u,v,w))
        print("Minimum Spanning Tree cost:", min_cost)
        print("Edges in MST:", mst)
        
graph = Graph(8)
graph.add_edges(0, 1, 3)
graph.add_edges(0, 2, 2)
graph.add_edges(1, 2, 1)
graph.add_edges(1, 3, 4)
graph.add_edges(2, 3, 5)
graph.add_edges(2, 4, 6)
graph.add_edges(3, 4, 7)
graph.add_edges(3, 5, 8)
graph.add_edges(4, 5, 9)
graph.add_edges(4, 6, 10)
graph.add_edges(5, 6, 11)
graph.add_edges(5, 7, 12)
graph.add_edges(6, 7, 13)
graph.kruskal()