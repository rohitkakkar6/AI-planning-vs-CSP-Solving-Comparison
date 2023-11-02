(set-option :produce-models true)
(declare-datatypes () ((Col x0 x1 x2)))
(declare-datatypes () ((Row y0 y1 y2)))
(declare-fun Board (Col Row) Int)


; Fill in the missing constraints into the designated sections


;;;;;; --- BEGIN-CONSTRAINTS-1 --- 

; ** Sudoku constraints **
; TODO constraints for 1.

; Sudoku constraints for distinct values in rows
(assert (distinct (Board x0 y0) (Board x0 y1) (Board x0 y2) (Board x1 y0) (Board x1 y1) (Board x1 y2) (Board x2 y0) (Board x2 y1) (Board x2 y2)))

; Sudoku constraints for distinct values in columns
(assert (distinct (Board x0 y0) (Board x1 y0) (Board x2 y0) (Board x0 y1) (Board x1 y1) (Board x2 y1) (Board x0 y2) (Board x1 y2) (Board x2 y2)))


;;;;;; --- END-CONSTRAINTS-1 ---


;;;;; 3x3
(assert (= (Board x0 y0) 6))
(assert (= (Board x2 y1) 9))
(assert (= (Board x0 y2) 2))
(assert (= (Board x2 y2) 4))



;;;;;; --- BEGIN-CONSTRAINTS-DOMAIN ---

; Each cell may be assigned only to integer values between 1 and 9:

(assert (and (< (Board x0 y0) 10) (> (Board x0 y0) 0)))
(assert (and (< (Board x0 y1) 10) (> (Board x0 y1) 0)))
(assert (and (< (Board x0 y2) 10) (> (Board x0 y2) 0)))
(assert (and (< (Board x1 y0) 10) (> (Board x1 y0) 0)))
(assert (and (< (Board x1 y1) 10) (> (Board x1 y1) 0)))
(assert (and (< (Board x1 y2) 10) (> (Board x1 y2) 0)))
(assert (and (< (Board x2 y0) 10) (> (Board x2 y0) 0)))
(assert (and (< (Board x2 y1) 10) (> (Board x2 y1) 0)))
(assert (and (< (Board x2 y2) 10) (> (Board x2 y2) 0)))

;;;;;; --- END-CONSTRAINTS-DOMAIN ---



; Compute solution

(check-sat)



; Print solution, line by line

(get-value ((Board x0 y0)))
(get-value ((Board x1 y0)))
(get-value ((Board x2 y0)))
(get-value ((Board x0 y1)))
(get-value ((Board x1 y1)))
(get-value ((Board x2 y1)))
(get-value ((Board x0 y2)))
(get-value ((Board x1 y2)))
(get-value ((Board x2 y2)))

