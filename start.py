class Start:   
   def choice(self):
        Welcome = int(input("1.New User\t 2.Returning User \n"))
        if (Welcome == 1):
            from Music import music
            mu=music()
            mu.New_User()

        elif(Welcome == 2):
            from log import Login
            mu=Login()
            mu.login()
s=Start()
s.choice()