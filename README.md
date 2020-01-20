> 基于`Python`的`unittest`单元测试报告美化

作为 [HwTTK（Test Tool Kit ）](https://github.com/hongweifuture/HwTTK)中的一员，`HwTestReport`具有以下特性：
- 支持`Python2`和`Python3`，自动兼容，无需设置
- 支持`中文`和`英文`手动切换
- 支持`Selenium`和`Appium`截图报告嵌入`Html`报告中，可根据需求设置开启或关闭截图展示功能
- 样式美化需要网络支持，采用CDN加持，如果本地使用请下载`离线版本`
- 增加测试人员条目、通过率统计、所有可能情况筛选功能等
- 增加`饼图`数据展示、测试详情数据展示
- 增加`返回顶部`按钮
- 其他细节修改

源自 [tungwaiyip.info](http://tungwaiyip.info/software/HTMLTestRunner.html) 的`0.82`版本 `HTMLTestRunner`

## 当前的环境
环境| 版本
-|-
Python2  |2.7.17
Python3  | 3.7.4
selenium    |3.141.0
geckodriver   |v0.26.0
Firefox   |72.0.1 (64 位)

## 中英文报告实例
```python
import unittest
# 中文 Chinese
from HwTestReport import HTMLTestReport

# 英文 English
from HwTestReport import HTMLTestReportEN

class Case_assert_1(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_ok(self):
        self.assertEqual(1,1)

    def test_faile(self):
        self.assertEqual(1,2)

    def test_error(self):
        raise Exception

class Case_assert_2(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_ok(self):
        self.assertTrue(True)

class Case_assert_3(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_error(self):
        raise Exception

class Case_assert_4(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_faile(self):
        self.assertEqual(1,3)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Case_assert_1('test_ok'))
    suite.addTest(Case_assert_1('test_faile'))
    suite.addTest(Case_assert_1('test_error'))
    suite.addTest(Case_assert_2('test_ok'))
    suite.addTest(Case_assert_3('test_error'))
    suite.addTest(Case_assert_4('test_faile'))

    # English：HTMLTestReportEN
    with open('./HwTestReport.html', 'wb') as report:
        runner = HTMLTestReport(stream=report,
                                verbosity=2,
                                title='HwTestReport 测试',
                                description='带饼图，带详情',
                                tester='Johnny')
        runner.run(suite)
```
## 带截图的报告实例
此截图功能是针对 [Selenium](https://selenium.dev/downloads/)和 [Appium](http://appium.io/)开发，支持`Python2`和`Python3`，不同的浏览器选择不同驱动

- Selenium
  ```
  pip install selenium
  conda install selenium
  ```

- `Firefox`
  - [火狐浏览器历史版本下载](http://ftp.mozilla.org/pub/firefox/releases/)
  - [geckodriver驱动下载地址](https://github.com/mozilla/geckodriver/releases)
  - [驱动与浏览器版本对应关系总结](https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html)
  
- `Chrome`，对应版本请查看版本文件夹内的`note.txt`
  - [chromedriver驱动官方下载地址](http://chromedriver.storage.googleapis.com/index.html)
  - [chromedriver驱动淘宝下载地址](https://npm.taobao.org/mirrors/chromedriver/)
  - [Chrome浏览器历史版本下载](https://google_chrome.en.downloadastro.com/old_versions/)
  - [驱动与浏览器版本对应关系总结](https://www.slimjet.com/chrome/google-chrome-old-version.php)
  
- [IE浏览器驱动IEDriverServer](http://selenium-release.storage.googleapis.com/index.html)
- [Edge浏览器驱动MicrosoftWebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- [Opera浏览器驱动operadriver](https://github.com/operasoftware/operachromiumdriver/releases)
- [PhantomJS浏览器驱动：phantomjs](https://phantomjs.org/)
  > selenium已经放弃PhantomJS，使用需将`selenium`降级为`2.48.0`版本，或者使用火狐或者谷歌无界面浏览器，推荐[Headless Chrome](https://developers.google.com/web/updates/2017/04/headless-chrome)，还是要了解一下[Headless Firefox](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless_mode)

驱动需要放在和`python`启动文件在同一个目录，或添加环境变量，如
- windows："D:\python\venv\Scripts\geckodriver.exe"
- linux："/opt/python/geckodriver.exe"

### 截图功能使用

1. **增加 `images` 参数**，默认为`False`，所以不需要截图可以不添加此参数，参考上面
2. 初始化`imgs`，必须为`driver`
   ```
    def setUp(self):
        self.imgs=[]  # （可选）初始化截图列表
        self.driver = webdriver.Firefox()
   ```

```python
import unittest
from HwTestReport import HTMLTestReport
from HwTestReport import HTMLTestReportEN
from selenium import webdriver

class Case_baidu(unittest.TestCase):
    '''
    在python3中因为unittest运行机制变动，在使用setUp/tearDown中初始化/退出driver时，可能会出现用例执行失败没有截图的问题，但我没有遇到过，如果出现请使用setUpClass/tearDownClass的用法
    '''
    def setUp(self):
        self.imgs = []
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def get_screenshot(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def test_baidu_search(self):
        '''用例通过，没有报告内容，有多张截图'''
        self.driver.get("https://www.baidu.com")
        self.get_screenshot()
        self.driver.find_element_by_id('kw').send_keys(u'百度一下')
        self.get_screenshot()
        self.driver.find_element_by_id('su').click()
        self.get_screenshot()

    def test_baidu_assert_ok(self):
        '''用例通过，有报告内容，有截图'''
        self.driver.get("https://www.baidu.com")
        hao123 = self.driver.find_element_by_xpath('//*[@id="u1"]/a[2]').text
        print(hao123)
        self.get_screenshot()
        self.assertEqual(hao123, 'hao123')

    def test_baidu_assert_ok_noimg(self):
        '''用例通过，有报告内容，没有截图'''
        self.driver.get("https://www.baidu.com")
        news = self.driver.find_element_by_xpath('//*[@id="u1"]/a[1]').text
        print(news)
        self.assertEqual(news, u"新闻")

    def test_baidu_assert_faile(self):
        '''用例失败，带有失败内容和截图'''
        self.driver.get("https://www.baidu.com")
        self.get_screenshot()
        news = self.driver.find_element_by_xpath('//*[@id="u1"]/a[1]').text
        print(news)
        self.get_screenshot()
        self.driver.find_element_by_xpath('//*[@id="u1"]/a[1]').click()
        self.get_screenshot()
        self.assertEqual(news, 'hao123')

    def test_baidu_assert_error(self):
        ''''用例错误，带有指定错误内容和截图'''
        self.driver.get("https://www.baidu.com")
        self.get_screenshot()
        raise EnvironmentError('Current environment can not testing!')

class Case_qq(unittest.TestCase):
    def setUp(self):
        self.imgs = []
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_qq_index_faile(self):
        '''用例错误，带有错误内容和没有截图'''
        self.driver.get("https://www.qq.com")
        self.driver.find_element_by_id('sougouTxt').send_keys(u'搜狗搜索')
        # self.driver.find_element_by_id('sougouTxt').send_keys(u'搜狗搜索')
        self.driver.find_element_by_id('searchBtn').click()
        self.assertIn(u"搜狗", u'搜索')

    def test_qq_index_ok(self):
        '''用例通过，没有内容和没有截图'''
        self.driver.get("https://www.qq.com")
        self.driver.find_element_by_id('sougouTxt').send_keys(u'搜狗搜索')
        self.driver.find_element_by_id('searchBtn').click()

class Case_163(unittest.TestCase):
    def setUp(self):
        self.imgs = []
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_163_ok(self):
        '''通过 没有内容和截图'''
        self.driver.get("https://www.163.com/")


if __name__ == "__main__":
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Case_baidu)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(Case_qq)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(Case_163)
    suites = unittest.TestSuite()
    suites.addTests([suite1, suite2, suite3])

    # HTMLTestReport or HTMLTestReportEN
    with open('./HwTestReportIMG.html', 'wb') as report:
        runner = HTMLTestReportEN(stream=report,
                                verbosity=2,
                                images=True,
                                title='HwTestReport 测试',
                                description='带截图，带饼图，带详情',
                                tester='Johnny')

```
## 离线报告
使用方法和上述一致，只是选择带`local`的版本即可，美化所需的样式在`/static/`目录下，故`/static/`目录要和`生成的报告在相同目录`
```
import unittest
from HwTestReport_local import HTMLTestReport
from HwTestReport_local import HTMLTestReportEN
```

## 关键字说明
关键字| 说明
-|- 
HTMLTestReport.py| 源文件
HTMLTestReport_local.py| 离线源文件
HTMLTestReport| 生成中文报告的类
HTMLTestReportEN| 生成英文报告的类
stream| 生成的报告文件
verbosity| 运行之后打印的格式，默认值为1，有0，1，2三个值，<br>0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80<br>)1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”<br>2 (详细模式):测试结果会显示每个测试用例的所有相关的信息,并且你在命令行里加入不同的参数可以起到一样的效果，<br>源码在/Lib/unittest/runner.py
images|True 为开启Selenium或Appium截图，False或不填为关闭截图模式
title|标题，不填默认为“测试报告”
description|描述，不填默认为空
tester|测试人员，不填默认为“Johnny”


## 预览
![中文带图](https://cdn.jsdelivr.net/gh/hongweifuture/jsDelivrCDN/project/20200114113847.png)

![图片展示](https://cdn.jsdelivr.net/gh/hongweifuture/jsDelivrCDN/project/20200114102851.png)

![英文不带图](https://cdn.jsdelivr.net/gh/hongweifuture/jsDelivrCDN/project/20200120103725.png)

