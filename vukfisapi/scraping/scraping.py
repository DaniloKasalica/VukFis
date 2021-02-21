from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from concurrent.futures import ThreadPoolExecutor, as_completed



#link za driver -> https://sites.google.com/a/chromium.org/chromedriver/downloads 

#path do driver-a
PATH =r"C:\Users\Jovan\Desktop\fiskalizacija\driver\chromedriver.exe"

def finddata(myurl):

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"


    ''' ''' 
       #Headless Snippet ---> https://www.youtube.com/watch?v=LN1a0JoKlX8  ------virtual display
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
  
    driver = webdriver.Chrome(PATH),options=options)
    #---------------------
  

    driver.get(myurl)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-verify-invoice/div/section[2]/div/div/div/div[1]/p")))

    before_XPath = "/html/body/app-root/app-verify-invoice/div/section[2]/div/div/div/div["
    afterlabel_XPath = "]/label"
    afterp_XPath = "]/p"
    data = []
    obj = {}
    for t_row in range(1,8):
        
            FinalXPath_1 = before_XPath  + str(t_row) + afterp_XPath
            FinalXPath_2 = before_XPath + str(t_row) + afterlabel_XPath
            value = driver.find_element_by_xpath(FinalXPath_1).text
            key = driver.find_element_by_xpath(FinalXPath_2).text          
            obj[key]= value
         

    before_XPath = "/html/body/app-root/app-verify-invoice/div/section[1]/div/ul/li["
    afterp_XPath="]"
    obj_basic_info = {}
    for t_row in range(1,4):
        
            FinalXPath_1 = before_XPath  + str(t_row) + afterp_XPath
            FinalXPath_2 = before_XPath + str(t_row) + afterlabel_XPath
            value = driver.find_element_by_xpath(FinalXPath_1).text
            key = "Null"+str(t_row)      
            obj_basic_info[key]= value
           
    obj_invoice_info = {}
    invoice = driver.find_element_by_xpath("/html/body/app-root/app-verify-invoice/div/section[1]/div/div[1]/h4").text
    obj_invoice_info["racun"]= invoice
    obj_invoice_info["cijena"]= driver.find_element_by_xpath("/html/body/app-root/app-verify-invoice/div/section[1]/div/div[2]/h1").text   
    obj_invoice_info["bez_pdv"]= driver.find_element_by_xpath("/html/body/app-root/app-verify-invoice/div/section[1]/div/div[2]/small[1]/strong").text 
    obj_invoice_info["pdv"] =   driver.find_element_by_xpath("/html/body/app-root/app-verify-invoice/div/section[1]/div/div[2]/small[1]/strong").text 

    data.append({"racun": obj_invoice_info})
    data.append({"osnovne_informacije":obj_basic_info})   
    data.append({"ostalo":obj}) 
    driver.quit()
    
    return data