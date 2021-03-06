# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        stack = [(root, root.val, root.val)]
        last_removed = None
        result = 0

        while stack:
            node, min_val, max_val = stack[-1]
            new_min_val = min(node.val, min_val)
            new_max_val = max(node.val, max_val)
            result = max(result, new_max_val - new_min_val)

            # DFS iterative example

            if node.right:
                if node.right == last_removed:
                    # Just traversed right subtree, going up
                    last_removed = node
                    stack.pop()
                    continue
                if not node.left or node.left == last_removed:
                    # Traversed entire left subtree, going right
                    stack.append((node.right, new_min_val, new_max_val))
                    continue

            if node.left:
                if node.left != last_removed:
                    # Haven't been to the left, going down to the left
                    stack.append((node.left, new_min_val, new_max_val))
                    continue

            # Nowhere to go down, going up
            last_removed = node
            stack.pop()

        return result

    def maxAncestorDiffRecursive(self, root: TreeNode) -> int:
        def dfs(node, min_val, max_val):
            new_min_val = min(node.val, min_val)
            new_max_val = max(node.val, max_val)

            max_diff = new_max_val - new_min_val

            if node.left:
                max_diff = max(max_diff, dfs(node.left, new_min_val, new_max_val))
            if node.right:
                max_diff = max(max_diff, dfs(node.right, new_min_val, new_max_val))

            return max_diff

        return dfs(root, root.val, root.val)

    def maxAncestorDiffRecursive2(self, root: TreeNode) -> int:
        max_diff = 0

        def dfs(node: TreeNode) -> Tuple[int, int]:
            nonlocal max_diff

            min_left, max_left = node.val, node.val
            if node.left:
                min_left, max_left = dfs(node.left)

            min_right, max_right = node.val, node.val
            if node.right:
                min_right, max_right = dfs(node.right)

            max_diff = max(
                max_diff,
                abs(node.val - min_left),
                abs(node.val - max_left),
                abs(node.val - min_right),
                abs(node.val - max_right),
            )

            return (
                min(min_left, min_right, node.val),
                max(max_left, max_right, node.val),
            )

        if not root:
            return 0

        dfs(root)

        return max_diff
