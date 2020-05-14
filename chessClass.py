#Avem lista cu mutarile executate de la inceputul partidei
"""
8   r   n   b   q   k   b   n   r
7   p   p   p   p   p   p   p   p       BLACK - litere mici
6
5
4
3
2   P   P   P   P   P   P   P   P       WHITE - litere mari
1   R   N   B   Q   K   B   N   R
    -----------------------------
    A   B   C   D   E   F   G   H

"""


map_from_char_to_number = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7
}

map_from_number_to_char = {
    0 : "a",
    1 : "b",
    2 : "c",
    3 : "d",
    4 : "e",
    5 : "f",
    6 : "g",
    7 : "h"
}

lista_caractere_posibile_mutare = ['a','b','c','d','e','f','g','h','r','n','k','q','O','-','x','+','#','0','1','2','3','4','5','6','7','8']

class Game:

    def __init__(self):
        self.turn = 'WHITE'  #WHITE or BLACK, WHITE e primul

        self.board = [[0] * 8 for _ in range(8)] #matrice de 8x8

        #WHITE PIECES
        self.board[1 -1][map_from_char_to_number['a']] = "R"
        self.board[1 -1][map_from_char_to_number['b']] = "N"
        self.board[1 -1][map_from_char_to_number['c']] = "B"
        self.board[1 -1][map_from_char_to_number['d']] = "Q"
        self.board[1 -1][map_from_char_to_number['e']] = "K"
        self.board[1 -1][map_from_char_to_number['f']] = "B"
        self.board[1 -1][map_from_char_to_number['g']] = "N"
        self.board[1 -1][map_from_char_to_number['h']] = "R"
        for i in range(8):
            self.board[2 -1][i] = "P"
        
        #BLACK PIECES
        self.board[8 -1][map_from_char_to_number['a']] = "r"
        self.board[8 -1][map_from_char_to_number['b']] = "n"
        self.board[8 -1][map_from_char_to_number['c']] = "b"
        self.board[8 -1][map_from_char_to_number['d']] = "q"
        self.board[8 -1][map_from_char_to_number['e']] = "k"
        self.board[8 -1][map_from_char_to_number['f']] = "b"
        self.board[8 -1][map_from_char_to_number['g']] = "n"
        self.board[8 -1][map_from_char_to_number['h']] = "r"
        for i in range(8):
            self.board[7 -1][i] = "p"


    def afisare_board(self):
        print("\n")
        for i in range(7,-1,-1):
            for j in range(8):
                if self.board[i][j] == 0:
                    print('•', end=" ")
                else:
                    print(self.board[i][j], end=" ")
            print(end='\n')
        print("\n")


    def verificare_lista_mutari(self, lista_mutari):
        for mutare in lista_mutari:
            if len(mutare) < 2 or len(mutare) > 7:
                return False
            for c in mutare:
                if c.lower() not in lista_caractere_posibile_mutare:
                    return False
        return True


    def move_king_or_queen(self, piesa, linie, coloana):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == piesa:
                    self.board[i][j] = 0
                    break
            
        self.board[linie][map_from_char_to_number[coloana]] = piesa


    def move_rook(self, piesa, linie, coloana):
        #cautam pe linie ROOK
        for j in range(8):
            if self.board[linie][j] == piesa:
                self.board[linie][j] = 0
                break
        
        #cautam pe coloana
        for i in range(8):
            if self.board[i][map_from_char_to_number[coloana]] == piesa:
                self.board[i][map_from_char_to_number[coloana]] = 0
                break
        
        #mutam piesa
        self.board[linie][map_from_char_to_number[coloana]] = piesa


    def move_bishop(self, piesa, linie, coloana):
        #cautam in cele 4 cadrane BISHOP

        #cadran 1
        try:
            for k in range(8):
                if self.board[linie + k][map_from_char_to_number[coloana] + k] == piesa:
                    self.board[linie + k][map_from_char_to_number[coloana] + k] = 0
        except:
            pass

        #cadran 2
        try:
            for k in range(8):
                if self.board[linie + k][map_from_char_to_number[coloana] - k] == piesa:
                    self.board[linie + k][map_from_char_to_number[coloana] - k] = 0
        except:
            pass

        #cadran 3
        try:
            for k in range(8):
                if self.board[linie - k][map_from_char_to_number[coloana] - k] == piesa:
                    self.board[linie - k][map_from_char_to_number[coloana] - k] = 0
        except:
            pass

        #cadran 4
        try:
            for k in range(8):
                if self.board[linie - k][map_from_char_to_number[coloana] + k] == piesa:
                    self.board[linie - k][map_from_char_to_number[coloana] + k] = 0
        except:
            pass

        #mutam piesa
        self.board[linie][map_from_char_to_number[coloana]] = piesa


    def move_knight(self, piesa, linie, coloana):
        #cautam in cele 8 posibile pozitii KNIGHT

        try:
            if self.board[linie + 2][map_from_char_to_number[coloana] - 1] == piesa:
                self.board[linie + 2][map_from_char_to_number[coloana] - 1] = 0
        except:
            pass

        try:
            if self.board[linie + 2][map_from_char_to_number[coloana] + 1] == piesa:
                self.board[linie + 2][map_from_char_to_number[coloana] + 1] = 0
        except:
            pass

        try:
            if self.board[linie + 1][map_from_char_to_number[coloana] - 2] == piesa:
                self.board[linie + 1][map_from_char_to_number[coloana] - 2] = 0
        except:
            pass

        try:
            if self.board[linie + 1][map_from_char_to_number[coloana] + 2] == piesa:
                self.board[linie + 1][map_from_char_to_number[coloana] + 2] = 0
        except:
            pass

        try:
            if self.board[linie - 1][map_from_char_to_number[coloana] - 2] == piesa:
                self.board[linie - 1][map_from_char_to_number[coloana] - 2] = 0
        except:
            pass

        try:
            if self.board[linie - 1][map_from_char_to_number[coloana] + 2] == piesa:
                self.board[linie - 1][map_from_char_to_number[coloana] + 2] = 0
        except:
            pass

        try:
            if self.board[linie - 2][map_from_char_to_number[coloana] - 1] == piesa:
                self.board[linie - 2][map_from_char_to_number[coloana] - 1] = 0
        except:
            pass

        try:
            if self.board[linie - 2][map_from_char_to_number[coloana] + 1] == piesa:
                self.board[linie - 2][map_from_char_to_number[coloana] + 1] = 0
        except:
            pass

        #mutam piesa
        self.board[linie][map_from_char_to_number[coloana]] = piesa


    def executare_mutare_len_2(self, mutare):
        temp_coloana = mutare[0]
        temp_linie = int(mutare[1]) - 1 # -1 pentru indexarea din matrice

        if self.turn == "WHITE":
            temp_piesa = 'P'  # pentru ca e pion alb, dupa ce il mutam, il cautam pe i-1 si i-2
            temp_linie_1 = temp_linie - 1
            temp_linie_2 = temp_linie - 2
            self.turn = "BLACK"
        else:
            temp_piesa = 'p'  # pentru ca e pion negru, dupa ce il mutam, il cautam pe i+1 si i+2
            temp_linie_1 = temp_linie + 1
            temp_linie_2 = temp_linie + 2
            self.turn = "WHITE"
        
        #verificam daca locul este gol
        if self.board[temp_linie][map_from_char_to_number[temp_coloana]] != 0:
            print(mutare + " este invalida. EXIT")
            return False

        #mutam pionul pe loc
        self.board[temp_linie][map_from_char_to_number[temp_coloana]] = temp_piesa
        #cautam pionul pe temp_linie_1 si temp_linie_2
        if self.board[temp_linie_1][map_from_char_to_number[temp_coloana]] == temp_piesa:
            self.board[temp_linie_1][map_from_char_to_number[temp_coloana]] = 0
        else:
            self.board[temp_linie_2][map_from_char_to_number[temp_coloana]] = 0
        

    def executare_mutare_len_3(self, mutare):
        #Avem 3 posibile tipuri de mutari
        #Nd2 -> piesa muta la pozitie
        #d7+ -> pion muta la pozitie si e sah
        #O-O -> castling mic

        if mutare[0] == 'O':
            #castling mic
            #WHITE inseamna linia 1
            #BLACK inseamna linia 8
            #KING se muta pe coloana G
            #ROOK se muta pe coloana F

            if self.turn == "WHITE":
                temp_linie = 0
                temp_rook = "R"
                temp_king = "K"
                self.turn = "BLACK"
            else:
                temp_linie = 7
                temp_rook = "r"
                temp_king = 'k'
                self.turn = "WHITE"
            
            self.board[temp_linie][map_from_char_to_number['e']] = 0
            self.board[temp_linie][map_from_char_to_number['h']] = 0
            self.board[temp_linie][map_from_char_to_number['g']] = temp_king
            self.board[temp_linie][map_from_char_to_number['f']] = temp_rook

        elif mutare[0] == 'R' or mutare[0] == 'N' or mutare[0] == 'B' or mutare[0] == 'Q' or mutare[0] == 'K':
            #piesa se muta la pozitia indicata
            if self.turn == "WHITE":
                temp_piesa = mutare[0]
                self.turn = "BLACK"
            else:
                temp_piesa = mutare[0].lower()
                self.turn = "WHITE"
            temp_coloana = mutare[1]
            temp_linie = int(mutare[2]) - 1

            if mutare[0] == 'K' or mutare[0] == 'Q':
                self.move_king_or_queen(temp_piesa, temp_linie, temp_coloana)
            
            elif mutare[0] == 'R':
                self.move_rook(temp_piesa, temp_linie, temp_coloana)
            
            elif mutare[0] == 'B':
                self.move_bishop(temp_piesa, temp_linie, temp_coloana)

            elif mutare[0] == 'N':
                self.move_knight(temp_piesa, temp_linie, temp_coloana)

        else:
            #pion muta la pozitie si e sah
            if self.executare_mutare_len_2(mutare) is False:
                return
            

    def executare_mutare_len_4(self, mutare):
        #Avem 6 tipuri de mutari posibile

        #bxc6 -> pion de pe coloana b captureaza piesa de la c6
        #Bxg2 -> Bishop captureaza piesa de la g2
        #Qc8+ -> Queen muta la c8 si e sah
        #c1=Q -> pion muta la c1 si este schimbat cu Queen
        #Rfe1 -> Rook de pe coloana f se muta la e1
        #N4f6 -> Knight muta de la linia 4 la f6

        if '+' in mutare:
            #piesa muta la pozitie si e sah
            temp_mutare = mutare[0] + mutare[1] + mutare[2]

            self.executare_mutare_len_3(temp_mutare)

        elif '=' in mutare:
            #pion de la pozitie este schimbat cu piesa

            #mutam pionul la pozitie
            temp_mutare = mutare[0] + mutare[1]
            self.executare_mutare_len_2(temp_mutare) #s-a schimbat si turn-ul

            #Apoi schimbam pionul cu piesa
            temp_coloana = mutare[0]
            temp_linie = int(mutare[1]) - 1

            if self.turn == "WHITE": #s-a schimbat turn-ul cu 5 linii de cod mai sus
                temp_piesa = mutare[3].lower()
            else:
                temp_piesa = mutare[3]
            
            self.board[temp_linie][map_from_char_to_number[temp_coloana]] = temp_piesa


        elif 'x' in mutare:
            #piesa captureaza alta piesa la pozitie


            if mutare[0] == mutare[0].lower(): #pion de pe coloana mutare[0] captureaza piesa de la pozitie
                
                temp_coloana = mutare[2]
                temp_linie = int(mutare[3]) - 1

                if self.turn == "WHITE": #pionul este inainte de capturare la board[linie - 1][mutare[0]]
                    self.board[temp_linie -1][map_from_char_to_number[mutare[0]]] = 0
                    self.board[temp_linie][map_from_char_to_number[temp_coloana]] = 'P'
                    self.turn = "BLACK"

                else: #pionul este inainte de capturare la board[linie + 1][mutare[0]]
                    self.board[temp_linie +1][map_from_char_to_number[mutare[0]]] = 0
                    self.board[temp_linie][map_from_char_to_number[temp_coloana]] = 'p'
                    self.turn = "WHITE"

            else: #piesa mutare[0] captureaza piesa de la pozitie
                
                temp_mutare = mutare[0] + mutare[2] + mutare[3]

                self.executare_mutare_len_3(temp_mutare)


        else:
            #Piesa mutare[0] de la linia sau coloana mutare[1] se muta la pozitie

            if self.turn == "WHITE":
                temp_piesa = mutare[0]
                self.turn = "BLACK"
            else:
                temp_piesa = mutare[0].lower()
                self.turn = "WHITE"

            temp_coloana = mutare[2]
            temp_linie = int(mutare[3]) - 1

            if mutare[1] in ['a','b','c','d','e','f','g','h']:
                coloana_curenta = mutare[1]
                for i in range(8):
                    if self.board[i][map_from_char_to_number[coloana_curenta]] == temp_piesa:
                        self.board[i][map_from_char_to_number[coloana_curenta]] = 0
                        break
            else:
                linia_curenta = int(mutare[1]) - 1
                for j in range(8):
                    if self.board[linia_curenta][map_from_char_to_number[j]] == temp_piesa:
                        self.board[linia_curenta][map_from_char_to_number[j]] = 0
                        break
            
            self.board[temp_linie][map_from_char_to_number[temp_coloana]] = temp_piesa


    def executare_mutare_len_5(self, mutare):
        #Avem 6 tipuri de mutari posibile

        #O-O-O -> castling mare
        #f1=Q+ -> pion muta la f1, schimba cu Queen si e sah
        #Q7c7+ -> Queen de pe linia 7 muta la c7 si e sah
        #Qbh2+ -> Queen de la coloana b muta la h2 si e sah
        #gxh2+ -> pion de la coloana g captureaza piesa de la h2 si e sah
        #Rexe4 -> Rook de pe coloana e captureaza piesa la e4

        if '+' in mutare:
            temp_mutare = mutare[0] + mutare[1] + mutare[2] + mutare[3]
            self.executare_mutare_len_4(temp_mutare)
        
        elif 'O' == mutare[0]:
            #castling mare
            #King la coloana c
            #Rook la coloana d

            if self.turn == "WHITE":
                temp_linie = 0
                temp_rook = "R"
                temp_king = "K"
                self.turn = "BLACK"
            else:
                temp_linie = 7
                temp_rook = "r"
                temp_king = 'k'
                self.turn = "WHITE"
            
            self.board[temp_linie][map_from_char_to_number['e']] = 0
            self.board[temp_linie][map_from_char_to_number['a']] = 0
            self.board[temp_linie][map_from_char_to_number['c']] = temp_king
            self.board[temp_linie][map_from_char_to_number['d']] = temp_rook

        else: #Piesa mutare[0] de pe coloana/linia mutare[1] captureaza piesa de la mutare[3] si mutare[4]

            temp_mutare = mutare[0] + mutare[1] + mutare[3] + mutare[4]
            self.executare_mutare_len_4(temp_mutare)


    def executare_mutare_len_6(self, mutare):
        #Qbxb3+ -> Queen de pe coloana b captureaza piesa la b3 si e sah
        #N7xe5+ -> Knight de pe linia 7 captureaza piesa la e5 si e sah
        #O-O-O+ -> casteling mare si e sah
        #fxg8=Q -> pion de pe coloana f captureaza piesa la g8 si schimba cu Queen
        #Rd2xd7 -> Rook pe pozitia d2 captureaza piesa de pe pozitia d7

        if '+' in mutare:
            temp_mutare = mutare[0] + mutare[1] + mutare[2] + mutare[3] + mutare[4]
            self.executare_mutare_len_5(temp_mutare)
        
        elif '=' in mutare:#pion de pe coloana mutare[0] captureaza piesa de la pozitie si se schimba cu mutare[5]
            
            if self.turn == "WHITE": #pionul este initial pe linia 7
                temp_piesa = mutare[5]
                temp_coloana = mutare[2]
                coloana_curenta = mutare[0]
                self.board[7 -1][map_from_char_to_number[coloana_curenta]] = 0
                self.board[8 -1][map_from_char_to_number[temp_coloana]] = temp_piesa
                self.turn = "BLACK"
            else: #pionul este initial pe linia 2
                temp_piesa = mutare[5].lower()
                temp_coloana = mutare[2]
                coloana_curenta = mutare[0]
                self.board[2 -1][map_from_char_to_number[coloana_curenta]] = 0
                self.board[1 -1][map_from_char_to_number[temp_coloana]] = temp_piesa
                self.turn = "WHITE"
        else: #Piesa mutare[0] captureaza piesa de pe pozitie pe pozitie
            
            if self.turn == "WHITE":
                temp_piesa = mutare[0]
                self.turn = "BLACK"
            else:
                temp_piesa = mutare[0].lower()
                self.turn = "WHITE"
            
            coloana_curenta = mutare[1]
            linia_curenta = int(mutare[2]) - 1
            temp_coloana = mutare[4]
            temp_linie = int(mutare[5]) - 1

            self.board[linia_curenta][map_from_char_to_number[coloana_curenta]] = 0
            self.board[temp_linie][map_from_char_to_number[temp_coloana]] = temp_piesa


    def executare_mutare_len_7(self, mutare):
        #Avem 2 cazuri posibile

        #dxc8=Q+ -> pion de pe coloana d captureaza piesa la c8, schimba cu Queen si e sah
        #Re6xe2+ -> Rook de la e6 captureaza piesa la e2 si e sah

        temp_mutare = mutare[0] + mutare[1] + mutare[2] + mutare[3] + mutare[4] + mutare[5]
        self.executare_mutare_len_6(temp_mutare)


    def parsare_executare_mutari(self, lista_mutari):
        #primul turn este WHITE
        for mutare in lista_mutari:

            if len(mutare) == 2:    # o singura posibila mutare : pion la pozitia indicata de mutare
                if self.executare_mutare_len_2(mutare) is False:
                    return

            if len(mutare) == 3:
                if self.executare_mutare_len_3(mutare) is False:
                    return
            
            if len(mutare) == 4:
                if self.executare_mutare_len_4(mutare) is False:
                    return
            
            if len(mutare) == 5:
                if self.executare_mutare_len_5(mutare) is False:
                    return

            if len(mutare) == 6:
                if self.executare_mutare_len_6(mutare) is False:
                    return
            
            if len(mutare) == 7:
                if self.executare_mutare_len_7(mutare) is False:
                    return
            

            self.afisare_board()
                
                
