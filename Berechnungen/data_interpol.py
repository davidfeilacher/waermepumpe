import matplotlib.pyplot as plt
import math
import csv
import numpy as np
from scipy.optimize import minimize

##################################################################################

def temp_year_f(print) :
    
    yeaer_adapt_avg_T=1.2
    year_max_avg_T=17.5
    year_min_avg_T=-3
    year_avg_T=10
    year_phase_d=20*24

    
    list_days = range(0, 365*24)
    list_days_inpie=[ (value*((math.pi*2)/(365*24))) for value in list_days]

    Temperature=[year_avg_T -(yeaer_adapt_avg_T*(year_max_avg_T-year_min_avg_T)/2)*math.cos(value-year_phase_d*(math.pi*2)/(365*24))  for value in list_days_inpie]

    if print=="on":
        plt.plot(list_days_inpie, Temperature)
        plt.xlabel('Tage')
        plt.ylabel('Temperatur')
        plt.title('...')
        plt.xlim(0, math.pi*2)  
        plt.ylim(-20, 30)  
        plt.show()
        
    return Temperature
        
 ##################################################################################
        
def temp_daily(print) :
    
    deltaT=10# zufallsgenerator für schwankungen ?
    
    list_hours = range(0, 24)
    list_hours_inpie=[ (value*((math.pi*2)/24)) for value in list_hours]

    Temperature=[ -(deltaT/2)*math.cos(value)  for value in list_hours_inpie]

    if print=="on":
        plt.plot(list_hours_inpie, Temperature)
        plt.xlabel('Tage')
        plt.ylabel('Temperatur')
        plt.title('...')
        plt.xlim(0, math.pi*2)  
        plt.ylim(-10, 10)  
        plt.show()
        
    return Temperature

##################################################################################

def remp_comb (print):
    
    temp_comb=[]
    temp_year=temp_year_f("off")
    temp_day=temp_daily("off")
    for i_year in range(0,len(temp_year),len(temp_day)) :
        for i_day in range(0,len(temp_day)):
            temp_comb.append( temp_year[i_year]+temp_day[i_day] )
        #print(i_year)
        
    hours = range(0,len(temp_year))
    if print=="on":
        plt.plot(hours, temp_comb)
        plt.xlabel('Tage')
        plt.ylabel('Temperatur')
        plt.title('...')
        plt.xlim(0, len(hours)) 
        plt.ylim(-20, 30)  
        plt.show()
    
    return temp_comb

##################################################################################

def read_zamg_data() :
    
    csv_file_path = 'ZAMG_Jahrbuch.csv'
    data=[]

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        #csv_reader = csv.DictReader(file)
        
        i = 0
        for row in csv_reader:
            
            data.append([])
            for value in row:
                data[i].append(value)
            i=i+1
         
    for i in range(len(data)) :
        data[i].pop(0)   
           
    data.pop(0)     
    
    plt.plot(range(len(data[0])), data[0], label='T7')
    plt.plot(range(len(data[1])), data[1], label='T14')
    plt.plot(range(len(data[1])), data[1], label='T19')
    #plt.plot(range(len(data[1])), data[1], label='T14')
    
    plt.xlabel('Tage')
    plt.ylabel('Temperatur')
    plt.title('...')
    #plt.xlim(0, len(hours)) 
    #plt.ylim(-20, 30)  
    plt.show()
    
    return data

##################################################################################

def target_func(x, O, A, P):
    return O + A * np.cos(x + P)

##################################################################################

def error_func(params, x, y):
    O, A, P = params
    y_pred = target_func(x, O, A, P)
    return np.sum((y - y_pred) ** 2)

##################################################################################

def find_cosine_parameters(x, y):

    initial_params = [1.0, 1.0, 0.0]
    result = minimize(error_func, initial_params, args=(x, y))
    [O,A,P] = result.x

    return O,A,P

##################################################################################

def interpolate_real_data_cos(T7,T14,T19,noCos):
    assert len(T7) == len(T14) and len(T19) == len(T14), "listen müssen gleich lang sein"

    T_ip=[]
    assert noCos%2==0, "noCos muss gerade zahl sein"
    
    #print("len(T7)" + str(len(T7)))
    
    for i in range(0,len(T7)) :
        x=[]
        y=[]
        for j in range(math.floor(-noCos/2),math.ceil(noCos/2)):
                     
            if i+j >=0 and i+j <= len(T7)-1:
                x.append([(7/24+24*j)*(2*math.pi),(14/24+24*j)*(2*math.pi),(19/24+24*j)*(2*math.pi)])
                y.append([T7[i+j],T14[i+j],T19[i+j]])
                
            elif i+j <0:                
                 x.append([(7/24+24*j)*(2*math.pi),(14/24+24*j)*(2*math.pi),(19/24+24*j)*(2*math.pi)])
                 y.append([T7[0],T14[0],T19[0]])
                 
            elif i+j >len(T7)-1:   
                 x.append([(7/24+24*j)*(2*math.pi),(14/24+24*j)*(2*math.pi),(19/24+24*j)*(2*math.pi)])
                 y.append([T7[len(T7)-1],T14[len(T7)-1],T19[len(T7)-1]])
            
            
        if find_cosine_parameters(x, y) == -1:
            
            continue
        else:
            O, A, P = find_cosine_parameters(x, y)
        
        x_24=range(24)
        x_24=[ (value*math.pi*2)/24 for value in x_24]         
        y_24=[ O+ A * math.cos(value + P) for value in x_24]  
       # print(x_24)
        T_ip=T_ip+y_24
       # print("len(i)" + str(i))
       # print("len(T_ip)" + str(len(T_ip)))
    
    return T_ip

##################################################################################

def interpolate_real_data_poly(T7,T14,T19):
    assert len(T7) == len(T14) and len(T19) == len(T14), "listen müssen gleich lang sein"
    T_ip=[]
    x=[]
    y=[]
    
    
    for i in range(0,len(T7)) :
        #x.append(24*i+7)
        #x.append(24*i+14)
        #x.append(24*i+19)
        x.append(7)
        x.append(14)
        x.append(19)
        y.append(T7[i])
        y.append(T14[i])
        y.append(T19[i])
    
    no_values=8
     
    for i in range(0,len(x),3) :
        
        # if i>=1 and i<=len(T7)-2:
        #     x=[-17,-10,-5,7,14,19,31,38,43]
        #     y=[T7[i-1],T14[i-1],T19[i-1],T7[i],T14[i],T19[i],T7[i+1],T14[i+1],T19[i+1]]
            
        # if i==0:
        #     x=[7,14,19,31,38,43,55]
        #     y=[T7[i],T14[i],T19[i],T7[i+1],T14[i+1],T19[i+1],T7[i+2]]
            
        # if i == len(T7)-1:
        #     x=[-29,-17,-10,-5,7,14,19]
        #     y=[T19[i-2],T7[i-1],T14[i-1],T19[i-1],T7[i],T14[i],T19[i]]
       
        
        
        y_int=[]
        
        for j in range(-math.floor(no_values/2),math.ceil(no_values/2)) :
            if i+j >=0 and i+j <= len(y)-1:
                x_int=[-29,-17,-10,-5,7,14,19,31]
                y_int.append(y[i+j])
               
            else:
                continue
        #print("xlen"+str(len(x_int)))
        #print("ylen"+str(len(y_int)))
                    
        if len(x_int) != len(y_int):
            continue
            raise ValueError("Die Listen müssen die gleiche Länge haben")

        # Erstellen der Vandermonde-Matrix
        vander = np.vander(x_int, increasing=True)

        # Lösen des Gleichungssystems
        coefficients = np.linalg.solve(vander, y_int)

        # Koeffizienten in umgekehrter Reihenfolge (höchster Grad zuerst)
        coefficients = np.flip(coefficients)

        hour_vals=[]
        
        for j in range(-12,12):
            hour_vals.append(np.polyval(coefficients, j))
            
        T_ip = T_ip+hour_vals
         
    return T_ip 

