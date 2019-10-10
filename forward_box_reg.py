#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 14:40:04 2019

@author: s1420671
"""


from netCDF4 import Dataset
#from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd


date = ['200401','200402','200403','200404','200405','200406','200407','200408',
        '200409','200410','200411','200412','200501','200502','200503','200504',
        '200505','200506','200507','200508','200509','200510','200511','200512',
        '200601','200602','200603','200604','200605','200606','200607','200608',
        '200609','200610','200611','200612','200701','200702','200703','200704',
        '200705','200706','200707','200708','200709','200710','200711','200712',
        '200801','200802','200803','200804','200805','200806','200807','200808',
        '200809','200810','200811','200812','200901','200902','200903','200904',
        '200905','200906','200907','200908','200909','200910','200911','200912',
        '201001','201002','201003','201004','201005','201006','201007','201008',
        '201009','201010','201011','201012','201101','201102','201103','201104',
        '201105','201106','201107','201108','201109','201110','201111','201112',
        '201201','201202','201203','201204','201205','201206','201207','201208',
        '201209','201210','201211','201212','201301','201302','201303','201304',
        '201305','201306','201307','201308','201309','201310','201311','201312',
        '201401','201402','201403','201404','201405','201406','201407','201408',
        '201409','201410','201411','201412','201501','201502','201503','201504',
        '201505','201506','201507','201508','201509','201510','201611','201512',
        '201601','201602','201603','201604','201605','201606','201607','201608',
        '201609','201610','201611','201612']

print(len(date))

region=['australia','europe','eurasianboreal','eurasiantemperate','northafrica',
        'northamericanboreal','northamericantemperate','southamericantemperate',
        'oceans','southamericantropical','southernafrica','tropicalasia']
nregions = len(region)


lati=[12,12,34,36,40,38,34,32,28,27,40,42,27,34, 9,11,27,21,26,24,17,17,22,24]
loni=[65,71,39,34,62,60,58,56,37,35, 5,17,17,18,22,22, 5,33,24,24,39,41,56,56]

nsites = len(lati) 

os.chdir('/geos/d21/s1420671/jacobian/12CH4/14yr/forward/goodsites')

mix = []

for lcount in np.arange(nsites):
    lat = lati[lcount]
    lon = loni[lcount]
    
    for n in np.arange(0,len(date),1):
        methane_12c= 'out.{}01.nc'.format((str(date[n])))
        fh = Dataset(methane_12c, mode='r')  
        CH4 = fh.variables['CH4-EMIS__CH4-TOT'][:]
        fh.close()
        MixR =CH4[0,lat,lon]
        mix = np.append(mix, MixR)
 
    
aus = mix[0:312]
eur = mix[312:624]
eub = mix[624:936]
eut = mix[936:1248]
naf = mix[1248:1560]
nab = mix[1560:1872]
nat = mix[1872:2184]
sat = mix[2184:2496]
oce = mix[2496:2808]
sar = mix[2808:3120]
saf = mix[3120:3432]
tra = mix[3432:3744]
    

    
aus_y=[]
eur_y=[]
eub_y=[]
eut_y=[]
naf_y=[]    
nab_y=[]
nat_y=[]
sat_y=[]
oce_y=[]
sar_y=[]
saf_y=[]
tra_y=[]

yr=0  

for y in np.arange(26):
    aus_y = np.append(aus_y,np.sum(aus[yr:yr+12]))
    eur_y = np.append(eur_y,np.sum(eur[yr:yr+12]))
    eub_y = np.append(eub_y,np.sum(eub[yr:yr+12]))
    eut_y = np.append(eut_y,np.sum(eut[yr:yr+12]))
    naf_y = np.append(naf_y,np.sum(naf[yr:yr+12]))
    nab_y = np.append(nab_y,np.sum(nab[yr:yr+12]))   
    nat_y = np.append(nat_y,np.sum(nat[yr:yr+12]))
    sat_y = np.append(sat_y,np.sum(sat[yr:yr+12]))
    oce_y = np.append(oce_y,np.sum(oce[yr:yr+12]))
    sar_y = np.append(sar_y,np.sum(sar[yr:yr+12]))
    saf_y = np.append(saf_y,np.sum(saf[yr:yr+12]))
    tra_y = np.append(tra_y,np.sum(tra[yr:yr+12]))
    yr=yr+12
  
    
aus_yr = np.zeros((13,), dtype=int)
eur_yr = np.zeros((13,), dtype=int)
eub_yr = np.zeros((13,), dtype=int)
eut_yr = np.zeros((13,), dtype=int)
naf_yr = np.zeros((13,), dtype=int)
nat_yr = np.zeros((13,), dtype=int)
sat_yr = np.zeros((13,), dtype=int)
nab_yr = np.zeros((13,), dtype=int)
oce_yr = np.zeros((13,), dtype=int)
sar_yr = np.zeros((13,), dtype=int)
saf_yr = np.zeros((13,), dtype=int)
tra_yr = np.zeros((13,), dtype=int)

#print(np.add(aus_y[0], aus_y[12]))


for yearcount in np.arange(13):
    aus_yr[yearcount]= np.add(aus_y[yearcount],aus_y[yearcount+12])
    eur_yr[yearcount]= np.add(eur_y[yearcount],eur_y[yearcount+12])
    eub_yr[yearcount]= np.add(eub_y[yearcount],eub_y[yearcount+12])
    eut_yr[yearcount]= np.add(eut_y[yearcount],eut_y[yearcount+12])
    naf_yr[yearcount]= np.add(naf_y[yearcount],naf_y[yearcount+12])
    nat_yr[yearcount]= np.add(nat_y[yearcount],nat_y[yearcount+12])
    nab_yr[yearcount]= np.add(nab_y[yearcount],nab_y[yearcount+12])
    sat_yr[yearcount]= np.add(sat_y[yearcount],sat_y[yearcount+12])
    sar_yr[yearcount]= np.add(sar_y[yearcount],sar_y[yearcount+12])
    saf_yr[yearcount]= np.add(saf_y[yearcount],saf_y[yearcount+12])
    oce_yr[yearcount]= np.add(oce_y[yearcount],oce_y[yearcount+12])
    tra_yr[yearcount]= np.add(tra_y[yearcount],tra_y[yearcount+12])


###
# Saunois data
###

os.chdir('/home/s1420671/Downloads/')

data = pd.read_excel (r'Global_Methane_Budget_2000-2012_v1.1.xlsx', sheet_name=6, header=16) 
CNA = pd.DataFrame(data, columns=['Central North America'])
CNA=CNA.iloc[9:29, 0]

TrSA = pd.DataFrame(data, columns=['Tropical South America'])
TrSA=TrSA.iloc[9:29, 0]

TeSA = pd.DataFrame(data, columns=['Temp. South America'])
TeSA=TeSA.iloc[9:29, 0]

NAF = pd.DataFrame(data, columns=['North Africa'])
NAF=NAF.iloc[9:29, 0]

SAF = pd.DataFrame(data, columns=['South Africa'])
SAF=SAF.iloc[9:29, 0]

SEA = pd.DataFrame(data, columns=['South East Asia'])
SEA=SEA.iloc[9:29, 0]

IND = pd.DataFrame(data, columns=['India'])
IND=IND.iloc[9:29, 0]

AUS = pd.DataFrame(data, columns=['Oceania'])
AUS=AUS.iloc[9:29, 0]

TNA = pd.DataFrame(data, columns=['Temp. North America'])
TNA=TNA.iloc[9:29, 0]

EUR = pd.DataFrame(data, columns=['Europe'])
EUR=EUR.iloc[9:29, 0]

CEJ = pd.DataFrame(data, columns=['Central Eurasia and Japan'])
CEJ=CEJ.iloc[9:29, 0]

CHI = pd.DataFrame(data, columns=['China'])
CHI=CHI.iloc[9:29, 0]

BNA = pd.DataFrame(data, columns=['Boreal North America'])
BNA=BNA.iloc[9:29, 0]

RUS = pd.DataFrame(data, columns=['Russia'])
RUS=RUS.iloc[9:29, 0]



fig=plt.figure()
fig.set_figheight(10)
fig.set_figwidth(15)


data = [AUS,aus_yr/10**8, EUR,eur_yr/10**8,RUS,eub_yr/10**8,CEJ,CHI,IND,eut_yr/10**8,NAF,
        naf_yr/10**8,SAF,saf_yr/10**8,BNA,nab_yr/10**8,TNA,CNA,nat_yr/10**8,TeSA,sat_yr/10**8,
        TrSA,sar_yr/10**8,SEA,tra_yr/10**8, oce_yr/10**8]

plt.rc('font', size=13)
box = plt.boxplot(data, patch_artist=True)

colors = ['blue', 'green', 'blue', 'green', 'blue', 'green','blue','blue',
          'blue','green','blue', 'green','blue', 'green','blue', 'green',
          'blue','blue', 'green','blue', 'green','blue', 'green',
          'blue', 'green','blue', 'green','green']
 
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    

plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26],
           ['Oceania','Oceania -GC','Europe',
           'Europe -GC','Russia','Eurasian Boreal -GC','Central Eurasia','China',
           'India','Eurasian Temperate -GC','North Africa','North Africa -GC',
           'Southern Africa','Southern Africa -GC','Boreal North America',
           'Boreal North America -GC','Temperate North America',
           'Central North America','Temperate North America -GC','Temperate South America',
           'Temperate South America -GC','Tropical South America',
           'Tropical South America -GC',
           'South East Asia','Tropical Asia -GC','Oceans -GC'], rotation=90)

#plt.ylim(-10,150)

plt.ylabel('CH4 emissions (Tg/yr)')
plt.tight_layout()
#os.chdir("/home/s1420671/python/Timeseries_Plots/long_inversion/CH4/inv_goodsites")
#plt.savefig("box_regions.jpg")


     