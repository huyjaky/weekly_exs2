from human import Human


class Teacher(Human):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject
        pass

    def describe(self):
        return f"Teacher - Name: {self.human.name} - YoB: {self.human.yob} - Specialiast: {self.subject}"
        pass

    pass
