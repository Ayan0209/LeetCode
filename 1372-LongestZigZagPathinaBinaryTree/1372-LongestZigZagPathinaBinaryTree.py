                dfs(node.right, "left", 1)
            else:
                dfs(node.right, "left", length + 1)
                dfs(node.left, "right", 1)

        max_length = 0
        dfs(root, "left", 0)
        dfs(root, "right", 0)

        return max_length

        
[
