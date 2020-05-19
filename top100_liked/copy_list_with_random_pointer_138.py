
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

import copy

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        a = copy.deepcopy(head)
        return a

