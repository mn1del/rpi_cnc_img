%
(1001)
(origin stock top)
(T2  D=6 CR=0 - ZMIN=-11.8 - flat end mill)
G90 G94
G17
G21

(2D Contour4)
M9
T2 M6
S8500 M3
G54
M9
G0 X-15 Y-140.537
Z15
Z5
G1 Z3.1 F30
G18 G3 X-15.6 Z2.5 I-0.6
G1 X-16.2 F3000
G17 G3 X-16.8 Y-141.137 J-0.6
G1 Y-270 Z-2
Y-508
G2 X-20 Y-511.2 I-3.2
G1 X-307.2
Y-520
G2 X-310.4 Y-523.2 I-3.2
G1 X-505
G2 X-508.2 Y-520 J3.2
G1 Y-20
G2 X-505 Y-16.8 I3.2
G1 X-310.4
G2 X-307.2 Y-20 J-3.2
G1 Y-28.8
X-20
G2 X-16.8 Y-32 J-3.2
G1 Y-270
Y-435.613 Z-4
Y-508
G2 X-20 Y-511.2 I-3.2
G1 X-307.2
Y-520
G2 X-310.4 Y-523.2 I-3.2
G1 X-505
G2 X-508.2 Y-520 J3.2
G1 Y-20
G2 X-505 Y-16.8 I3.2
G1 X-310.4
G2 X-307.2 Y-20 J-3.2
G1 Y-28.8
X-20
G2 X-16.8 Y-32 J-3.2
G1 Y-270
Y-435.613
Y-508 Z-4.874
G2 X-20 Y-511.2 Z-4.935 I-3.2
G1 X-108.2 Z-6
X-307.2
Y-520
G2 X-310.4 Y-523.2 I-3.2
G1 X-505
G2 X-508.2 Y-520 J3.2
G1 Y-20
G2 X-505 Y-16.8 I3.2
G1 X-310.4
G2 X-307.2 Y-20 J-3.2
G1 Y-28.8
X-20
G2 X-16.8 Y-32 J-3.2
G1 Y-435.613
Y-508
G2 X-20 Y-511.2 I-3.2
G1 X-108.2
X-257.252 Z-7.8
X-307.2
Y-520
G2 X-310.4 Y-523.2 I-3.2
G1 X-505
G2 X-508.2 Y-520 J3.2
G1 Y-20
G2 X-505 Y-16.8 I3.2
G1 X-310.4
G2 X-307.2 Y-20 J-3.2
G1 Y-28.8
X-20
G2 X-16.8 Y-32 J-3.2
G1 Y-508
G2 X-20 Y-511.2 I-3.2
G1 X-257.252
G0 Z15

(2D Contour6)
M9
X-275 Y-288.1
Z15
Z5
G1 Z3.1 F30
G18 G2 X-274.4 Z2.5 I0.6
G1 X-273.8 F3000
G17 G3 X-273.2 Y-287.5 J0.6
G1 Y-180 Z-1.254
G3 X-280 Y-173.2 Z-1.627 I-6.8
X-286.8 Y-180 Z-2 J-6.8
G1 Y-360
G3 X-273.2 I6.8
G1 Y-180
G3 X-280 Y-173.2 I-6.8
X-286.8 Y-180 J-6.8
G1 Y-237.273 Z-4
Y-360
G3 X-273.2 I6.8
G1 Y-180
G3 X-280 Y-173.2 I-6.8
X-286.8 Y-180 J-6.8
G1 Y-237.273
Y-294.545 Z-6
Y-360
G3 X-273.2 I6.8
G1 Y-180
G3 X-280 Y-173.2 I-6.8
X-286.8 Y-180 J-6.8
G1 Y-294.545
Y-351.818 Z-8
Y-360
G3 X-273.2 I6.8
G1 Y-180
G3 X-280 Y-173.2 I-6.8
X-286.8 Y-180 J-6.8
G1 Y-294.545
Y-351.818
Y-360 Z-8.286
G3 X-273.2 Z-9.032 I6.8
G1 Y-332.273 Z-10
Y-321
Z-9
Y-309
Z-10 F30
Y-231 F3000
Z-9
Y-219
Z-10 F30
Y-180 F3000
G3 X-280 Y-173.2 I-6.8
X-286.8 Y-180 J-6.8
G1 Y-219
Z-9
Y-231
Z-10 F30
Y-309 F3000
Z-9
Y-321
Z-10 F30
Y-360 F3000
G3 X-273.2 I6.8
G1 Y-332.273
Y-321 Z-10.394
Z-9
Y-309
Z-10.813 F30
Y-280.728 Z-11.8 F3000
Y-231
Z-9
Y-219
Z-11.8 F30
Y-180 F3000
G3 X-280 Y-173.2 I-6.8
X-286.8 Y-180 J-6.8
G1 Y-219
Z-9
Y-231
Z-11.8 F30
Y-309 F3000
Z-9
Y-321
Z-11.8 F30
Y-360 F3000
G3 X-273.2 I6.8
G1 Y-321
Z-9
Y-309
Z-11.8 F30
Y-280.728 F3000
G0 Z15

(2D Contour5)
S9500 M3
M9
X-274.8 Y-180.6
Z15
Z5
G1 Z1 F30
Z-7.4
G18 G2 X-274.2 Z-8 I0.6
G1 X-273.6 F3000
G17 G3 X-273 Y-180 J0.6
X-287 I-7
G1 Y-360
G3 X-273 I7
G1 Y-180
G0 Z5
X-310.705 Y-15.172
G1 Z1 F30
Z-7.4
X-310.706 Y-15.18 Z-7.494
X-310.707 Y-15.202 Z-7.585
X-310.709 Y-15.238 Z-7.672
X-310.712 Y-15.287 Z-7.753
X-310.716 Y-15.348 Z-7.824
X-310.72 Y-15.419 Z-7.885
X-310.725 Y-15.499 Z-7.935
X-310.731 Y-15.586 Z-7.971
X-310.736 Y-15.677 Z-7.993
X-310.742 Y-15.771 Z-8
X-310.779 Y-16.37 F3000
G3 X-310.216 Y-17.006 I0.599 J-0.037
G2 X-307.4 Y-20 I-0.184 J-2.994
G1 Y-29
X-20
G2 X-17 Y-32 J-3
G1 Y-508
G2 X-20 Y-511 I-3
G1 X-307.4
Y-520
G2 X-310.4 Y-523 I-3
G1 X-505
G2 X-508 Y-520 J3
G1 Y-20
G2 X-505 Y-17 I3
G1 X-310.4
G2 X-310.216 Y-17.006 J-3
G0 Z15
M9
M30
%
