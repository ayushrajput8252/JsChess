#CLASSS
class employee:
    #magic method
    def __init__(self):
        print("attributes are being initialized")
        self.name = "John Jones"
        self.salary = 1000
        self.titel = "developer"
        print("attributes initialized")

    def travel(self, destination):
        print("travel method is called")
        print(f"{self.name} is going to {destination}")
#OBJECT
sam = employee()
#METHOD CALL
sam.travel("London")
