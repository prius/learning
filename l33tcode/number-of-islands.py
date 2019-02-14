import unittest
from collections import deque

class Solution:
    def numIslands(self, grid):
        queue = deque()
        visited = {}
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and int(grid[i][j]) == 1:
                    islands += 1
                    queue.append((i, j))

                    while len(queue):
                        m, n = queue.popleft()

                        if m < 0 or m >= len(grid) or \
                          n < 0 or n >= len(grid[0]):
                            continue

                        if (m, n) in visited:
                            continue

                        visited[(m, n)] = True

                        if int(grid[m][n]) == 0:
                            continue

                        neighbours = [
                            (m - 1, n),
                            (m + 1, n),
                            (m, n - 1),
                            (m, n + 1),
                        ]

                        for neighbour in neighbours:
                            queue.append(neighbour)

        return islands


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.numIslands([]), 0)

    def test_just_zero(self):
        self.assertEqual(self.sol.numIslands([[0]]), 0)

    def test_just_one(self):
        self.assertEqual(self.sol.numIslands([[1]]), 1)

    def test_1(self):
        grid = [
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(self.sol.numIslands(grid), 1)

    def test_2(self):
        grid = [
            [1, 1, 0, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(self.sol.numIslands(grid), 2)

    def test_3(self):
        grid = [
            [0, 1, 0, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 1],
        ]
        self.assertEqual(self.sol.numIslands(grid), 4)


unittest.main()