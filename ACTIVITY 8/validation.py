import re


def validate_fields(student_id, name, course, year_level, gender, email):
    """Returns (True, '') if valid, or (False, error_message) if invalid."""

    if not student_id.strip():
        return False, "Student ID cannot be empty."

    if not student_id.strip().isdigit() or int(student_id.strip()) < 5001:
        return False, "Student ID must be a number starting at 5001 or above."

    if not name.strip():
        return False, "Name cannot be empty."

    if any(char.isdigit() for char in name):
        return False, "Name must not contain numbers."

    if not course.strip():
        return False, "Course cannot be empty."

    if any(char.isdigit() for char in course):
        return False, "Course must not contain numbers."

    if not year_level.strip():
        return False, "Year Level cannot be empty."

    if not year_level.strip().isdigit():
        return False, "Year Level must contain numbers only."

    if not gender:
        return False, "Please select a Gender."

    if not email.strip():
        return False, "Email cannot be empty."

    # Basic email format check
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if not re.match(email_pattern, email.strip()):
        return False, "Invalid email format."

    return True, ""