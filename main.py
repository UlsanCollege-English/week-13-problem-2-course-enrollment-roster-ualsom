

def build_roster(registrations):
    """
    Given a list of (student_id, course_id) pairs, build a course roster.

    The result should be a dictionary where:
      - each key is a course id (string)
      - each value is a sorted list of unique student ids (strings)
        enrolled in that course

    Duplicate registrations for the same (student_id, course_id) pair
    should appear only once in the output.
    """

    # TODO Step 1–3: Understand the story, and list input, output, and variables.
    # TODO Step 4: Plan how to group registrations by course and remove duplicates.
    # TODO Step 5: Write pseudocode for building and then sorting the rosters.
    # TODO Step 6: Implement your algorithm in Python.
    # TODO Step 7: Run tests and add your own small manual tests.
    # TODO Step 8: Check that your solution is roughly O(n log n) time.
    pass


if __name__ == "__main__":
    # Optional manual test
    sample = [
        ("s1", "CS101"),
        ("s2", "CS101"),
        ("s1", "MATH200"),
        ("s1", "CS101"),
    ]
    print(build_roster(sample))
