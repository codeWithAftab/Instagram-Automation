from selenium import webdriver
import time
import random
import datetime
import pyttsx3
import os
speaker = pyttsx3.init('sapi5')
voices = speaker.getProperty('voices')
speaker.setProperty("voice",voices[1].id)

username1 = "username"
password1 = 'password'
deepak ="//div[contains(text(),'deepak78697')]"
pradeep =  "//div[contains(text(),'pradeepvermaj9_')]"
shobha = "//div[contains(text(),'shobha_halder')]"
surya = "//div[contains(text(),'surendrachoudharyj')]"
name = [deepak,pradeep,shobha,surya]

def speak(audio):
    speaker.say(audio)
    speaker.runAndWait()
def message():
    Time = int(datetime.datetime.now().hour)
    if Time >= 5 and Time <=12:
        driver.find_elements_by_tag_name('textarea')[0].send_keys('good morning')
        
    elif Time > 12 and Time <= 18:
        driver.find_elements_by_tag_name('textarea')[0].send_keys('good evening')
    else:
        driver.find_elements_by_tag_name('textarea')[0].send_keys('good night')

driver = webdriver.Chrome()
def openinsta():
        driver.get('https://instagram.com')
        speak('openning instagram!')
        speak("it's take few time! so I want to play music for you sir!")
        os.startfile('background.mp3')
        time.sleep(2)
        driver.maximize_window()
def login():
    # music.close()
    speak('going to login!')
    facebook = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[5]/button/span[2]')
    facebook.click()
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(username1)
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password1)
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
    time.sleep(15)
    driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
    speak('this is home tab of instagram!')
def messenger():
    driver.find_element_by_xpath('//a[@href="/direct/inbox/"]').click()
    speak("this is messenger")
    time.sleep(4)
def pradeepbhai():
    for i in range(len(name)):
        driver.find_elements_by_xpath(name[i])[0].click()
        speak("sending message")
        time.sleep(1)
        message()
        time.sleep(1)
        driver.find_elements_by_xpath("//button[contains(text(),'Send')]")[0].click()
        i = i+1
def jump_hometab():
    time.sleep(3)
    speak("jump on instagram's home tab")
    driver.find_element_by_xpath('//a[@href="instagram.com"]').click()
    time.sleep(10)

def instahometab():
    
    speak('hello sir ! welcome to auto insta script! made by bruteking!')
    openinsta()
    login()

# login authentication

if __name__ == "__main__":
    instahometab()
    messenger()
    # pradeepbhai()
    speak("all done")
    jump_hometab()
    

