class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        return self._search_by_id(self.root, id)

    def _search_by_id(self, node, id):
        if node is None:
            return None
        
        if node.get('id') == id:
            return node
        
        for child in node.get('children', []):
            result = self._search_by_id(child, id)
            if result is not None:
                return result
        
        return None
