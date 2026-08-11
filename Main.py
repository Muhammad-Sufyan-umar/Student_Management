class student:
    def __init__(self, Roll_No, name,Gr_No,Marks,Grade):
        self.Roll_No = Roll_No
        self.name = name
        self.Gr_No = Gr_No
        self.Marks = Marks
        self.Grade = Grade

    def __str__(self):
        return f"Roll_No: {self.Roll_No} | Name: {self.name} | Gr_No: {self.Gr_No} | Marks: {self.Marks} | Grade: {self.Grade}"

    


class Management:
    def __init__(self):
        self.records=[]

    def Add_std(self):
        Roll_No=int(input("Enter Roll Number:  "))
        name=input("Enter  Student  Name: ")
        Gr_No=input("Enter GR.No of Student: ")
        Marks=int(input("Enter Marks of Student: "))
        Grade=input("Enter Grade of Student: ")



        for record in self.records:
            if record.Roll_No==Roll_No:
               print(" \nStudent already Exists❗ ")
               return 
        self.records.append(student(Roll_No,name,Gr_No,Marks,Grade))
        print("\n--->student added Sucessfully✔")

    def display_records(self):
        if not self.records:
            print("No records available \n")
            return

        print("=======Records========\n")
        for record in self.records:
            print(record)

    def Search_student(self):
        Roll_No=int(input("Enter Roll NO: "))
        for record in self.records:
            if record.Roll_No==Roll_No:
                print("\n",record)
                return 
            
        print("Record Not Found")
        return 
        
    def Delete_std(self):
        Roll_No=int(input("\nEnter Roll Number " \
        "to delete: "))
        for record in self.records:
            if record.Roll_No==Roll_No:
                self.records.remove(record)
                print("\n--->Record deleted sucessfully ✔ ")
                return
            
        print("Record not found❗")
        return


obj=Management()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View student")
    print("3. search student")
    print("4. Delete student record")
    print("5. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        obj.Add_std()

    elif choice == "2":
        obj.display_records()

    elif choice == "3":
        obj.Search_student()
    elif choice == "4":
        obj.Delete_std()
    elif choice=="5":
        print("==============================================")
        print("Thank for using Student management system")
        print("==============================================")
        break
    else:
        print("Unknown command🥵")