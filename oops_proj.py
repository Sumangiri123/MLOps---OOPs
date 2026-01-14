class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedIn = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook !! How would you like to proceed?
                           1. Press 1 to Signup
                           2. Press 2 to Signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. press any other key to exit
                           
                           ->""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()   


    def signup(self):
        email = input("Enter your email here -- ")
        pwd = input("setup your passsword -- ")
        self.username = email
        self.password = pwd
        print("You have Signup Successfully !!")
        print("\n")
        self.menu()
    

    def signin(self):
        if self.username == '' and self.username == '':
            print("Please Signup first by pressing 1 in the main menu")
        else:
            uname = input("Enter your email here ---> ")
            pwd = input("enter your passsword  ---> ")
            if self.username == uname and self.password == pwd:
                print("You have Signed in Successfully")
                self.loggedIn = True
            else:
                print("Please input correct credentials..")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedIn == True:
            txt = input("Enter your message here ->")
            print(f"Following content has been Posted --> {txt}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedIn == True:
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send the msg? ->")
            print(f"Your message has been  sent to post something...")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()
        


# user1 = chatbook()

