(define (problem sudoku9x9)
	(:domain sudoku)
	(:objects
    	one two three four five six seven eight nine - digit
	    cell00 cell01 cell02 cell03 cell04 cell05 cell06 cell07 cell08 - cell
		cell10 cell11 cell12 cell13 cell14 cell15 cell16 cell17 cell18 - cell
		cell20 cell21 cell22 cell23 cell24 cell25 cell26 cell27 cell28 - cell
	    cell30 cell31 cell32 cell33 cell34 cell35 cell36 cell37 cell38 - cell
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
		(BelongColumn ?col ?c)
		


		(filled cell00 nine)
		(filled cell20 two)
		(filled cell01 one)
		(filled cell11 eight)
		(filled cell12 seven)
		
		(empty cell01)
		(empty cell21)
		(empty cell02)
		(empty cell22)
		
		(filled cell40 seven)
		(filled cell50 eight)
		(filled cell32 five)
		
		(empty cell30)
		(empty cell31)
		(empty cell41)
		(empty cell51)
		(empty cell42)
		(empty cell52)
		
		(filled cell61 seven)
		(filled cell71 six)
		
		(empty cell60)
		(empty cell70)
		(empty cell80)
		(empty cell81)
		(empty cell62)
		(empty cell72)
		(empty cell82)
		
		(filled cell03 seven)
		(filled cell13 five)
		(filled cell04 four)
		(filled cell24 six)
		(filled cell15 one)
		
		(empty cell23)
		(empty cell14)
		(empty cell05)
		(empty cell25)
		
		(filled cell53 six)
		(filled cell45 four)
		(filled cell55 five)
		
		(empty cell33)
		(empty cell43)
		(empty cell34)
		(empty cell44)
		(empty cell54)
		
		(filled cell73 eight)
		(filled cell84 four)
		(filled cell64 one)
		(filled cell74 five)
		(filled cell84 seven)
		(filled cell65 three)
		(filled cell75 nine)
		(filled cell85 six)
		
		(empty cell63)
		
		(filled cell16 two)
		(filled cell07 six)
		(filled cell27 nine)
		
		(empty cell06)
		(empty cell26)
		(empty cell17)
		(empty cell08)
		(empty cell18)
		(empty cell28)
		
		(filled cell57 seven)
		(filled cell38 nine)
		(filled cell48 eight)
		(filled cell58 four)
		
		(empty cell36)
		(empty cell46)
		(empty cell56)
		(empty cell37)
		(empty cell47)
		
		(filled cell66 five)
		(filled cell86 nine)
		(filled cell67 eight)
		(filled cell77 three)
		(filled cell78 seven)
		
		(empty cell76)
		(empty cell87)
		(empty cell68)
		(empty cell88)
		
	)
	(:goal
        (and
          (not (empty cell00))
          (not (empty cell01))
          (not (empty cell02))
          (not (empty cell03))
          (not (empty cell04))
          (not (empty cell05))
          (not (empty cell06))
          (not (empty cell07))
          (not (empty cell08))
          (not (empty cell10))
          (not (empty cell11))
          (not (empty cell12))
          (not (empty cell13))
          (not (empty cell14))
          (not (empty cell15))
          (not (empty cell16))
          (not (empty cell17))
          (not (empty cell18))
          (not (empty cell20))
          (not (empty cell21))
          (not (empty cell22))
          (not (empty cell23))
          (not (empty cell24))
          (not (empty cell25))
          (not (empty cell26))
          (not (empty cell27))
          (not (empty cell28))
          (not (empty cell30))
          (not (empty cell31))
          (not (empty cell32))
          (not (empty cell33))
          (not (empty cell34))
          (not (empty cell35))
          (not (empty cell36))
          (not (empty cell37))
          (not (empty cell38))
          (not (empty cell40))
          (not (empty cell41))
          (not (empty cell42))
          (not (empty cell43))
          (not (empty cell44))
          (not (empty cell45))
          (not (empty cell46))
          (not (empty cell47))
          (not (empty cell48))
          (not (empty cell50))
          (not (empty cell51))
          (not (empty cell52))
          (not (empty cell53))
          (not (empty cell54))
          (not (empty cell55))
          (not (empty cell56))
          (not (empty cell57))
          (not (empty cell58))
          (not (empty cell60))
          (not (empty cell61))
          (not (empty cell62))
          (not (empty cell63))
          (not (empty cell64))
          (not (empty cell65))
          (not (empty cell66))
          (not (empty cell67))
          (not (empty cell68))
          (not (empty cell70))
          (not (empty cell71))
          (not (empty cell72))
          (not (empty cell73))
          (not (empty cell74))
          (not (empty cell75))
          (not (empty cell76))
          (not (empty cell77))
          (not (empty cell78))
          (not (empty cell80))
          (not (empty cell81))
          (not (empty cell82))
          (not (empty cell83))
          (not (empty cell84))
          (not (empty cell85))
          (not (empty cell86))
          (not (empty cell87))
          (not (empty cell88))
		)
    )
)