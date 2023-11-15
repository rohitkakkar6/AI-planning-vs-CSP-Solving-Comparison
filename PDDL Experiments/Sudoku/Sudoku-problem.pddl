(define (problem sudoku9x9)
	(:domain sudoku)
	(:objects
    	one two three four five six seven eight nine - digit
	    cell00 cell01 cell02 cell03 cell04 cell05 cell06 cell07 cell08 - cell
		cell10 cell11 cell12 cell13 cell14 cell15 cell16 cell17 cell18 - cell
		cell20 cell21 cell22 cell23 cell24 cell25 cell26 cell27 cell28 - cell
	    cell30 cell31 cell32 cell43 cell34 cell35 cell36 cell37 cell38 - cell
	    cell40 cell41 cell42 cell43 cell44 cell45 cell46 cell47 cell48 - cell
	    cell50 cell51 cell52 cell53 cell54 cell55 cell56 cell57 cell58 - cell
	    cell60 cell61 cell62 cell63 cell64 cell65 cell66 cell67 cell68 - cell
	    cell70 cell71 cell72 cell73 cell74 cell75 cell76 cell77 cell78 - cell
	    cell80 cell81 cell82 cell83 cell84 cell85 cell86 cell87 cell88 - cell
	    row0 row1 row2 row3 row4 row5 row6 row6 row8 - row
	    column0 column1 column2 column3 column4 column5 column6 column7 column8 - column
	    subgrid0 subgrid1 subgrid2 subgrid3 subgrid4 subgrid5 subgrid6 subgrid7 subgrid8 - subgrid
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