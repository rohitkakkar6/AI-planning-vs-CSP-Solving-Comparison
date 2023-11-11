(define (domain sudoku)
  (:requirements :strips :typing)

  (:types
    cell digit
  )

  (:constants
    cell11 cell12 cell13 cell21 cell22 cell23 cell31 cell32 cell33 - cell
    digit1 digit2 digit3 digit4 digit5 digit6 digit7 digit8 digit9 - digit
  )

  (:predicates
    (at ?c - cell ?d - digit)
    (empty ?c - cell)
    (filled ?c - cell ?d - digit)
    (distinct ?d1 - digit ?d2 - digit)
  )

  (:action place
    :parameters (?c - cell ?d - digit)
    :precondition (and (at ?c ?d) (empty ?c))
    :effect (and (filled ?c ?d) (not (empty ?c)))
  )
)
