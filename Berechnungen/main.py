import matplotlib.pyplot as plt
import math
import data_interpol
import power_calc
import data
import numpy as np

T7,T14,T19, Tav = data.T7_20, data.T14_20, data.T19_20, data.Tav_20

#T_ip=utility.interpolate_real_data_poly(T7,T14,T19)
T_ip_1=data_interpol.interpolate_real_data_cos(T7,T14,T19,2)
#T_ip_2=data_interpol.interpolate_real_data_cos(T7,T14,T19,4)
T_ip_av=[]

#for i in range(len(T_ip_1)):
#    T_ip_av.append((T_ip_1[i]+T_ip_2[i])/2)
T_ip_av=T_ip_1

remp_comb_app=data_interpol.remp_comb("off")
T7_app=[]
T14_app=[]
T19_app=[]
Tav_app=[]

for i in range(7,len(remp_comb_app),24) :
    T7_app.append(remp_comb_app[i])
for i in range(14,len(remp_comb_app),24) :
    T14_app.append(remp_comb_app[i])
for i in range(19,len(remp_comb_app),24) :
    T19_app.append(remp_comb_app[i])
    
    
for i in range(0,len(remp_comb_app),24) :  
    sum=0
    for j in range(i,i+24) :
        sum=sum+remp_comb_app[i]
    Tav_app.append(sum/24) 


print(len(T7_app),len(T14_app),len(T19_app))

#plt.plot(range(len(T7)), T7, label='T7')
#plt.plot(range(len(T14)), T14, label='T14')
#plt.plot(range(len(T19)), T19, label='T19')
#plt.plot(range(len(Tav)), Tav, label='Tav')
# plt.plot(range(len(T7_app)), T7_app, label='T7_app')
# plt.plot(range(len(T14_app)), T14_app, label='T14_app')
# plt.plot(range(len(T19_app)), T19_app, label='T19_app')
# plt.plot(range(len(Tav_app)), Tav_app, label='Tav_app')

plt.plot(range(len(T_ip_av)), T_ip_av, label='T_ip_av')
#plt.plot(range(len(remp_comb_app)), remp_comb_app, label='remp_comb_app')



EWärme=[]
EWärmeSum=0
Eel=[]
EelSumMonth=[0]



daysPerMonth=data.daysPerMonth_20

hoursPerMonth=[value*24 for value in daysPerMonth]
hoursPerMonthCS = np.cumsum(hoursPerMonth).tolist()
monthindex=0

# for i in range(len(T_ip_1)):
    
#     Pw,Pel = data_interpol.PowerRequirement(T_ip_1[i])
    
#     EWärme.append(Pw*1)# leisuntg in kW * 1 h
#     EWärmeSumMonth[-1]+=Pw*1
#     EWärmeSum+=Pw
    
#     if i >= hoursPerMonthCS[0]:
#         EWärmeSumMonth[-1]=EWärmeSumMonth[-1]
#         EWärmeSumMonth.append(0)
#         hoursPerMonthCS.pop(0)
    
    
  

total_sum,EwMonth, Ew=power_calc.est_power_for_measured_period(T_ip_1)
    
SumE_gemessen=0
for x in data.E_gemessen:
    SumE_gemessen+=x   
    
    
print ("schätzwerte",EwMonth ,total_sum)
print ("messwerte  ",data.E_gemessen, SumE_gemessen)


plt.plot(range(len(EWärme)), EWärme, label='EWärme')

plt.xlabel('Stunden')
plt.ylabel('Temperatur')
plt.title('...')
plt.legend()
#plt.xlim(0, len(hours)) 
#plt.ylim(-20, 30)  

#plt.show()