class Student:
    def __init__(self, name, marks):
        self.name = name      # 'self' is used to assign the value to the instance variable
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Example usage:
student1 = Student("Alice", 92)
student1.display()
