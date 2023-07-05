#https://www.haustechnikverstehen.de/berechnung-der-leistung-einer-waermepumpe/

#SCOP = (Σ (COPi * HLwi * Ti)) / (Σ (HLwi * Ti))
#SCOP: Seasonal Coefficient of Performance
#COPi: Coefficient of Performance bei der Außentemperatur i
#HLwi: Gewichtungsfaktor für die Heizlast bei der Außentemperatur i
#Ti: Zeitanteil (häufigkeitsgewichteter Anteil) der Außentemperatur i über die Heizperiode

#leistung Luftwärmepumpe
#Leistung (kW) = Heizlast (kW) / COP
#Heizlast (kW) = Volumen (m³) * U-Wert (W/m²K) * Temperaturdifferenz (K)
# 150*3* 2.5 *40 / 2

import data
import data_interpol
import numpy as np

def COP(Tv,Ta):
    
    COP=4
    
    return COP

def Tempvorlauf(Ta_av_day):
    #Ta=> Tav day verwenden
    #bei 22* => Tvl = 30
    #bei -10 => Tvl = 65
    #lineare anpassung (Regler)

    
    return 55.85-(32/35)*Ta_av_day
    
def uWert_function(x, x0):
    if x >= x0:
        return 1
    else:
        return 1+((x-x0)**2)/75
    
##################################################################################

def PowerRequirement(Ta,Heiz_on,Area_Setting,Tinnen):
    #Effekte der effizienz von pufferung modulierung und regelung NICHT beachtet
    
    #energieverbrauch in kW
    Pww=400 #konst aufheizen des warmwasserspeichers
    Tww=50#warmwassertemp
    
    Pelww=Pww*COP(Tww,Ta)
    
    #u werte von https://www.heizsparer.de/heizung/heiztechnik/heizleistung-berechnen
    
    if Heiz_on == 1:
    #if Ta<=Tinnen and Ta_av_av<= 17 and Ta_max< 23:#wann wird die heizung ausgeschalten ?
        
       # Aheiz=75                   
        #if Ta_av_av<= 15 or Ta_max< 22:
        Aheiz=Area_Setting
        uwert=2.15
##BESSERES MODEL NÖTIG        
        # Muss man mit wandfläche berechnen, nicht mit bodenfläche!
        # bei mir dann aussentemp im winter immer um 8 grad herum ?
        # Ausser bei front wänden
        # eigentlicher u wert ca 0.5 
        # 
        #uWert_function(Ta_av_av,5)
        Pheiz= uwert* Aheiz * (Tinnen-Ta)
        
    else:
        Pheiz=0

    Pelheiz=Pheiz*COP(Tempvorlauf(Ta),Ta)
    
    
    return (Pww+Pheiz)/1000,(Pelww+Pelheiz)/1000

##################################################################################

def est_power_for_measured_period(T_ip,Tinnen) :
    # sucht die gemessenen tage aus E_gemessen und 
    # rechnet nur an diesen, mit den tempdaten von T_ip_1
    # den verbrauch aus
    Ew=[]
    EwMonth=[]
    total_sum=0
    days_cumsum =0;    

    for monat in range(len(data.E_gemessen)) :
        EWärmeSumtemp=0
        for tag in range(data.E_gemessen[monat][1]-1,data.E_gemessen[monat][2]) :
            for hour in range(24) :
                Heiz_on=0
                for i in range(len(data.Timer_Setting[monat])):
                    if  data.Timer_Setting[monat][i][0] <= hour and hour <= data.Timer_Setting[monat][i][1] :
                        #print(hour)
                        Heiz_on=1
                
                Pw,Pel = PowerRequirement(T_ip_day_av,T_ip[hour +tag*24 + days_cumsum*24 ],Heiz_on,data.Area_Setting[monat],Tinnen)
                Ew.append(Pw)
                EWärmeSumtemp+=Pw
                total_sum+=Pw
                
        EwMonth.append(int(EWärmeSumtemp))
        days_cumsum+=data.daysPerMonth_20[monat]
        
    
    EwMonth =[int(value) for value in EwMonth]    
    
    return int(total_sum), EwMonth, Ew

##################################################################################

def est_power(T_ip,Tinnen):

    hoursPerMonth=[value*24 for value in data.daysPerMonth_20]
    hoursPerMonthCS = np.cumsum(hoursPerMonth).tolist()
    
    Ew=[]
    EwMonth=[0]
    total_sum=0
    T_ip_day_a=[]
    
    for hour in range(len(T_ip)):
        
       # T_ip_day_a.append(T_ip[hour])
      #  if len(T_ip_day_a)>=24 :
      #      T_ip_day_a.pop(0)
        
        hour_of_day=hour%24
        Heiz_on=0
        
        for hour_of_timer in range(len(data.Timer_Setting[len(EwMonth)-1])):
            if  data.Timer_Setting[len(EwMonth)-1][hour_of_timer][0] <= hour_of_day \
                and hour_of_day <= data.Timer_Setting[len(EwMonth)-1][hour_of_timer][1] :
                    
                Heiz_on=1        
        
        Pw,Pel = PowerRequirement(T_ip_day_av,T_ip[hour],Heiz_on,data.Area_Setting[len(EwMonth)-1],Tinnen)
        
        Ew.append(Pw*1)# leisuntg in kW * 1 h
        EwMonth[-1]+=Pw*1
        total_sum+=Pw
        
        if hour >= hoursPerMonthCS[0]:
            EwMonth.append(0)
            hoursPerMonthCS.pop(0)
         
    for monat in range(len(EwMonth)) :
        EwMonth[monat]=int (EwMonth[monat])
           
    return [int(total_sum), EwMonth, Ew]
        