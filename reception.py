class Reception:
    patients_admitted = [] #stores the name of the patient
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def admit(self,patient,room):
        if len(self.patients_admitted) != room.num:
            patient.name = input("Enter your name: ")
            patient.problem = input("Address your issues : ")
            self.patients_admitted.append(patient.name)
            print()
            print(patient.name, "is alloted a room")
        else:
            return print('\n Sorry, rooms are not available')

    def display_patients_list(self,recep):
        if len(self.patients_admitted) == 0:
            return print('\nNo record found')  
        else:
            print("\nPatients admitted:")
            for i in recep.patients_admitted:
                print(i)         

    def discharge(self,patient,recep):
        if len(self.patients_admitted) != 0:
            self.display_patients_list(recep)
            patient.name = input("\nEnter the name of patient which need to be discharged: ")
            if patient.name in self.patients_admitted:
                self.patients_admitted.remove(patient.name)
                print()
                print(patient.name, "has been discharged from the hospital ")
            elif patient.name not in self.patients_admitted:
                print("No match found!")
                patient.name = input("Please enter the correct name of patient: ")
                if patient.name in self.patients_admitted:
                    self.patients_admitted.remove(patient.name)
                    print()
                    print(patient.name, "has been discharged from the hospital ")
                else:
                    print('No match found!')
        else:
            print('\nNo record found')

    def room_availibility(self,room):
        if len(self.patients_admitted) != room.num:
            return print('\nRooms are available')
        else:
            return print("\nSorry, rooms are not available")
        