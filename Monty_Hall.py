import random

class Monty_Hall:
    def __init__(self,autoplay = False,num_runs = 1,switch = True):
        self.autoplay = autoplay
        self.num_runs = 1
        if self.autoplay:
            self.num_runs = num_runs
            self.switch = switch
        self.num_doors = 3
        self.doors = ['car','goat','goat']

    def Shuffler(self):
        random.shuffle(self.doors)

    def Auto_Pick_Door(self):
        return random.randint(0,2)

    def Reveal(self,door):
        if self.doors[door] != 'car':
            if self.doors[door - 1] != 'car':
                print("Not the car: ",door - 1)
                if door - 2 < 0:
                    door2 = door + 1
                else:
                    door2 = door - 2
                return door2
            else:
                print("Not the car: ", door - 2)
                if door - 1 < 0:
                    door2 = door + 2
                else:
                    door2 = door - 1
                return door2
        else:
            print("Not the car: ", door - 1)
            if door - 2 < 0:
                door2 = door + 1
            else:
                door2 = door - 2
            return door2

    def Result(self,door):
        if self.doors[door] == 'car':
            print("You Win!!")
            return True
        else:
            print("You lose...")
            return False

    def Play(self):
        count = 0
        wins = 0
        if self.autoplay:
            for i in range(self.num_runs):
                self.Shuffler()
                door = self.Auto_Pick_Door()
                door2 = self.Reveal(door)
                if self.switch:
                    win = self.Result(door2)
                else:
                    win = self.Result(door)
                if win:
                    count += 1
                    wins += 1
                else:
                    count += 1
            print("Win percentage: ",wins/count)
        else:
            playing = True
            count = 0
            wins = 0
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
                    count += 1
                    wins += 1
                else:
                    count += 1
                keep_play = input("Would you like to keep playing? (y/n): ")
                if keep_play == 'y':
                    playing = True
                else:
                    playing = False
            print("Win percentage: ",wins/count)

my_game = Monty_Hall(autoplay=True,num_runs=100000)
my_game.Play()