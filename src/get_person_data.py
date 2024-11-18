"""Get person data"""
from PIL.ImageCms import Flags

DATA = {
     111: {
         "name": "Dan",
         "age": 20
     },
     112: {
         "name": "Maria",
         "age": 33
     },
}

def get_name_and_age(person_id):
    """Return person name and age"""
    return DATA[person_id]


def save_data(file, person_data):
    """Save person data to file"""
    with open(file, "w") as fw:
        fw.write(person_data)

def read_data(file):
    """Return a list with all rows from file"""
    with open(file,"r") as fr:
        content = fr.readlines()

    return content


if __name__ == "__main__":
    try:
        person = get_name_and_age(112)
        print(person)
    except KeyError:
        print("Not a good user id")
