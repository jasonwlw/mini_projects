from random import shuffle

class BlackJack:
    def __init__(self,num_players):
        self.num_players = num_players
        self.waste_deck = []
        ### Keeps track of where we are in the deck
        self.count = 0
        self.num_cards = [i for i in range(52)]
        self.card_symb = ['As','Ac','Ad','Ah','2s','2c','2d','2h','3s','3c','3d','3h','4s','4c','4d','4h',\
             '5s','5c','5d','5h','6s','6c','6d','6h','7s','7c','7d','7h','8s','8c','8d','8h',\
             '9s','9c','9d','9h','10s','10c','10d','10h','Js','Jc','Jd','Jh','Qs','Qc','Qd','Qh',\
             'Ks','Kc','Kd','Kh']
        value_arr = []
        for i in range(1,14):
            for j in range(4):
                val = i
                if i > 10:
                    val = 10
                value_arr.append(val)

        self.card_value = dict(zip(self.card_symb,value_arr))
        print(self.card_value)
        self.player_cards = self.Initialize_Players()
        self.Shuffle_Deck()
        self.cards = self.Create_Card_Dictionary()
        print(self.cards)

    def Initialize_Players(self):
        player_cards = []
        for i in range(self.num_players):
            player_cards.append([])
        return player_cards

    def Shuffle_Deck(self):
        '''
        Shuffles the deck using random module
        :return: shuffled deck
        '''
        shuffle(self.card_symb)
        return 0

    def Create_Card_Dictionary(self):
        '''
        Maps numbers to card symbols above
        :param shuffled: shuffled card symbols
        :return: dictionary attaching 0-51 to shuffled deck
        '''
        return dict(zip(self.num_cards,self.card_symb))

    def Deal(self):
        for i in range(self.num_players):
            self.player_cards[i].append(self.cards[i])
            self.count += 1
            if self.Check_Deck():
                self.count = 0
        for i in range(self.num_players):
            self.player_cards[i].append(self.cards[i+self.num_players])
            self.count += 1
            if self.Check_Deck():
                self.count = 0

    def Player_Hit(self,i):
        print(self.player_cards[i])
        if i == 0:
            #self.Count_Update(self.player_cards[i][0],self.player_cards[i][1])
            pass
        else:
            pass
            #self.Count_Update(self.player_cards[i][1])
        hit = input("Would you like to hit?")
        bust = False
        while hit == 'y' and not bust:
            self.count += 1
            if self.Check_Deck():
                self.count = 0
            self.player_cards[i].append(self.cards[self.count])
            print(self.player_cards[i])
            bust = self.Check_Bust(i)
            if not bust:
                hit = input("Would you like to hit?")
        return 0

    def Check_Bust(self,i):
        summ = 0
        for card in self.player_cards[i]:
            summ += self.card_value[card]
        if summ > 21:
            print("BUSTED")
            return True
        else:
            return False

    '''
    def Rotate_Cards(self,count):
        rem = 52 % count
        self.waste_deck.append(self.cards[0:count])
        self.cards[0:count] = self.cards[count:2*count]
        for j in range(2*count,len(cards)):
            self.cards[j-count] = self.cards[j]
        self.cards[len(cards) - count:len(cards)] = self.waste_deck[0:count]
    '''

    def Check_Deck(self):
        ### Check deck to see how much is left
        return bool(len(self.cards) % self.count)

    def Play_Round(self):
        #self.Place_Bets()
        print("Next Deal")
        self.Deal()
        for i in range(self.num_players):
            self.Player_Hit(i)

game = BlackJack(2)
game.Play_Round()