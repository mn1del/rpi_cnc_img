%
(1001)
(outline_ z0 stock top)
(T1  D=6 CR=0 - ZMIN=-3 - flat end mill)
G90 G94
G17
G21

(2D Contour5)
M9
T1 M6
S6000 M3
G54
M9
G0 X-3.6 Y293.8
Z15
Z5
G1 Z2 F850
Z-0.4 F283.3
G19 G2 Y293.2 Z-1 J-0.6
G1 Y292.6 F850
G17 G3 X-3 Y292 I0.6
G1 X375
G2 X378 Y289 J-3
G1 Y0
Y-3
G3 X378.6 Y-3.6 I0.6
G1 X379.2
G18 G2 X379.8 Z-0.4 K0.6
G0 Z5
X-3.6 Y293.8
G1 Z1 F850
Z-1.4 F283.3
G19 G2 Y293.2 Z-2 J-0.6
G1 Y292.6 F850
G17 G3 X-3 Y292 I0.6
G1 X375
G2 X378 Y289 J-3
G1 Y0
Y-3
G3 X378.6 Y-3.6 I0.6
G1 X379.2
G18 G2 X379.8 Z-1.4 K0.6
G0 Z5
X-3.6 Y293.8
G1 Z0 F850
Z-2.4 F283.3
G19 G2 Y293.2 Z-3 J-0.6
G1 Y292.6 F850
G17 G3 X-3 Y292 I0.6
G1 X375
G2 X378 Y289 J-3
G1 Y0
Y-3
G3 X378.6 Y-3.6 I0.6
G1 X379.2
G18 G2 X379.8 Z-2.4 K0.6
G0 Z15
G17
M9
M30
%