(define (domain sudokuv)
  (:requirements :strips :typing)
  (:types
    digit cell
  )

  (:predicates
    (is-available ?d)
    (empty ?cell)
    (filled ?cell ?digit)
  )
  
  (:action place-digit
    :parameters (?d - digit ?c - cell)
    :precondition (and (empty ?c) (is-available ?d))
    :effect (and (filled ?c ?d) (not (empty ?c)) (not(is-available ?d)))
  )
)

