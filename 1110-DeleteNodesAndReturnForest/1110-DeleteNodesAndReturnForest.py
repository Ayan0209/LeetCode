
                    queue.append(node.left)
                    if node.left.val in to_delete:
                        node.left = None
                    self.delNodes(node.right, to_delete)
            else: 
                if node.left:
                if node.left:
                    self.delNodes(node.left, to_delete)
                if node.right:

            if node.val in to_delete:
[
