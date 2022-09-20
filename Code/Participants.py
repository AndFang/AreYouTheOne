from random import randint

class Participant:
    def __init__(self, basic, information): # sets up contestant based on information
        self.name = basic[0]
        self.basic = basic
        self.information = information
        self._id = basic[4] # used for match
        self.known = []
        #self.known.append("ID: " + str(self._id))
    def learn(self): # every week new information on each participant is given
        if len(self.information) != 0:
            index = randint(0,len(self.information)-1)
            info = self.information[index]
            del self.information[index]
            self.known.append(info)
        else:
            raise IndexError("No more information")
    def given(self): # data that user is given from the start
        # [None, "22", "Jan 5th", "Female", 1]
        name = "Name: " + self.basic[0]
        age = "Age: " + self.basic[1]
        bd = "Birthday: " + self.basic[2]
        gender = "Gender: " + self.basic[3]
        ans = [name,age,bd,gender]
        for preference in self.basic[5:]:
            ans.append(preference)
        return ans
    def getData(self):
        return self.given() + self.known


