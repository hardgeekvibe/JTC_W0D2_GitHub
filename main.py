def hello_world():
    return "Hello from Nashid!"

name = input("What is your name: ")

def greet_person(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(f"{hello_world()}\n{greet_person(name)}")