(define (problem problem-pathfinding)
	(:domain pathfinding)
	(:objects
	    cell00 cell01 cell02 - position
	)

	(:init
        (at cell02)
        (right-of cell01 cell00)
        (right-of cell02 cell01)
        (left-of cell00 cell01)
        (left-of cell01 cell02)
	)
	(:goal
        (and
        (at cell00)
		)
    )
)