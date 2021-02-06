personList=[]


class Person():
    def __init__(self,task,name,age,languages):
        self.name=name
        self.age=age
        self.languages=languages
        
class Manager(Person):
    def __init__(self):
        self.task="manager"
class Employee(Person):
    def __init__(self):
        self.task="employee"
        
manager1=Manager()
manager1.name="Mehmet"
manager1.age=38
manager1.languages=["Turkish","English","German"]

manager2=Manager()
manager2.name="John"
manager2.age=43
manager2.languages=["English","French","Italian"]

employee1=Employee()
employee1.name="Can"
employee1.age=25
employee1.languages=["Turkish","English"]

employee2=Employee()
employee2.name="Habib"
employee2.age=22
employee2.languages=["Arabic","English"]

employee3=Employee()
employee3.name="Tom"
employee3.age=29
employee3.languages=["English"]

employee4=Employee()
employee4.name="Clara"
employee4.age=24
employee4.languages=["English","French"]

personList.append(manager1)
personList.append(manager2)
personList.append(employee1)
personList.append(employee2)
personList.append(employee3)
personList.append(employee4)

for i in range(0,len(personList)):
    print("\n"+personList[i].name +" can speak:")
    for j in range(0,len(personList[i].languages)):
        print(personList[i].languages[j])

