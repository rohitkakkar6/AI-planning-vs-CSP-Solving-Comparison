(define (problem sudoku9x9)
	(:domain sudbuild)
	(:objects
    	one two three four five six seven eight nine - digit
	    cell00 cell01 cell02 cell03 cell04 cell05 cell06 cell07 cell08 - cell
	    cell10 cell11 cell12 cell13 cell14 cell15 cell16 cell17 cell18 - cell
	    cell20 cell21 cell22 cell23 cell24 cell25 cell26 cell27 cell28 - cell
	    row0 row1 row2 - row
	    column0 column1 column2 column3 column4 column5 column6 column7 column8 - column
	    subgrid0 subgrid1 subgrid2 - subgrid
	)

	(:init
		;Cell connections
		(BelongRow row0 cell00) (BelongRow row0 cell01) (BelongRow row0 cell02) (BelongRow row0 cell03) (BelongRow row0 cell04) (BelongRow row0 cell05) (BelongRow row0 cell06) (BelongRow row0 cell07) (BelongRow row0 cell08)
        (BelongRow row1 cell10) (BelongRow row1 cell11) (BelongRow row1 cell12) (BelongRow row1 cell13) (BelongRow row1 cell14) (BelongRow row1 cell15) (BelongRow row1 cell16) (BelongRow row1 cell17) (BelongRow row1 cell18)
        (BelongRow row2 cell20) (BelongRow row2 cell21) (BelongRow row2 cell22) (BelongRow row2 cell23) (BelongRow row2 cell24) (BelongRow row2 cell25) (BelongRow row2 cell26) (BelongRow row2 cell27) (BelongRow row2 cell28)
        
		(BelongColumn column0 cell00) (BelongColumn column0 cell10) (BelongColumn column0 cell20) 
		(BelongColumn column1 cell01) (BelongColumn column1 cell11) (BelongColumn column1 cell21) 
		(BelongColumn column2 cell02) (BelongColumn column2 cell12) (BelongColumn column2 cell22) 
		(BelongColumn column3 cell03) (BelongColumn column3 cell13) (BelongColumn column3 cell23) 
		(BelongColumn column4 cell04) (BelongColumn column4 cell14) (BelongColumn column4 cell24) 
		(BelongColumn column5 cell05) (BelongColumn column5 cell15) (BelongColumn column5 cell25) 
		(BelongColumn column6 cell06) (BelongColumn column6 cell16) (BelongColumn column6 cell26) 
		(BelongColumn column7 cell07) (BelongColumn column7 cell17) (BelongColumn column7 cell27) 
		(BelongColumn column8 cell08) (BelongColumn column8 cell18) (BelongColumn column8 cell28)

		(BelongSubgrid subgrid0 cell00) (BelongSubgrid subgrid0 cell01) (BelongSubgrid subgrid0 cell02) (BelongSubgrid subgrid0 cell10) (BelongSubgrid subgrid0 cell11) (BelongSubgrid subgrid0 cell12) (BelongSubgrid subgrid0 cell20) (BelongSubgrid subgrid0 cell21) (BelongSubgrid subgrid0 cell22)
		(BelongSubgrid subgrid1 cell03) (BelongSubgrid subgrid1 cell04) (BelongSubgrid subgrid1 cell05) (BelongSubgrid subgrid1 cell13) (BelongSubgrid subgrid1 cell14) (BelongSubgrid subgrid1 cell15) (BelongSubgrid subgrid1 cell23) (BelongSubgrid subgrid1 cell24) (BelongSubgrid subgrid1 cell25)
		(BelongSubgrid subgrid2 cell06) (BelongSubgrid subgrid2 cell07) (BelongSubgrid subgrid2 cell08) (BelongSubgrid subgrid2 cell16) (BelongSubgrid subgrid2 cell17) (BelongSubgrid subgrid2 cell18) (BelongSubgrid subgrid2 cell26) (BelongSubgrid subgrid2 cell27) (BelongSubgrid subgrid2 cell28)
	
		(UsedRow row0 six) (UsedColumn column1 six) (UsedSubgrid subgrid0 six)
		(UsedRow row0 two) (UsedColumn column5 two) (UsedSubgrid subgrid1 two)
		(UsedRow row0 seven) (UsedColumn column8 seven) (UsedSubgrid subgrid2 seven)
		
		(UsedRow row1 four) (UsedColumn column2 four) (UsedSubgrid subgrid0 four)
		(UsedRow row1 eight) (UsedColumn column7 eight) (UsedSubgrid subgrid2 eight)
		
		(UsedRow row2 one) (UsedColumn column0 one) (UsedSubgrid subgrid0 one)
		(UsedRow row2 five) (UsedColumn column4 five) (UsedSubgrid subgrid1 five)
		
		(empty cell00)
		(empty cell02)
		(empty cell03)
		(empty cell04)
		(empty cell06)
		(empty cell07)
		
		(empty cell10)
		(empty cell11)
		(empty cell13)
		(empty cell14)
		(empty cell15)
		(empty cell16)
		(empty cell18)
		
		(empty cell21)
		(empty cell22)
		(empty cell23)
		(empty cell25)
		(empty cell26)
		(empty cell27)
		(empty cell28)
		
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
		)
    )
)