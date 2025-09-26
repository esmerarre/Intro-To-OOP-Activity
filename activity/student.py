class Student:
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, new_class):
        self.classes.append(new_class)
        return self.classes
    
    def get_num_classes(self):
        return len(self.classes)
    
    def summary(self):
        num_classes = self.get_num_classes()
        print(f"{self.name} is a {self.grade} enrolled in {num_classes} classes")