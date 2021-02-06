class Animal():
    def __init__(self,genus,name,age,weight,voice):
        self.genus=genus
        self.name=name
        self.age=age
        self.weight=weight
        self.voice=voice
        
    def printVoice(self):
        print(self.voice)
    
    
class Dog(Animal):
    def __init__(self,color):
        self.color=color
        
    def swim(self):
        print(self.name +" is swimming")
    
class Cat(Animal):
    def __init__(self,toy):
        self.toy=toy
    def sleep(self):
        print("cat is sleeping")
    def play(self):
        print(self.name+" is playing with his "+self.toy)
        
#-----------------     -------------------          ------------------  

dog1=Dog("black")

dog1.voice="hav hav"
dog1.genus="dog"
dog1.name="bobo"

print("its name is "+ dog1.name)
dog1.swim()
dog1.printVoice()

cat1=Cat("ball")
cat1.name="misha"
cat1.voice="miyaav"

print("its name is "+cat1.name)
cat1.play()
cat1.printVoice()
        
    
    
    
    
    