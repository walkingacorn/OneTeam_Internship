class Phone:
    def __init__(self,brand,_password):
        self.brand=brand
        self.password=_password #protected attribute
        
    def unlock(self,password):
        if password==self.password:
            print(f"{self.brand} Phone unlocked!")
        else:
            print("Inocrrect password!")
            
my_phone=Phone("iPhone","1234")
my_phone.unlock("1234")
my_phone.unlock("0000")