Student_Name = input("Enter Student Name:")
USN = input("Enter USN:")
Branch = input("Enter Branch:")
Semester = input("Enter Semester:")

mark1 = float(input("Enter marks for subject 1:"))
mark2 = float(input("Enter marks for subject 2:"))
mark3 = float(input("Enter marks for subject 3:"))

Total_Marks = mark1 + mark2 + mark3
Average = Total_Marks/3

print("\nSTUDENT_REPORT")
print(f"Student_Name :{Student_Name}")
print(f"USN  :{USN}")
print(f"Branch:{Branch}")
print(f"Semester :{Semester}")
print(f"Total_Marks:{Total_Marks}")
print(f"Average : {Average:.2f}")