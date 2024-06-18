from human import Human


class Student(Human):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade
        pass

    def describe(self):
        return f"Student - Name: {self.human.name} - YoB: {self.human.yob} - Specialiast: {self.grade}"
        pass

    pass
