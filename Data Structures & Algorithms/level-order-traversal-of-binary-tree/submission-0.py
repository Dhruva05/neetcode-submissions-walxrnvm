# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        final_list = []
        q.append(root)

        while q:
            sublist = []
            lenq = len(q)
            for i in range(lenq):
                node = q.popleft()
                if node:
                    sublist.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if sublist:
                final_list.append(sublist)
        return final_list