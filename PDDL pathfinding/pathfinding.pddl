(define (domain pathfinding)
  (:requirements :strips :typing)
  (:types
    position
  )
  (:predicates
    (at ?p - position)  ; Agent is at position p
    (cell ?p - position)  ; Indicates a cell at position p
  )

  ; Define actions here
  (:action move-right
    :parameters (?from ?to - position)
    :precondition (and 
        (at ?from) 
        (cell ?to) 
    )
    :effect (and 
        (not (at ?from))
        (at ?to)
    )
  )
)

