import random
import tkinter as tk

#Cuboid Class
class Cube:
    def __init__(self, length=2.0, width=3.0, height=4.0):
        self.__length = length
        self.__width = width
        self.__height = height

    #Accessors
    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    #Mutators
    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    #Surface area calculation
    def findArea(self):
        return 2 * (self.__length*self.__width + self.__length*self.__height + self.__width*self.__height)

    #Displays class name
    def display(self):
        return "Cuboid"

#Circle Class
class Circle:
    def __init__(self, radius=4.3):
        self.__radius = radius

    #Accessor
    def get_radius(self):
        return self.__radius

    #Mutator
    def set_radius(self, radius):
        self.__radius = radius

    #Area calculation
    def findArea(self):
        return 3.14159 * self.__radius**2

    #Displays class name
    def display(self):
        return "Circle"

#Square Class
class Square:
    def __init__(self, side=4.0):
        self.__side = side

    #Accessor
    def get_side(self):
        return self.__side

    #Mutator
    def set_side(self, side):
        self.__side = side

    #Area calculation
    def findArea(self):
        return self.__side**2

    #Display class name
    def display(self):
        return "Square"


#Generates new 10 shapes
def generate_shapes():
    shapes_list = []
    for _ in range(10):
        num = random.randint(0, 2)  # 0 = Circle, 1 = Square, 2 = Cube
        if num == 0:
            shapes_list.append(Circle())
        elif num == 1:
            shapes_list.append(Square())
        else:
            shapes_list.append(Cube())
    return shapes_list

#Outputs Results
def print_to_screen(shapes_list):
    print("\nShape Areas:")
    for obj in shapes_list:
        print(f"{obj.display()} - Area: {obj.findArea():.2f}")

def save_to_file(shapes_list):
    filename = input("Enter filename to save results: ")
    with open(filename, "w") as f:
        for obj in shapes_list:
            f.write(f"{obj.display()} - Area: {obj.findArea():.2f}\n")
    print(f"Results saved to {filename}")

def show_in_gui(shapes_list):
    root = tk.Tk()
    root.title("Shapes Area Results")
    text = ""
    for obj in shapes_list:
        text += f"{obj.display()} - Area: {obj.findArea():.2f}\n"
    label = tk.Label(root, text=text, justify="left", padx=10, pady=10)
    label.pack()
    root.mainloop()

#Main Menu 
def main_menu():
    while True:
        print("\nSelect an option:")
        print("1. Save results to a file")
        print("2. Print results on screen")
        print("3. Show results in GUI window")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        #Generates new 10 random shapes for every option
        if choice == '1':
            shapes_list = generate_shapes()
            save_to_file(shapes_list)

        elif choice == '2':
            shapes_list = generate_shapes()
            print_to_screen(shapes_list)

        elif choice == '3':
            shapes_list = generate_shapes()
            show_in_gui(shapes_list)

        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

#Program Run
if __name__ == "__main__":
    main_menu()
