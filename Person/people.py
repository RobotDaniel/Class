class People():
    def __init__(self,name,age,gender,conutry):
        self.name=name
        self.age=age
        self.gender=gender
        self.country=conutry
        
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGender(self):
        return self.gender
    def getCountry(self):
        return self.country
    
    def drinkCheck(self):
        DrinkingCounries=[["USA",21],["UK",18]]
        for i in DrinkingCounries:
            if self.getCountry() == i[0]:
                if self.getAge() >= i[1]:
                    print("you can drink")
                else:
                    print("you can't drink")
            
        
mike = People("Michael",34,"Male","USA")
mike.drinkCheck() 