import collections

'''
Given a non-directional cyclic graph, return a two dimensional array of the graph.
For simplicity sake, each node's value is the same as the node's index (1-indexed). For example,
the first node with val = 1, the second node with val = 2, and so on. The graph is represented in
the test case using an adjacency list.

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: Output: [[2,4],[1,3],[2,4],[1,3]]

1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
'''

class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node.neighbors == None:
            return [[]]
        
        ret = []
        ourMap = collections.defaultdict(list)
        visited = set()
        
        def traverse(node):
            if node == None:
                return
            visited.add(id(node))
            for neighbor in node.neighbors:
                ourMap[node.val-1].append(neighbor.val)
                if id(neighbor) not in visited:
                    traverse(neighbor)
         
        traverse(node)
        
        highest = max(ourMap.keys())+1
        for i in range(highest):
            ret.append(ourMap[i])
        return ret
    
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1 = Node(1)
node2 = Node(2,[node1,node3,node4])
node2.neighbors[0].val = 1
node2.neighbors[1].val = 3
node2.neighbors[2].val = 4
node2.neighbors[0].neighbors = [node2]
node2.neighbors[1].neighbors = [node2,node2.neighbors[2]]
node2.neighbors[2].neighbors = [node2, node2.neighbors[1]]


S = Solution()
new = S.cloneGraph(node1)
print(new)
