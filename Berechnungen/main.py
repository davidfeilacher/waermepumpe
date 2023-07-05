import matplotlib.pyplot as plt
import math
import data_interpol
import power_calc
import data
import numpy as np
import general_util
import multiprocessing
import time

if __name__ == '__main__':
    
    start_time = time.time()
    
    pool = multiprocessing.Pool(processes=4)
    
    res1 = pool.apply_async(data_interpol.interpolate_real_data_cos,
                            (data.T7_20, data.T14_20, data.T19_20,2))
    res2 = pool.apply_async(data_interpol.interpolate_real_data_cos,
                            (data.T7_22, data.T14_22, data.T19_22,2))
    res3 = pool.apply_async(data_interpol.interpolate_real_data_cos,
                            (data.T7_20, data.T14_20, data.T19_20,4))
    res4 = pool.apply_async(data_interpol.interpolate_real_data_cos,
                            (data.T7_22, data.T14_22, data.T19_22,4))
    
    T_ip_1_20=res1.get()
    T_ip_1_22=res2.get()
    T_ip_2_20=res3.get()
    T_ip_2_22=res4.get()
    T_ip_20=[]
    T_ip_22=[]
    
    for i in range(len(T_ip_1_20)):
        T_ip_20.append((T_ip_1_20[i]+T_ip_2_20[i])/2)
    for i in range(len(T_ip_1_22)):
       T_ip_22.append((T_ip_1_22[i]+T_ip_2_22[i])/2)
        
    ###############################################################################
    
    pool = multiprocessing.Pool(processes=3)
    
    res1 = pool.apply_async(power_calc.est_power_for_measured_period,(T_ip_20,21.5))
    res2 = pool.apply_async(power_calc.est_power,(T_ip_20,21.5))
    res3 = pool.apply_async(power_calc.est_power,(T_ip_22,20))
    
    
    [year_sum_meas_per_20,EwMonth_meas_per_20, Ew_meas_per_20] =res1.get()
    [year_sum_20,EwMonth_20, Ew_20] =res2.get()
    [year_sum_22,EwMonth_22, Ew_22] =res3.get()   
    
    SumE_gemessen=0
    E_gemessen=[]

    for x in data.E_gemessen:
        E_gemessen.append(x[3])
        SumE_gemessen+=x[3]   

    print ("messwerte 2020 \n insg ", SumE_gemessen)
    general_util.print_table(E_gemessen)
    
    print ("schätzwerte 2020 während gemessen\n insg " ,year_sum_meas_per_20)
    general_util.print_table(EwMonth_meas_per_20)

    print ("schätzwerte 2020 gesammt\n insg=" ,year_sum_20)
    general_util.print_table(EwMonth_20)

    print ("schätzwerte 2022 gesammt\n insg=" ,year_sum_22)
    general_util.print_table(EwMonth_22)


    end_time = time.time()
    elapsed_time = end_time - start_time
    print("TIME PARALLEL = ",elapsed_time)
    #########################################################################


    remp_comb_app=data_interpol.remp_comb("off")
    T7_app=[]
    T14_app=[]
    T19_app=[]
    Tav_app=[]

    # for i in range(7,len(remp_comb_app),24) :
    #     T7_app.append(remp_comb_app[i])
    # for i in range(14,len(remp_comb_app),24) :
    #     T14_app.append(remp_comb_app[i])
    # for i in range(19,len(remp_comb_app),24) :
    #     T19_app.append(remp_comb_app[i])
        
        
    # for i in range(0,len(remp_comb_app),24) :  
    #     sum=0
    #     for j in range(i,i+24) :
    #         sum=sum+remp_comb_app[i]
    #     Tav_app.append(sum/24) 


    #print(len(T7_app),len(T14_app),len(T19_app))

    #plt.plot(range(len(T7)), T7, label='T7')
    #plt.plot(range(len(T14)), T14, label='T14')
    #plt.plot(range(len(T19)), T19, label='T19')
    #plt.plot(range(len(Tav)), Tav, label='Tav')
    # plt.plot(range(len(T7_app)), T7_app, label='T7_app')
    # plt.plot(range(len(T14_app)), T14_app, label='T14_app')
    # plt.plot(range(len(T19_app)), T19_app, label='T19_app')
    # plt.plot(range(len(Tav_app)), Tav_app, label='Tav_app')

    plt.plot(range(len(T_ip_1_20)), T_ip_1_20, label='T_ip_1_20')
    plt.plot(range(len(T_ip_1_22)), T_ip_1_22, label='T_ip_1_22')
    #plt.plot(range(len(remp_comb_app)), remp_comb_app, label='remp_comb_app')


    plt.plot(range(len(Ew_20)), Ew_20, label='EWärme_20')
    plt.plot(range(len(Ew_22)), Ew_22, label='EWärme_22')
    plt.xlabel('Stunden')
    plt.ylabel('Temperatur')
    plt.title('...')
    plt.legend()
    #plt.xlim(0, len(hours)) 
    #plt.ylim(-20, 30)  

    plt.show()
    
    