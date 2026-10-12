import Event 

c = 'y'
while c.lower() == 'y' :
    print("<=== Event Management System ===>".center(60 , '.'))
    print('1. Add Event')
    print('2. Events Management')
    print('3. Register Student')
    print('4. Login Student')
    print('5. Exit')
    choice4 = int(input("Enter the serial number of your choice : "))
    if choice4 == 1 :
        Event.add_event()
    elif choice4 == 3 :
        Event.add_student()
    elif choice4 == 2 :
        C = 'y'
        while C.lower() == 'y' :
              print("Event Management".center(60 , '='))
              print("1. List Events")
              print("2. List Students")
              print("3. Print Blank Attendance")
              print("4. Enter Attendance")
              print("5. Print Final Attendance")
              print("6. Exit")
              choice = int(input("Enter the serial number of your choice : "))
              if choice == 1 :
                 Event.view_event()
              elif choice == 2 :
                 Event.view_student()
              elif choice == 3 :
                 Event.view_battend()
              elif choice == 4 :
                 Event.enter_attend()
              elif choice == 5 :
                 Event.view_fattend()
              elif choice == 6 :
                  print("Good Bye")
                  break
              else : print("INVALID CHOICE")
    elif choice4 == 4 :
        if Event.login() :
            C = 'y'
            while C.lower() == 'y' :
                print("Students Registeration Details".center(60 , '='))
                print("1. Register for an Event")
                print("2. List Registered Events")
                print("3. Exit")
                choice = int(input("Enter the serial number of your choice : "))
                if choice == 1 :                   
                    if Event.register_event() :
                        print ("Get ready")
                elif choice == 2 :
                    Event.list_registered()
                elif choice == 3 :
                        print("Good Bye")
                        break
                else : print("INVALID CHOICE")
                C = input("Do you want to continue (y/n) : ")
        else : 
            print("Either your username or password is incorrect")            
    elif choice4 == 5 :
        print("Thanks for using Event Management System....")
        break
    else : print("INVALID CHOICE")
    c = input("Do you want to return to main menu (y/n) : ")
else : print("Exiting...")
