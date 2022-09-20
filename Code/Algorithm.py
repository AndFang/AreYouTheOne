from data import playerdata as pd
from random import randint, shuffle
from Participants import Participant

class Algorithm:
    def __init__(self, dif): # dif is based on the difficulty choosen, a harder difficulty will give less preferences early on making the matching harder
        names = ['Alex', 'Cameron', 'Casey', 'Drew', 'Frederick', 'Jackie', 'Jaime', 'Jessie', # list of possible names
                 'Maple', 'Morgan', 'Peyton', 'Riley', 'Ryan', 'Sydney', 'Taylor', 'Zane']
        self.save = ['Alex', 'Cameron', 'Casey', 'Drew', 'Frederick', 'Jackie', 'Jaime', 'Jessie', # list of possible names
                 'Maple', 'Morgan', 'Peyton', 'Riley', 'Ryan', 'Sydney', 'Taylor', 'Zane']
        i = 0
        while len(names) != 0: # randomly assigns names to each set of data
            index = randint(0,len(names)-1)
            name = names[index]
            pd[i][0][0] = name
            i += 1
            del names[index]
        #for i in range(16):
        #    pd[i][0][0] = self.save[i]
        c1 = Participant(pd[0][0] + pd[0][1][:dif], pd[0][2] + pd[0][1][dif:])
        c2 = Participant(pd[1][0] + pd[1][1][:dif], pd[1][2] + pd[1][1][dif:])
        c3 = Participant(pd[2][0] + pd[2][1][:dif], pd[2][2] + pd[2][1][dif:])
        c4 = Participant(pd[3][0] + pd[3][1][:dif], pd[3][2] + pd[3][1][dif:])
        c5 = Participant(pd[4][0] + pd[4][1][:dif], pd[4][2] + pd[4][1][dif:])
        c6 = Participant(pd[5][0] + pd[5][1][:dif], pd[5][2] + pd[5][1][dif:])
        c7 = Participant(pd[6][0] + pd[6][1][:dif], pd[6][2] + pd[6][1][dif:])
        c8 = Participant(pd[7][0] + pd[7][1][:dif], pd[7][2] + pd[7][1][dif:])
        c9 = Participant(pd[8][0] + pd[8][1][:dif], pd[8][2] + pd[8][1][dif:])
        c10 = Participant(pd[9][0] + pd[9][1][:dif], pd[9][2] + pd[9][1][dif:])
        c11 = Participant(pd[10][0] + pd[10][1][:dif], pd[10][2] + pd[10][1][dif:])
        c12 = Participant(pd[11][0] + pd[11][1][:dif], pd[11][2] + pd[11][1][dif:])
        c13 = Participant(pd[12][0] + pd[12][1][:dif], pd[12][2] + pd[12][1][dif:])
        c14 = Participant(pd[13][0] + pd[13][1][:dif], pd[13][2] + pd[13][1][dif:])
        c15 = Participant(pd[14][0] + pd[14][1][:dif], pd[14][2] + pd[14][1][dif:])
        c16 = Participant(pd[15][0] + pd[15][1][:dif], pd[15][2] + pd[15][1][dif:])

        self.players = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16]
        shuffle(self.players)

        self.weeks = 0
    def perfectPair(self,c1,c2):
        return c1._id + c2._id == 17
    def perfectMatches(self,pairs):
        ans = 0
        for pair in pairs:
            if self.getName(pair[0])._id + self.getName(pair[1])._id == 17:
                ans += 1
        return ans
    def getName(self,name):
        for player in self.players:
            if player.name == name:
                return player

