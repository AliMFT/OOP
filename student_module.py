
class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.marks = []
        self.average = 0
        self.total = 0

    def add_mark(self, mark):
        self.marks.append(mark)

    def get_all_marks(self):
        return self.marks

    def calc_average(self):
        if len(self.marks) == 0:
            return 0
        else:
            self.total = sum(self.marks)
            self.average = self.total / len(self.marks)
            return self.average