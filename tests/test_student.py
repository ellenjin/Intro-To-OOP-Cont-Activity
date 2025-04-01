from school_schedule.student import Student

def test_student_attributes():
    student = Student("Clara", "Junior", ["Art", "Math"])

    assert student.name == "Clara"
    assert student.grade == "Junior"
    assert student.classes == ["Art", "Math"]

def test_add_class():
    student = Student("Clara", "Junior", ["Art", "Math"])
    updated_classes = student.add_class("History")

    assert len(student.classes) == 3
    assert updated_classes == ["Art", "Math", "History"]
    assert student.classes == ["Art", "Math", "History"]

def test_display_classes():
    student = Student("Clara", "Junior", ["Art", "Math"])

    displayed = student.display_classes()
    assert displayed == "Art, Math"

def test_no_classes():
    student = Student("Clara", "Junior", [])
    num_classes = student.get_num_classes()
    
    assert num_classes == 0

def test_summary():
    student = Student("Clara", "Junior", ["Art", "Math"])
    summary = student.summary()
    assert summary == "Clara is a Junior enrolled in 2 classes: Art, Math"