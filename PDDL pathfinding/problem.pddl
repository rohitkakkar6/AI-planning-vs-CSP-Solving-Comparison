(define (problem maze-problem)
    (:domain maze)
    (:objects
        cellx0y0 cellx0y1 cellx0y2 cellx0y3 cellx0y4 cellx0y5 cellx0y6 cellx0y7 cellx0y8 cellx1y0 cellx1y1 cellx1y2 cellx1y3 cellx1y4 cellx1y5 cellx1y6 cellx1y7 cellx1y8 cellx2y0 cellx2y1 cellx2y2 cellx2y3 cellx2y4 cellx2y5 cellx2y6 cellx2y7 cellx2y8 cellx3y0 cellx3y1 cellx3y2 cellx3y3 cellx3y4 cellx3y5 cellx3y6 cellx3y7 cellx3y8 cellx4y0 cellx4y1 cellx4y2 cellx4y3 cellx4y4 cellx4y5 cellx4y6 cellx4y7 cellx4y8 cellx5y0 cellx5y1 cellx5y2 cellx5y3 cellx5y4 cellx5y5 cellx5y6 cellx5y7 cellx5y8 cellx6y0 cellx6y1 cellx6y2 cellx6y3 cellx6y4 cellx6y5 cellx6y6 cellx6y7 cellx6y8 cellx7y0 cellx7y1 cellx7y2 cellx7y3 cellx7y4 cellx7y5 cellx7y6 cellx7y7 cellx7y8 cellx8y0 cellx8y1 cellx8y2 cellx8y3 cellx8y4 cellx8y5 cellx8y6 cellx8y7 cellx8y8 - cell)
    (:init
        (at cellx0y0)
        (right-of cellx1y4 cellx0y4)
        (left-of cellx0y4 cellx1y4)
        (right-of cellx4y3 cellx3y3)
        (left-of cellx3y3 cellx4y3)
        (right-of cellx4y5 cellx3y5)
        (left-of cellx3y5 cellx4y5)
        (right-of cellx2y0 cellx1y0)
        (left-of cellx1y0 cellx2y0)
        (right-of cellx5y6 cellx4y6)
        (left-of cellx4y6 cellx5y6)
        (right-of cellx1y6 cellx0y6)
        (left-of cellx0y6 cellx1y6)
        (right-of cellx8y2 cellx7y2)
        (left-of cellx7y2 cellx8y2)
        (right-of cellx2y1 cellx1y1)
        (left-of cellx1y1 cellx2y1)
        (right-of cellx8y6 cellx7y6)
        (left-of cellx7y6 cellx8y6)
        (right-of cellx4y7 cellx3y7)
        (left-of cellx3y7 cellx4y7)
        (right-of cellx4y6 cellx3y6)
        (left-of cellx3y6 cellx4y6)
        (right-of cellx3y2 cellx2y2)
        (left-of cellx2y2 cellx3y2)
        (right-of cellx3y6 cellx2y6)
        (left-of cellx2y6 cellx3y6)
        (right-of cellx5y8 cellx4y8)
        (left-of cellx4y8 cellx5y8)
        (right-of cellx6y2 cellx5y2)
        (left-of cellx5y2 cellx6y2)
        (right-of cellx7y3 cellx6y3)
        (left-of cellx6y3 cellx7y3)
        (right-of cellx1y8 cellx0y8)
        (left-of cellx0y8 cellx1y8)
        (right-of cellx2y8 cellx1y8)
        (left-of cellx1y8 cellx2y8)
        (right-of cellx6y7 cellx5y7)
        (left-of cellx5y7 cellx6y7)
        (right-of cellx1y1 cellx0y1)
        (left-of cellx0y1 cellx1y1)
        (right-of cellx8y8 cellx7y8)
        (left-of cellx7y8 cellx8y8)
        (right-of cellx7y0 cellx6y0)
        (left-of cellx6y0 cellx7y0)
        (right-of cellx6y8 cellx5y8)
        (left-of cellx5y8 cellx6y8)
        (right-of cellx8y0 cellx7y0)
        (left-of cellx7y0 cellx8y0)
        (right-of cellx4y8 cellx3y8)
        (left-of cellx3y8 cellx4y8)
        (right-of cellx6y1 cellx5y1)
        (left-of cellx5y1 cellx6y1)
        (right-of cellx8y3 cellx7y3)
        (left-of cellx7y3 cellx8y3)
        (right-of cellx7y7 cellx6y7)
        (left-of cellx6y7 cellx7y7)
        (right-of cellx7y1 cellx6y1)
        (left-of cellx6y1 cellx7y1)
        (right-of cellx3y5 cellx2y5)
        (left-of cellx2y5 cellx3y5)
        (right-of cellx4y0 cellx3y0)
        (left-of cellx3y0 cellx4y0)
        (right-of cellx1y0 cellx0y0)
        (left-of cellx0y0 cellx1y0)
        (right-of cellx5y3 cellx4y3)
        (left-of cellx4y3 cellx5y3)
        (right-of cellx5y1 cellx4y1)
        (left-of cellx4y1 cellx5y1)
        (right-of cellx6y0 cellx5y0)
        (left-of cellx5y0 cellx6y0)
        (right-of cellx2y6 cellx1y6)
        (left-of cellx1y6 cellx2y6)
        (right-of cellx3y8 cellx2y8)
        (left-of cellx2y8 cellx3y8)
        (right-of cellx1y2 cellx0y2)
        (left-of cellx0y2 cellx1y2)
        (right-of cellx6y5 cellx5y5)
        (left-of cellx5y5 cellx6y5)
        (right-of cellx2y7 cellx1y7)
        (left-of cellx1y7 cellx2y7)
        (right-of cellx3y3 cellx2y3)
        (left-of cellx2y3 cellx3y3)
        (right-of cellx2y2 cellx1y2)
        (left-of cellx1y2 cellx2y2)
        (right-of cellx3y1 cellx2y1)
        (left-of cellx2y1 cellx3y1)
        (right-of cellx3y0 cellx2y0)
        (left-of cellx2y0 cellx3y0)
        (right-of cellx5y7 cellx4y7)
        (left-of cellx4y7 cellx5y7)
        (right-of cellx5y4 cellx4y4)
        (left-of cellx4y4 cellx5y4)
        (right-of cellx3y7 cellx2y7)
        (left-of cellx2y7 cellx3y7)
        (right-of cellx4y1 cellx3y1)
        (left-of cellx3y1 cellx4y1)
        (right-of cellx6y3 cellx5y3)
        (left-of cellx5y3 cellx6y3)
        (right-of cellx8y4 cellx7y4)
        (left-of cellx7y4 cellx8y4)
        (right-of cellx2y3 cellx1y3)
        (left-of cellx1y3 cellx2y3)
        (right-of cellx7y5 cellx6y5)
        (left-of cellx6y5 cellx7y5)
        (right-of cellx7y8 cellx6y8)
        (left-of cellx6y8 cellx7y8)
        (is-above cellx5y0 cellx5y1)
        (is-underneath cellx5y1 cellx5y0)
        (is-above cellx0y7 cellx0y8)
        (is-underneath cellx0y8 cellx0y7)
        (is-above cellx1y7 cellx1y8)
        (is-underneath cellx1y8 cellx1y7)
        (is-above cellx1y4 cellx1y5)
        (is-underneath cellx1y5 cellx1y4)
        (is-above cellx5y4 cellx5y5)
        (is-underneath cellx5y5 cellx5y4)
        (is-above cellx3y6 cellx3y7)
        (is-underneath cellx3y7 cellx3y6)
        (is-above cellx7y1 cellx7y2)
        (is-underneath cellx7y2 cellx7y1)
        (is-above cellx7y7 cellx7y8)
        (is-underneath cellx7y8 cellx7y7)
        (is-above cellx8y1 cellx8y2)
        (is-underneath cellx8y2 cellx8y1)
        (is-above cellx8y5 cellx8y6)
        (is-underneath cellx8y6 cellx8y5)
        (is-above cellx4y2 cellx4y3)
        (is-underneath cellx4y3 cellx4y2)
        (is-above cellx2y4 cellx2y5)
        (is-underneath cellx2y5 cellx2y4)
        (is-above cellx1y5 cellx1y6)
        (is-underneath cellx1y6 cellx1y5)
        (is-above cellx5y3 cellx5y4)
        (is-underneath cellx5y4 cellx5y3)
        (is-above cellx0y4 cellx0y5)
        (is-underneath cellx0y5 cellx0y4)
        (is-above cellx5y5 cellx5y6)
        (is-underneath cellx5y6 cellx5y5)
        (is-above cellx0y3 cellx0y4)
        (is-underneath cellx0y4 cellx0y3)
        (is-above cellx4y0 cellx4y1)
        (is-underneath cellx4y1 cellx4y0)
        (is-above cellx2y2 cellx2y3)
        (is-underneath cellx2y3 cellx2y2)
        (is-above cellx6y4 cellx6y5)
        (is-underneath cellx6y5 cellx6y4)
        (is-above cellx2y5 cellx2y6)
        (is-underneath cellx2y6 cellx2y5)
        (is-above cellx5y1 cellx5y2)
        (is-underneath cellx5y2 cellx5y1)
        (is-above cellx1y6 cellx1y7)
        (is-underneath cellx1y7 cellx1y6)
        (is-above cellx6y5 cellx6y6)
        (is-underneath cellx6y6 cellx6y5)
        (is-above cellx0y1 cellx0y2)
        (is-underneath cellx0y2 cellx0y1)
        (is-above cellx5y7 cellx5y8)
        (is-underneath cellx5y8 cellx5y7)
        (is-above cellx2y3 cellx2y4)
        (is-underneath cellx2y4 cellx2y3)
        (is-above cellx6y6 cellx6y7)
        (is-underneath cellx6y7 cellx6y6)
        (is-above cellx7y5 cellx7y6)
        (is-underneath cellx7y6 cellx7y5)
        (is-above cellx3y4 cellx3y5)
        (is-underneath cellx3y5 cellx3y4)
        (is-above cellx0y5 cellx0y6)
        (is-underneath cellx0y6 cellx0y5)
        (is-above cellx8y0 cellx8y1)
        (is-underneath cellx8y1 cellx8y0)
        (is-above cellx6y2 cellx6y3)
        (is-underneath cellx6y3 cellx6y2)
        (is-above cellx3y3 cellx3y4)
        (is-underneath cellx3y4 cellx3y3)
        (is-above cellx3y7 cellx3y8)
        (is-underneath cellx3y8 cellx3y7)
        (is-above cellx0y2 cellx0y3)
        (is-underneath cellx0y3 cellx0y2)
        (is-above cellx2y0 cellx2y1)
        (is-underneath cellx2y1 cellx2y0)
        (is-above cellx4y1 cellx4y2)
        (is-underneath cellx4y2 cellx4y1)
        (is-above cellx8y7 cellx8y8)
        (is-underneath cellx8y8 cellx8y7)
        (is-above cellx1y3 cellx1y4)
        (is-underneath cellx1y4 cellx1y3)
        (is-above cellx0y0 cellx0y1)
        (is-underneath cellx0y1 cellx0y0)
        (is-above cellx7y0 cellx7y1)
        (is-underneath cellx7y1 cellx7y0)
        (is-above cellx8y4 cellx8y5)
        (is-underneath cellx8y5 cellx8y4)
        (is-above cellx4y4 cellx4y5)
        (is-underneath cellx4y5 cellx4y4)
        (is-above cellx8y3 cellx8y4)
        (is-underneath cellx8y4 cellx8y3)
        (is-above cellx7y6 cellx7y7)
        (is-underneath cellx7y7 cellx7y6)
        (is-above cellx3y1 cellx3y2)
        (is-underneath cellx3y2 cellx3y1)
        (is-above cellx0y6 cellx0y7)
        (is-underneath cellx0y7 cellx0y6)
        (is-above cellx8y6 cellx8y7)
        (is-underneath cellx8y7 cellx8y6)
        (is-above cellx7y4 cellx7y5)
        (is-underneath cellx7y5 cellx7y4)
        (is-above cellx7y2 cellx7y3)
        (is-underneath cellx7y3 cellx7y2)
        (is-underneath cellx6y6 cellx6y5)
        (is-above cellx6y5 cellx6y6)
        (is-underneath cellx8y1 cellx8y0)
        (is-above cellx8y0 cellx8y1)
        (is-underneath cellx0y2 cellx0y1)
        (is-above cellx0y1 cellx0y2)
        (is-underneath cellx5y1 cellx5y0)
        (is-above cellx5y0 cellx5y1)
        (is-underneath cellx2y1 cellx2y0)
        (is-above cellx2y0 cellx2y1)
        (is-underneath cellx0y3 cellx0y2)
        (is-above cellx0y2 cellx0y3)
        (is-underneath cellx0y7 cellx0y6)
        (is-above cellx0y6 cellx0y7)
        (is-underneath cellx1y6 cellx1y5)
        (is-above cellx1y5 cellx1y6)
        (is-underneath cellx8y5 cellx8y4)
        (is-above cellx8y4 cellx8y5)
        (is-underneath cellx5y4 cellx5y3)
        (is-above cellx5y3 cellx5y4)
        (is-underneath cellx0y1 cellx0y0)
        (is-above cellx0y0 cellx0y1)
        (is-underneath cellx4y1 cellx4y0)
        (is-above cellx4y0 cellx4y1)
        (is-underneath cellx8y6 cellx8y5)
        (is-above cellx8y5 cellx8y6)
        (is-underneath cellx2y4 cellx2y3)
        (is-above cellx2y3 cellx2y4)
        (is-underneath cellx1y7 cellx1y6)
        (is-above cellx1y6 cellx1y7)
        (is-underneath cellx3y2 cellx3y1)
        (is-above cellx3y1 cellx3y2)
        (is-underneath cellx3y7 cellx3y6)
        (is-above cellx3y6 cellx3y7)
        (is-underneath cellx0y4 cellx0y3)
        (is-above cellx0y3 cellx0y4)
        (is-underneath cellx3y4 cellx3y3)
        (is-above cellx3y3 cellx3y4)
        (is-underneath cellx6y3 cellx6y2)
        (is-above cellx6y2 cellx6y3)
        (is-underneath cellx7y3 cellx7y2)
        (is-above cellx7y2 cellx7y3)
        (is-underneath cellx2y5 cellx2y4)
        (is-above cellx2y4 cellx2y5)
        (is-underneath cellx3y8 cellx3y7)
        (is-above cellx3y7 cellx3y8)
        (is-underneath cellx8y8 cellx8y7)
        (is-above cellx8y7 cellx8y8)
        (is-underneath cellx5y8 cellx5y7)
        (is-above cellx5y7 cellx5y8)
        (is-underneath cellx0y6 cellx0y5)
        (is-above cellx0y5 cellx0y6)
        (is-underneath cellx7y1 cellx7y0)
        (is-above cellx7y0 cellx7y1)
        (is-underneath cellx4y3 cellx4y2)
        (is-above cellx4y2 cellx4y3)
        (is-underneath cellx0y5 cellx0y4)
        (is-above cellx0y4 cellx0y5)
        (is-underneath cellx2y3 cellx2y2)
        (is-above cellx2y2 cellx2y3)
        (is-underneath cellx3y5 cellx3y4)
        (is-above cellx3y4 cellx3y5)
        (is-underneath cellx4y2 cellx4y1)
        (is-above cellx4y1 cellx4y2)
        (is-underneath cellx5y2 cellx5y1)
        (is-above cellx5y1 cellx5y2)
        (is-underneath cellx7y7 cellx7y6)
        (is-above cellx7y6 cellx7y7)
        (is-underneath cellx1y5 cellx1y4)
        (is-above cellx1y4 cellx1y5)
        (is-underneath cellx8y2 cellx8y1)
        (is-above cellx8y1 cellx8y2)
        (is-underneath cellx8y4 cellx8y3)
        (is-above cellx8y3 cellx8y4)
        (is-underneath cellx2y6 cellx2y5)
        (is-above cellx2y5 cellx2y6)
        (is-underneath cellx7y5 cellx7y4)
        (is-above cellx7y4 cellx7y5)
        (is-underneath cellx7y2 cellx7y1)
        (is-above cellx7y1 cellx7y2)
        (is-underneath cellx5y5 cellx5y4)
        (is-above cellx5y4 cellx5y5)
        (is-underneath cellx4y5 cellx4y4)
        (is-above cellx4y4 cellx4y5)
        (is-underneath cellx1y8 cellx1y7)
        (is-above cellx1y7 cellx1y8)
        (is-underneath cellx5y6 cellx5y5)
        (is-above cellx5y5 cellx5y6)
        (is-underneath cellx6y5 cellx6y4)
        (is-above cellx6y4 cellx6y5)
        (is-underneath cellx6y7 cellx6y6)
        (is-above cellx6y6 cellx6y7)
        (is-underneath cellx8y7 cellx8y6)
        (is-above cellx8y6 cellx8y7)
        (is-underneath cellx1y4 cellx1y3)
        (is-above cellx1y3 cellx1y4)
        (is-underneath cellx7y6 cellx7y5)
        (is-above cellx7y5 cellx7y6)
        (is-underneath cellx7y8 cellx7y7)
        (is-above cellx7y7 cellx7y8)
        (is-underneath cellx0y8 cellx0y7)
        (is-above cellx0y7 cellx0y8)
        (left-of cellx2y5 cellx3y5)
        (right-of cellx3y5 cellx2y5)
        (left-of cellx7y4 cellx8y4)
        (right-of cellx8y4 cellx7y4)
        (left-of cellx5y3 cellx6y3)
        (right-of cellx6y3 cellx5y3)
        (left-of cellx6y8 cellx7y8)
        (right-of cellx7y8 cellx6y8)
        (left-of cellx3y5 cellx4y5)
        (right-of cellx4y5 cellx3y5)
        (left-of cellx3y6 cellx4y6)
        (right-of cellx4y6 cellx3y6)
        (left-of cellx6y3 cellx7y3)
        (right-of cellx7y3 cellx6y3)
        (left-of cellx3y0 cellx4y0)
        (right-of cellx4y0 cellx3y0)
        (left-of cellx3y1 cellx4y1)
        (right-of cellx4y1 cellx3y1)
        (left-of cellx0y2 cellx1y2)
        (right-of cellx1y2 cellx0y2)
        (left-of cellx4y3 cellx5y3)
        (right-of cellx5y3 cellx4y3)
        (left-of cellx4y6 cellx5y6)
        (right-of cellx5y6 cellx4y6)
        (left-of cellx3y8 cellx4y8)
        (right-of cellx4y8 cellx3y8)
        (left-of cellx4y1 cellx5y1)
        (right-of cellx5y1 cellx4y1)
        (left-of cellx5y2 cellx6y2)
        (right-of cellx6y2 cellx5y2)
        (left-of cellx0y0 cellx1y0)
        (right-of cellx1y0 cellx0y0)
        (left-of cellx3y3 cellx4y3)
        (right-of cellx4y3 cellx3y3)
        (left-of cellx4y7 cellx5y7)
        (right-of cellx5y7 cellx4y7)
        (left-of cellx5y1 cellx6y1)
        (right-of cellx6y1 cellx5y1)
        (left-of cellx0y1 cellx1y1)
        (right-of cellx1y1 cellx0y1)
        (left-of cellx2y0 cellx3y0)
        (right-of cellx3y0 cellx2y0)
        (left-of cellx0y8 cellx1y8)
        (right-of cellx1y8 cellx0y8)
        (left-of cellx1y2 cellx2y2)
        (right-of cellx2y2 cellx1y2)
        (left-of cellx1y6 cellx2y6)
        (right-of cellx2y6 cellx1y6)
        (left-of cellx5y7 cellx6y7)
        (right-of cellx6y7 cellx5y7)
        (left-of cellx6y5 cellx7y5)
        (right-of cellx7y5 cellx6y5)
        (left-of cellx2y6 cellx3y6)
        (right-of cellx3y6 cellx2y6)
        (left-of cellx1y3 cellx2y3)
        (right-of cellx2y3 cellx1y3)
        (left-of cellx3y7 cellx4y7)
        (right-of cellx4y7 cellx3y7)
        (left-of cellx0y6 cellx1y6)
        (right-of cellx1y6 cellx0y6)
        (left-of cellx7y2 cellx8y2)
        (right-of cellx8y2 cellx7y2)
        (left-of cellx7y0 cellx8y0)
        (right-of cellx8y0 cellx7y0)
        (left-of cellx1y1 cellx2y1)
        (right-of cellx2y1 cellx1y1)
        (left-of cellx5y5 cellx6y5)
        (right-of cellx6y5 cellx5y5)
        (left-of cellx2y7 cellx3y7)
        (right-of cellx3y7 cellx2y7)
        (left-of cellx4y4 cellx5y4)
        (right-of cellx5y4 cellx4y4)
        (left-of cellx0y4 cellx1y4)
        (right-of cellx1y4 cellx0y4)
        (left-of cellx6y1 cellx7y1)
        (right-of cellx7y1 cellx6y1)
        (left-of cellx1y7 cellx2y7)
        (right-of cellx2y7 cellx1y7)
        (left-of cellx1y0 cellx2y0)
        (right-of cellx2y0 cellx1y0)
        (left-of cellx6y7 cellx7y7)
        (right-of cellx7y7 cellx6y7)
        (left-of cellx5y0 cellx6y0)
        (right-of cellx6y0 cellx5y0)
        (left-of cellx2y8 cellx3y8)
        (right-of cellx3y8 cellx2y8)
        (left-of cellx6y0 cellx7y0)
        (right-of cellx7y0 cellx6y0)
        (left-of cellx1y8 cellx2y8)
        (right-of cellx2y8 cellx1y8)
        (left-of cellx2y2 cellx3y2)
        (right-of cellx3y2 cellx2y2)
        (left-of cellx4y8 cellx5y8)
        (right-of cellx5y8 cellx4y8)
        (left-of cellx7y6 cellx8y6)
        (right-of cellx8y6 cellx7y6)
        (left-of cellx7y3 cellx8y3)
        (right-of cellx8y3 cellx7y3)
        (left-of cellx2y3 cellx3y3)
        (right-of cellx3y3 cellx2y3)
        (left-of cellx7y8 cellx8y8)
        (right-of cellx8y8 cellx7y8)
        (left-of cellx2y1 cellx3y1)
        (right-of cellx3y1 cellx2y1)
        (left-of cellx5y8 cellx6y8)
        (right-of cellx6y8 cellx5y8)
    )
    (:goal (
        (at cellx8y8)
    )
))
