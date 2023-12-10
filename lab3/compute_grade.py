def get_valid_mark():
    while True:
        try:
            mark = float(input("Please enter a the student's midterm exam mark (0-100):"))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Please enter a student's midterm exam mark (0-100)")
        except ValueError:
            print("Please enter a valid exam mark (0-100)")

def calculate_grade(midterm, final):
    total_score = round(0.4 * midterm + 0.6 * final, 2)
    if 80 <= total_score <= 100:
        grade = 'A'
    elif 70 <= total_score < 80:
        grade = 'B'
    elif 60 <= total_score < 70:
        grade = 'C'
    elif 50 <= total_score < 60:
        grade = 'D'
    else:
        grade = 'F'
    
    return total_score, grade

def main():
    print("Welcome to the Grade Calculator!")

    student_id = input("Please enter a student ID: ")

    midterm_mark = get_valid_mark()
    final_mark = get_valid_mark()

    total_score, grade = calculate_grade(midterm_mark, final_mark)

    print(f"{student_id} has total mark as {total_score:.2f} and grade as {grade}")

if __name__ == "__main__":
    main()
