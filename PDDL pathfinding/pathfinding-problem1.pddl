(define (problem problem-pathfinding)
	(:domain pathfinding)
	(:objects
	    cell00 cell01 - position
	)

	(:init
        (at cell00)
        (right-of cell01 cell00)
	)
	(:goal
        (and
        (at cell01)
		)
    )
)