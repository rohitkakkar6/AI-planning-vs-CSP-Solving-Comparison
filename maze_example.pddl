(define (problem problem-pathfinding)
    (:domain pathfinding)
    (:objects
        cellx0y0 cellx0y1 cellx0y2 cellx0y3 - position
        cellx1y0 cellx1y1 cellx1y2 cellx1y3 - position
        cellx2y0 cellx2y1 cellx2y2 cellx2y3 - position
        cellx3y0 cellx3y1 cellx3y2 cellx3y3 - position
    )

    (:init
        (at cellx0y0)
        
        ; Horizontal connections
        (right-of cellx1y0 cellx0y0) (right-of cellx2y0 cellx1y0)
        ; Intentionally omitting right-of from cellx2y0 to cellx3y0 to create a wall
        (right-of cellx1y1 cellx0y1) (right-of cellx2y1 cellx1y1) (right-of cellx3y1 cellx2y1)
        ; Intentionally omitting connections on y2 to simulate walls
        (right-of cellx2y3 cellx1y3) (right-of cellx3y3 cellx2y3)
        
        (left-of cellx0y0 cellx1y0) (left-of cellx1y0 cellx2y0)
        ; Intentionally omitting left-of from cellx3y0 to cellx2y0
        (left-of cellx0y1 cellx1y1) (left-of cellx1y1 cellx2y1) (left-of cellx2y1 cellx3y1)
        ; Intentionally omitting connections on y2 to simulate walls
        (left-of cellx1y3 cellx2y3) (left-of cellx2y3 cellx3y3)
        
        ; Vertical connections
        (is-underneath cellx0y1 cellx0y0) (is-underneath cellx0y2 cellx0y1) (is-underneath cellx0y3 cellx0y2)
        (is-underneath cellx1y1 cellx1y0) ; Intentionally omitting some connections to simulate walls
        (is-underneath cellx2y1 cellx2y0) (is-underneath cellx2y2 cellx2y1) (is-underneath cellx2y3 cellx2y2)
        (is-underneath cellx3y1 cellx3y0) (is-underneath cellx3y3 cellx3y2)
        
        (is-above cellx0y0 cellx0y1) (is-above cellx0y1 cellx0y2) (is-above cellx0y2 cellx0y3)
        (is-above cellx1y0 cellx1y1) ; Intentionally omitting some connections to simulate walls
        (is-above cellx2y0 cellx2y1) (is-above cellx2y1 cellx2y2) (is-above cellx2y2 cellx2y3)
        (is-above cellx3y0 cellx3y1) (is-above cellx3y2 cellx3y3)
    )
    (:goal
        (at cellx3y3)
    )
)

