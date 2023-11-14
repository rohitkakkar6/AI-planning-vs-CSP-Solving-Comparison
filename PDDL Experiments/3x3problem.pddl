(define (problem problem-3x3)
	(:domain sudokuv)
	(:objects
    	one two three four five six seven eight nine - digit
	    cell1 cell2 cell3 cell4 cell5 cell6 cell7 cell8 cell9 - cell
	)

	(:init
		(filled cell1 two)
		(not (is-available two))
		(filled cell2 four)
		(not (is-available four))
		(filled cell3 six)
		(not (is-available six))
		(filled cell4 eight)
		(not (is-available eight))

		(is-available one)
		(is-available three)
		(is-available five)
		(is-available seven)
		(is-available nine)
		
		(empty cell5)
		(empty cell6)
		(empty cell7)
		(empty cell8)
		(empty cell9)
	)
	(:goal
        (and
          (not (empty cell1))
          (not (empty cell2))
          (not (empty cell3))
          (not (empty cell4))
          (not (empty cell5))
          (not (empty cell6))
          (not (empty cell7))
          (not (empty cell8))
          (not (empty cell9))
		)
    )
)