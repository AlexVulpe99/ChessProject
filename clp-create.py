import os
import clips

env = clips.Environment()
env.clear()
env.load("output.clp")
env.reset()
env.run()

""" env.clear()
env.load('lab2.clp')
env.reset()
#env.run()
env.assert_string("(pdnp y)")
env.assert_string("(rlf n)")
env.assert_string("(punrec y)")

env.run()
"""

for fact in env.facts():
    print(fact) 


#rule1 = """
#(defrule cpc
#    (and (pdnp y)
#         (rlf n)
#         (punrec y)
#    )
#    =>
#    (printout t "Check the power cable  ")
#)
#"""

#env.build(rule1)

#env.save("output.clp")

""" env.clear()
env.load("output.clp")
env.reset()
env.assert_string("(pdnp y)")
env.assert_string("(rlf n)")
env.assert_string("(punrec y)")

env.run() """

#assert (d 4 black R)
#assert (e 5 white Q)
#assert (piesa P e 2)

# (= (str-compare e e) 0)

""" (defrule closed-valves
   (temp high)
   (valve ?v closed)
   =>
   (if (= ?v 6)
      then
      (printout t "The special valve " ?v " is closed!" crlf)
      (assert (perform special operation))
      else
      (printout t "Valve " ?v " is normally closed" crlf))) """
