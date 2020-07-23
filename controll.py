from create_data import add_data
from face_recognize import recognize
print("Press A-To insert new face in database\n B- To recognise faces")
user=input("Enter here")

if(user=='a'):
    print("Enter Name of user")
    name=input("Enter name here")
    add_data(name)
if(user=='b'):
    recognize()