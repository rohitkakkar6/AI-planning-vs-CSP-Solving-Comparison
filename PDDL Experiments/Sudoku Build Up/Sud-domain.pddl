(define (domain sudbuild)
  (:requirements :strips :typing :negative-preconditions)
  (:types
    digit cell row column subgrid - objects
  )

  (:predicates
    (BelongRow ?r - row ?c - cell) ;Indicates that cell ?c belongs to row ?r.
    (UsedRow ?r - row ?num - digit)
    (BelongColumn ?col - column ?c - cell)
    (UsedColumn ?col - column ?num - digit)
    (BelongSubgrid ?s - subgrid ?c - cell)
    (UsedSubgrid ?s - subgrid ?num - digit)
    (empty ?c - cell)
  )
  
  (:action place-digit
    :parameters (?num - digit ?c - cell ?r - row ?col - column ?s - subgrid)
    :precondition (and (empty ?c)
                       (BelongRow ?r ?c)
                       (BelongColumn ?col ?c)
                       (BelongSubgrid ?s ?c)
                       (not (UsedRow ?r ?num))
                       (not (UsedSubgrid ?s ?num))
                       (not (UsedColumn ?col ?num)))
    :effect (and (not (empty ?c))
                 (UsedColumn ?col ?num)
                 (UsedRow ?r ?num)
                 (UsedSubgrid ?s ?num))
  )
)