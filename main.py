
import numpy as np
import pandas as pd 
import requests
from bs4 import BeautifulSoup
page = requests.get('https://www.amazon.in/deal/47dab85b/?_encoding=UTF8&showVariations=true&_ref=dlx_gate_sd_dcl_tlt_47dab85b_dt&pd_rd_w=xxI9q&content-id=amzn1.sym.0d1fafce-0d80-4ffc-b8c3-74f55ca06beb&pf_rd_p=0d1fafce-0d80-4ffc-b8c3-74f55ca06beb&pf_rd_r=035ZRG52QWX16G67SD3F&pd_rd_wg=zgwK0&pd_rd_r=d041809d-3016-4f17-b65f-6cffc527e571&ref_=pd_gw_unk')


sd = BeautifulSoup(page.content,'html5lib')

price = sd.find_all('span',{'class':"a-price-whole"})

all_price = []
all_title= []

#getting price of the product and then storing into all_price list

for n in np.arange(0,len(price)):
  
   all_price.append(price[n].get_text())

 #getting title of the product then storing it into all_title list

at = sd.find_all('a',{'class' : 'a-size-base a-color-base a-link-normal a-text-normal'})

for n in np.arange(0,len(at)):

 all_title.append(at[n].get('title'))


dictionary ={'price':all_price,'title':all_title }

data =  pd.DataFrame(dictionary)

csv = data.to_csv('C:/Users/srjpn/Desktop/sd.csv') 

 



 
  
    
