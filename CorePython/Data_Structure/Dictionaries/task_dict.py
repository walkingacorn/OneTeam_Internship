# Create a dictionary to store student names and their marks. Update the marks for one student and retrieve another students amrks usign the get()method.

student={
    "Anjali":23,
    "Aswathi":74,
    "Mahima":54
}

student['Anjali']=30
print(student)

student.update({'Aswathi':75})
print(student)

print(student.get("Mahima"))