class Student:
    def __init__(self, name: str, age: int, grade: float, subjects: list):
        """
        Object initiator for student class of objects
        :param name: str - name of the student
        :param age: int - age of the student
        :param grade: float - grade of the student
        :param subjects: list - of subjects attending
        """
        self.name: str = name
        self.age: int = age
        self.grade: float = grade
        self.subjects: list = subjects

    @property
    def name(self):
        """
        getter func for name
        :return: str - name
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        setter func for name, checks for no name
        :param name: str name
        """
        if not name:
            raise ValueError('Name cannot be empty string')
        self._name = name

    @property
    def age(self):
        """
        getter func for age
        :return: int - age
        """
        return self._age

    @age.setter
    def age(self, age):
        """
        setter func for age, checks if value is a number
        :param age: int - age
        """
        if not int:
            raise ValueError('Age can only be a digit')
        self._age = age

    @property
    def grade(self):
        """
        getter func for grade
        :return: float - grade
        """
        return self._grade

    @grade.setter
    def grade(self, grade):
        """
        setter func for grade, checks if value is an valid grade
        :param grade: float - grade
        """
        if not 2.00 <= grade <= 6:
            raise ValueError('Invalid grade')
        self._grade = grade

    @property
    def subjects(self):
        """
        getter func for subjects
        :return: list of subjects
        """
        return self._subjects

    @subjects.setter
    def subjects(self, subject):
        """
        setter func for subject, checks if subjects are validated
        :param subject: list of subjects
        """
        subjects: list = ['Bulgarian and literature', 'English', 'Math', 'Biology', 'Chemistry',
                          'Arts', 'Information technology', 'Physics', 'Psychology']
        validated: list = []
        for item in subject:
            if item in subjects:
                validated.append(item)
            else:
                print(item + ' is not valid subject')
        self._subjects = validated

    def __str__(self) -> str:
        """
        defines the format for printing
        :return: formated string of the instance of the class
        """
        return (f'name: {self.name}, age: {self.age}, score: {self.grade:.2f},'
                f'attending subjects: {self.subjects}')

    def __del__(self) -> None:
        """
        Deletes an instance of class Student
        :return: None
        """
        print('Student deleted')

    def update(self, age, grade, subjects) -> None:
        """
        Change the values for an instance of the student class object
        :param age: int age of the student
        :param grade: float the score for the student
        :param subjects: list validated list of subjects
        :return: None
        """
        self.age = age
        self.grade = grade
        self.subjects = subjects


students_list = []


def main():
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        choice = input('Enter the number of the action you want to take and press Enter')

        match choice:
            case '1':
                # collect and parse data for creation of instance of object class including exception handling
                student_name = input('Student name: ')
                try:
                    student_age = int(input('Student age: '))

                except ValueError:
                    print('Age must be a number')
                    continue
                try:
                    student_grade = float(input('Student score: '))
                except ValueError:
                    print("Score must be real number between 2 and 6")
                    continue

                student_subject = input('Attending subjects: ').title().strip().split(', ')

                try:
                    students_list.append(Student(student_name, student_age, student_grade, student_subject))
                except ValueError as error:
                    print(f'Registry import failed - {error}')

            case '2':
                # Collect data to update the values of instance of Student
                stud_id: str = input('Student name to update: ')

                try:
                    student_age = int(input('Student age: '))

                except ValueError:
                    print('Age must be a number')
                    continue
                try:
                    student_grade = float(input('Student score: '))
                except ValueError:
                    print("Score must be real number between 2 and 6")
                    continue

                student_subject = input('Attending subjects: ').title().strip().split(', ')

                for i, o in enumerate(students_list):
                    if o.name == stud_id:
                        Student.update(o, student_age, student_grade, student_subject)
            case '3':
                # delete an instance object of class Student
                stud_id: str = input('Student name to delete: ')
                for i, o in enumerate(students_list):
                    if o.name == stud_id:
                        del students_list[i]
                        break
            case '4':
                # Searching func for instance -> prints the result via __str__ fun of the cls
                stud_id: str = input('Student name to search for: ')
                for i, o in enumerate(students_list):
                    if o.name == stud_id:
                        print(o)
            case '5':
                # Prints all instances of the Student class via __str__ fun of the cls
                if len(students_list) == 0:
                    print('No records of students found')
                else:
                    for student in students_list:
                        print(student)
            case '6':
                # Stops the program (sys.exit may be better)
                break


if __name__ == '__main__':
    main()
