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
        (right-of cell01 cell00) (right-of cell02 cell01) (right-of cell03 cell02) (right-of cell04 cell03)
        (right-of cell11 cell10) (right-of cell12 cell11) (right-of cell13 cell12) (right-of cell14 cell13)
        (right-of cell21 cell20) (right-of cell22 cell21) (right-of cell23 cell22) (right-of cell24 cell23)
        (right-of cell31 cell30) (right-of cell32 cell31) (right-of cell33 cell32) (right-of cell34 cell33)
        (right-of cell41 cell40) (right-of cell42 cell41) (right-of cell43 cell42) (right-of cell44 cell43)

        (left-of cell00 cell01) (left-of cell01 cell02) (left-of cell02 cell03) (left-of cell03 cell04)
        (left-of cell10 cell11) (left-of cell11 cell12) (left-of cell12 cell13) (left-of cell13 cell14)
        (left-of cell20 cell21) (left-of cell21 cell22) (left-of cell22 cell23) (left-of cell23 cell24)
        (left-of cell30 cell31) (left-of cell31 cell32) (left-of cell32 cell33) (left-of cell33 cell34)
        (left-of cell40 cell41) (left-of cell41 cell42) (left-of cell42 cell43) (left-of cell43 cell44)
        
        (is-underneath cell10 cell00) (is-underneath cell20 cell10) (is-underneath cell30 cell20) (is-underneath cell40 cell30)
        (is-underneath cell11 cell01) (is-underneath cell21 cell11) (is-underneath cell31 cell21) (is-underneath cell41 cell31)
        (is-underneath cell12 cell02) (is-underneath cell22 cell12) (is-underneath cell32 cell22) (is-underneath cell42 cell32)
        (is-underneath cell13 cell03) (is-underneath cell23 cell13) (is-underneath cell33 cell23) (is-underneath cell43 cell33)
        (is-underneath cell14 cell04) (is-underneath cell24 cell14) (is-underneath cell34 cell24) (is-underneath cell44 cell34)

        (is-above cell00 cell10) (is-above cell10 cell20) (is-above cell20 cell30) (is-above cell30 cell40)
        (is-above cell01 cell11) (is-above cell11 cell21) (is-above cell21 cell31) (is-above cell31 cell41)
        (is-above cell02 cell12) (is-above cell12 cell22) (is-above cell22 cell32) (is-above cell32 cell42)
        (is-above cell03 cell13) (is-above cell13 cell23) (is-above cell23 cell33) (is-above cell33 cell43)
        (is-above cell04 cell14) (is-above cell14 cell24) (is-above cell24 cell34) (is-above cell34 cell44)

	)
	(:goal
        (and
        (at cell44)
		)
    )
)