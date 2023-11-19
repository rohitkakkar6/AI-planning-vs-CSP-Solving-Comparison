(define (domain sudoku)
  (:requirements :strips :typing)
  (:types
    digit cell
  )

  (:predicates
    (in-row ?d - digit ?c - cell)
    (in-column ?d - digit ?c - cell)
    (in-subgrid ?d - digit ?c - cell)
    (empty ?c - cell)
    (filled ?c - cell ?d - digit)
  )
  
  (:action place-digit
    :parameters (?d - digit ?c - cell)
    :precondition (and (empty ?c)
                       (not (in-row ?d ?c))
                       (not (in-column ?d ?c))
                       (not (in-subgrid ?d ?c)))
    :effect (and (filled ?c ?d)
                 (not (empty ?c))
                 (in-row ?d ?c)
                 (in-column ?d ?c)
                 (in-subgrid ?d ?c))
  )
)
