"""
Map Search
"""

import comp140_module7 as maps

class Queue:
    """
    A simple implementation of a FIFO queue.
    """
    def __init__(self):
        """
        Initialize the queue.
        """
        self._queue = []
        

    def __len__(self):
        """
        Returns: an integer representing the number of items in the queue.
        """
        length = len(self._queue)
        return length

    def __str__(self):
        """
        Returns: a string representation of the queue.
        """
        str1 = ""
 
        for element in self._queue:
            str1 += str(element)
 

        return str1

    def push(self, item):
        """
        Add item to the queue.

        input:
            - item: any data type that's valid in a list
        """
        self._queue.insert(0, item)


    def pop(self):
        """
        Remove the least recently added item.

        Assumes that there is at least one element in the queue.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the least recently added item.
        """
        popped = self._queue.pop()
        return popped

    def clear(self):
        """
        Remove all items from the queue.
        """
        while len(self._queue) != 0:
            self._queue.pop()

class Stack:
    """
    A simple implementation of a LIFO stack.
    """
    def __init__(self):
        """
        Initialize the stack.
        """
        self._stack = []
        

    def __len__(self):
        """
        Returns: an integer representing the number of items in the stack.
        """
        length = len(self._stack)
        return length

    def __str__(self):
        """
        Returns: a string representation of the stack.
        """
        str1 = ""
 
        for element in self._stack:
            str1 += str(element)
 

        return str1

    def push(self, item):
        """
        Add item to the stack.

        input:
            - item: any data type that's valid in a list
        """
        self._stack.append(item)


    def pop(self):
        """
        Remove the least recently added item.

        Assumes that there is at least one element in the stack.  It
        is an error if there is not.  You do not need to check for
        this condition.

        Returns: the least recently added item.
        """
        popped = self._stack.pop()
        return popped

    def clear(self):
        """
        Remove all items from the stack.
        """
        while len(self._stack) != 0:
            self._stack.pop()

            
def bfs_dfs(graph, rac_class, start_node, end_node):
    """
    Performs a breadth-first search or a depth-first search on graph
    starting at the start_node.  The rac_class should either be a
    Queue class or a Stack class to select BFS or DFS.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - rac_class: a restricted access container (Queue or Stack) class to
          use for the search
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end

    Returns: a dictionary associating each visited node with its parent
    node.
    """
    objects = rac_class()
    
    dist = {}
    parent = {}
    
    for node in graph.nodes():
        dist[node] = float("inf")
        parent[node] = None
        
    dist[start_node] = 0
    objects.push(start_node)
    
    while len(objects) != 0:
        node = objects.pop()
        for nbr in graph.get_neighbors(node):
            if dist[nbr] == float("inf"):
                dist[nbr] = dist[node] + 1
                parent[nbr] = node
                objects.push(nbr)
            if nbr == end_node:
                return parent
    
        
    
    return parent

def dfs(graph, start_node, end_node, parent):
    """
    Performs a recursive depth-first search on graph starting at the
    start_node.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end
        - parent: a dictionary that initially has one entry associating
                  the original start_node with None

    Modifies the input parent dictionary to associate each visited node
    with its parent node
    """
    #Base Case(s)
    if start_node in (None, end_node):
        return parent
    
    neighbors = graph.get_neighbors(start_node)
    nbr_list = []
    for nbr in neighbors:
        if (nbr in neighbors) and (nbr not in parent):
            nbr_list.append(nbr)
    #Recursive Case(s)        
    if len(nbr_list) == 0:
        return dfs(graph, parent[start_node], end_node, parent)
    
    else:
        for nbr in nbr_list:
            parent[nbr] = start_node
            return dfs(graph, nbr, end_node, parent)
    
    
            
            
            
      


def astar(graph, start_node, end_node,
          edge_distance, straight_line_distance):
    """
    Performs an A* search on graph starting at start_node.

    Completes when end_node is found or entire graph has been
    searched.

    inputs:
        - graph: a directed Graph object representing a street map
        - start_node: a node in graph representing the start
        - end_node: a node in graph representing the end
        - edge_distance: a function which takes two nodes and a graph
                         and returns the actual distance between two
                         neighboring nodes
        - straight_line_distance: a function which takes two nodes and
                         a graph and returns the straight line distance 
                         between two nodes

    Returns: a dictionary associating each visited node with its parent
    node.
    """
    open_set = set()
    closed_set = set()
    g_cost = {}
    cost = {}
    parents = {}
    
    open_set.add(start_node)
    g_cost[start_node] = 0
    parents[start_node] = None
    cost[start_node] = straight_line_distance(start_node, end_node, graph)
    current_node = start_node
    
    while open_set:
        minimum = float("inf")
        for node, f_val in cost.items():
            if minimum > f_val and node in open_set:
                minimum = f_val
                current_node = node
                
        closed_set.add(current_node)
        open_set.remove(current_node)
        
        neighbors = graph.get_neighbors(current_node)
        for nbr in neighbors:
            g_total = edge_distance(current_node, nbr, graph) + g_cost[current_node]
            h_val = straight_line_distance(current_node, nbr, graph)
            f_val = h_val + g_total
                                                                  
            if nbr in open_set:
                if g_total < g_cost[nbr]:
                    g_cost[nbr] = g_total
                    cost[nbr] = f_val
                    parents[nbr] = current_node
            
            if nbr not in open_set and nbr not in closed_set:
                open_set.add(nbr)
                g_cost[nbr] = g_total
                cost[nbr] = f_val
                parents[nbr] = current_node
    
    return parents



        
        
        
        
        
        
        
        
  


maps.start(bfs_dfs, Queue, Stack, dfs, astar)
