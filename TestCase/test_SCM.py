from Common.Baseui import baseUI
from time import sleep
import time
from selenium.webdriver.support.select import Select
import pytest

class Test_scm():

    def test_ckzl(self,base):
        # 点击更新日期-月
        base.click('点击更新日期-月','''//span[text()="月"]''')
        # 选择七月
        base.click('选择七月','//em[contains(text(),"7月")]')
        # 点击更新日期-年
        base.click('点击更新日期-年','//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/div[1]/span')
        time.sleep(1)
        # 选择2018年
        base.click('选择2018年','//em[contains(text(),"2018")]')
        time.sleep(1)
        # 点击库存金额-国内
        base.click('点击库存金额-国内','(//label[contains(text(),"国内")])[1]')
        time.sleep(1)
        # 点击库存金额-国外
        base.click('点击库存金额-国外','//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[1]/p[1]/div[2]/label[2]')
        time.sleep(1)
        # 点击出库金额-一级
        base.click('点击出库金额-一级','//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/p[1]/div[2]/label[1]')
        time.sleep(1)
        # 点击出库金额-二级
        base.click('点击出库金额-二级','//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/p[1]/div[2]/label[2]')
        time.sleep(1)
        # 点击出库金额-三级
        base.click('点击出库金额-三级','//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/p[1]/div[2]/label[3]')
        time.sleep(1)
        # 点击采购未到金额-国内
        base.click('点击采购未到金额-国内','//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[3]/p[1]/div[2]/label[1]')
        time.sleep(1)
        # 点击采购未到金额-国外
        base.click('点击采购未到金额-国外','//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div[3]/p[1]/div[2]/label[2]')
        time.sleep(1)
        # 滑动页面到底
        base.scroll_screen('滑动页面到底')
        time.sleep(1)
        # 点击周转率-更多
        base.click('点击周转率-更多','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[3]/div[3]/div/div[1]/div/span''')
        time.sleep(1)
        # 点击周转率国内外
        base.click('点击周转率国内外','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[1]/div/div[1]/div/span''')
        # 周转率国内外-国内
        base.click('周转率国内外-国内','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[1]/div/div[2]/ul[2]/li[1]''')
        time.sleep(1)
        # 周转率国内外-国外
        base.click('周转率国内外-国外','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[1]/div/div[2]/ul[2]/li[2]''')
        time.sleep(1)
        # 周转率0-1
        base.send_keys('输入0','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[2]/div[1]/input''',0)
        # 周转率0-1
        base.send_keys('输入1','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[2]/div[2]/input''',1)
        # 周转天数
        base.send_keys('输入0','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[3]/div[1]/input''',0)
        base.send_keys('输入100','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[3]/div[2]/input''',100)
        # 选择年月
        base.click('选择起始年月','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[4]/div[1]/div[1]/div/input''')
        base.click('点击起始时间','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[4]/div[1]/div[2]/div/div/div/div[1]/span[2]/span[1]''')
        base.click('选择起始时间2018','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[4]/div[1]/div[2]/div/div/div/div[2]/div/span[9]/em''')
        base.click('选择起始时间七月','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[4]/div[1]/div[2]/div/div/div/div[2]/div/span[7]/em''')
        base.click('选择终止年月','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[4]/div[2]/div[1]/div/input''')
        base.click('点击终止时间','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[4]/div[2]/div[2]/div/div/div/div[1]/span[2]/span[1]''')
        base.click('选择终止时间2019','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[4]/div[2]/div[2]/div/div/div/div[2]/div/span[10]/em''')
        base.click('选择终止时间八月','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[4]/div[2]/div[2]/div/div/div/div[2]/div/span[8]/em''')
        # 点击查询
        base.click('点击查询','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/button[1]/span''')
        # 点击重置
        base.click('点击重置','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/button[2]''')

        time.sleep(3)

    def test_kcpp(self,base):
        # 点击库存品牌
        base.click('点击库存品牌', '''//*[@id="app"]/div/div/div[1]/div[1]/div/ul/div[2]/li/div''')
        #点击AHC
        base.click('点击AHC','''//*[@id="app"]/div/div/div[1]/div[1]/div/ul/div[2]/li/ul/a[1]''')
        time.sleep(1)
        # 点击出库金额
        base.click('点击未出库','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[2]/p[1]/div[2]/label[2]''')
        base.click('点击已出库','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[2]/p[1]/div[2]/label[1]''')
        # 点击折损状态
        base.click('点击数量','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/label[2]''')
        base.click('点击金额','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/label[1]''')
        # 滑动到底
        base.scroll_screen('滑动到底')
        # 点击所有品牌达成
        base.click('点击所有品牌达成','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[4]/div/div[1]/div/span''')
        time.sleep(2)
        # 品牌周转达成-国外
        base.click('点击国内外','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[1]/div/div[1]/div/span''')
        base.click('点击国外','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[1]/div/div[2]/ul[2]/li[2]''')
        # 输入品牌
        base.send_keys('输入品牌名','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[2]/div/div[1]/div/input''','萌蒂')
        time.sleep(1)
        # 输入pm
        base.send_keys('输入pm','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[3]/div/div[1]/div/input''','赵怡玮')
        time.sleep(1)
        # 输入起止周转率目标
        base.send_keys('输入周转率目标起始值','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[4]/div[1]/input''',0)
        base.send_keys('输入周转率目标最大值','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[4]/div[2]/input''',100)
        # 输入起止周转率
        base.send_keys('输入周转率起始值','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[5]/div[1]/input''',0)
        base.send_keys('输入周转率最大值','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[5]/div[2]/input''',100)
        # 输入起止周转天数
        base.send_keys('输入起始周转天数','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[6]/div[1]/input''',0)
        base.send_keys('输入最大周转天数','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[6]/div[2]/input''',100)
        # 点击目标达成(等待开发完成)
        # 点击年月
        time.sleep(2)
        base.click('点击起始年月','''(//input[@class='ivu-input ivu-input-default ivu-input-with-suffix'])[1]''')
        time.sleep(1)
        base.click('点击起始年','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[8]/div[1]/div[2]/div/div/div/div[1]/span[2]/span[1]''')
        time.sleep(1)
        base.click('点击起始年2019','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[8]/div[1]/div[2]/div/div/div/div[2]/div/span[10]/em''')
        time.sleep(1)
        base.click('点击起始月3','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[8]/div[1]/div[2]/div/div/div/div[2]/div/span[3]/em''')
        time.sleep(1)
        base.click('点击终止年月','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[8]/div[2]/div[1]/div/input''')
        base.click('点击终止年','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[8]/div[2]/div[2]/div/div/div/div[1]''')
        base.click('点击终止年2019','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[8]/div[2]/div[2]/div/div/div/div[2]/div/span[10]/em''')
        base.click('点击终止月8','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li[8]/div[2]/div[2]/div/div/div/div[2]/div/span[8]/em''')
        # 点击查询
        base.click('点击查询','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/button[1]/span''')
        # 点击重置
        base.click('点击重置','''//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/button[2]/span''')
        time.sleep(3)