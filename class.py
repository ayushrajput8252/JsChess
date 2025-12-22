class chatbook():
    def __init__(self):
        #hiding a method
        self.__name = ''
        self.username = ''
        self.password = ''
        self.author = ''
        self.loggin = False
        self.menu()

    def menu(self):
        user_input = input(""""Welcome to Chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           -> """)
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.sendmsg == '5'
        else:
            exit()
    def signup(self):
        email = input("enter your email here -> ")
        pwd = input("setup your password here -> ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' or self.password == '':
            print("FIRST SIGNUP TO SIGN IN")
            self.signup()
            
        else :
            username = input("write you emial here")
            userpass = input("write your password here ")
            if username == self.username and userpass == self.password:
               print("You have been logged in successfulu")
               self.loggin = True
               
            else :
                print(f"your password does not match try again {self.signup}")
    
    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()
    def sendmsg(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send the msg? -> ")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()

user1 = chatbook()
        
        

            

    
