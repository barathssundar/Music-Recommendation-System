class music:
    def New_User(self):
        global users1,pwd1
        users1 = []
        pwd1 =[]
        print("Please enter the following details : ")         
        while True:
            Username = input("Enter Username: ")
            if Username in users1:
                print("Username Exists. Try something new!")
                continue
            users1.append(Username)
            Password = input("Enter password: ")   
            pwd1.append(Password)
            print("User generation successful")
            from log import Login
            l=Login()
            l.login()
            False

    def home(self):
        file=open('home.txt','r')
        print(file.read())
        X = int(input("1.Search\t2.Library\t3.MyProfile\t4.Logout \n")) 
        if X == 1: 
            print("Search") 
            from music_files import files
            f=files()
            f.music()
        elif X == 2: 
            print("Library") 
            from music_files import files
            fi=files()
            fi.library()
        elif X == 3: 
            print("MyProfile")
            from data1 import myprofile 
            m=myprofile ()
            m.profile()
        elif X == 4:
            print("Logout")
            exit()
        else: 
            print("Enter valid credentials")
mu=music() 
