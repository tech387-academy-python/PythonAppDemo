import re

class Validators:
    
    @staticmethod
    def validateEmail(email):
        
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        
        isValid = re.search(regex, email)
        
        print(isValid)
        
        if isValid is None:
            return False
        return True