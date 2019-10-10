#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 15:45:22 2019

@author: s1420671
"""

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset


os.chdir('/home/s1420671/Downloads/')

data = pd.read_excel (r'Global_Methane_Budget_2000-2012_v1.1.xlsx', sheet_name=6, header=88) 
df = pd.DataFrame(data, columns=['GLOBAL'])

df=df.iloc[:, 0]

wtl = df[2:21]
otn = df[23:42]
agw = df[44:63]
ffu = df[65:84]
bbn = df[86:105]





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

#print(len(date))

mix = []

os.chdir('/geos/d21/s1420671/jacobian/12CH4/14yr/forward/goodsites')

C12_EMISS = []
C12_og  = []
C12_coal = []
C12_liv = []
C12_wst = []
C12_bfl = []
C12_ric = []
C12_ota = []
C12_bbn = []
C12_wtl = []
C12_otn = []


for n in np.arange(len(date)):
    methane_12c= 'out.{}01.nc'.format((str(date[n])))
    fh = Dataset(methane_12c, mode='r') 
    lons = fh.variables['LON'][:]
    lats = fh.variables['LAT'][:]
    CH4_EMISS = np.append(C12_EMISS, np.mean(fh.variables['CH4-EMIS__CH4-TOT'][:]))
    C12_coal = np.append(C12_coal, np.mean(fh.variables['CH4-EMIS__CH4-COL'][:]))
    C12_og = np.append(C12_og, np.mean(fh.variables['CH4-EMIS__CH4-GAO'][:]))
    C12_liv = np.append(C12_liv, np.mean(fh.variables['CH4-EMIS__CH4-LIV'][:]))
    C12_wst = np.append(C12_wst, np.mean(fh.variables['CH4-EMIS__CH4-WST'][:]))
    C12_bfl = np.append(C12_bfl, np.mean(fh.variables['CH4-EMIS__CH4-BFL'][:]))
    C12_ric = np.append(C12_ric, np.mean(fh.variables['CH4-EMIS__CH4-RIC'][:]))
    C12_ota = np.append(C12_ota, np.mean(fh.variables['CH4-EMIS__CH4-OTA'][:]))
    C12_bbn = np.append(C12_bbn, np.mean(fh.variables['CH4-EMIS__CH4-BBN'][:]))
    C12_wtl = np.append(C12_wtl, np.mean(fh.variables['CH4-EMIS__CH4-WTL'][:]))
    C12_otn = np.append(C12_otn, np.mean(fh.variables['CH4-EMIS__CH4-OTN'][:]))
    fh.close()
 
    
emiss_yr=[]
coal_yr=[]
og_yr=[]
liv_yr=[]
wst_yr=[]    
bfl_yr=[]
ric_yr=[]
ota_yr=[]
bbn_yr=[]
wtl_yr=[]
otn_yr=[]

yr=0  
for y in np.arange(13):
    emiss_yr = np.append(emiss_yr,np.sum(CH4_EMISS[yr:yr+12]))
    coal_yr = np.append(coal_yr,np.sum(C12_coal[yr:yr+12]))
    og_yr = np.append(og_yr,np.sum(C12_og[yr:yr+12]))
    liv_yr = np.append(liv_yr,np.sum(C12_liv[yr:yr+12]))
    wst_yr = np.append(wst_yr,np.sum(C12_wst[yr:yr+12]))
    bfl_yr = np.append(bfl_yr,np.sum(C12_bfl[yr:yr+12]))    
    ric_yr = np.append(ric_yr,np.sum(C12_ric[yr:yr+12]))
    ota_yr = np.append(ota_yr,np.sum(C12_ota[yr:yr+12]))
    bbn_yr = np.append(bbn_yr,np.sum(C12_bbn[yr:yr+12]))
    wtl_yr = np.append(wtl_yr,np.sum(C12_wtl[yr:yr+12]))
    otn_yr = np.append(otn_yr,np.sum(C12_otn[yr:yr+12]))
    yr=yr+12
    
    
    
    
    
os.chdir('/geos/d21/s1420671/jacobian/12CH4/14yr/forward/normal')

C12_EMISS = []
C12_og  = []
C12_coal = []
C12_liv = []
C12_wst = []
C12_bfl = []
C12_ric = []
C12_ota = []
C12_bbn = []
C12_wtl = []
C12_otn = []


for n in np.arange(len(date)):
    methane_12c= 'out.{}01.nc'.format((str(date[n])))
    fh = Dataset(methane_12c, mode='r') 
    lons = fh.variables['LON'][:]
    lats = fh.variables['LAT'][:]
    CH4_EMISS = np.append(C12_EMISS, np.mean(fh.variables['CH4-EMIS__CH4-TOT'][:]))
    C12_coal = np.append(C12_coal, np.mean(fh.variables['CH4-EMIS__CH4-COL'][:]))
    C12_og = np.append(C12_og, np.mean(fh.variables['CH4-EMIS__CH4-GAO'][:]))
    C12_liv = np.append(C12_liv, np.mean(fh.variables['CH4-EMIS__CH4-LIV'][:]))
    C12_wst = np.append(C12_wst, np.mean(fh.variables['CH4-EMIS__CH4-WST'][:]))
    C12_bfl = np.append(C12_bfl, np.mean(fh.variables['CH4-EMIS__CH4-BFL'][:]))
    C12_ric = np.append(C12_ric, np.mean(fh.variables['CH4-EMIS__CH4-RIC'][:]))
    C12_ota = np.append(C12_ota, np.mean(fh.variables['CH4-EMIS__CH4-OTA'][:]))
    C12_bbn = np.append(C12_bbn, np.mean(fh.variables['CH4-EMIS__CH4-BBN'][:]))
    C12_wtl = np.append(C12_wtl, np.mean(fh.variables['CH4-EMIS__CH4-WTL'][:]))
    C12_otn = np.append(C12_otn, np.mean(fh.variables['CH4-EMIS__CH4-OTN'][:]))
    fh.close()
 
    
emiss_pri=[]
coal_pri=[]
og_pri=[]
liv_pri=[]
wst_pri=[]    
bfl_pri=[]
ric_pri=[]
ota_pri=[]
bbn_pri=[]
wtl_pri=[]
otn_pri=[]

yr=0  
for y in np.arange(13):
    emiss_pri = np.append(emiss_pri,np.sum(CH4_EMISS[yr:yr+12]))
    coal_pri = np.append(coal_pri,np.sum(C12_coal[yr:yr+12]))
    og_pri = np.append(og_pri,np.sum(C12_og[yr:yr+12]))
    liv_pri = np.append(liv_pri,np.sum(C12_liv[yr:yr+12]))
    wst_pri = np.append(wst_pri,np.sum(C12_wst[yr:yr+12]))
    bfl_pri = np.append(bfl_pri,np.sum(C12_bfl[yr:yr+12]))    
    ric_pri = np.append(ric_pri,np.sum(C12_ric[yr:yr+12]))
    ota_pri = np.append(ota_pri,np.sum(C12_ota[yr:yr+12]))
    bbn_pri = np.append(bbn_pri,np.sum(C12_bbn[yr:yr+12]))
    wtl_pri = np.append(wtl_pri,np.sum(C12_wtl[yr:yr+12]))
    otn_pri = np.append(otn_pri,np.sum(C12_otn[yr:yr+12]))
    yr=yr+12

    
    

fig=plt.figure()
fig.set_figheight(10)
fig.set_figwidth(15)


data = [wtl, wtl_yr/10**6, wtl_pri/10**6, otn, otn_yr/10**6, otn_pri/10**6, 
        agw, liv_yr/10**6, liv_pri/10**6, wst_yr/10**6, wst_pri/10**6, 
        ric_yr/10**6, ric_pri/10**6, ffu, coal_yr/10**6, coal_pri/10**6,
        og_yr/10**6, og_pri/10**6, bbn, bbn_yr/10**6, bbn_pri/10**6,
        bfl_yr/10**6, bfl_pri/10**6]
        


plt.rc('font', size=13)
box = plt.boxplot(data, patch_artist=True)

#colors = ['blue', 'green', 'blue', 'green', 'blue', 'green','green','green',
#          'blue','green','green','blue','green','green','blue','green','green']
# 
#for patch, color in zip(box['boxes'], colors):
#    patch.set_facecolor(color)
#
#plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14], 
#           ['Wetlands','Wetlands (GC)','Other Natural','Other Natural (GC)','Agri/waste', 
#            'Livestock (GC)','Waste (GC)','Rice (GC)','Fossil Fuels','Coal (GC)','O&G (GC)',
#            'Biofuel','Biomass Burning (GC)','Biofuel (GC)'], rotation=90)

plt.ylabel('CH4 emissions (Tg/yr)')
plt.tight_layout()
os.chdir("/home/s1420671/python/Timeseries_Plots/long_inversion/CH4/inv_goodsites")
#plt.savefig("box_sourcetype.jpg")