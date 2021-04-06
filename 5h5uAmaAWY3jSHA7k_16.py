
def landscape_type(numbers):
    validator = PeekTroughValidator(numbers)
    return validator.validate()
    
class PeekTroughValidator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.max = max(numbers)
        self.min = min(numbers)
        
    def validate(self):
        
        
        try:
            self._validate_peek()
            return 'mountain'
        except ValueError:
            try:
                self._validate_trough()
                return 'valley'
            except ValueError:
                return 'neither'
        
        
​
    def _validate_peek(self):
        
        index = self.numbers.index(self.max)
        self._validate_boundaries(index)
        
        self._validate_side(self.numbers[:index], 'increase')
        self._validate_side(self.numbers[index+1:], 'decrease')
​
    def _validate_trough(self):
        
        index = self.numbers.index(self.min)
        self._validate_boundaries(index)
        
        self._validate_side(self.numbers[:index], 'decrease')
        self._validate_side(self.numbers[index+1:], 'increase')
    
    def _validate_boundaries(self, index):
        if index == 0 or index == len(self.numbers) - 1:
            raise ValueError
    
    def _validate_side(self, list_, type_):
        for index, val in enumerate(list_):
            
            if index == 0:
                pass
            
            elif type_ == 'increase' and val < last_val:
                raise ValueError
​
            elif type_ == 'decrease' and val > last_val:
                raise ValueError
                
            last_val = val

