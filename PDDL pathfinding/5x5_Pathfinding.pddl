(define (problem problem-pathfinding)
	(:domain pathfinding)
	(:objects
	    cellx0y0 cellx0y1 cellx0y2 cellx0y3 cellx0y4 - position
	    cellx1y0 cellx1y1 cellx1y2 cellx1y3 cellx1y4 - position
	    cellx2y0 cellx2y1 cellx2y2 cellx2y3 cellx2y4 - position
	    cellx3y0 cellx3y1 cellx3y2 cellx3y3 cellx3y4 - position
	    cellx4y0 cellx4y1 cellx4y2 cellx4y3 cellx4y4 - position
	)

	(:init
        (at cellx0y2)
        (right-of cellx0y1 cellx0y0) (right-of cellx0y2 cellx0y1) (right-of cellx0y3 cellx0y2) (right-of cellx0y4 cellx0y3)
        (right-of cellx1y1 cellx1y0) (right-of cellx1y2 cellx1y1) (right-of cellx1y3 cellx1y2) (right-of cellx1y4 cellx1y3)
        (right-of cellx2y1 cellx2y0) (right-of cellx2y2 cellx2y1) (right-of cellx2y3 cellx2y2) (right-of cellx2y4 cellx2y3)
        (right-of cellx3y1 cellx3y0) (right-of cellx3y2 cellx3y1) (right-of cellx3y3 cellx3y2) (right-of cellx3y4 cellx3y3)
        (right-of cellx4y1 cellx4y0) (right-of cellx4y2 cellx4y1) (right-of cellx4y3 cellx4y2) (right-of cellx4y4 cellx4y3)

        (left-of cellx0y0 cellx0y1) (left-of cellx0y1 cellx0y2) (left-of cellx0y2 cellx0y3) (left-of cellx0y3 cellx0y4)
        (left-of cellx1y0 cellx1y1) (left-of cellx1y1 cellx1y2) (left-of cellx1y2 cellx1y3) (left-of cellx1y3 cellx1y4)
        (left-of cellx2y0 cellx2y1) (left-of cellx2y1 cellx2y2) (left-of cellx2y2 cellx2y3) (left-of cellx2y3 cellx2y4)
        (left-of cellx3y0 cellx3y1) (left-of cellx3y1 cellx3y2) (left-of cellx3y2 cellx3y3) (left-of cellx3y3 cellx3y4)
        (left-of cellx4y0 cellx4y1) (left-of cellx4y1 cellx4y2) (left-of cellx4y2 cellx4y3) (left-of cellx4y3 cellx4y4)
        
        (is-underneath cellx1y0 cellx0y0) (is-underneath cellx2y0 cellx1y0) (is-underneath cellx3y0 cellx2y0) (is-underneath cellx4y0 cellx3y0)
        (is-underneath cellx1y1 cellx0y1) (is-underneath cellx2y1 cellx1y1) (is-underneath cellx3y1 cellx2y1) (is-underneath cellx4y1 cellx3y1)
        (is-underneath cellx1y2 cellx0y2) (is-underneath cellx2y2 cellx1y2) (is-underneath cellx3y2 cellx2y2) (is-underneath cellx4y2 cellx3y2)
        (is-underneath cellx1y3 cellx0y3) (is-underneath cellx2y3 cellx1y3) (is-underneath cellx3y3 cellx2y3) (is-underneath cellx4y3 cellx3y3)
        (is-underneath cellx1y4 cellx0y4) (is-underneath cellx2y4 cellx1y4) (is-underneath cellx3y4 cellx2y4) (is-underneath cellx4y4 cellx3y4)

        (is-above cellx0y0 cellx1y0) (is-above cellx1y0 cellx2y0) (is-above cellx2y0 cellx3y0) (is-above cellx3y0 cellx4y0)
        (is-above cellx0y1 cellx1y1) (is-above cellx1y1 cellx2y1) (is-above cellx2y1 cellx3y1) (is-above cellx3y1 cellx4y1)
        (is-above cellx0y2 cellx1y2) (is-above cellx1y2 cellx2y2) (is-above cellx2y2 cellx3y2) (is-above cellx3y2 cellx4y2)
        (is-above cellx0y3 cellx1y3) (is-above cellx1y3 cellx2y3) (is-above cellx2y3 cellx3y3) (is-above cellx3y3 cellx4y3)
        (is-above cellx0y4 cellx1y4) (is-above cellx1y4 cellx2y4) (is-above cellx2y4 cellx3y4) (is-above cellx3y4 cellx4y4)

	)
	(:goal
        (and
        (at cellx4y4)
		)
    )
)