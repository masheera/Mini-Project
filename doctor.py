class Doctor:
    doctor_list = []

    def addDoctors(self,name,degree):
        self.name = name
        self.degree = degree
        self.doctor_list.append(self.name)

    def displayDoc(self):
        for i in self.doctor_list:
            print(i)