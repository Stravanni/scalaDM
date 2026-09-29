"""
Simple implementation of skip-lists in python, one of the two important algorithms to
understand to implement/understand HNSW.
"""

from __future__ import annotations

import random

random.seed(42)


class Node:
    def __init__(self, *args) -> None:
        # what does a node store inside?
        # consider that we will work only on simple integer values
        ...

    def __repr__(self) -> str:
        # a simple representation of the node?
        ...


class SkipList:
    """
    Our skip-list implementation. Note that it doesn't support duplicates (!!!), so it's more
    of a skip-set.
    """

    def __init__(self, max_level: int = 2, p: float = 0.5) -> None:
        assert max_level >= 0

        self.max_level = max_level  # note: max_level is 0-indexed (0 means 1 level, 1 means 2 levls, etc.)
        self.level = 0
        self.p = p
        self.header = ...  # what is the header?

    def _random_level(self) -> int:
        """
        Coin-flipping implementation for sampling
        """
        ... # in a Skip List, how is defined the node level? 
        
    def search(self, value: int) -> Node | None:
        current = ... # at the beginning, what is the current node?
        level = ... # and on which level are we placed?

        while ...: # when do we stop the search?
            next = # which node is the next node?

            # we now have three possibilities:
            # 1. we can't move to the next node --> move down a level 
            if False:
                level -= 1
                continue

            # 2. we are on the right node! --> return it
            if False:
                return next
            
            # 3. we have to move to the next node --> move over one pointer
            if False:
                current = current.pointers[level]

        return None


    def insert(self, value: int) -> None:
        # step 1 is to traverse the skip-list and make a list of all the
        # nodes that need to be updated
        current = ... # self.header

        # list of all nodes that might need to update their forward pointer
        update = ... # [self.header for _ in range(self.max_level + 1)]
        
        # how to we update the "update" nodes list?
        
        # once the update list is filled, what is the current node?
        current = ...

        if current is None or current.value != value:
            # sample the level for the current node, and...
            level = self._random_level()
            # ...update the current level if necessary
            self.level = ...

            new_node = Node(value, level)

            # and now actually update the nodes previously identified
            ...
                