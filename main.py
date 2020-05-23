import os
import clips
import tkinter as tk

game_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "game.txt"))
clips_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "generatorMutare.clp"))

p_black_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "black/p32.png"))
b_black_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "black/b32.png"))
k_black_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "black/k32.png"))
n_black_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "black/n32.png"))
q_black_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "black/q32.png"))
r_black_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "black/r32.png"))

p_white_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "white/p32.png"))
b_white_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "white/b32.png"))
k_white_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "white/k32.png"))
n_white_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "white/n32.png"))
q_white_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "white/q32.png"))
r_white_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "white/r32.png"))

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


with open(game_file, "r") as f:
    game_string = f.read()

moves_list = game_string.split(' ')
moves_list = [x for x in moves_list if x != '' and '\n' not in x]

#moves_list contine secventa de mutari din game.txt

from chessClass import Game
from interface import GameBoard

game = Game()
game.afisare_board()
""" if game.verificare_lista_mutari(moves_list) is False:
    print("Lista mutari contine caractere invalide")
    print("Introduceti mutari valide in fisier")
else: """
game.parsare_executare_mutari(moves_list)

env = clips.Environment()
env.clear()
env.load(clips_file)
env.reset()

root = tk.Tk()
board = GameBoard(root)
board.pack(side="top", fill="both", expand="true", padx=4, pady=4)

p_black = tk.PhotoImage(file = p_black_file)
b_black = tk.PhotoImage(file = b_black_file)
r_black = tk.PhotoImage(file = r_black_file)
k_black = tk.PhotoImage(file = k_black_file)
n_black = tk.PhotoImage(file = n_black_file)
q_black = tk.PhotoImage(file = q_black_file)

p_white = tk.PhotoImage(file = p_white_file)
b_white = tk.PhotoImage(file = b_white_file)
r_white = tk.PhotoImage(file = r_white_file)
k_white = tk.PhotoImage(file = k_white_file)
n_white = tk.PhotoImage(file = n_white_file)
q_white = tk.PhotoImage(file = q_white_file)

for i in range(8):
    for j in range(8):
        if game.board[i][j] == 'p':
            env.assert_string("(black " + map_from_number_to_char[j] + " " + str(i+1) + ")")
            board.addpiece("piece " + str(i)+str(j), p_black, abs(7-i), j)
        if game.board[i][j] == 'q':
            env.assert_string("(black " + map_from_number_to_char[j]+ " " + str(i+1) + ")")
            board.addpiece("piece " + str(i)+str(j), q_black, abs(7-i), j)
        if game.board[i][j] == 'r':
            env.assert_string("(black " + map_from_number_to_char[j]+ " " + str(i+1) + ")")
            board.addpiece("piece " + str(i)+str(j), r_black, abs(7-i), j)
        if game.board[i][j] == 'n':
            env.assert_string("(black " + map_from_number_to_char[j]+ " " + str(i+1) + ")")
            board.addpiece("piece " + str(i)+str(j), n_black, abs(7-i), j)
        if game.board[i][j] == 'k':
            env.assert_string("(black " + map_from_number_to_char[j]+ " " + str(i+1) + ")")
            board.addpiece("piece " + str(i)+str(j), k_black, abs(7-i), j)
        if game.board[i][j] == 'b':
            env.assert_string("(black " + map_from_number_to_char[j]+ " " + str(i+1) + ")")
            board.addpiece("piece " + str(i)+str(j), b_black, abs(7-i), j)
        
        if game.board[i][j] == 'P':
            env.assert_string("(white " + map_from_number_to_char[j]+ " " + str(i+1) + ")")
            board.addpiece("piece " + str(i)+str(j), p_white, abs(7-i), j)
        if game.board[i][j] == 'Q':
            env.assert_string("(white " + map_from_number_to_char[j]+ " " + str(i+1) + ")")
            board.addpiece("piece " + str(i)+str(j), q_white, abs(7-i), j)
        if game.board[i][j] == 'R':
            env.assert_string("(white " + map_from_number_to_char[j]+ " " + str(i+1) + ")")
            board.addpiece("piece " + str(i)+str(j), r_white, abs(7-i), j)
        if game.board[i][j] == 'N':
            env.assert_string("(white " + map_from_number_to_char[j]+ " " + str(i+1) + ")")
            board.addpiece("piece " + str(i)+str(j), n_white, abs(7-i), j)
        if game.board[i][j] == 'K':
            env.assert_string("(white " + map_from_number_to_char[j]+ " " + str(i+1) + ")")
            board.addpiece("piece " + str(i)+str(j), k_white, abs(7-i), j)
        if game.board[i][j] == 'B':
            env.assert_string("(white " + map_from_number_to_char[j]+ " " + str(i+1) + ")")
            board.addpiece("piece " + str(i)+str(j), b_white, abs(7-i), j)
        
env.assert_string("(piesa P f 2)")
#env.assert_string("(piesa P a 2)")
#env.assert_string("(piesa R f 1)")
#env.assert_string("(piesa K g 1)")
#env.assert_string("(piesa N c 3)")
#env.assert_string("(piesa Q g 7)")
#env.assert_string("(piesa B c 4)")

env.run()

rule1 = """
;regula pentru transformare coloana int -> string
(defrule ColoanaMutare
     ?r <- (mutarePosibila ?c ?l)
     =>
     (if (= ?c 1)  ;daca piesa este pe coloana a
     then
          (assert (posibilaMutare a ?l))
          (retract ?r)
     else
          (if (= ?c 2)
          then
               (assert (posibilaMutare b ?l))
               (retract ?r)
          else
               (if (= ?c 3)
               then
                    (assert (posibilaMutare c ?l))
                    (retract ?r)
               else
                    (if (= ?c 4)
                    then
                         (assert (posibilaMutare d ?l))
                         (retract ?r)
                    else
                         (if (= ?c 5)
                         then
                              (assert (posibilaMutare e ?l))
                              (retract ?r)
                         else
                              (if (= ?c 6)
                              then
                                   (assert (posibilaMutare f ?l))
                                   (retract ?r)
                              else
                                   (if (= ?c 7)
                                   then
                                   (assert (posibilaMutare g ?l))
                                   (retract ?r)
                                   else
                                        (if (= ?c 8)
                                        then
                                        (assert (posibilaMutare h ?l))
                                        (retract ?r)
                                        )
                                   )
                              )
                         )
                    )
               )
          )
     )
)
"""

env.build(rule1)

env.run()

for fact in env.facts():
    if fact.template == env.find_template("posibilaMutare"):
        print(fact)

root.mainloop()


