(define (problem problem-pathfinding)
	(:domain pathfinding)
	(:objects
	    cell00 cell01 cell02 cell03 cell04 - position
	    cell10 cell11 cell12 cell13 cell14 - position
	    cell20 cell21 cell22 cell23 cell24 - position
	    cell30 cell31 cell32 cell33 cell34 - position
	    cell40 cell41 cell42 cell43 cell44 - position
	)

	(:init
        (at cell02)
        (right-of cell01 cell00) (right-of cell02 cell01)
        (left-of cell00 cell01) (left-of cell01 cell02)
        (is-underneath cell10 cell00)
	)
	(:goal
        (and
        (at cell10)
		)
    )
)