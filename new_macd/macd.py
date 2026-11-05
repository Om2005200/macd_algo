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




    
    def opening_the_order_log(self):

        file_path = r"C:\Users\dasho\macd_code_orderbook.json"

        try:

            with open(file_path, "r") as x:
                data = json.load(x)

            if data is None:
                data = []

            return data

        except FileNotFoundError:

            #print(f"NO ORDERBOOK FOUND FOR {file_name}. CREATING NEW FILE")

            with open(file_path, "w") as x:
                json.dump([], x, indent=4)

            return []

        except json.JSONDecodeError:

            #print(f"ORDERBOOK CORRUPTED FOR {file_name}. RESETTING")

            with open(file_path, "w") as x:
                json.dump([], x, indent=4)

            return []











     

    def analyzing_the_main_data(self,stock_data:str):
        stock_list=['macd']




        latest_date="2026-10-28"
        avg_k_holder=[]
        index_loader_=[]
        final_values=[]
        dummy_index_=[]
        
        master_close_list=[]
        main_list=[]
        revised_datas=[]
        level_1_data=[]
        trunk_data=[]
        ranger_1=[]
        main_results=[]
        ranger_2=[]
        master_absolute=[]
       
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
        k_holder=[]
        index_loader=[]
        finalized_values=[]
        dummy_index=[]
        master_date_data=[]
        main_data,file_name=stock_data
        order_log=self.opening_the_order_log(file_name)
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
            master_date_data.append(date_)

        ct_close=master_close_list[-1]
        ct_open=master_open_list[-1]
        ct_time=master_time_list[-1]
        if order_log:
            for orders in order_log:
                status=orders['STATUS']
                if status=='OPEN':
                    candle=orders['CANDLE']
                   
                    #candle_3=orders['CANDLE_3']
                    candle_1_close=candle['CLOSE']
                    candle_1_open=candle['OPEN']
                    candle_1_timing=candle['TIME']
                    if candle_1_close>candle_1_open:  # IF IT  WAS A BEARISH SETUP MEANS THE GREEN CANDLES
                        if ct_time>candle_1_timing:
                            if ct_close<ct_open:

                                orders['STATUS']='CLOSED'
                                stock_symbol=file_name.replace('_revised_dataset_macd_pro_data.json','').lower()
                                confirmation_candle = {
                                    "DATE": current_date,
                                    "TIME": ct_time,
                                    "OPEN": ct_open,
                                    "HIGH": main_data[-1]["HIGH"],
                                    "LOW": main_data[-1]["LOW"],
                                    "CLOSE": ct_close
                                }
                                orders['STATUS']='CLOSED'
                                with open(r"C:\Users\dasho\{}macd_orderbook.json".format(file_name),'w') as ki:
                                    json.dump(order_log,ki,indent=4)
                                    print('NEXT CANDLE WAS A RED CANDLE')





                    

               
                




        #print(master_time_list)
        last_12=master_close_list[:12]
        initialized_ema=sum(last_12)/12
        #print(initialized_ema)


        main_data[11]['EMA_12']=initialized_ema
        # with open(r"C:\Users\dasho\divergence_test.json",'w') as cv:
        #     json.dump(main_data,cv,indent=4)




        for data in main_data:
            ema_12_data=data['EMA_12']
            master_ema_list.append(ema_12_data)
        main_ema.append(initialized_ema)
        #print(main_ema)
        for closings in master_close_list[12:]:
            
            for emas in main_ema:



                values=closings*2/13+emas*11/13
            main_ema.append(values)

        for index, ema in enumerate(main_ema):
            main_data[index + 11]['EMA_12'] = ema

        # with open(r"C:\Users\dasho\divergence_test.json", 'w') as cv:
        #     json.dump(main_data, cv, indent=4)

        
        last_26=master_close_list[:26]
        initialized_ema_26=sum(last_26)/26
        main_data[25]['EMA_26']=initialized_ema_26
        # with open(r"C:\Users\dasho\divergence_test.json",'w') as xx:
        #     json.dump(main_data,xx,indent=4)

        for data_ in main_data:
            ema_26_data=data_['EMA_26']
            master_ema_list.append(ema_26_data)


        
        main_ema_.append(initialized_ema_26)
        for closings_ in master_close_list[26:]:
            for ema_ in main_ema_:
                values_=closings_*2/27+ema_*25/27
            main_ema_.append(values_)
        for index_ ,ema_ in enumerate(main_ema_):
            main_data[index_+25]['EMA_26']=ema_

        # with open(r"C:\Users\dasho\divergence_test.json",'w') as ll:
        #     json.dump(main_data,ll,indent=4)
        jjj=[]
        for revised in main_data[25:]:
            current_date=revised['DATE']
            

            ema_12=revised['EMA_12']
            ema_26=revised['EMA_26']


            macd_line=ema_12-ema_26
            macd_data.append(macd_line)





        
        for index__ ,his in enumerate(macd_data):
            main_data[index__+25]['MACD']=abs(his)
        
        # with open(r"C:\Users\dasho\divergence_test.json",'w') as tt:
        #     json.dump(main_data,tt,indent=4)



        
      
        for initialized_signal_line in main_data:
            mac_line_data=initialized_signal_line['MACD']
            mac_master.append(mac_line_data)


        initialized_signal_value=mac_master[26:35]
        total_value=sum(initialized_signal_value)/9

        main_data[33]['SIGNAL_LINE']=total_value
        # with open(r"C:\Users\dasho\divergence_test.json",'w') as yy:
        #     json.dump(main_data,yy,indent=4)


        multiplier=0.2
        
        main_signal_line.append(total_value)
        
        for nt in mac_master[34:]:
            if nt == '':
                continue
            for t in main_signal_line:

                val=(nt*multiplier)+(t*0.8)
            main_signal_line.append(val)
        #print(len(main_signal_line))
      
               
        
        for inde,signal in enumerate(main_signal_line):
            main_data[inde+33]['SIGNAL_LINE']=signal
        # with open(r"C:\Users\dasho\divergence_test.json",'w') as rr:
        #     json.dump(main_data,rr,indent=4)
        for vars in main_data[33:]:
            vars_macd=vars['MACD']
            vars_signal_line=vars['SIGNAL_LINE']



            histogram_value=vars_macd-vars_signal_line
            vars['HISTOGRAM']=histogram_value
            histogram_data.append(histogram_value)

        # with open(r"C:\Users\dasho\divergence_test.json",'w') as kk:
        #     json.dump(main_data,kk,indent=4)

        

        ##### STOCHIATIC VALUES 
        
        for x in master_close_list:
            main_datas=master_close_list.index(x)
            if main_datas not in main_list:
                main_list.append(main_datas)
            if main_datas in main_list:
                values=main_list[-1]
                new_index_value=values+1
                main_list.append(new_index_value)
        original_list_length=len(master_close_list)
        new_list_length=len(main_list)
        if new_list_length>original_list_length:
            new_revised_list=main_list[0:new_list_length-1]
            for value_finding in new_revised_list:
                value_finder=master_close_list[value_finding]
                revised_datas.append(value_finder)
            for t in new_revised_list[3:]:
                trunk_data.append(t)
                required_values=t-3
                level_1_data.append(required_values)
            for a,b in zip(level_1_data,trunk_data):
                rangers=master_close_list[a:b]
                mi=min(rangers)
                ranger_1.append(mi)
                ma=max(rangers)
                ranger_2.append(ma)
            results=[j-v/w-v for j,v,w in zip(trunk_data,ranger_1,ranger_2)]
            main_results=results
            for rev in main_results:
                absolute_values=abs(rev)
                master_absolute.append(absolute_values)

            
            for ind ,intialized_k in enumerate(master_absolute):
                main_data[ind+3]['K']=intialized_k

            # with open(r"C:\Users\dasho\divergence_test.json",'w') as ee:
            #     json.dump(main_data,ee,indent=4)

        #### SMOOTHED K
        
        for k in main_data[3:]:
            initialized_k=k['K']
            k_holder.append(initialized_k)
        for avg_k in k_holder:
            index_finder=k_holder.index(avg_k)
            if index_finder not in index_loader:
                index_loader.append(index_finder)
            if index_finder in index_loader:
                main_values=index_loader[-1]
                new_values=main_values+1
                index_loader.append(new_values)
            new_length=len(index_loader)
            ranger_data=index_loader[0:new_length-1]
        for data in ranger_data:
            required_datas=data-3
            dummy_index.append(required_datas)
        dummy_index.reverse()
        ranger_data.reverse()


        for j,u in zip(dummy_index,ranger_data):
            place_holder=sum(k_holder[j:u])
            finalized_values.append(place_holder)
       
        for i ,averaged_k in enumerate(finalized_values):
            main_data[i+3]['AVG_K']=averaged_k

        # with open(r"C:\Users\dasho\divergence_test.json",'w') as oo:
        #     json.dump(main_data,oo,indent=4)



        #INITIALIZED_D
       



        for d in main_data[3:]:
            average_k=d['AVG_K']
            avg_k_holder.append(average_k)



        for vg in avg_k_holder:
            index_finder_=avg_k_holder.index(vg)
            if index_finder_ not in index_loader_:
                index_loader_.append(index_finder_)

            if index_finder_ in index_loader_:
                main_values_=index_loader_[-1]
                new_values_=main_values_+1
                index_loader_.append(new_values_)
            new_length_=len(index_loader_)
            ranger_datas=index_loader_[0:new_length_-1]
        for dat in ranger_datas[3:]:
            da=dat-3
            dummy_index_.append(da)
        dummy_index_.reverse()
        ranger_datas.reverse()


        for s,l in zip(dummy_index_,ranger_datas):
            place_holder_=sum(avg_k_holder[s:l])
            final_values.append(place_holder_)



        for p ,averaged_d in enumerate(final_values):
                main_data[p+3]['D']=averaged_d
    
        with open(r"C:\Users\dasho\divergence_test.json",'w') as rr:
            json.dump(main_data,rr,indent=4)



        time_data=[]
       
        for current_data in main_data[3:]:
            current_closing_price=current_data['CLOSE']
            current_opening_price=current_data['OPEN']
            current_date_data=current_data['DATE']
            current_time_data=current_data['TIME']
            if latest_date==current_date_data:
                time_data.append(current_time_data)

                current_close=master_close_list[-1]
                current_open=master_open_list[-1]
                current_time=master_time_list[-1]
                #print(current_time)
                if current_close>current_open:
                    finalized_green_candle=[]
                    for green_data in main_data:
                        green_close_price=green_data['CLOSE']
                        green_open_price=green_data['OPEN']
                        green_date=green_data['DATE']
                        green_time=green_data['TIME']
                        if latest_date==green_date:
                            if current_close>current_open:
                                if green_time==current_time:
                                    finalized_green_candle.append(green_data)


                    if finalized_green_candle:
                        for candles in finalized_green_candle:
                            candle_close=candles['CLOSE']
                            candle_open=candles['OPEN']
                            macd=candles['MACD']
                            k_value=candles['K']
                            d_value=candles['D']



                        if macd>0:
                            if k_value>d_value:
                                new_setup={
                                    'STATUS':'OPEN',
                                    'CANDLE':candles
                                }
                                if new_setup not in order_log:
                                    order_log.append(new_setup)
                                    with open(r"C:\Users\dasho\macd_code_orderbook.json",'w') as code:
                                        json.dump(order_log,code,indent=4)
                                        


                                    print(order_log)

                #finalizd_red_candle=[]
                elif current_close<current_open:
                    finalized_red_candle=[]
                    for red_candles in main_data:
                        red_candle_close=red_candles['CLOSE']
                        red_candle_open=red_candles['OPEN']
                        red_candle_dates=red_candles['DATE']
                        red_candle_times=red_candles['TIME']
                        if latest_date==red_candle_dates:
                            if red_candle_times==current_time:

                                if current_close<current_open:
                                    finalized_red_candle.append(red_candles)
                    if finalized_red_candle:
                        for reds in finalized_red_candle:
                            red_k=reds['K']
                            red_d=reds['D']
                            red_macd=reds['MACD']
                        if red_macd>0:
                            if red_k>red_d:
                                new_setup={
                                    'STATUS':'OPEN',
                                    'CANDLE':reds
                                }
                                print(new_setup)


                                if new_setup not in order_log:
                                    order_log.append(new_setup)

                                    with open(r"C:\Users\dasho\macd_code_orderbook.json",'w') as lx:
                                        json.dump(order_log,lx,indent=4)



                




                                    


                



            




m=MACD()
m.getting_the_main_data()
m.analyzing_the_main_data()     



    


