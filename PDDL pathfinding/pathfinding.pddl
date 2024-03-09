(define (domain pathfinding)
  (:requirements :strips :typing)
  (:types
    position
  )
  (:predicates
    (at ?p - position)  ; Agent is at position p
    (right-of ?p1 ?p2 - position);Defines adjacency rules
    (left-of ?p1 ?p2 - position)  ; Define left adjacent rule
    (is-underneath ?p1 ?p2 - position)  ; Define underneath adjacency rule
    (is-above ?p1 ?p2 - position) ; Define above adjacency rule
  )

  ; Actions
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

  (:action move-left
    :parameters (?from ?to - position)
    :precondition (and 
        (at ?from)
        (left-of ?to ?from)
    )
    :effect (and
        (not (at ?from))
        (at ?to)
    )
  )

  (:action move-down
    :parameters (?from ?to - position)
    :precondition (and 
        (at ?from)
        (is-underneath ?to ?from)
    )
    :effect (and
        (not (at ?from))
        (at ?to)
    )
  )

  (:action move-up
    :parameters (?from ?to - position)
    :precondition (and 
        (at ?from)
        (is-above ?to ?from)
    )
    :effect (and
        (not (at ?from))
        (at ?to)
    )
  )
)

