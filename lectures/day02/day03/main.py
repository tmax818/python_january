# import module
from package.module import API_KEY as Other_key
from package.dog import Dog

API_KEY = "new api"

print(API_KEY)
print(Other_key)

fido = Dog()
fido.bark()

print(__name__)

if __name__ == "__main__":
    fido.bark()