# doctor.py
from human import Human


class Doctor(Human):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}"
