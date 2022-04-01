class Student():
    university = "UAM"
    def __init__(self, firstname, lastname, subject):
        self.firstname = firstname
        self.lastname = lastname
        self.subject = subject

    def email(self):
        return f'{self.lastname}.{self.firstname}@{self.university}.pl'.lower()

# stwórz obiekt instancję klasy Student
obj_anna = Student('Anna', 'Kowalska', 'Informatyka')
obj_jan = Student("Jan", "Nowak", "Biologia")

print(obj_anna.firstname, obj_anna.lastname, obj_anna.subject, obj_anna.university, obj_anna.email)
print(obj_jan.firstname, obj_jan.lastname, obj_jan.subject, obj_jan.university, obj_jan.email())

print(obj_jan.university)

print(obj_jan.__dict__)
print(Student.__dict__)
