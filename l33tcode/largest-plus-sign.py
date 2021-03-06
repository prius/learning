from collections import defaultdict

class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        def update_cell(dp, row, col, empty, mines_s):
            if (row, col) in mines_s:
                empty = 0
            else:
                empty += 1

            dp[row][col] = min(empty, dp[row][col])

            return empty

        dp = [[float("+inf")] * N for _ in range(N)]

        mines_s = set((m[0], m[1]) for m in mines)

        for row in range(N):
            empty = 0
            # left right
            for col in range(N):
                empty = update_cell(dp, row, col, empty, mines_s)

            empty = 0
            # right left
            for col in reversed(range(N)):
                empty = update_cell(dp, row, col, empty, mines_s)

        for col in range(N):
            empty = 0
            # left right
            for row in range(N):
                empty = update_cell(dp, row, col, empty, mines_s)

            empty = 0
            # right left
            for row in reversed(range(N)):
                empty = update_cell(dp, row, col, empty, mines_s)

        return max(max(r) for r in dp)

    def orderOfLargestPlusSignNonDP(self, N, mines):
        rows, cols = defaultdict(lambda: list([-1])), defaultdict(lambda: list([-1]))

        for mine in mines:
            rows[mine[0]].append(mine[1])
            cols[mine[1]].append(mine[0])

        cols_pos = [0] * N

        plus_max = 0

        for row in range(N):
            row_pos = 0

            if rows[row][-1] != N:
                rows[row] = sorted(rows[row])
                rows[row].append(N)

            for col in range(N):
                if cols[col][-1] != N:
                    cols[col] = sorted(cols[col])
                    cols[col].append(N)

                row_pos = row_pos + 1 if rows[row][row_pos] < col else row_pos
                col_pos = cols_pos[col] = cols_pos[col] + 1 if cols[col][cols_pos[col]] < row else cols_pos[col]

                row_left = rows[row][row_pos - 1]
                row_right = rows[row][row_pos]
                col_upper = cols[col][col_pos - 1]
                col_lower = cols[col][col_pos]

                plus_max = max(
                    plus_max,
                    min(
                        col - row_left,
                        row_right - col,
                        row - col_upper,
                        col_lower - row,
                    ),
                )

        return plus_max


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.orderOfLargestPlusSign(
            3,
            [[1, 1]],
        ) == 1

    def test_case2(self):
        assert self.sol.orderOfLargestPlusSign(
            5,
            [[4, 2]]
        ) == 2

    def test_case3(self):
        assert self.sol.orderOfLargestPlusSign(
            2,
            []
        ) == 1

    def test_case4(self):
        assert self.sol.orderOfLargestPlusSign(
            1,
            [[0,0]]
        ) == 0

    def test_case5(self):
        assert self.sol.orderOfLargestPlusSign(
            5,
            [[3,0], [3,3]]
        ) == 3
