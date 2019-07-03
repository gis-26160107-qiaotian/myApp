Import   arcpy 
from  arcpy import env  
from  arcpy.sa import *
env.workspace = "C:/2018nnujianmo /data"
outAspect = Aspect("elevation")
outAspect.save("C:/2018nnujianmo /output/outaspect01.img")
坡向计算代码如下：
像元 e 在 x 方向上的变化率将通过以下算法进行计算：
[dz/dx] = ((c + 2f + i) - (a + 2d + g)) / 8
像元 e 在 y 方向上的变化率将通过以下算法进行计算：
[dz/dy] = ((g + 2h + i) - (a + 2b + c)) / 8
代入像元 e 在 x 方向和 y 方向上的变化率，坡向将通过以下算法进行计算：
aspect = 57.29578 * atan2 ([dz/dy], -[dz/dx])
然后，坡向值将根据以下规则转换为罗盘方向值（0 到 360 度）：
if aspect < 0     cell = 90.0 - aspect   else if aspect > 90.0     cell = 360.0 - aspect + 90.0   else     cell = 90.0 – aspect
