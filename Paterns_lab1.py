from datetime import datetime
from typing import List, Any


class CourseProgress:
    def __init__(
        self,
        received_marks: dict,
        visited_lectures: int,
        completed_assigments: dict,
    ):
        self.received_marks = received_marks
        self.visited_lectures = visited_lectures
        self.completed_assigments = completed_assigments
        self.notes = notes

    def get_progress_to_date(self, date: datetime):
        pass  # to do

    # Calculates the final mark
    def get_final_mark(self):
        """The sum of grades is divided by their number to determine the final grade"""
        final_mark = sum(self.received_marks.values()) / len(self.received_marks)
        return final_mark

    def fill_notes(self):
        """In the cycle, you need to enter the text 5 times, it adds this text to the notes"""
        i = 0
        while i <= 5:
            text = input()
            self.notes[i] = text
            i += 1

    def remove_note(self):
        """Clearing array with notes"""
        self.notes.clear()


class Course:
    def __init__(
        self,
        title: str,
        star_date: datetime,
        end_date: datetime,
        description: str,
        lectures: list[str],
        assigments: list[str],
        limit: int,
    ):
        self.title = title
        self.start_date = star_date
        self.end_date = end_date
        self.description = description
        self.lectures = lectures
        self.assigments = assigments
        self.limit = limit
        self.students = []

    # Add student name to list
    def add_student(self, student: Any):
        """Checks whether there are still places for the student

        and whether there is no student already in the course

        after checks, adds the student to the list
        """

        if self.limit > len(self.students) and student.name not in self.students:
            self.students.append(student.name)
            print(f"Student {student.name} as been added to the course {self.title}")
        else:
            print("Too many students or this student is already in the course")

    # Remove student name from list
    def remove_student(self, student: Any):
        """Removes a student from the list of students enrolled in a course"""
        self.students.remove(student.name)  # ?
        print(f"{student.name} remove from course {self.title}")

    # Returns a list of students from the course
    def check_students(self):
        """Returns the list of students enrolled in the course"""
        return self.students


class Student:
    def __init__(
        self,
        name: str,
        address: str,
        phone_number: str,
        email: str,
        student_number: int,
        course_progress: CourseProgress,
    ):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.student_number = student_number
        self.average_mark = 0.0
        self.courses: List[Course] = []
        self.course_progress = course_progress

    def taken_course(self):
        """Returns the courses for which the student is enrolled"""
        return self.courses

    def enroll(self, course: Course):
        """Adds a course to the student's list of courses"""
        self.courses.append(course)
        print(f"Student {self.name} enroll to course {course.title}")

    def unenroll(self, course: Course):
        """Deletes a course from the student's list of courses"""
        self.courses.remove(course.title)  # ?
        print(f"Student {self.name} unenroll to course {course.title}")


class Professor:
    def __init__(
        self, name: str, address: str, phone_numer: str, email: str, salary: float
    ):
        self.name = name
        self.address = address
        self.phone_number = phone_numer
        self.email = email
        self.salary = salary

    def check_assignment(self, assigment: dict):
        """Checks the assignment and assigns a grade for it"""
        if assigment["is_done"]:
            assigment["mark"] = 5.0
        else:
            assigment["mark"] = 1.0
        print(f"{self.name} check your assigment")
        print(f"Your mark:{assigment['mark']}")


assigment_1 = {
    "title": "assigment_1",
    "deskription": "deskription_1",
    "is_done": True,
    "mark": 0.0,
}
marks = {1: 5, 2: 4, 3: 3.5, 4: 2, 5: 5}
notes = {}
course_progres1 = CourseProgress(marks, 2, None)
student_1 = Student(
    "Arsen", "Kosiv", "nomer_telefony", "arsemn.shvedyuk@gmail.com", 1, course_progres1
)
profesor_1 = Professor("Oleh", "adress", "phone_nuber", "email@gmail.com", 100)

course_1 = Course(
    "Programing",
    (2022, 5, 17),
    (2020, 6, 17),
    "Very cool",
    ["math", "Eng"],
    ["lab1", "lab2"],
    3,
)


course_1.add_student(student_1)


student_1.enroll(course_1)
profesor_1.check_assignment(assigment_1)
print(f"Final_mark:{course_progres1.get_final_mark()}")
