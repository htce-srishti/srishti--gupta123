import json


student1 = {
    "studentid": int(input("Enter First Student ID: ")),
    "studentname": input("Enter First Student Name: "),
    "experience": input("Enter First Student Experience: "),
    "skills": input("Enter First Student Skills: "),
    "qualification": [
        {
            "name": input("Enter First Student two Qualification Name: "),
            "passingyear": int(input("Enter First Student  Passing Year: "))
        }
    ]

}
    
student2 = {
    "studentid": int(input("Enter Second Student ID: ")),
    "studentname": input("Enter Second Student Name: "),
    "experience": input("Enter Second Student Experience: "),
    "skills": input("Enter Second Student Skills: "),
    "qualification": [
        {
            "name": input("Enter Second Student Qualification Name: "),
            "passingyear": int(input("Enter Second Student Passing Year: "))
        }
    ]
}


students_data = [student1, student2]


print("\nStudents Data:")
print(json.dumps(students_data, indent=4))

