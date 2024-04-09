class HashTable:
    
    def __init__(self):
        self.Size = 10
        self.arr = [None for i in range(self.Size)]
        
    def give_index(self, get_key: str):
        h = 0
        for character in get_key:
            h += ord(character)
        return h % (self.Size)

    def add_to_table(self, key: str, value: int):
        index = self.give_index(key)
        if not self.arr[index]:
            self.arr[index] = value
        else: 
            self.arr[index + 1] = value
            
    def get_by_key(self, key: str):
        index = self.give_index(key) 
        return self.arr[index]
    
    def delete_item(self, key: str):
        index = self.give_index(key)
        self.arr[index] = None
