; sudoku-problem.pddl

(define (problem sudoku-3x3)
  (:domain sudoku)

  (:init
    (at cell11 digit1)
    (at cell12 digit2)
    (at cell13 digit3)
    (at cell21 digit4)
    (at cell22 digit5)
    (at cell23 digit6)
    (at cell31 digit7)
    (at cell32 digit8)
    (at cell33 digit9)
    
    (empty cell11)
    (empty cell12)
    (empty cell13)
    (empty cell21)
    (empty cell22)
    (empty cell23)
    (empty cell31)
    (empty cell32)
    (empty cell33)
  )

  (:goal
    (and
      (filled cell11 digit1)
      (filled cell12 digit2)
      (filled cell13 digit3)
      (filled cell21 digit4)
      (filled cell22 digit5)
      (filled cell23 digit6)
      (filled cell31 digit7)
      (filled cell32 digit8)
      (filled cell33 digit9)
    )
  ) 
)


