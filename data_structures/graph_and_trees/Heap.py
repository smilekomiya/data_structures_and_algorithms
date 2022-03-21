class Heap:
    tree_list = []
    def getMax(self) -> Optional[int]:
        if len(self.tree_list) > 0:
            return self.tree_list[0]
        return None
        
    def deleteMax(self) -> bool:
        if len(self.tree_list) == 0:
            return False
        
        self.tree_list[0], self.tree_list[len(self.tree_list) - 1] = self.tree_list[len(self.tree_list) - 1], self.tree_list[0]
        self.tree_list.pop()
        
        i = 0
        while len(self.tree_list) > (2 * i + 1):
            index_of_max_value = 2 * i + 2 if len(self.tree_list) > (2 * i + 2) and self.tree_list[2 * i + 2] >= self.tree_list[2 * i + 1] else 2 * i + 1
            if self.tree_list[i] >= self.tree_list[index_of_max_value]:
                break
                
            self.tree_list[i], self.tree_list[index_of_max_value] = self.tree_list[index_of_max_value], self.tree_list[i]
            i, index_of_max_value = index_of_max_value, i
        
        return True
            
    def insert(self, value: int) -> bool:
        self.tree_list.append(value)
        index_of_parent, _ = divmod(len(self.tree_list) - 1 - 1, 2)
        index_of_inserted_value = len(self.tree_list) - 1
        
        while self.tree_list[index_of_parent] < self.tree_list[index_of_inserted_value]:
            self.tree_list[index_of_parent], self.tree_list[index_of_inserted_value] = self.tree_list[index_of_inserted_value], self.tree_list[index_of_parent]
            index_of_inserted_value = index_of_parent
            
            if index_of_inserted_value == 0:
                break
                
            index_of_parent, _ = divmod(index_of_inserted_value - 1, 2)
            
        return True
