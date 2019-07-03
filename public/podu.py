import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/2018nnujianmo/data"
outSlope = Slope("elevation", "DEGREE", 0.3043)
outSlope.save("C:/2018nnujianmo/output/outslope01")
slope_radians = ATAN ( √ ([dz/dx]2 + [dz/dy]2) )
像元大小为 5 个单位。默认情况下，将使用度来计算坡度。
中心像元 e 在 x 方向上的变化率为：
[dz/dx] = ((c + 2f + i) - (a + 2d + g) / (8 * x_cellsize)
          = ((50 + 60 + 10) - (50 + 60 + 8)) / (8 * 5)
          = (120 - 118) / 40
          = 0.05
像元 e 在 y 方向上的变化率为：
[dz/dy] = ((g + 2h + i) - (a + 2b + c)) / (8 * y_cellsize)
          = ((8 + 20 + 10) - (50 + 90 + 50)) / (8 * 5)
          = (38 - 190 ) / 40
          = -3.8
代入 x 方向和 y 方向上的变化率，计算中心像元 e 的坡度：
rise_run = √ ([dz/dx]2 + [dz/dy]2)
           = √ ((0.05)2 + (-3.8)2)
           = √ (0.0025 + 14.44)
           = 3.80032
slope_degrees = ATAN (rise_run) * 57.29578
                = ATAN (3.80032) * 57.29578
                = 1.31349 * 57.29578
                = 75.25762
