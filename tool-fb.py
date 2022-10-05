from email import message
from email.mime import image
from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from os import link
from selenium import webdriver
import time
import pandas
import pyautogui

excel_data_df = pandas.read_excel('content.xlsx')
message=excel_data_df['Noidung'].tolist()
LinkGroup=excel_data_df['UID'].tolist()
TaiKhoan=excel_data_df['TaiKhoan'].tolist()
MatKhau=excel_data_df['MatKhau'].tolist()

imageFolderPath =r"E:\haha\anh.jpg"
time.sleep(2)
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

for i in range (len(LinkGroup)):
    
    driver.find_element("name","email").send_keys(TaiKhoan[i])
    driver.find_element("name","pass").send_keys(MatKhau[i])
    driver.find_element("name","login").click()
    time.sleep(2)
    driver.get(LinkGroup[i])
    time.sleep(2)
    element = driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div").click()
    time.sleep(3)
    element = driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div").send_keys(message[i])
    time.sleep(1)
    clickanh=driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[1]/div/span/div/div/div[1]/div/div/div[1]/i").click()
    time.sleep(3)
    # clickAnh=driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div/i").click()
    # time.sleep(3)
    pyautogui.write(imageFolderPath)
    time.sleep(2)
    pyautogui.keyDown("enter")
    time.sleep(2)
    dangbai=driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div[1]").click()
    time.sleep(5)
    
print("Dang bai thanh cong")    

   
     