class Person ():
    def __init__(self, name, occupation, age):
        self.name = name
        self.occupation = occupation
        self.age = age

people = [Person("Dan", "Consultant", "23"), Person("NotDan", "Biologist", "18")]

for i in range(1 , len(people)+1):
    file = open("txtfiles/"+ str(i) +".txt", "w+")
    file.write(people[i-1].name + "/" + people[i-1].age + "/" + people[i-1].occupation)
    file.close

readpeople = []

for i in range(1 , len(people)+1):
    file = open("txtfiles/" + str(i) +".txt", "r")
    per = str(file.read()).split("/")
    file.close()
    readpeople.append(Person(per[0], per[1], per[2]))

