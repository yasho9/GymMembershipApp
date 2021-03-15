
class Gym:
    member_info={}
    dict1={}
    def createMember(self):
        name=input("Enter Your Full Name ")
        age=int(input("Enter Your Age "))
        gender=input("Enter Gender ")
        mob_no=int(input("Enter Mobile Number "))
        mail=input("Enter Your Mail ")
        bmi=float(input("Enter Your BMI "))
        duration=int(input("Enter Duration in Months "))
        self.member_info[mob_no]={}
        self.member_info[mob_no]["Name"]=name
        self.member_info[mob_no]["Age"] = age
        self.member_info[mob_no]["Gender"] = gender
        self.member_info[mob_no]["Mail"] = mail
        self.member_info[mob_no]["BMI"] = bmi
        self.member_info[mob_no]["Duration"] = duration

    def viewMember(self):
        mob_no = int(input("\nEnter Mobile Number "))
        print()
        if mob_no in self.member_info:
            print("Name:",self.member_info[mob_no]["Name"])
            print("Age:",self.member_info[mob_no]["Age"])
            print("Gender:", self.member_info[mob_no]["Gender"])
            print("Mail:", self.member_info[mob_no]["Mail"])
            print("BMI:", self.member_info[mob_no]["BMI"])
            print("Duration:", self.member_info[mob_no]["Duration"])
        else:
            print("No Member Found")

    def deleteMember(self):
        mob_no = int(input("\nEnter Mobile Number "))
        del self.member_info[mob_no]
        print("\nMember Deleted Successfully ")
        print()

    def UpdateMember(self):
        mob_no = int(input('Enter Mobile Number '))
        duration = int(input("Enter The Duration to Update Membership "))
        self.member_info[mob_no]["Duration"]=duration
        print("\nMember Updated Successfully ")
        print()

    def CreateRegimen(self):
        self.dict1["bmi<18.5"]={"Mon":"Chest","Tue":"Biceps","Wed":"Rest","Thu":"Back","Fri":"Triceps","Sat":"Rest","Sun":"Rest"}
        self.dict1["bmi<25"]={"Mon":"Chest","Tue":"Biceps","Wed":"Cardio/Abs","Thu":"Back","Fri":"Triceps","Sat":"Legs","Sun":"Rest"}
        self.dict1["bmi<30"]={"Mon": "Chest", "Tue": "Biceps", "Wed": "Cardio/Abs", "Thu": "Back", "Fri": "Triceps","Sat": "Legs", "Sun": "Rest"}
        self.dict1["bmi>30"]={"Mon": "Chest", "Tue": "Biceps", "Wed": "Cardio", "Thu": "Back", "Fri": "Triceps","Sat": "Cardio", "Sun": "Cardio"}
        print("\nRegimen Created Successfully\n")


    def ViewRegimen(self):
        print()
        if self.dict1:
            for i in self.dict1:
                print("**************************")
                print("for",i)
                print("--------------------------")
                print("Mon ", self.dict1[i]["Mon"])
                print("Tue ", self.dict1[i]["Tue"])
                print("Wed ", self.dict1[i]["Wed"])
                print("Thu ", self.dict1[i]["Thu"])
                print("Fri ", self.dict1[i]["Fri"])
                print("Sat ", self.dict1[i]["Sat"])
                print("Sun ", self.dict1[i]["Sun"])
        else:
            print("Regiment Not Present\nCreate Regimen First")
        print()


    def DeleteRegimen(self):
        if self.dict1:
            self.dict1.clear()
            print("\nRegimen Deleted Successfully\n")
        else:
            print("Regimen is not Present\nCreate Regimen First")

    def UpdateRegimen(self):
        print()

        if self.dict1:
            update = int(input("Enter BMI to Update Regimen"))
            if update<18.5:
                self.dict1["bmi<18.5"]["Mon"] = input('Mon ')
                self.dict1["bmi<18.5"]["Tue"] = input('Tue ')
                self.dict1["bmi<18.5"]["Wed"] = input('Wed ')
                self.dict1["bmi<18.5"]["Thu"] = input('Thu ')
                self.dict1["bmi<18.5"]["Fri"] = input('Fri ')
                self.dict1["bmi<18.5"]["Sat"] = input('Sat ')
                self.dict1["bmi<18.5"]["Sun"] = input('Sun ')
            elif update<25:
                self.dict1["bmi<25"]["Mon"] = input('Mon ')
                self.dict1["bmi<25"]["Tue"] = input('Tue ')
                self.dict1["bmi<25"]["Wed"] = input('Wed ')
                self.dict1["bmi<25"]["Thu"] = input('Thu ')
                self.dict1["bmi<25"]["Fri"] = input('Fri ')
                self.dict1["bmi<25"]["Sat"] = input('Sat ')
                self.dict1["bmi<25"]["Sun"] = input('Sun ')
            elif update<30:
                self.dict1["bmi<30"]["Mon"] = input('Mon ')
                self.dict1["bmi<30"]["Tue"] = input('Tue ')
                self.dict1["bmi<30"]["Wed"] = input('Wed ')
                self.dict1["bmi<30"]["Thu"] = input('Thu ')
                self.dict1["bmi<30"]["Fri"] = input('Fri ')
                self.dict1["bmi<30"]["Sat"] = input('Sat ')
                self.dict1["bmi<30"]["Sun"] = input('Sun ')
            elif update>30:
                self.dict1["bmi>30"]["Mon"] = input('Mon ')
                self.dict1["bmi>30"]["Tue"] = input('Tue ')
                self.dict1["bmi>30"]["Wed"] = input('Wed ')
                self.dict1["bmi>30"]["Thu"] = input('Thu ')
                self.dict1["bmi>30"]["Fri"] = input('Fri ')
                self.dict1["bmi>30"]["Sat"] = input('Sat ')
                self.dict1["bmi>30"]["Sun"] = input('Sun ')
            print("\nRegiment Updated Sucessfully...\n")
        else:
            print("Regimen is not Created")

    def MyRegimen(self):
        mob_no = int(input("\nEnter Mobile Number "))
        if mob_no in self.member_info:
            if self.member_info[mob_no]["BMI"]<18.5:
                print("Mon ", self.dict1["bmi<18.5"]["Mon"])
                print("Tue ", self.dict1["bmi<18.5"]["Tue"])
                print("Wed ", self.dict1["bmi<18.5"]["Wed"])
                print("Thu ", self.dict1["bmi<18.5"]["Thu"])
                print("Fri ", self.dict1["bmi<18.5"]["Fri"])
                print("Sat ", self.dict1["bmi<18.5"]["Sat"])
                print("Sun ", self.dict1["bmi<18.5"]["Sun"])
                print()
            elif self.member_info[mob_no]["BMI"]<25:
                print("Mon ", self.dict1["bmi<25"]["Mon"])
                print("Tue ", self.dict1["bmi<25"]["Tue"])
                print("Wed ", self.dict1["bmi<25"]["Wed"])
                print("Thu ", self.dict1["bmi<25"]["Thu"])
                print("Fri ", self.dict1["bmi<25"]["Fri"])
                print("Sat ", self.dict1["bmi<25"]["Sat"])
                print("Sun ", self.dict1["bmi<25"]["Sun"])
                print()
            elif self.member_info[mob_no]["BMI"]<30:
                print("Mon ", self.dict1["bmi<30"]["Mon"])
                print("Tue ", self.dict1["bmi<30"]["Tue"])
                print("Wed ", self.dict1["bmi<30"]["Wed"])
                print("Thu ", self.dict1["bmi<30"]["Thu"])
                print("Fri ", self.dict1["bmi<30"]["Fri"])
                print("Sat ", self.dict1["bmi<30"]["Sat"])
                print("Sun ", self.dict1["bmi<30"]["Sun"])
                print()
            elif self.member_info[mob_no]["BMI"]>30:
                print("Mon ", self.dict1["bmi>30"]["Mon"])
                print("Tue ", self.dict1["bmi>30"]["Tue"])
                print("Wed ", self.dict1["bmi>30"]["Wed"])
                print("Thu ", self.dict1["bmi>30"]["Thu"])
                print("Fri ", self.dict1["bmi>30"]["Fri"])
                print("Sat ", self.dict1["bmi>30"]["Sat"])
                print("Sun ", self.dict1["bmi>30"]["Sun"])
                print()

        else:
            print("\nUser Not Found \n")

    def MyProfile(self):
        mob_no = int(input("\nEnter Mobile Number "))
        if mob_no in self.member_info:
            print("Name:", self.member_info[mob_no]["Name"])
            print("Age:", self.member_info[mob_no]["Age"])
            print("Gender:", self.member_info[mob_no]["Gender"])
            print("Mail:", self.member_info[mob_no]["Mail"])
            print("BMI:", self.member_info[mob_no]["BMI"])
            print("Duration", self.member_info[mob_no]["Duration"])
        else:
            print("No record Found")
        print()
