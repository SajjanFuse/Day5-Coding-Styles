import json
import logging
import os

logging.basicConfig(filename="records.log", level=logging.INFO)


def load_students():
    """
    Load student records from JSON file.

    Returns
    -------
    list
        List of student records.
    """
    try:
        with open("student_records.json", "r", encoding="utf-8") as file:
            students = json.load(file)
        logging.info("Loaded student records from student_records.json")
        return students
    except FileNotFoundError:
        logging.warning("student_records.json not found")
        return []
    except json.JSONDecodeError:
        logging.error("Failed to decode JSON data")
        return []


def save_students(students):
    """
    Save student records to JSON file.

    Parameters
    ----------
    students : list
        List of student records to save.
    """
    try:
        with open("student_records.json", "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        logging.info("Saved student records to student_records.json")
    except Exception as e:
        logging.error(f"Failed to save data: {e}")


def add_student(name, age, grade, student_id):
    """
    Add a new student record.

    Parameters
    ----------
    name : str
        Name of the student.
    age : int
        Age of the student.
    grade : float
        Grade of student.
    student_id : int
        Identity number of student.
    """
    try:
        students = load_students()
        new_student = {"Name": name, "Age": age, "Grade": grade, "ID": student_id}
        students.append(new_student)
        save_students(students)
        logging.info(f"Added student: {new_student}")
    except Exception as e:
        logging.error(f"Failed to add student: {e}")


def search_student(key):
    """
    Search for a student by ID or name.

    Parameters
    ----------
    key : int or str
        Key to search the student.

    Returns
    -------
    str or None
        Age and grade of student if found else None.
    """
    try:
        students = load_students()
        if isinstance(key, int):
            for student in students:
                if student["ID"] == key:
                    return f"Age: {student['Age']}, Grade: {student['Grade']}"
        elif isinstance(key, str):
            for student in students:
                if student["Name"] == key:
                    return f"Age: {student['Age']}, Grade: {student['Grade']}"
        logging.info("Student not found")
        return None
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        return None


def update_student(key, age=None, grade=None):
    """
    Update a student's age or grade.

    Parameters
    ----------
    key : int or str
        ID is int, Name is str.
    age : int, optional
        Age to update student, by default None.
    grade : float, optional
        Grade to update, by default None.
    """
    try:
        students = load_students()
        updated = False
        for student in students:
            if student["ID"] == key or student["Name"] == key:
                if age:
                    student["Age"] = age
                    updated = True
                if grade:
                    student["Grade"] = grade
                    updated = True
        if updated:
            save_students(students)
            logging.info(f"Updated student {key}: Age={age}, Grade={grade}")
        else:
            logging.info("Student not found")
    except Exception as e:
        logging.error(f"Exception occurred: {e}")


add_student("Sansa", 25, 59.0, 13)
add_student("Jon", 12, 69.0, 14)
add_student("Samuel", 32, 90.0, 154)
add_student("Arya", 25, 19.0, 123)
add_student("Manish", 27, 99.0, 114)
add_student("Pratik", 23, 90.0, 4)

print(search_student(123))

update_student(123, age=26, grade=95.0)
print(search_student(123))
