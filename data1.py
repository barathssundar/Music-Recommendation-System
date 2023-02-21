import log
class myprofile:
    def profile(self):
        username = log.Username1
        password = log.Password1
        print(username)    
        print(password)  
        X = int(input("1.Logout\t 2.Login\n")) 
        if X == 1:
            print("Logout")
            exit()
        elif X :
            print("Re-enter valid credentials   :")
            
p=myprofile()
#p.profile()