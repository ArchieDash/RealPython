class Greeter:
    def __init__(self, name):
        self.name = name
        
    def __enter__(self):  # execution before the function call
        print(f"Hello {self.name}")
        return self  # __enter__ method should return the object to handle
    
    def __exit__(self, exc_type, exc_value, exc_tb):  # execution after the function call
        print(f"See you later, {self.name}")
        
        
if __name__ == "__main__":
    with Greeter("Alex") as grt:
        print(f"{grt.name} is doing some stuff...")
