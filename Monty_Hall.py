import random

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt


class Monty_Hall:
    def __init__(self,autoplay = False,num_runs = 1,switch = True, num_doors = 3, num_cars = 1):
        self.autoplay = autoplay
        self.num_runs = 1
        if self.autoplay:
            self.num_runs = num_runs
            self.switch = switch
        self.count = 0
        self.wins = 0
        self.num_doors = num_doors
        self.num_cars = num_cars
        self.doors = self.Initialize_Doors(num_doors,num_cars)

    def Initialize_Doors(self,num_doors,num_cars):
        """
        Initialize 'doors' list; with 'num_cars' cars and 'num_doors'-'num_cars' goats
        i.e. if num_cars=3 & num_doors = 6, 'doors' will be ['car','car','car','goat','goat','goat']
        :param num_doors: total number of doors in Monty Hall Problem
        :param num_cars: number of cars (must be less than num_doors; should be less than or equal to num_doors - 2)
        :return doors: a list of what's behind each door, car or goat
        """
        doors = []
        for j in range(num_cars):
            doors.append('car')
        for i in range(num_doors-num_cars):
            doors.append('goat')
        return doors

    def Shuffler(self):
        """
        Randomly shuffles the 'doors' list; because the 'doors' list is just in order, we need to make the door setup random
        """
        random.shuffle(self.doors)

    def Auto_Pick_Door(self):
        """
        When play is auto, we will randomly select one of the doors
        :return index of 'doors' list
        """
        return random.randint(0,self.num_doors - 1)

    def Get_Cars_Goats(self):
        """
        After shuffling, get indices where 'doors' is "car" or "goat"
        :return indices where 'doors' is "car", indices where 'doors' is "goat:
        """
        car_inds = []
        goat_inds = []
        for i in range(self.num_doors):
            if self.doors[i] == 'car':
                car_inds.append(i)
            else:
                goat_inds.append(i)
        return car_inds,goat_inds

    def Reveal(self,door):
        """
        When Monty reveals a random door with a goat, return the list of possible doors
        to switch to.
        :return list of possible doors to switch  
        """
        # Note; calls to index below are linear, for large lists may need to switch
        cars,goats = self.Get_Cars_Goats()
        if door in cars:
            goats.pop(random.randint(0,len(goats)-1))
            cars.pop(cars.index(door))
            return cars + goats
        else:
            goats.pop(goats.index(door))
            goats.pop(random.randint(0,len(goats)-1))
            return cars + goats

    def Result(self,door):
        if self.doors[door] == 'car':
            #print("You Win!!")
            return True
        else:
            #print("You lose...")
            return False

    def Play(self):
        if self.autoplay:
            for i in range(self.num_runs):
                if not i % 1000:
                    print("Run: ",i)
                self.Shuffler()
                door = self.Auto_Pick_Door()
                doors_to_switch = self.Reveal(door)
                if self.switch:
                    win = self.Result(doors_to_switch[random.randint(0,len(doors_to_switch)-1)])
                else:
                    win = self.Result(door)
                if win:
                    self.count += 1
                    self.wins += 1
                else:
                    self.count += 1
            print("Win percentage: ",float(self.wins)/self.count)
            return float(self.wins)/self.count
        else:
            playing = True
            while playing:
                self.Shuffler()
                door = int(input("Welcome to the Monty Hall Problem! Please pick a door, (0,1,2): "))
                door2 = self.Reveal(door)
                switch = input("Would you like to switch doors? (y/n)")
                if switch == 'y':
                    win = self.Result(door2)
                else:
                    win = self.Result(door)
                if win:
                    self.count += 1
                    self.wins += 1
                else:
                    self.count += 1
                keep_play = input("Would you like to keep playing? (y/n): ")
                if keep_play == 'y':
                    playing = True
                else:
                    playing = False
            print("Win percentage: ",self.wins/self.count)
doors = []
cars = []
win_percent = []
for num_doors in range(3,26):
    for num_cars in range(1,num_doors - 1):
        doors.append(num_doors)
        cars.append(num_cars)
        my_game = Monty_Hall(autoplay=True,num_runs=10000,num_doors=num_doors,num_cars=num_cars)
        win_percent.append(my_game.Play())
df = []
for i in range(len(doors)):
    df.append([doors[i],cars[i],win_percent[i]])
df = np.asarray(df)
df = pd.DataFrame(df, columns = ['Doors','Cars','Win %'])
print(df)
df.to_csv('./Monty_Hall_10000runs_doors3-50.csv')
#plt.scatter(cars,doors,c=win_percent)
#plt.show()
