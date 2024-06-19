class Sem3:
                                                #pass -we can use this if there is nothing to show
    def __init__(self,name) :
        self.name=name
    def duties(self):
        print('Attendance')

classrep=Sem3('Sivanand')
placementrep=Sem3('Merrin')
print(classrep.name,placementrep.name)
classrep.duties()