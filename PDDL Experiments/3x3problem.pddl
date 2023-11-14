(define (problem problem-3x3)
	(:domain sudokuv)
	(:objects
    	one two three four five six seven eight nine - digit
	    cell00 cell01 cell02 - cell
		cell10 cell11 cell12 - cell
		cell20 cell21 cell22 - cell
	)

	(:init
		(filled cell00 two)
		(not (is-available two))
		(filled cell01 four)
		(not (is-available four))
		(filled cell02 six)
		(not (is-available six))
		(filled cell10 eight)
		(not (is-available eight))

		(is-available one)
		(is-available three)
		(is-available five)
		(is-available seven)
		(is-available nine)
		
		(empty cell11)
		(empty cell12)
		(empty cell20)
		(empty cell21)
		(empty cell22)
	)
	(:goal
        (and
          (not (empty cell00))
          (not (empty cell01))
          (not (empty cell02))
          (not (empty cell10))
          (not (empty cell11))
          (not (empty cell12))
          (not (empty cell20))
          (not (empty cell21))
          (not (empty cell22))
		)
    )
)