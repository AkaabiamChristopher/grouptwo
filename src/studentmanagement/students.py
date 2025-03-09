from src.studentmanagement.user import User
from src.studentmanagement.admin import CourseAdmin


class StudentManagement(User):
    def __init__(self, firstname, lastname, email, password):
        super().__init__(firstname, lastname, email, password)
        self.__course_list = []

    @property
    def course_list(self):
        return self.__course_list

    def add_course(self, course_id):
        self.__course_list.append(course_id)

    def get_course_list_size(self):
        return len(self.__course_list)

    def view_offered_course(self):
        for course in self.__course_list:
            print(f"{course}")




