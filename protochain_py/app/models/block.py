class Block():
    
    def __init__(self, index:int, hash:str) -> None:
        self.index = index
        self.hash = hash
        
    def is_valid(self) -> bool:
        return False if self.index < 0 or not self.hash else True
