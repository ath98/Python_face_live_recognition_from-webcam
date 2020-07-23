from create_data import add_data
from face_recognize import recognize
print("Press 1-To insert new face in database\n 2- To recognise faces")
user=input("Enter here")

if(user=='a'):
    print("Enter Name of user")
    name=input("Enter name here")
    add_data(name)
if(user=='b'):
    recognize()