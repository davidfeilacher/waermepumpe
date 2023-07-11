
import numpy as np
import math
daysMeasured_20=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysPerMonth_22=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysPerMonth_20=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# messwerte von 2021 berücksichtigen und das im märz nur ab 10. und das im jänner nur bis 27. !

T7_22=[10.1, 2.6, 5.8, 7, 6.1, 1.8, -4.3, -1.3, -3.6, 1.8, -1.1, -6.5, -2.1, -1.1, 1.5, -4.1, 3, 0.1, -3.8, 2.8, -2.2, 0.1, 1.8, 2.1, -0.8, 0.4, 1, 2.6, 2.1, 6.8, 2.2, 1.8, 4.1, 2.4, 3, 4.7, 3.2, 3.6, 2, 6.2, -0.3, 3.5, 2.4, -4.8, -4.9, -0.1, 2.3, 11.1, 7.2, 7.6, 2.5, 9.6, 3.8, 6.2, -2.7, 3.3, 2, 1.3, 0.7, -5.9, -6.2, -3.9, -2.9, -0.2, -1.5, -1.1, -1.4, -2.6, -2.5, -3, -0.9, -2, -2.4, 1.8, 7.9, 1.6, 2.7, -0.1, 2.7, 1.1, -0.2, -0.2, 4, 1.9, 2.5, 5.1, 4.8, 6.7, 7.2, 8, 3.2, 1.8, -0.1, -0.3, 5.5, 10.8, 9.4, 8.3, 6.7, 3.6, 2.8, 3.1, 7.7, 8.4, 11.6, 7.3, 4, 2.2, 5.6, 2.9, 4.4, 8.8, 7.5, 10.1, 9.7, 7.4, 6.9, 8.2, 8.7, 8, 11.2, 11.3, 10, 13.1, 14.1, 12.7, 12.5, 12.6, 14.4, 13, 15, 18.7, 15.8, 14.9, 14.8, 15.1, 16.7, 13.7, 11.3, 18.1, 19.2, 16.1, 15.1, 17.9, 14.6, 13.6, 17, 13.1, 10.4, 10.2, 12, 15.7, 16.7, 16.7, 19.6, 18.8, 18.2, 17.9, 15.6, 14.2, 13.2, 16.5, 16.8, 16.2, 15.7, 15.2, 17.9, 18.3, 17.2, 19, 20.6, 16.5, 17, 20, 19.9, 15.5, 18.3, 21.7, 20.7, 21.5, 19, 21, 14.8, 17.2, 19.8, 17.9, 18.1, 17.6, 14.5, 15.4, 15.8, 14.8, 16.1, 16.7, 19, 17.7, 15.9, 16.8, 15.8, 18.5, 19.8, 23, 21.6, 23.3, 21.6, 20, 19.7, 19.4, 16.9, 19, 17.3, 17.8, 20.6, 18.6, 18.7, 19.5, 21.5, 20, 16.9, 17.6, 14.6, 15.5, 16.1, 14.8, 16.5, 17.3, 17.7, 19.4, 19.5, 20.3, 19, 18.7, 17, 15.7, 14.7, 16.9, 19, 17.7, 19.2, 19, 18.9, 16.8, 16.3, 13.9, 11.4, 11.4, 15.4, 14.7, 14.8, 15.2, 16.4, 13.4, 14, 14.5, 13.8, 10.9, 16, 18.2, 13.9, 11.2, 8.6, 8.3, 9.7, 8, 7.2, 4, 6.5, 10.7, 12.3, 11.1, 7.8, 8.7, 10.1, 11.1, 11.8, 11, 10.2, 5.1, 10.6, 11.8, 12.3, 8.5, 7.8, 11.6, 9.9, 8.9, 9.4, 10.1, 11.5, 11.1, 11.4, 12.7, 4.3, 6.4, 8.1, 6.7, 11.1, 12.3, 7.8, 10.8, 10.1, 10.1, 9.3, 9.6, 9.8, 11.2, 5.8, 11.6, 6.7, 5.4, 7.4, 2.4, 5.1, 6.6, 4.3, 3.7, 4.4, 5, 5.2, 7.2, 6, 4.9, -1.4, -0.5, 4.5, 2, 0.8, 3.8, 2.8, 6.3, 4, -1.1, 2.1, 0.6, 0.6, -0.1, 1.6, 4.7, 2.1, 2.4, 3.3, 0.6, 1.9, 1.3, -0.4, -3.4, -8.9, -6.4, 0, 0.4, -0.6, -8.4, -5, -1.7, -1.4, -1, 4.4, 9.4, 6.4, 2.7, 6.2, -1.7, -1.5, 2.2, 4.8]
T14_22=[11.8, 6.5, 8.9, 10, 5.7, 3.2, -1.6, -0.9, 1.3, 1.4, -0.4, -0.8, 0.3, 3.7, 4.6, 0, 4.7, 4.3, 2.5, 4.4, 0, 2.3, 2.4, 0.8, 1.5, 1.4, 5.2, 3.6, 3.5, 7.1, 2.5, 2.6, 5.6, 7.6, 7.8, 5.7, 9.6, 3.5, 6.3, 10.8, 11.1, 6.3, 6.9, 8.8, 5.8, 5.9, 13.7, 11.6, 11.8, 9.8, 10.5, 7.6, 7.3, 10.1, 13.3, 6.4, 4.6, 7, 2.9, 4.6, 7.3, 7.8, 3.9, 3.6, 2.5, 2.2, 6.9, 9.7, 6.6, 4.7, 9.5, 11.7, 14.6, 13, 8.5, 12.8, 11.5, 10.2, 10.5, 13.2, 16.9, 20.7, 20.1, 17.5, 18.5, 15.5, 20.2, 20.1, 16.3, 6.3, 4.7, 1.7, 2.4, 7.5, 8.5, 17.9, 16.4, 11.8, 6.3, 5.7, 12.1, 17.1, 21.4, 23.5, 16.1, 8, 12.3, 7.9, 1.9, 11.7, 15.5, 8, 11.8, 18.2, 14.6, 14.8, 10.3, 16.8, 18.3, 20.3, 13.9, 17.7, 22, 20.1, 22.4, 15.2, 15.1, 17.7, 22.5, 24.1, 27.3, 27.7, 22.5, 23.2, 24.5, 26.3, 18, 20, 26.4, 30.1, 24.3, 24, 21.1, 22.2, 15.3, 22.7, 24.2, 18.4, 15, 18.4, 24.7, 23, 23, 28.1, 28.7, 27.1, 25.3, 17.7, 21.5, 15.1, 15.8, 24.2, 26.6, 22.8, 23.2, 26.7, 29.7, 24.1, 28.7, 33.3, 27, 24.9, 24.8, 27.7, 29.1, 21.3, 29.4, 34, 28.1, 24.3, 28.8, 27.7, 24.3, 28.7, 28.4, 21.3, 16.5, 16.7, 15.8, 22, 20.9, 20.1, 21.3, 27.1, 31.2, 23.5, 25.3, 24.8, 27.5, 30.5, 34.2, 31.7, 31.1, 30.5, 28.5, 34, 20.1, 22.3, 26.6, 22.4, 22.3, 24.4, 20.5, 25.2, 30.3, 32.3, 33.7, 19.9, 21.6, 18.1, 26, 26.5, 25.9, 24.4, 26, 23.5, 29.5, 28.1, 32.3, 32.5, 26.4, 19.4, 20.2, 16.1, 16.3, 23.9, 24.9, 28.8, 27.2, 21.4, 23.5, 25.6, 18.3, 20.3, 21.1, 22.7, 21.9, 24.5, 24.4, 26.4, 17.5, 17.8, 19.5, 17.2, 21.3, 23.6, 22.6, 18.8, 16.9, 11.8, 11.6, 10.9, 9.7, 11.3, 14.5, 16.6, 15.4, 15.2, 15.8, 13.2, 17.4, 14.9, 13.7, 15.4, 12.9, 12.7, 16.5, 18.1, 22.3, 22.9, 18.7, 15.8, 19.8, 18.3, 16.3, 14.4, 16.5, 14.5, 14.1, 21.9, 16.9, 17.6, 15.2, 13.2, 14.1, 16.4, 18.5, 18.6, 14.3, 20.1, 12, 14.7, 12.6, 10.9, 13, 16.2, 19.7, 8.4, 9.6, 11.5, 15.3, 5.4, 7.9, 10.8, 9.5, 11, 12.5, 15.9, 6.9, 7.5, 7.6, 8, -1.3, 5.4, 7.2, 3.7, 3.9, 8.1, 8.6, 8.5, 6.4, 6.5, 5.9, 5.2, 1.7, 0.2, 4.7, 4.4, 3.2, 4.5, 4.5, 4.8, 2.5, 2.4, -0.9, -1.7, -1.4, 0.8, 0.4, 0.9, -0.4, -3.7, -0.5, -0.5, 0.1, 4, 9.8, 10, 10.3, 10, 6.6, 5.5, 3.9, 9.3, 14.2]
T19_22=[9.7, 6.8, 7.8, 8.4, 3.3, -0.5, -2.3, 1.2, 2.9, 1.3, -2.1, -1.2, 0.5, 3, -0.6, 1.5, 3.8, -0.2, 1.5, 0.8, -0.9, 0.5, 2.4, 0.8, 1.4, 1.7, 3.1, 3, 5.8, 5, 2.7,2.3, 4.4, 5.8, 5.3, 3.4, 8.1, 3.8, 5.9, 7.2, 7.6, 3.7, 3.7, 4.2, 3.2, 3.1, 10, 7.8, 7.8, 6.2, 8.5, 6.7, 4.9, 7.4, 9.8, 4.2, 4.6, 4.2, 1.2, 0.9, 2.4, 3.4, 1.8, 2.2, 1.8, 1.7, 3.9, 6.7, 3.1, 1.3, 4.7, 8.1, 9.4, 9.4, 8.5, 8.8, 7.1, 7.7, 6.6, 8.6, 12.6, 15.7, 14, 12.2, 14.3, 13.3, 16.4, 15.8, 13.8, 4.7, 4, 0, 1.1, 5.7, 8.2, 14.9, 14.1, 10.2, 6, 6.3, 9.6, 13.9, 17.1, 20.2, 11.8, 7.8, 11, 8.1, 2.8, 10, 13.9, 7.7, 11.5, 10.5, 12.1, 12.7, 9.8, 14.6, 14.4, 17.3, 12.9, 16.1, 18.4, 15.9, 17.1, 15.2, 14.9, 16.3, 19.6, 20.8, 23.8, 24.9, 18.4, 21, 22.2, 23.5, 17.6, 18.1, 23.9, 27.4, 21.7, 21, 20.4, 14.8, 14.8, 20.6, 21.7, 15.9, 11.1, 16.6, 22.6, 22.7, 21.9, 24.9, 23.2, 24.5, 23.7, 15.7, 21.2, 14.2, 17.3, 22.2, 24.9, 18.8, 21.1, 24.2, 18, 23.7, 26.9, 30.4, 27, 23.2, 23.3, 25.6, 25.9, 22, 27.7, 30.8, 26.6, 22.9, 28.6, 14.6, 23, 27.3, 22, 22, 19.9, 16, 16.8, 17.2, 17.6, 18.9, 21.8, 25.1, 27.7, 22.1, 23, 23.8, 24.9, 28.9, 30.3, 28.4, 30.4, 27.9, 26.9, 31.4, 20.8, 22.3, 25.8, 23.4, 20.2, 23.1, 24.2, 24, 27.7, 29.6, 30.5, 18.4, 19.3, 18.3, 23.5, 24, 22.8, 21.1, 24, 23.7, 25.4, 25.5, 27.3, 19.8, 23.8, 18.4, 19.4, 14.9, 16.3, 21.5, 23.5, 24.8, 23.8, 19.7, 22.1, 21.8, 16.2, 17.4, 18.4, 18.8, 19.2, 21.4, 21.6, 20.6, 16.4, 15.3, 14.4, 16, 16.3, 19.7, 20.3, 17.6, 14, 9.5, 10.7, 10.3, 8.7, 9.5, 9.4, 11.8, 13.4, 13.7, 13.2, 9.4, 12.9, 12.2, 13.3, 12.7, 12.1, 12.2, 10.3, 13.5, 15.5, 15.2, 14.7, 11.6, 13.4, 14.3, 12.7, 11.3, 12.8, 14.4, 12.7, 14.5, 16.2, 11.6, 10.7, 10.7, 13.1, 11.1, 14.5, 12.3, 14, 14.5, 11.4, 12.1, 11, 10.7, 11.5, 12.2, 12.4, 6.1, 8.2, 7.3, 8, 6.1, 7, 8.4, 6.8, 5.2, 8.1, 9, 6.9, 7, 6.5, 1.9, -1, 4, 2, 3.2, 4.3, 7, 5, 6.7, 1.7, 3.6, 2.4, 3.6, 1.7, 0.7, 4.2, 4, 3.7, 3.6, 2.6, 4.1, 2.9, 2, -1.6, -2.5, -3.9, -0.5, 0, 0.3, -1.3, -4.2, -1.1, -1.2, 0.8, 5.2, 9.3, 8.9, 6.4, 10.4, 3.2, 1.1, 1.7, 4.2, 7.1]
Tav_22=[11.2, 5.9, 6.3, 7.8, 7.7, 1.9, -2.9, -0.8, -0.6, 2, -0.5, -3.9, -0.7, 1.5, 2.3, -1.8, 3.2, 2.3, -0.1, 2.2, -1.4, 0.9, 1.6, 1.4, 0.5, 1, 3.2, 3, 3.7, 6.3, 3.2, 2.4, 3.9, 4.9, 5.2, 4.4, 4.4, 4.8, 4.1, 8.5, 5.4, 5.5, 4.9, 2.9, 1.1, 3, 8.1, 12.1, 9, 8.8, 5.1, 8.2, 5.4, 7.4, 5.8, 6.5, 3.8, 4.4, 2.4, 0, 1, 1.9, 0.5, 1.7, 0.6, 0.5, 2.8, 3.7, 2.5, 0.8, 4.2, 5.3, 6.3, 7.1, 8.4, 7.2, 6.9, 5.1, 6.9, 6.8, 8.2, 10.5, 12.3, 9.7, 10.4, 10.9, 12.1, 13.3, 11.8, 9.3, 4, 2, 1.6, 3.8, 6.8, 13.7, 13.1, 11.1, 8.4, 6.2, 7.3, 9.1, 13.6, 14.8, 15.8, 9.4, 7.6, 5.8, 5, 8.1, 8.9, 10.4, 10.6, 13, 12.5, 10.5, 9.6, 12.6, 12, 12.8, 13.4, 14.6, 14.8, 16, 16.5, 14.1, 14.2, 15.7, 17.6, 17, 20, 21.4, 20, 17.6, 17.9, 20.1, 19.9, 15.4, 16.9, 22.8, 22.6, 18.7, 17.6, 18.6, 16, 17.3, 18.5, 16.5, 11.8, 14.2, 17.4, 19.2, 19.1, 21.6, 23.9, 22.2, 21.6, 19.3, 19.6, 17.5, 15.5, 19.4, 20.6, 20.2, 18, 19.1, 21.7, 21.3, 21.6, 24.7, 24.3, 21.4, 20.3, 23.2, 23.4, 20.6, 22.1, 25.8, 25.1, 23.8, 24.1, 21.6, 18.9, 22.1, 22.7, 20.5, 19.3, 17.2, 15.8, 18.7, 17.8, 17.6, 19.1, 20.9, 24.7, 21.9, 19.1, 20.3, 20.3, 22.9, 25, 24.6, 26.1, 26.6, 25.2, 25.6, 25.1, 20.2, 21.1, 21, 20.7, 21.5, 22, 21.9, 23.4, 24.1, 26.3, 24.5, 19.4, 18, 19.8, 19.7, 19.2, 19, 20.8, 22.3, 22.6, 23.2, 25.1, 25.4, 23.2, 20.8, 18.3, 17.1, 15.7, 20.9, 22.8, 23.1, 23.3, 21.2, 21.9, 20.8, 18.3, 17.5, 15.7, 16.6, 19.4, 19.6, 19.3, 20.7, 18.8, 16.7, 17.1, 16.5, 17.4, 16.3, 20.3, 19.2, 15.6, 11.7, 10.5, 10.1, 11, 11.1, 11.1, 10.1, 10.6, 13.4, 14.8, 11.4, 12.5, 11.9, 12.4,13.4, 12.3, 13.2, 13.8, 11.4, 16.1, 16.6, 15.3, 12.3, 14.1, 15, 13, 11.3, 13, 12, 14.2, 16.7, 15, 15.4, 10.1, 9.4, 11.1, 11.5, 15.1, 15.2, 10.7, 15.6, 12.1, 12.6, 11, 10.3, 11.8, 13.8, 12.7, 9.1, 8.1, 8.5, 9.1, 5.2, 6.4, 8.8, 7, 7.4, 7.9, 9.9, 7, 7.4, 6.5, 5.2, 0.1, 2.3, 4.3, 2.2, 2.4, 5.8, 5.9, 6.4, 4.2, 2.7, 4.1, 3, 2.1, 0.8, 2.9, 5.1, 2.9, 2.7, 3.8, 2.8, 2.8, 2, 0, -2.6, -5.4, -4.5, 0, 0.4, -0.5, -5.3, -3.4, -1.1, -0.4, 1.9, 6.8, 9.5, 8.1, 7, 6.8, 1.7, 1.1, 4.6, 8.1]

T7_20=[-1, -4.3, -1.4, 5.1, 1.9, -3.2, -1.9, 0.6, 4, -0.3, 5.6, -3.3, -0.4, 0.1, -1.6, -0.9, -0.6, -0.3, 1.4, 0.7, -0.4, -1.7, -0.5, -0.6, -1.5, -0.8, -0.9, -0.9, 1.2, 2.9, 6.6, 12.1, 7.4, 7, 5.3, 2.9, -0.5, 0.8, -0.7, -3.4, 0.7, 4.1, 2, 0.8, 5.9, 3.4, -0.8, 2, 6.6, 0.3, 1.7, 4.6, 2.7, 8.4, 6.3, 1.5, 6.1, 1.9, 2.1, -0.3,6.4, 4.6, 6.1, 2.6, -1.2, 4.2, 4.2, 3.2, 1.1, 4.8, 10.9, 9.8, 8.2, 2.1, -2.3, -1.9, 2.3, 6.6, 4.4, 4.7, 7, -0.9, -4.2, -3.2, -3.1, 0.8, 4.1, 3.4, 6.6, 1.2, -2.2,-2.7, -1.4, 3, 5.9, 1.8, 8.8, 5.9, 4.3, 6.9, 9.7, 9.7, 7.4, 12.6, 4.4, 2.4, 5.9, 11.8, 10.6, 11.4, 5.4, 9.3, 6.8, 7.5, 8, 13.4, 7.1, 8.2, 10.4, 14, 12.1, 10.4, 11.2, 8.5, 8.4, 10.1, 6.9, 9.2, 9.8, 12.4, 15.9, 12.8, 5.4, 8, 9.6, 8, 9.3, 12.7, 13.3, 15.7, 15.7, 14.2, 11.1, 14.9, 11.3, 11.6, 10.5, 10.6, 12.3, 9.6, 9, 9.8, 11.6, 13.7, 14.3, 14.3, 12.6, 14.4, 17.5, 12, 14.2, 14.1, 13.9, 16.4, 19.8, 19.2, 14.3, 15.7, 17.5, 14.1, 16, 14.1, 14, 15.2, 19.4, 16.2, 14.9, 16.1, 18.3, 21.1, 19.3, 18.5, 20.8, 20.2, 16.7, 18, 19.7, 22.2, 14.4, 14.7, 18.1, 20.9, 19.1, 13.7, 14, 13.9, 17.3, 15.9, 13.8, 13, 15.3, 16.7, 18.2, 18.6, 17.9, 16.9, 17.4, 17, 18.5, 19.6, 20.6, 19.6, 19.4, 19.1, 18.6, 18.8, 16.3, 13.3, 15.2, 18.1, 18.5, 19.6, 19.6, 19.9, 19.1, 19.6, 20.1, 19.3, 19.4, 18.5, 19.2, 16.8, 16.3, 18.1, 19.8, 18.6, 16.8, 15.6, 15.5, 17.2, 13.4, 17.3, 17.5, 15.1,13.4, 11.5, 12.9, 14.5, 14.1, 17.5, 14.7, 10.8, 11.8, 15.6, 13.9, 14.8, 17.2, 15, 16.9, 14.6, 18.2, 8.6, 8.9, 8.8, 10.5, 12.3, 13.9, 14.8, 14.4, 6.9, 5.7, 8.8, 9.9, 11.5,9.2, 9.3, 13.2, 11.4, 14.5, 7.5, 11, 10.9, 9.4, 11.3, 8.8, 5.5, 6.9, 6.2, 5.2, 6.7, 6.5, 6.6, 6.3, 5.7, 6.8, 8.1, 8.5, 12.4, 10, 10.6, 6.5, 3.1, 8.9, 8.4, 12, 7.9, 13.9, 15, 9.5, 5.8, 0.2, 2, 1.3, 3.3, 5.1, 3.7, 4.9, 5.4, 5.8, 5.1, 5.1, 8, 3, 2, 6.2, -0.1, -3, 2.7, 1.6, 1, 0.5, -1.1, -0.9, 0, 1.3,-5.1, -2.6, -1.7, -0.5, 7.6, 7.4, 6.4, 1.3, 3.5, 0.6, 0.8, 0.4, 1.5, 4.5, 1.2, 2.6, 1.6, 1.1, 0.7, 1.8, 1.2, 1.7, 9.4, 9.6, 3, 0.1, -6.4, -0.3, 0.2, -0.4, 1.5]
T14_20=[4.2, 2, 1.8, 5.3, 3.8, 2.7, 3.4, 3.5, 6.4, 7.6, 6.8, 3.1, 4.8, -0.3, 0, 1.8, -0.2, 1, 1.1, 2.4, 0.1, -0.8, 4.7, 2.2, -0.2, -0.5, 6.2, 1.7, 3.9, 7.3, 14.1, 16.2, 12.6, 6, 5.6, 3.6, 3.9, 4.6, 4, 7.5, 8.9, 4.2, 6.1, 9.4, 7.5, 10.8, 9, 11.2, 10.5, 9.4, 7.6, 6.1, 12.2, 10.4, 7.5, 14.9, 6.1, 6.9, 4.1, 5.9, 9, 12.1, 6.4, 8, 13.6, 10.2, 8.8, 8.7, 8.5, 11.1, 15.3, 19.4, 9.2, 9.2, 11.4, 15.6, 14.5, 18.8, 18.8, 18.4, 4.2, 0.4, 3.1, 6, 2, 7.1, 15.6, 17.6, 12.5, 5.7, 5.4, 7.8, 13.2, 14.8, 13.8, 16.8, 21.4, 20.6, 22.7, 23.4, 20.1, 18.8, 23.2, 21.5, 8.1, 14.9, 22.4, 24.8, 18.4, 12, 16.1, 16, 17.9, 19.5, 21.7, 18.1, 17.4, 20.2, 24.6, 13.4, 22.3, 18.8, 16.5, 13.4, 19.1, 14, 14.2, 19.1, 24.1, 26.9, 20.1, 20.1, 12.3, 15.3, 12.8, 8.3, 17.5, 22.3, 25.5, 24.2, 20.2, 20.6, 20.6, 23, 17.2, 10.9, 11.2, 18.8, 12.3, 13.8, 12.9, 9, 18.2, 19.9, 22.1, 23.8, 14.5, 25.6, 26.6, 15.9, 16.8, 15.1, 21.3, 25.9, 27.5, 16.1, 16, 19.5, 19.9, 19.8, 21.3, 15.3, 13.9, 22.7, 23.7, 20.4, 21.6, 25.5, 29, 30.7, 17.7, 26.2, 29.8, 26.8, 21.6, 26, 28.1, 28.1, 19.9, 25.6, 28.9, 33.9, 15.5, 20.1, 22.9, 24.1, 27.3, 17, 15.4, 14.9, 19.7, 25.6, 27.8, 24.9, 25.9, 23.3, 24.4, 21.2, 27.5, 32.9, 26.7, 29.4, 30.3, 28, 26.3, 19, 14.7, 14.5, 24.2, 28.7, 30.6, 30.3, 30.5, 27.7, 28.8, 30, 24.2, 25.5, 25.3, 25.5, 21.5, 20.8, 27.5, 30.3, 29.5, 24.4, 22.4, 24.3, 28.8, 23.9, 26.8, 20.9, 23.2, 18.3, 15.1, 20, 20.9, 24.3, 26.5, 18.5, 17.4, 21.7, 23.5, 23.5, 23.2, 25.1, 26.5, 26.7, 27.8, 26.2, 21.1, 18, 21.2, 22.8, 23.3, 26.2, 19.1, 23.4, 14.8, 10.1, 15.6, 10.6, 11.8, 15.7, 18.3, 18.8, 22.3, 18.7, 12.1, 18.1, 13.9, 16.5, 20.3, 18.1, 9.4, 8, 6.8, 8.2, 10.2, 7.3, 7.9, 11.6, 12, 13.8, 10.5, 11.4, 12.2, 15.3, 11.2, 13.1, 7.5, 11.9, 11.9, 11.9, 15.2, 11.8, 18.3, 18, 10.8, 10.1, 9.6, 10.1, 3.8, 5.1, 5.8, 5.8, 8.1, 7.4, 9, 5.9, 8.2, 11.1, 11.2, 6.3, 6.8, 5.1, 5.4, 6.4, 1.4, 1.1, 0.7, -0.2, 0.7, 3.1, 4.3, -0.5, -0.5, 0.5, 4.5, 13.9, 9, 7.9, 5.7, 3.6, 1.7, 4, 2.6, 4.3, 7.4, 3.3, 2.7, 2.7, 2.3, 1.8, 2.2, 2.4, 7.1, 12.7, 9, 1.9, 1.4, 3.3, 0.7, 7.4, 2.8, 5.6]
T19_20=[-0.4, -2, 1.9, 3.7, 0, -1.6, 2.8, 3.1, 2, 5.2, 3.4, -0.8, 1.5, -0.3, -0.4, 0.4, 0.1, 1.8, 1.5, 1.8, -0.5, -1.1, 0.7, -0.1, -0.1, -0.7, 0.9, 3.9, 2.9, 3.8, 12.6, 10.9, 10, 6.5, 2.4, 2.2, 2.1, 1.7, 1, 2.2, 8.5, 5, 2.4, 5.6, 6.9, 7.4, 8.6, 9, 6.5, 4.3, 6.1, 5.2, 10.4, 14.5, 7, 11.4, 2.5, 4.9, 1.9, 5.6, 7.9, 10.9, 5, 5.2, 8.9, 8.2, 4.3, 5.3, 6.6, 7.9, 13.2, 16.6, 8.3, 6, 7, 11.4, 11.1, 14.1, 14.9, 15.2, 3.5, 0.5, 1.8, 3.5, 1.4, 5.2, 11.6, 15, 9.1, 3.3, 2.6, 5.7, 9.7, 11.5, 10.7, 13.2, 15.9, 16.9, 17.3, 18.6, 17.5, 15.9, 18.8, 11.3, 6.6, 12.4, 18, 20, 17.1, 11.7, 13.6, 13.6, 15, 16.5, 18.6, 14.3, 15.3, 15.1, 20.8, 12.4, 19.5, 16.3, 13.1, 11.9, 15.6, 11.3, 13.4, 17.9, 19.8, 22.3, 19, 15.8, 10.9, 11.4, 12.4, 9.1, 16.3, 19.8, 23, 21.1, 18, 19.1, 19.6, 15.5, 14.5, 10.7, 12.3, 18.5, 13, 12.1, 13.3, 9.3, 19.9, 14.9, 16.4, 20.2, 17.5, 23.7, 12.7, 14.8, 17.7, 16.2, 21.7, 24.8, 26.6, 16.8, 16, 19.6, 20.1, 19.7, 16.6, 14.4, 15, 23.9, 22.8, 16.9, 19.9, 22.2, 27.5, 27.9, 19.9, 25.2, 19.1, 20.8, 21, 23.8, 27, 17.2, 19.8, 24.4, 24.1, 30.1, 14.7, 19.8, 21.1, 22.3, 21.3, 15, 14.8, 15, 20.1, 25.3, 21.1, 24, 24.9, 17.4, 19.9, 22, 25.3, 30.6, 24.5, 27.2, 28.4, 26.9, 21.6, 18.1, 13, 15.1, 23.3, 25.6, 26.2, 25.3, 27.8, 24.2, 26.9, 21, 24.2, 20.4, 23.3, 22.7, 19, 19.6, 24.4, 28.3, 19.5, 21.5, 19.7, 20.2, 24.3, 20.6, 23.8, 19.9, 20.1, 16.5, 13.6, 16.5, 16.8, 20, 23.5, 15.7, 15.9, 17.6, 19.6, 18.8, 20.4, 21.3, 21, 22.5, 23.3, 21, 17.7, 12.6, 16.1, 17.5, 20.4, 21.3, 17.4, 18.5, 9.3, 8.7, 10.7, 10, 11.6, 13.9,12.1, 16.4, 21.3, 13.9, 9.7, 12.7, 12.4, 10.7, 15, 10.5, 6.9, 7.5, 6.1, 7.4, 8.6, 6.6, 7.7, 7.4, 7.3, 9, 7.2, 9.3, 9.4, 13.2, 11, 11.1, 7.3, 8.4, 9, 12.7, 10.6, 10.4, 14.8, 15.3, 9.9, 6, 3.9, 4.5, 3.4, 5.6, 4.9, 5.4, 6.2, 6.1, 5.6, 6.3, 7.3, 6.5, 7.2, 8.8, 4.3, -0.1, 2.8, 5.4, 1.8, 1.3, -0.1, -0.3, 1.5, 2.5, 0.6, -0.4, -1.4, -0.7, 3.5, 8.6, 8.8, 6.5, 4.6, 3.2, 1.4, 0.1, 1.7, 3.9, 2.9, 2.8, 2.3, 2.6, 1.7, 1.9, 2.1, 2.4, 9.5, 11.4, 7.5, 2.4, -1.3, 1.3, 3.8, 2.3, 2.2, 1.4]
Tav_20=[1.8, -1.3, 0.9, 4.4, 2, -0.5, 0.2, 1.7, 4.6, 3.9, 4.9, 0, 1.6, 0.4, -0.8, 0.2, -0.1, 0.7, 1.3, 1.6, 0.6, -1, 1.9, 0.3, -1.3, -0.6, 3.2, 1.9, 2.2, 4.7, 8.8, 13.1, 10.3, 9.6, 5.6, 2.9, 2.2, 2.5, 2.3, 2.1, 4.5, 6, 4.2, 5.1, 6, 7.2, 4.7, 6.6, 8.7, 5.2, 4.9, 3.6, 6.8, 11.4, 11.3, 8.3, 6.8, 4.7, 3.9, 2.9, 6.2, 8.6, 8.5, 5.7, 6.3, 7.7, 6.5, 6.5, 4.4, 8, 11.2, 14.6, 12.2, 5.9, 4.6, 7.3, 7.7, 13.1, 11.9, 11.9, 9.2, 1.1, -0.8, 1.7, 0.4, 4, 9, 10.1, 10.4, 5.1, 1.5, 2.6, 5.7, 8.2, 9.7, 8.7, 13.5, 12, 12.2, 13.3, 14.4, 14.1, 14.4, 16.5, 7.3, 8.8, 12.9, 17.6, 14.5, 13.7, 10, 10.6, 11.2, 11.7, 12.9, 15.5, 10.8, 12.8, 15.8, 16.6, 16.4, 15, 13.2, 11.4, 12.4, 12.5, 9.9, 13.5, 15.7, 18.1, 17.4, 18.6, 10.5, 10.9, 11.1, 10, 12.1, 16.6, 17.4, 19, 18.3, 16.2, 14.5, 19.8, 14.2, 12.2, 13.1, 14.6, 13.8, 12.1, 11.9, 10.7, 15, 14.9, 17, 17.2, 16.3, 19.4, 20.2, 13.9, 16.9, 15.7, 18.2, 19.1, 22.5, 21.3, 16, 18.6, 18.2, 18, 18.7, 15.3, 14.3, 20.7, 20.3, 17.2, 18, 21, 23.8, 25.8, 22.8, 21.5, 23.6, 22.4, 20.2, 21.1, 22.2, 23.3, 16.7, 19.4, 22.9, 25.2, 22.4, 17.5, 16.7, 18, 20.2, 18.3, 14.9, 14.8, 18, 21.3, 22.5, 21.4, 21.1, 21.1, 21, 19.5, 22.6, 25.2, 24.7, 23.8, 24.2,22.9, 21.3, 19.7, 15.7, 13.8, 19.7, 22.9, 23.6, 24.2, 24, 22.5, 23.4, 23.7, 22.8, 22.3, 22.8, 22, 20.7, 20.1, 21.3, 23.6, 24, 21.6, 19.5, 19.7, 21.9, 20, 20.1, 20.4, 20.4, 17.2,15, 15.2, 16.9, 18.4, 20.2, 19.6, 15.7, 16.2, 17.9, 19.2, 18.4, 19.7, 21.6, 20.5, 22.1, 19.9, 19.9, 13.2, 14.7, 15.5, 16.7, 19.3, 17.5, 18.7, 14.1, 7.7, 11.1, 9.8, 11, 13.6, 13.9, 14.2, 18.6, 16.4, 13.3, 12.3, 12.2, 13.4, 13.8, 14.8, 8.9, 6.4, 6.8, 7.1, 8, 7.6, 7.6, 9.1, 8.9, 9.9, 7.7, 8.8, 10.4, 12.6, 11.3, 11.6, 8.8, 7.6, 9.7, 10.4, 13.2, 9.1, 14.5, 16.2, 12.4, 8.1, 4.9, 6, 2.6, 4.5, 5.4, 4.9, 6.5, 6.5, 7, 5.7, 5.9, 8.9, 7.1, 5.7, 6.5, 2.4, 1.3, 3.6, 2.9, 1.4, 0.6, -0.6, 0.4, 1.6, 2.6, -2.2, -1.8, -0.6, 1.9, 7.8, 8.5, 7.2, 4.3, 3.8, 1.8, 2.4, 0.2, 2.6, 5.2, 2.5, 2.6, 2.2, 1.7, 1.2, 2.1, 1.9, 5.7, 11.1, 9.5, 4.6, 0.6, -1.4, 1.7, 3.2, 1.1, 3.1]


# monat, von bis (tage), wert
E_gemessen=[[1,1,0,0],[2,1,0,0],[3,10,31,2123],[4,1,30,1600],[5,1,31,987],[6,1,30,562], \
            [7,1,31,330],[8,1,31,250],[9,1,30,406],[10,1,31,1890],[11,1,30,3603],[12,1,31,4840]]
            
#    "10.3.2020 bis 31.3.2020" : 2123,"04 2020" : 1600, "05 2020" : 987, "06 2020" : 562, \
#    "07 2020" : 330, "08 2020" : 250, "09 2020": 406, "10 2020": 1890, "11 2020": 3630, "12 2020" : 4840, \
#    "1.1. 2021 bis 27.1 2021" :  5087 }

Timer_Setting=[[[0,23]], [[0,23]], [[0,21]], [[0,21]], [[5,21]], [[5,9],[15,21]],
               [[0,0]], [[0,0]], [[5,10],[12,21]], [[0,10],[12,23]], [[0,21]], [[0,23]] ]

Area_Setting=[  150, 150, 117, 90, 70, 50,
                0, 0, 50, 80, 140, 150]

wandfl_oben=round((12.8+2*7.5)*2.7+3*(3.5*2+5))
wandfl_unten=round(3.3*(2*5+2*7))
dT=6000/(wandfl_oben+wandfl_unten)  -20
print(dT)
#daten von verbrauchsschätzung von CS3400iAWS
# kWh pro monat [elektrisch zugeführt,erzeugte wärmeengerie]
E_wp=[[1472,4334],[1150,3618],[777,2934],[342,1555],[134,570],
      [51,238],[51,238],[51,238],[103,518],[383,1700],[767,2944],
      [1316,4085]]

cop=[ round(value[1]/value[0],1) for value in E_wp]

class T_av(object):
    
    def __init__(self):
        self.T_arr= np.zeros(24)
        self.T_av=0
        
    def add_val(self,T):
        
       self.T_arr= np.roll(self.T_arr,1)
       self.T_arr[0]=T
       self.T_av=np.mean( self.T_av)
       
       return T_av
       
        
        