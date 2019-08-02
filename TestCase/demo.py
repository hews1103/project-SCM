from selenium import webdriver
import time

driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
driver.get('http://192.168.11.179:8081')

if __name__ == '__main__':
    try:
        # 点击更新日期-月
        driver.find_element_by_xpath('//span[text()="月"]').click()
        time.sleep(1)
        # 选择七月
        driver.find_element_by_xpath('//em[contains(text(),"7月")]').click()
        time.sleep(1)
        # 点击更新日期-年
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div[1]/span').click()
        time.sleep(1)
        # 选择2018年
        driver.find_element_by_xpath('//em[contains(text(),"2018")]').click()
        time.sleep(1)
        # 点击库存金额-国内
        driver.find_element_by_xpath('(//label[contains(text(),"国内")])[1]').click()
        time.sleep(1)
        # 点击库存金额-国外
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[1]/p[1]/div[2]/label[2]').click()
        time.sleep(1)
        # 点击出库金额-一级
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/p[1]/div[2]/label[1]').click()
        time.sleep(1)
        # 点击出库金额-二级
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/p[1]/div[2]/label[2]').click()
        time.sleep(1)
        # 点击出库金额-三级
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/p[1]/div[2]/label[3]').click()
        time.sleep(1)
        # 点击采购未到金额-国内
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[3]/p[1]/div[2]/label[1]').click()
        time.sleep(1)
        # 点击采购未到金额-国外
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[3]/p[1]/div[2]/label[2]').click()
        time.sleep(2)
    except:
        print('报错了')
driver.quit()

