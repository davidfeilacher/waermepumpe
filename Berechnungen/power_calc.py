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


def COP(Tv,Ta):
    
    COP=4
    
    return COP

def Tempvorlauf(Ta):
    #bei 22* => Tvl = 0
    #bei -10 => Tvl = 65
    #lineare anpassung
    #ToDo : Stufenweise anpassen (wie in realität manuell)
    #BZW haben die COP kurven ja nur für bestimmte Vrltemp ?
    
    return 22-(1/2)*Ta
    
def uWert_function(x, x0):
    if x >= x0:
        return 1
    else:
        return 1+((x-x0)**2)/75
    
##################################################################################

def PowerRequirement(Ta,Heiz_on,Area_Setting):
    #Effekte der effizienz von pufferung modulierung und regelung NICHT beachtet
    
    #energieverbrauch in kW
    Pww=400 #konst aufheizen des warmwasserspeichers
    Tww=52#warmwassertemp
    
    Pelww=Pww*COP(Tww,Ta)
    
    #u werte von https://www.heizsparer.de/heizung/heiztechnik/heizleistung-berechnen
    
    Tinnen=21.5
    
    if Heiz_on == 1:
    #if Ta<=Tinnen and Ta_av_av<= 17 and Ta_max< 23:#wann wird die heizung ausgeschalten ?
        
       # Aheiz=75                   
        #if Ta_av_av<= 15 or Ta_max< 22:
        Aheiz=Area_Setting
        uwert=2.4
        
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

def est_power_for_measured_period(T_ip) :
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
                
                Pw,Pel = PowerRequirement(T_ip[hour +tag*24 + days_cumsum*24 ],Heiz_on,data.Area_Setting[monat])
                Ew.append(Pw)
                EWärmeSumtemp+=Pw
                total_sum+=Pw
                
        EwMonth.append(int(EWärmeSumtemp))
        days_cumsum+=data.daysPerMonth_20[monat]
        
    for monat in range(len(data.E_gemessen)) :
        data.E_gemessen[monat]=data.E_gemessen[monat][3]
        
    EwMonth =[int(value) for value in EwMonth]    
    
    return int(total_sum), EwMonth, Ew

##################################################################################

