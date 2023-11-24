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
	    row0 row1 row2 row3 row4 row5 row6 row7 row8 - row
	    column0 column1 column2 column3 column4 column5 column6 column7 column8 - column
	    subgrid0 subgrid1 subgrid2 subgrid3 subgrid4 subgrid5 subgrid6 subgrid7 subgrid8 - subgrid
	)

	(:init
		;Cell connections
		(BelongRow row0 cell00) (BelongRow row0 cell01) (BelongRow row0 cell02) (BelongRow row0 cell03) (BelongRow row0 cell04) (BelongRow row0 cell05) (BelongRow row0 cell06) (BelongRow row0 cell07) (BelongRow row0 cell08)
		(BelongRow row1 cell10) (BelongRow row1 cell11) (BelongRow row1 cell12) (BelongRow row1 cell13) (BelongRow row1 cell14) (BelongRow row1 cell15) (BelongRow row1 cell16) (BelongRow row1 cell17) (BelongRow row1 cell18)
		(BelongRow row2 cell20) (BelongRow row2 cell21) (BelongRow row2 cell22) (BelongRow row2 cell23) (BelongRow row2 cell24) (BelongRow row2 cell25) (BelongRow row2 cell26) (BelongRow row2 cell27) (BelongRow row2 cell28)
		(BelongRow row3 cell30) (BelongRow row3 cell31) (BelongRow row3 cell32) (BelongRow row3 cell33) (BelongRow row3 cell34) (BelongRow row3 cell35) (BelongRow row3 cell36) (BelongRow row3 cell37) (BelongRow row3 cell38)
		(BelongRow row4 cell40) (BelongRow row4 cell41) (BelongRow row4 cell42) (BelongRow row4 cell43) (BelongRow row4 cell44) (BelongRow row4 cell45) (BelongRow row4 cell46) (BelongRow row4 cell47) (BelongRow row4 cell48)
		(BelongRow row5 cell50) (BelongRow row5 cell51) (BelongRow row5 cell52) (BelongRow row5 cell53) (BelongRow row5 cell54) (BelongRow row5 cell55) (BelongRow row5 cell56) (BelongRow row5 cell57) (BelongRow row5 cell58)
		(BelongRow row6 cell60) (BelongRow row6 cell61) (BelongRow row6 cell62) (BelongRow row6 cell63) (BelongRow row6 cell64) (BelongRow row6 cell65) (BelongRow row6 cell66) (BelongRow row6 cell67) (BelongRow row6 cell68)
		(BelongRow row7 cell70) (BelongRow row7 cell71) (BelongRow row7 cell72) (BelongRow row7 cell73) (BelongRow row7 cell74) (BelongRow row7 cell75) (BelongRow row7 cell76) (BelongRow row7 cell77) (BelongRow row7 cell78)
		(BelongRow row8 cell80) (BelongRow row8 cell81) (BelongRow row8 cell82) (BelongRow row8 cell83) (BelongRow row8 cell84) (BelongRow row8 cell85) (BelongRow row8 cell86) (BelongRow row8 cell87) (BelongRow row8 cell88)

		(BelongColumn column0 cell00) (BelongColumn column0 cell10) (BelongColumn column0 cell20) (BelongColumn column0 cell30) (BelongColumn column0 cell40) (BelongColumn column0 cell50) (BelongColumn column0 cell60) (BelongColumn column0 cell70) (BelongColumn column0 cell80)
		(BelongColumn column1 cell01) (BelongColumn column1 cell11) (BelongColumn column1 cell21) (BelongColumn column1 cell31) (BelongColumn column1 cell41) (BelongColumn column1 cell51) (BelongColumn column1 cell61) (BelongColumn column1 cell71) (BelongColumn column1 cell81)
		(BelongColumn column2 cell02) (BelongColumn column2 cell12) (BelongColumn column2 cell22) (BelongColumn column2 cell32) (BelongColumn column2 cell42) (BelongColumn column2 cell52) (BelongColumn column2 cell62) (BelongColumn column2 cell72) (BelongColumn column2 cell82)
		(BelongColumn column3 cell03) (BelongColumn column3 cell13) (BelongColumn column3 cell23) (BelongColumn column3 cell33) (BelongColumn column3 cell43) (BelongColumn column3 cell53) (BelongColumn column3 cell63) (BelongColumn column3 cell73) (BelongColumn column3 cell83)
		(BelongColumn column4 cell04) (BelongColumn column4 cell14) (BelongColumn column4 cell24) (BelongColumn column4 cell34) (BelongColumn column4 cell44) (BelongColumn column4 cell54) (BelongColumn column4 cell64) (BelongColumn column4 cell74) (BelongColumn column4 cell84)
		(BelongColumn column5 cell05) (BelongColumn column5 cell15) (BelongColumn column5 cell25) (BelongColumn column5 cell35) (BelongColumn column5 cell45) (BelongColumn column5 cell55) (BelongColumn column5 cell65) (BelongColumn column5 cell75) (BelongColumn column5 cell85)
		(BelongColumn column6 cell06) (BelongColumn column6 cell16) (BelongColumn column6 cell26) (BelongColumn column6 cell36) (BelongColumn column6 cell46) (BelongColumn column6 cell56) (BelongColumn column6 cell66) (BelongColumn column6 cell76) (BelongColumn column6 cell86)
		(BelongColumn column7 cell07) (BelongColumn column7 cell17) (BelongColumn column7 cell27) (BelongColumn column7 cell37) (BelongColumn column7 cell47) (BelongColumn column7 cell57) (BelongColumn column7 cell67) (BelongColumn column7 cell77) (BelongColumn column7 cell87)
		(BelongColumn column8 cell08) (BelongColumn column8 cell18) (BelongColumn column8 cell28) (BelongColumn column8 cell38) (BelongColumn column8 cell48) (BelongColumn column8 cell58) (BelongColumn column8 cell68) (BelongColumn column8 cell78) (BelongColumn column8 cell88)

		(BelongSubgrid subgrid0 cell00) (BelongSubgrid subgrid0 cell01) (BelongSubgrid subgrid0 cell02) (BelongSubgrid subgrid0 cell10) (BelongSubgrid subgrid0 cell11) (BelongSubgrid subgrid0 cell12) (BelongSubgrid subgrid0 cell20) (BelongSubgrid subgrid0 cell21) (BelongSubgrid subgrid0 cell22)
		(BelongSubgrid subgrid1 cell03) (BelongSubgrid subgrid1 cell04) (BelongSubgrid subgrid1 cell05) (BelongSubgrid subgrid1 cell13) (BelongSubgrid subgrid1 cell14) (BelongSubgrid subgrid1 cell15) (BelongSubgrid subgrid1 cell23) (BelongSubgrid subgrid1 cell24) (BelongSubgrid subgrid1 cell25)
		(BelongSubgrid subgrid2 cell06) (BelongSubgrid subgrid2 cell07) (BelongSubgrid subgrid2 cell08) (BelongSubgrid subgrid2 cell16) (BelongSubgrid subgrid2 cell17) (BelongSubgrid subgrid2 cell18) (BelongSubgrid subgrid2 cell26) (BelongSubgrid subgrid2 cell27) (BelongSubgrid subgrid2 cell28)
		(BelongSubgrid subgrid3 cell30) (BelongSubgrid subgrid3 cell31) (BelongSubgrid subgrid3 cell32) (BelongSubgrid subgrid3 cell40) (BelongSubgrid subgrid3 cell41) (BelongSubgrid subgrid3 cell42) (BelongSubgrid subgrid3 cell50) (BelongSubgrid subgrid3 cell51) (BelongSubgrid subgrid3 cell52)
		(BelongSubgrid subgrid4 cell33) (BelongSubgrid subgrid4 cell34) (BelongSubgrid subgrid4 cell35) (BelongSubgrid subgrid4 cell43) (BelongSubgrid subgrid4 cell44) (BelongSubgrid subgrid4 cell45) (BelongSubgrid subgrid4 cell53) (BelongSubgrid subgrid4 cell54) (BelongSubgrid subgrid4 cell55)
		(BelongSubgrid subgrid5 cell36) (BelongSubgrid subgrid5 cell37) (BelongSubgrid subgrid5 cell38) (BelongSubgrid subgrid5 cell46) (BelongSubgrid subgrid5 cell47) (BelongSubgrid subgrid5 cell48) (BelongSubgrid subgrid5 cell56) (BelongSubgrid subgrid5 cell57) (BelongSubgrid subgrid5 cell58)
		(BelongSubgrid subgrid6 cell60) (BelongSubgrid subgrid6 cell61) (BelongSubgrid subgrid6 cell62) (BelongSubgrid subgrid6 cell70) (BelongSubgrid subgrid6 cell71) (BelongSubgrid subgrid6 cell72) (BelongSubgrid subgrid6 cell80) (BelongSubgrid subgrid6 cell81) (BelongSubgrid subgrid6 cell82)
		(BelongSubgrid subgrid7 cell63) (BelongSubgrid subgrid7 cell64) (BelongSubgrid subgrid7 cell65) (BelongSubgrid subgrid7 cell73) (BelongSubgrid subgrid7 cell74) (BelongSubgrid subgrid7 cell75) (BelongSubgrid subgrid7 cell83) (BelongSubgrid subgrid7 cell84) (BelongSubgrid subgrid7 cell85)
		(BelongSubgrid subgrid8 cell66) (BelongSubgrid subgrid8 cell67) (BelongSubgrid subgrid8 cell68) (BelongSubgrid subgrid8 cell76) (BelongSubgrid subgrid8 cell77) (BelongSubgrid subgrid8 cell78) (BelongSubgrid subgrid8 cell86) (BelongSubgrid subgrid8 cell87) (BelongSubgrid subgrid8 cell88)


		; top left subgrid
		(filled cell00 nine) (UsedRow row0 nine) (UsedColumn column0 nine) (UsedSubgrid subgrid0 nine)
		(filled cell21 seven) (UsedRow row2 seven) (UsedColumn column1 seven) (UsedSubgrid subgrid0 seven)

		(empty cell01)
		(empty cell02)
		(empty cell10)
		(empty cell11)
		(empty cell12)
		(empty cell20)
		(empty cell22)
		
		; top middle subgrid
		(filled cell04 one) (UsedRow row0 one) (UsedColumn column4 one) (UsedSubgrid subgrid1 one)
		(filled cell14 six) (UsedRow row1 six) (UsedColumn column4 six) (UsedSubgrid subgrid1 six)
		(filled cell23 nine) (UsedRow row2 nine) (UsedColumn column3 nine) (UsedSubgrid subgrid1 nine)
		(filled cell25 eight) (UsedRow row2 eight) (UsedColumn column5 eight) (UsedSubgrid subgrid1 eight)

		(empty cell03)
		(empty cell05)
		(empty cell13)
		(empty cell15)
		(empty cell24)

		; top right subgrid
		(filled cell07 seven) (UsedRow row0 seven) (UsedColumn column7 seven) (UsedSubgrid subgrid2 seven)
		(filled cell17 two) (UsedRow row1 two) (UsedColumn column7 two) (UsedSubgrid subgrid2 two)
		(filled cell18 four) (UsedRow row1 four) (UsedColumn column8 four) (UsedSubgrid subgrid2 four)

		(empty cell06)
		(empty cell08)
		(empty cell16)
		(empty cell26)
		(empty cell27)
		(empty cell28)

		; left middle subgrid
		(filled cell32 six) (UsedRow row3 six) (UsedColumn column2 six) (UsedSubgrid subgrid3 six)
		(filled cell40 two) (UsedRow row4 two) (UsedColumn column0 two) (UsedSubgrid subgrid3 two)
		(filled cell41 one) (UsedRow row4 one) (UsedColumn column1 one) (UsedSubgrid subgrid3 one)
		(filled cell42 eight) (UsedRow row4 eight) (UsedColumn column2 eight) (UsedSubgrid subgrid3 eight)
		(filled cell51 five) (UsedRow row5 five) (UsedColumn column1 five) (UsedSubgrid subgrid3 five)
		(filled cell52 three) (UsedRow row5 three) (UsedColumn column2 three) (UsedSubgrid subgrid3 three)

		(empty cell30)
		(empty cell31)
		(empty cell50)

		; middle subgrid
		(filled cell53 two) (UsedRow row5 two) (UsedColumn column3 two) (UsedSubgrid subgrid4 two)
		(filled cell55 four) (UsedRow row5 four) (UsedColumn column5 four) (UsedSubgrid subgrid4 four)

		(empty cell33)
		(empty cell34)
		(empty cell35)
		(empty cell43)
		(empty cell44)
		(empty cell45)
		(empty cell54)

		; right middle subgrid
		(filled cell56 six) (UsedRow row5 six) (UsedColumn column6 six) (UsedSubgrid subgrid5 six)

		(empty cell36)
		(empty cell37)
		(empty cell38)
		(empty cell46)
		(empty cell47)
		(empty cell48)
		(empty cell57)
		(empty cell58)

		; bottom left subgrid
		(filled cell80 five) (UsedRow row8 five) (UsedColumn column0 five) (UsedSubgrid subgrid6 five)

		(empty cell60)
		(empty cell61)
		(empty cell62)
		(empty cell70)
		(empty cell71)
		(empty cell72)
		(empty cell81)
		(empty cell82)

		; bottom middle subgrid
		(filled cell63 five) (UsedRow row6 five) (UsedColumn column3 five) (UsedSubgrid subgrid7 five)
		(filled cell64 four) (UsedRow row6 four) (UsedColumn column4 four) (UsedSubgrid subgrid7 four)
		(filled cell65 nine) (UsedRow row6 nine) (UsedColumn column5 nine) (UsedSubgrid subgrid7 nine)

		(empty cell73)
		(empty cell74)
		(empty cell75)
		(empty cell83)
		(empty cell84)
		(empty cell85)

		; bottom right subgrid
		(filled cell76 seven) (UsedRow row7 seven) (UsedColumn column6 seven) (UsedSubgrid subgrid8 seven)
		(filled cell78 two) (UsedRow row7 two) (UsedColumn column8 two) (UsedSubgrid subgrid8 two)
		(filled cell87 eight) (UsedRow row8 eight) (UsedColumn column7 eight) (UsedSubgrid subgrid8 eight)

		(empty cell66)
		(empty cell67)
		(empty cell68)
		(empty cell77)
		(empty cell86)
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