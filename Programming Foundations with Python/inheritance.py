class Parent():
    def __init__(this, ln, ec):
        print("Parent init is called")
        this.last_name=ln
        this.eye_color=ec

    def show_info(this):
        print("Last name is "+this.last_name)
        print("Eye color is "+this.eye_color)
        
class Child(Parent):
    def __init__(this, ln, ec, nots):
        print("Child init is called")
        Parent.__init__(this, ln, ec)
        this.number_of_toys=nots

    def show_info(this):
        print("Last name is "+this.last_name)
        print("Eye color is "+this.eye_color)
        print("Number of toys "+str(this.number_of_toys))

billy=Parent("Cyrus", "blue")
miley=Child("John", "black", 5)
#print(billy.last_name)
#print(miley.last_name)
billy.show_info()
miley.show_info()
