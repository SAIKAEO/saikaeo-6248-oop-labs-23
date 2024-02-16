class ComEnStudent:

    def __init__(self, name):
        self.name = name
        self.course_ids = []

    def __str__(self):
        return f"{self.name} has take these courses: {self.course_ids}"

    def take_course(self, *course_ids):
        self.course_ids.extend(course_ids)

class CoEStudent(ComEnStudent):
    pass

class DMEStudent(ComEnStudent):
    def __str__(self):
        return f"{self.name} has take these courses: {self.course_ids}"


if __name__ == '__main__':
    com_students = []
    manee = CoEStudent("Manee")
    mana = DMEStudent("Mana")

    manee.take_course("842004")
    mana.take_course("842004", "842005", "813701")

    manee.take_course("EN813702", "EN811301", "EN811302")
    mana.take_course("EN842005")

    com_students.append(manee)
    com_students.append(mana)

    for com_student in com_students:
        com_student.take_course("SC401206")
        print(com_student)
print("\tspecialized in creating content type:Infographics")
        