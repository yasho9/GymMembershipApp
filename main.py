import Gym
obj=Gym.Gym()
print("****************************************************")
print("----------- Welcome To Fitness Focus Gym -----------")
print("****************************************************")
while True:
    choice=int(input("Enter the Type of User \n 1) Log In as Super User \n 2) Log In as Member User \n 3) Exit \n"))
    if choice==1:
        while(True):
            print("**********************************************")
            print(" 1) Create Member \n 2) View Member \n 3) Delete Member \n 4) Update Member \n 5) Create Regimen \n 6) View Regimen \n 7) Delete Regimen \n 8) Update Regimen \n 9) Exit ")
            print("**********************************************")
            ch=int(input("Enter Your Choice "))

            print("**********************************************")
            if ch==1:
                obj.createMember()
            elif ch==2:
                obj.viewMember()
            elif ch==3:
                obj.deleteMember()
            elif ch==4:
                obj.UpdateMember()
            elif ch==5:
                obj.CreateRegimen()
            elif ch==6:
                obj.ViewRegimen()
            elif ch==7:
                obj.DeleteRegimen()
            elif ch==8:
                obj.UpdateRegimen()
            elif ch==9:
                break
            else:
                print("\nYou Entered Wrong Choice\n")

    elif choice==2:
        while True:
            print("**********************************************")
            print(" 1) My Regimen \n 2) My Profile \n 3) Exit \n")
            print("**********************************************")
            ch=int(input("Enter your Choice "))
            print("**********************************************")
            if ch==1:
                obj.MyRegimen()
            elif ch==2:
                obj.MyProfile()
            elif ch==3:
                break
            else:
                print("\n You Entered Wrong Choice ")
    elif choice==3:
        break




