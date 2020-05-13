(deffacts fapte
     (piesa B c 1)
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
   (if (= ?l 1)  ;daca piesa este pe linia 1
   then
     (assert (linia 1))
   else
     (if (= ?l 2)
     then
          (assert (linia 2))
     else
          (if (= ?l 3)
          then
               (assert (linia 3))
          else
               (if (= ?l 4)
               then
                    (assert (linia 4))
               else
                    (if (= ?l 5)
                    then
                         (assert (linia 5))
                    else
                         (if (= ?l 6)
                         then
                              (assert (linia 6))
                         else
                              (if (= ?l 7)
                              then
                              (assert (linia 7))
                              else
                                   (if (= ?l 8)
                                   then
                                   (assert (linia 8))
                                   )
                              )
                         )
                    )
               )
          )
     )
   )
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
     =>
     (bind ?a ?c)
     (bind ?b ?l)
     ;primul cadran , linie + 1, coloana + 1
     (while (and (< ?a 8) (< ?b 8))
          (bind ?a (+ ?a 1))
          (bind ?b (+ ?b 1))
          (assert (mutarePosibila ?a ?b))
     )
)


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