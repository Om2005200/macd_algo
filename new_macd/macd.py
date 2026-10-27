import requests as rq
import pandas as pd
import csv 
import json 
from datetime import datetime
import time 





class MACD:






    def __init__(self):
        pass




    def getting_the_main_data(self):
        with open(r"C:\Users\dasho\divergence_test.json",'r') as xv:
            data=json.load(xv)


        return data



     

    def analyzing_the_main_data(self):
        recent_date="2026-10-21"
        main_data=self.getting_the_main_data()
        master_close_list=[]
        addas=[]
        hanuman=[]
        balmain=[]
        master_open_list=[]
        master_time_list=[]
        master_ema_list=[]
        master_low_list=[]
        master_high_list=[]
        mac_master=[]
        macd_data=[]
        main_ema=[]
        main_signal_line=[]
        main_ema_=[]
        histogram_data=[]
        for datas in main_data:
            close_=datas['CLOSE']
            open_=datas['OPEN']
            date_=datas['DATE']
            time_=datas['TIME']
            low=datas['LOW']
            high=datas['HIGH']


            
            master_close_list.append(close_)
            master_open_list.append(open_)
            master_low_list.append(low)
            master_high_list.append(high)
            master_time_list.append(time_)



        # #print(master_time_list)
        # last_12=master_close_list[:12]
        # initialized_ema=int(sum(last_12))/12
        # #print(initialized_ema)


        # main_data[12]['EMA_12']=initialized_ema
        # with open(r"C:\Users\dasho\divergence_test.json",'w') as cv:
        #     json.dump(main_data,cv,indent=4)




        # for data in main_data:
        #     ema_12_data=data['EMA_12']
        #     master_ema_list.append(ema_12_data)
        # main_ema.append(initialized_ema)
        # #print(main_ema)
        # for closings in master_close_list[13:]:
            
        #     for emas in main_ema:



        #         values=closings*2/13+emas*11/13
        #     main_ema.append(values)

        # for index, ema in enumerate(main_ema):
        #     main_data[index + 12]['EMA_12'] = ema

        # with open(r"C:\Users\dasho\divergence_test.json", 'w') as cv:
        #     json.dump(main_data, cv, indent=4)

        
        # last_26=master_close_list[:26]
        # initialized_ema_26=int(sum(last_26))/26
        # main_data[26]['EMA_26']=initialized_ema_26
        # with open(r"C:\Users\dasho\divergence_test.json",'w') as xx:
        #     json.dump(main_data,xx,indent=4)

        # for data_ in main_data:
        #     ema_26_data=data_['EMA_26']
        #     master_ema_list.append(ema_26_data)


        
        # main_ema_.append(initialized_ema_26)
        # for closings_ in master_close_list[27:]:
        #     for ema_ in main_ema_:
        #         values_=closings_*2/13+ema*11/13
        #     main_ema_.append(values_)
        # for index_ ,ema_ in enumerate(main_ema_):
        #     main_data[index_+26]['EMA_26']=ema_

        # with open(r"C:\Users\dasho\divergence_test.json",'w') as ll:
        #     json.dump(main_data,ll,indent=4)
       
        # for revised in main_data[26:]:
        #     current_date=revised['DATE']
            

        #     ema_12=revised['EMA_12']
        #     ema_26=revised['EMA_26']


        #     macd_line=ema_12-ema_26
        #     macd_data.append(macd_line)
           




        
        # for index__ ,his in enumerate(macd_data):
        #     main_data[index__+26]['MACD']=his
        
        # with open(r"C:\Users\dasho\divergence_test.json",'w') as tt:
        #     json.dump(main_data,tt,indent=4)



        
      
        # for initialized_signal_line in main_data:
        #     mac_line_data=initialized_signal_line['MACD']
        #     mac_master.append(mac_line_data)


        # initialized_signal_value=mac_master[26:35]
        # total_value=sum(initialized_signal_value)/9

        # main_data[27]['SIGNAL_LINE']=total_value
        # with open(r"C:\Users\dasho\divergence_test.json",'w') as yy:
        #     json.dump(main_data,yy,indent=4)


        # multiplier=0.2
        
        # main_signal_line.append(total_value)

        # for nt in mac_master[28:]:
        #     for t in main_signal_line:
        #         val=(nt*multiplier)+(t*0.8)
        #     main_signal_line.append(val)
        # #print(len(main_signal_line))
        # for inde,signal in enumerate(main_signal_line):
        #     main_data[inde+27]['SIGNAL_LINE']=signal
        # with open(r"C:\Users\dasho\divergence_test.json",'w') as rr:
        #     json.dump(main_data,rr,indent=4)
        # for vars in main_data[27:]:
        #     vars_macd=vars['MACD']
        #     vars_signal_line=vars['SIGNAL_LINE']



        #     histogram_value=vars_macd-vars_signal_line
        #     vars['HISTOGRAM']=histogram_value
        #     histogram_data.append(histogram_value)

        #     with open(r"C:\Users\dasho\divergence_test.json",'w') as kk:
        #         json.dump(vars,kk,indent=4)

        
        # for ind ,his_ in enumerate(histogram_data):
        #     main_data[ind+26]['HISTOGRAM']=his_
        
        # with open(r"C:\Users\dasho\divergence_test.json",'w') as tt:
        #     json.dump(main_data,tt,indent=4)


        ##### STOCHIATIC VALUES 



        tera_close=[]
        tera_high=[]
        tera_low=[]
        max_high_value=
        


        for data in main_data[6:]:
            close_prices=data['CLOSE']
            low_prices=data['LOW']
            high_prices=data['HIGH']
            tera_high.append(high_prices)
            tera_low.append(low_prices)
            max_high=max(tera_high)

            max_low=min(tera_low)

        

        
        

            


            









    


        










        










        


    
    





            




m=MACD()
m.getting_the_main_data()
m.analyzing_the_main_data()


