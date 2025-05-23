room_number = {
    "CSC101":"3004",
    "CSC102":"4501",
    "CSC103":"6755",
    "NET110":"1244",
    "COM241":"1411"
}

instructor = {
    "CSC101":"Haynes",
    "CSC102":"Alvarado",
    "CSC103":"Rich",
    "NET110":"Burke",
    "COM241":"Lee"
}

meeting_tme = {
    "CSC101":"8:00 a.m.",
    "CSC102":"9:00 a.m.",
    "CSC103":"10:00 a.m.",
    "NET110":"11:00 a.m.",
    "COM241":"1:00 p.m."
}


course_number = input("Enter a course number: ")

if course_number not in room_number:
    print("Invalid course number")
    exit()

print("The course details for", course_number, "are:")
print("Room: ", room_number[course_number])
print("Instructor: ", instructor[course_number])
print("Meeting Time: ", meeting_tme[course_number])