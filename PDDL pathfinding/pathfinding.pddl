(define (domain pathfinding)
  (:requirements :strips :typing)
  (:types
    position
  )
  (:predicates
    (at ?p - position)  ; Agent is at position p
    (cell ?p - position)  ; Indicates a cell at position p
    (right-of ?p1 ?p2 - position) ;Defines adjacency rules
  )

  ; Define actions here
  (:action move-right
    :parameters (?from ?to - position)
    :precondition (and 
        (at ?from)
        (right-of ?to ?from)
    )
    :effect (and
        (not (at ?from))
        (at ?to)
    )
  )
)

