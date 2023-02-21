class Login:
    def login(self):
        print("---Login---")
        global Username1,Password1
        self.users = ["Chandru", "Manoj", "Abi"]
        self.pwd=["234", "124", "12"]
        while True:
            Username1 = input("Enter Username : ") 
            Password1 = input("Enter Password : ")
            import Music
            if (((Username1 in self.users) and (Password1 in self.pwd)) or ((Username1 in Music.users1) and (Password1 in Music.pwd1))):
                print("Welcome! Have a great time!")
                from Music import music
                mu=music()
                mu.home()  
                False     
            elif Username1 not in self.users :
                print("Incorrect Username or Password")
l = Login()
