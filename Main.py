class student:
    def __init__(self, roll, name,gr):
        self.roll = roll
        self.name = name
        self.gr = gr

    def __str__(self):
        return f"Roll_No: {self.roll} | Name: {self.name} | Gr_No: {self.gr}"


class Management:
    def __init__(self):
        self.records=[]

    def adding_std(self):
        roll=int(input("Enter Roll Number:  "))
        name=input("Enter  Student  Name: ")
        gr=input("Enter GR.No of Student: ")

        for record in self.records:
            if record.roll==roll:
               print(" Student already Exists ")
               return 
        self.records.append(student(roll,name,gr))
        print("student added Sucessfully ")

    def display_records(self):
        if not self.records:
            print("No records available \n")
            return

        print("=======Records========")
        for record in self.records:
            print(record)

    def searching_student(self):
        roll=int(input("Enter roll NO: "))
        for record in self.records:
            if record.roll==roll:
                print(record)
                return 
            
        print("Record Not Found")
        return 
        
    def deleting_std(self):
        roll=int(input("Enter roll Number to delete: "))
        for record in self.records:
            if record.roll==roll:
                self.records.remove(record)
                print("Record deleted sucessfully")
                return
            
        print("Record not found ")
        return


obj=Management()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View student")
    print("3. search student")
    print("4. Delete student record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        obj.adding_std()

    elif choice == "2":
        obj.display_records()

    elif choice == "3":
        obj.searching_student()
    elif choice == "4":
        obj.deleting_std()
    elif choice=="5":
        print("Thank for using Student management system")
        break
    else:
        print("Unknown command")