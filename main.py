from rooms import Rooms
from doctor import Doctor
from patient import Patient
from reception import Reception

room = Rooms(10)

doct = Doctor()
doct.addDoctors("Dr. Ana",'MBBS')
doct.addDoctors("Dr. Emma",'MBBS')

patient = Patient()

recep = Reception('Elsa',101)

def Options():
    print('\n'+ recep.name, '''can perform below operations:
          
1) Display patient names who are admitted
2) Check room availability
3) Admit a patient
4) Discharge patient
5) Display Doctors''')
    print()

def prompt():
    message = input('\n Want to perform more operations?(Y/N):')
    if message == 'Y':
        operation()
    elif message == 'N':
        return
    else:
        print('Invalid input')
        prompt()

def operation():
    while True: 
        Options()
        number = int(input("Enter operation no. which you want to perform:"))
        if number <=5 : 
            if number == 1:
                recep.display_patients_list(recep)
                prompt()
                break
            elif number == 2:
                recep.room_availibility(room)
                prompt()
                break
            elif number == 3:
                recep.admit(patient,room)
                prompt()
                break
            elif number == 4:
                recep.discharge(patient,recep)
                prompt()
                break
            elif number == 5:
                doct.displayDoc()
                prompt()
                break
        else: 
            print('\nPlease enter number from the given options')
            return operation()

operation()   