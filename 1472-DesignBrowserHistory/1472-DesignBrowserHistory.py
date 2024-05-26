
    def back(self, steps: int) -> str:
        self.history.append(url)
        

        self.current_index = max(0, self.current_index-steps)
    def forward(self, steps: int) -> str:
        
        self.current_index = min(len(self.history)-1, self.current_index+steps)
        return self.history[self.current_index]
        return self.history[self.current_index]

[
