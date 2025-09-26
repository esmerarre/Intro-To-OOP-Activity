# add your get_student_with_more_classes function here!
def get_student_with_more_classes(first_student, second_student):
    if first_student.get_num_classes() > second_student.get_num_classes():
        return first_student.name
    elif first_student.get_num_classes() == second_student.get_num_classes():
        return None
    return second_student.name
    