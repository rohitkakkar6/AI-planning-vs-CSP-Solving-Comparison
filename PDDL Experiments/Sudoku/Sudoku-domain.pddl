(define (domain sudoku)
  (:requirements :strips ::typing)
  (:types
    digit cell
  )

  (:predicates
    (in-row ?digit ?row)
    (in-column ?digit ?column)
    (in-subgrid ?digit ?subgrid)
    (is-available ?digit)
    (empty ?cell)
    (filled ?cell ?digit)
  )
  
  (:action place-digit
    :parameters (?d - digit ?c - cell)
    :precondition (and (empty ?c) (not(in-row ?d ?c) (not(in-column ?d ?c)) (not(in-subgrid ?d ?c)))
    :effect (and (filled ?c ?d) (not (empty ?c)) (in-row ?d ?c) (in-column ?d ?c) (in-subgrid ?d ?c))
  )
)