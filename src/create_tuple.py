# Write your solution here
def create_tuple(x: int, y: int, z: int):
    values = [x, y, z]
    my_tuple=(min(values), max(values), x+y+z)
    return my_tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))