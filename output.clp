(deffacts fapte
     (piesa B d 4)
     (white f 6)
     (white b 6)
     (white b 2)
     (white f 2)
)

;Regula pentru aflarea liniei si a coloanei
(defrule LinieSiColoana
   (piesa ? ?c ?l)
   =>
   (if (= (str-compare ?c a) 0)  ;daca piesa este pe coloana a
   then
     (assert (coloana 1))
   else
     (if (= (str-compare ?c b) 0)
     then
          (assert (coloana 2))
     else
          (if (= (str-compare ?c c) 0)
          then
               (assert (coloana 3))
          else
               (if (= (str-compare ?c d) 0)
               then
                    (assert (coloana 4))
               else
                    (if (= (str-compare ?c e) 0)
                    then
                         (assert (coloana 5))
                    else
                         (if (= (str-compare ?c f) 0)
                         then
                              (assert (coloana 6))
                         else
                              (if (= (str-compare ?c g) 0)
                              then
                              (assert (coloana 7))
                              else
                                   (if (= (str-compare ?c h) 0)
                                   then
                                   (assert (coloana 8))
                                   )
                              )
                         )
                    )
               )
          )
     )
   )
   (assert (linia ?l))
)

(defrule ColoanaBlack
     ?r <- (black ?c ?l)
     =>
     (if (= (str-compare ?c a) 0)  ;daca piesa este pe coloana a
     then
          (assert (blackc 1 ?l))
          (retract ?r)
     else
          (if (= (str-compare ?c b) 0)
          then
               (assert (blackc 2 ?l))
               (retract ?r)
          else
               (if (= (str-compare ?c c) 0)
               then
                    (assert (blackc 3 ?l))
                    (retract ?r)
               else
                    (if (= (str-compare ?c d) 0)
                    then
                         (assert (blackc 4 ?l))
                         (retract ?r)
                    else
                         (if (= (str-compare ?c e) 0)
                         then
                              (assert (blackc 5 ?l))
                              (retract ?r)
                         else
                              (if (= (str-compare ?c f) 0)
                              then
                                   (assert (blackc 6 ?l))
                                   (retract ?r)
                              else
                                   (if (= (str-compare ?c g) 0)
                                   then
                                   (assert (blackc 7 ?l))
                                   (retract ?r)
                                   else
                                        (if (= (str-compare ?c h) 0)
                                        then
                                        (assert (blackc 8 ?l))
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

(defrule ColoanaWhite
     ?r <- (white ?c ?l)
     =>
     (if (= (str-compare ?c a) 0)  ;daca piesa este pe coloana a
     then
          (assert (whitec 1 ?l))
          (retract ?r)
     else
          (if (= (str-compare ?c b) 0)
          then
               (assert (whitec 2 ?l))
               (retract ?r)
          else
               (if (= (str-compare ?c c) 0)
               then
                    (assert (whitec 3 ?l))
                    (retract ?r)
               else
                    (if (= (str-compare ?c d) 0)
                    then
                         (assert (whitec 4 ?l))
                         (retract ?r)
                    else
                         (if (= (str-compare ?c e) 0)
                         then
                              (assert (whitec 5 ?l))
                              (retract ?r)
                         else
                              (if (= (str-compare ?c f) 0)
                              then
                                   (assert (whitec 6 ?l))
                                   (retract ?r)
                              else
                                   (if (= (str-compare ?c g) 0)
                                   then
                                   (assert (whitec 7 ?l))
                                   (retract ?r)
                                   else
                                        (if (= (str-compare ?c h) 0)
                                        then
                                        (assert (whitec 8 ?l))
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


;Reguli pentru pion
(defrule Pion1
     ?r <- (piesa P ? ?)
     (coloana ?c)
     (linia ?l)
     =>
     (retract ?r)
     (assert (pion 1))
     (if (= ?l 2) ;daca pionul este pe linia 2, el poate face 2 mutari
     then
          (assert (mutarePosibila ?c (+ ?l 1)))
          (assert (mutarePosibila ?c (+ ?l 2)))
     else
          (assert (mutarePosibila ?c (+ ?l 1)))
     )
)


(defrule Pion2
     (pion ?)
     (coloana ?c)
     (linia ?l)
     ?r <- (blackc ?bc ?bl)
     =>
     (if (and (= ?l (- ?bl 1))
          (or (= ?c (- ?bc 1))
               (= ?c (+ ?bc 1))
               )
          )
     then (assert (mutarePosibila ?bc ?bl))
          (retract ?r)
     )
)


;Reguli pentru Rook
(defrule Rook1
     ?r <- (piesa R ? ?)
     (coloana ?c)
     (linia ?l)
     =>
     (retract ?r)
     (assert (rook 1))
)

(defrule Rook2
     (rook ?)
     (coloana ?c)
     (linia ?l)
     =>
     (bind ?a ?l)
     (while (< ?a 8)
          (assert (mutarePosibila ?c (+ ?a 1)))
          (bind ?a (+ ?a 1))
     )
     (bind ?a ?l)
     (while (> ?a 1)
          (assert (mutarePosibila ?c (- ?a 1)))
          (bind ?a (- ?a 1))
     )
     (bind ?a ?c)
     (while (> ?a 1)
          (assert (mutarePosibila (- ?a 1) ?l))
          (bind ?a (- ?a 1))
     )
     (bind ?a ?c)
     (while (< ?a 8)
          (assert (mutarePosibila (+ ?a 1) ?l))
          (bind ?a (+ ?a 1))
     )
)

(defrule Rook3 ; pentru Est
     (rook ?)
     (coloana ?c)
     (linia ?l)
     ?r <- (mutarePosibila ?mc ?l)
     (whitec ?wc ?l)
     =>
     (
          if (and (> ?mc ?wc) (> ?wc ?c))
          then (retract ?r)
     )
)

(defrule Rook4 ; pentru Vest
     (rook ?)
     (coloana ?c)
     (linia ?l)
     ?r <- (mutarePosibila ?mc ?l)
     (whitec ?wc ?l)
     =>
     (
          if (and (< ?mc ?wc) (< ?wc ?c))
          then (retract ?r)
     )
)

(defrule Rook5 ; pentru Nord
     (rook ?)
     (coloana ?c)
     (linia ?l)
     ?r <- (mutarePosibila ?c ?ml)
     (whitec ?c ?wl)
     =>
     (
          if (and (> ?ml ?wl) (> ?wl ?l))
          then (retract ?r)
     )
)

(defrule Rook6 ; pentru Sud
     (rook ?)
     (coloana ?c)
     (linia ?l)
     ?r <- (mutarePosibila ?c ?ml)
     (whitec ?c ?wl)
     =>
     (
          if (and (< ?ml ?wl) (< ?wl ?l))
          then (retract ?r)
     )
)



;reguli pentru Bishop
(defrule Bishop1
     ?r <- (piesa B ? ?)
     (coloana ?c)
     (linia ?l)
     =>
     (retract ?r)
     (assert (bishop 1))
)

(defrule Bishop2
     (bishop ?)
     (linia ?l)
     (coloana ?c)
     ?r <- (whitec ?wc ?wl)
     =>
     (bind ?a ?c)
     (bind ?b ?l)
     ;primul cadran , linie + 1, coloana + 1
     (while (and (and (< ?a 8) (< ?b 8)) (and (< ?a ?wc) (< ?b ?wl)))
          (bind ?a (+ ?a 1))
          (bind ?b (+ ?b 1))
          (assert (mutarePosibila ?a ?b))
     )
    
     (bind ?a ?c)
     (bind ?b ?l)
     ;al doilea cadran, linie + 1, coloana - 1
     (while (and (and (> ?a 1) (< ?b 8)) (and (> ?a ?wc) (< ?b ?wl)))
          (bind ?a (- ?a 1))
          (bind ?b (+ ?b 1))
          (assert (mutarePosibila ?a ?b))
     )
     
     (bind ?a ?c)
     (bind ?b ?l)
     ;al treilea cadran, linie - 1, coloana - 1
     (while (and (and (> ?a 1) (> ?b 1)) (and (> ?a ?wc) (> ?b ?wl)))
          (bind ?a (- ?a 1))
          (bind ?b (- ?b 1))
          (assert (mutarePosibila ?a ?b))
     )
     
     (bind ?a ?c)
     (bind ?b ?l)
     ;al patrulea cadran, linie - 1, coloana + 1
     (while (and (and (< ?a 8) (> ?b 1)) (and (< ?a ?wc) (> ?b ?wl)))
          (bind ?a (+ ?a 1))
          (bind ?b (- ?b 1))
          (assert (mutarePosibila ?a ?b))
     )
)



;reguli pentru Knight
(defrule Knight1
     ?r <- (piesa N ? ?)
     (coloana ?c)
     (linia ?l)
     =>
     (retract ?r)
     (assert (knight 1))
)

(defrule Knight2
     (knight ?)
     (coloana ?c)
     (linia ?l)
     =>
     ;cadran 1 : coloana + 2, linia + 1 ; coloana + 1, linia + 2
     (
          if (and (> 8 (+ ?c 2)) (> 8 (+ ?l 1)) )
          then (assert (mutarePosibila (+ ?c 2) (+ ?l 1)))
     )
     (
          if (and (> 8 (+ ?c 1)) (> 8 (+ ?l 2)) )
          then (assert (mutarePosibila (+ ?c 1) (+ ?l 2)))
     )
     ;cadran 2 : coloana - 2, linia + 1 ; coloana - 1, linia + 2
     (
          if (and (< 1 (- ?c 2)) (> 8 (+ ?l 1)) )
          then (assert (mutarePosibila (- ?c 2) (+ ?l 1)))
     )
     (
          if (and (< 1 (- ?c 1)) (> 8 (+ ?l 2)) )
          then (assert (mutarePosibila (- ?c 1) (+ ?l 2)))
     )
     ;cadran 3 : coloana - 2, linia - 1 ; coloana - 1, linia - 2
     (
          if (and (< 1 (- ?c 2)) (< 1 (- ?l 1)) )
          then (assert (mutarePosibila (- ?c 2) (- ?l 1)))
     )
     (
          if (and (< 1 (- ?c 1)) (< 1 (- ?l 2)) )
          then (assert (mutarePosibila (- ?c 1) (- ?l 2)))
     )
     ;cadran 4 : coloana + 2, linia - 1 ; coloana + 1, linia - 2
     (
          if (and (> 8 (+ ?c 2)) (< 1 (- ?l 1)) )
          then (assert (mutarePosibila (+ ?c 2) (- ?l 1)))
     )
     (
          if (and (> 8 (+ ?c 1)) (< 1 (- ?l 2)) )
          then (assert (mutarePosibila (+ ?c 1) (- ?l 2)))
     )

)


;reguli pentru Queen
;Queen este Bishop + Rook
(defrule Queen1
     ?r <- (piesa Q ? ?)
     (coloana ?c)
     (linia ?l)
     =>
     (retract ?r)
     (assert (queen 1))
     (assert (bishop 1))
     (assert (rook 1))
)


;reguli pentru King
(defrule King1
     ?r <- (piesa K ? ?)
     (coloana ?c)
     (linia ?l)
     =>
     (retract ?r)
     (assert (king 1))
)

(defrule King2 
     (king ?)
     (coloana ?c)
     (linia ?l)
     =>
     ;Nord -> coloana , linia + 1
     (
          if (> 8 (+ ?l 1)) 
          then (assert (mutarePosibila ?c (+ ?l 1)))
     )
     ;Nord-Est -> coloana + 1, linia + 1
     (
          if (and (> 8 (+ ?c 1)) (> 8 (+ ?l 1)) )
          then (assert (mutarePosibila (+ ?c 1) (+ ?l 1)))
     )
     ;Est -> coloana + 1, linia
     (
          if  (> 8 (+ ?c 1))
          then (assert (mutarePosibila (+ ?c 1) ?l))
     )
     ;Sud-Est -> coloana + 1, linia - 1
     (
          if (and (> 8 (+ ?c 1)) (< 1 (- ?l 1)) )
          then (assert (mutarePosibila (+ ?c 1) (- ?l 1)))
     )
     ;Sud -> coloana , linia - 1
     (
          if  (< 1 (- ?l 1)) 
          then (assert (mutarePosibila ?c (- ?l 1)))
     )
     ;Sud-Vest -> coloana - 1, linia - 1
     (
          if (and (< 1 (- ?c 1)) (< 1 (- ?l 1)) )
          then (assert (mutarePosibila (- ?c 1) (- ?l 1)))
     )
     ;Vest -> coloana - 1, linia
     (
          if (< 1 (- ?c 1)) 
          then (assert (mutarePosibila (- ?c 1) ?l))
     )
     ;Nord-Vest -> coloana - 1, linia + 1
     (
          if (and (< 1 (- ?c 1)) (> 8 (+ ?l 1)) )
          then (assert (mutarePosibila (- ?c 1) (+ ?l 1)))
     )

)

;reguli pentru piese albe aflate pe o mutare posibila
(defrule WhiteMutarePosibila1
     ?r <- (mutarePosibila ?c ?l)
     (whitec ?c ?l)
     =>
     (retract ?r)
)


;reguli pentru piese negre



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