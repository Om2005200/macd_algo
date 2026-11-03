import requests as rq
import pandas as pd
import csv 
import json 
from datetime import datetime
import time 





class MACD:






    def __init__(self):
        pass



    def getting_the_live_data(self):
        with open(r"C:\Users\dasho\divergence_test.json",'r') as xx:
            data=json.load(xx)
            return data 



    def analyzing_the_data(self):
        master_close_list=[]
        master_open_list=[]
        master_high_list=[]
        master_low_list=[]
        master_date_list=[]


        main_data=self.getting_the_live_data()
        for datas in main_data :
            closing_prices=datas['CLOSE']
            opening_prices=datas['OPEN']
            low_prices=datas['LOW']
            high_prices=datas['HIGH']


            master_close_list.append(closing_prices)
            master_open_list.append(opening_prices)
            master_low_list.append(low_prices)
            master_high_list.append(high_prices)


        last_12=master_close_list[:12]
        initialized_ema=sum(last_12)
        main_data[11]['EMA_12']=initialized_ema
        with open(r"C:\Users\dasho\divergence_test.json",'r') as x:
            json.dump(main_data,x,indent=4)


            



        








        






        
        
            







            



            
        








        
        

            


            









    


        










        










        


    
    





            




m=MACD()
m.getting_the_live_data()
m.analyzing_the_data()



