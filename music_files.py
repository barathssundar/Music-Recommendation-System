import random 
class files:
    def library(self):
        global songs
        songs = ["Bohemians Rhapsody", "Stairway to Heaven", "Hotel California", "Smells Like Teen Spirit", "Imagine", "Hey Jude", "Like a Rolling Stone", "Purple Haze", "Sweet Child O Mine", "Billie Jean"]
        print(songs)
        X = int(input("1.Search\t2.MyProfile\t3.Logout \n")) 
        if X == 1: 
            print("Search") 
            f.music()
        elif X == 2: 
            print("MyProfile")
            from data1 import myprofile 
            m=myprofile ()
            m.profile()
        elif X == 3:
            print("Logout")
            exit()
        else: 
            print("Enter valid credentials")


    def music(self):
        mood = input("What is your mood? happy or sad: ") 

        if mood == "happy": 
            recommendations = ["Hey Jude", "Sweet Child O Mine", "Billie Jean"] 
        elif mood == "sad": 
            recommendations = ["Imagine", "Like a Rolling Stone", "Purple Haze"] 
        else: 
            recommendations = songs 

        song = random.choice(recommendations) 

        print("We recommend listening to: ", song) 
        X = int(input("1.MyProfile\t2.Library\t3.Logout \n")) 

        if X == 1: 
            print("MyProfile")
            from data1 import myprofile 
            m=myprofile ()
            m.profile()
        elif X == 2:
            print("Library") 
            f.library() 
        elif X == 3:
            print("Logout")
            exit()
        else: 
            print("Enter valid credentials")

f=files()