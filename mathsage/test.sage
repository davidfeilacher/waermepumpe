restart
var('O,A,P,x1,x2,x3,y1,y2,y3')

y1_=O+A*cos(x1+P)
y2_=O+A*cos(x2+P)
y3_=O+A*cos(x3+P)

eqc=(y1-y1_)^2+(y2-y2_)^2+(y3-y3_)^2

deqo=eqc.diff(O)==0
deqa=eqc.diff(A)==0
deqp=eqc.diff(P)==0

solve([deqo,deqa,deqp],[O,A,P])