(define (problem sudoku9x9)
	(:domain sudbuild)
	(:objects
    	one two three four five six seven eight nine - digit
	    cell00 cell01 cell02 cell03 cell04 cell05 cell06 cell07 cell08 - cell
	    row0 - row
	    column0 column1 column2 column3 column4 column5 column6 column7 column8 - column
	    subgrid0 subgrid1 subgrid2 - subgrid
	)

	(:init
		;Cell connections
		(BelongRow row0 cell00) (BelongRow row0 cell01) (BelongRow row0 cell02) (BelongRow row0 cell03) (BelongRow row0 cell04) (BelongRow row0 cell05) (BelongRow row0 cell06) (BelongRow row0 cell07) (BelongRow row0 cell08)
        
        
		(BelongColumn column0 cell00)
		(BelongColumn column1 cell01)
		(BelongColumn column2 cell02)
		(BelongColumn column3 cell03)
		(BelongColumn column4 cell04)
		(BelongColumn column5 cell05)
		(BelongColumn column6 cell06)
		(BelongColumn column7 cell07)
		(BelongColumn column8 cell08)

		(BelongSubgrid subgrid0 cell00) (BelongSubgrid subgrid0 cell01) (BelongSubgrid subgrid0 cell02) 
		(BelongSubgrid subgrid1 cell03) (BelongSubgrid subgrid1 cell04) (BelongSubgrid subgrid1 cell05) 
		(BelongSubgrid subgrid2 cell06) (BelongSubgrid subgrid2 cell07) (BelongSubgrid subgrid2 cell08) 
	
		(UsedRow row0 six) (UsedColumn column1 six) (UsedSubgrid subgrid0 six)
		(UsedRow row0 two) (UsedColumn column5 two) (UsedSubgrid subgrid1 two)
		(UsedRow row0 seven) (UsedColumn column8 seven) (UsedSubgrid subgrid2 seven)
		
		
		(empty cell00)
		(empty cell02)
		(empty cell03)
		(empty cell04)
		(empty cell06)
		(empty cell07)
		
		
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
          (not (empty cell08)))
    )
)
