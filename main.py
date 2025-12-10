def build_roster(registrations):
    """
    Given a list of (student_id, course_id) pairs, build a course roster.

    The result will be a dictionary where:
      - each key is a course id (string)
      - each value is a sorted list of unique student ids (strings)
    """
    roster = {}

    for student_id, course_id in registrations:
        if course_id not in roster:
            roster[course_id] = set()  # use set to avoid duplicates
        roster[course_id].add(student_id)

    # Convert sets to sorted lists
    final_roster = {}
    for course_id, students_set in roster.items():
        final_roster[course_id] = sorted(students_set)

    return final_roster


if __name__ == "__main__":
    sample = [
        ("s1", "CS101"),
        ("s2", "CS101"),
        ("s1", "MATH200"),
        ("s1", "CS101"),
    ]
    print(build_roster(sample))
