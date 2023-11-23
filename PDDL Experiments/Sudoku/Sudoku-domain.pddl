(define (domain sudoku)
  (:requirements :strips :typing)
  (:types
    digit cell row column subgrid
  )

  (:predicates
    (BelongRow ?r - row ?c - cell) ;Indicates that cell ?c belongs to row ?r.
    (UsedRow ?r - row ?num - digit)
    (BelongColumn ?col - column ?c - cell)
    (UsedColumn ?col - column ?num - digit)
    (BelongSubgrid ?s - subgrid ?c - cell)
    (UsedSubgrid ?s - subgrid ?num - digit)
    (empty ?c - cell)
    (filled ?c - cell ?d - digit)
  )
  
  (:action place-digit
    :parameters (?d - digit ?c - cell ?r - row ?col - column ?s - subgrid)
    :precondition (and (empty ?c)
                       (not (in-row ?c ?r))
                       (BelongColumn ?col ?c)
                       (BelongRow ?r ?c)
                       (BelongSubgrid ?s ?c)
                       (not (UsedRow ?r ?num))
                       (not (UsedSubgrid ?s ?num))
                       (not (UsedColumn ?col ?num)))
    :effect (and (filled ?c ?d)
                 (not (empty ?c))
                 (UsedColumn ?col ?num)
                 (UsedRow ?r ?num)
                 (UsedSubgrid ?s ?num))
  )
)

