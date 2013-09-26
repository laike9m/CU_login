import httplib2
import time
import os
from sys import exit
from threading import Timer
from platform import system

class ChinaUnicom_Login():
    
    def __init__(self, interval=10):
        self.interval = interval
        self.state = False  # 未登录
        self.userinfo_dir = ''  # 保存用户信息的路径
        self.phone_number = ''
        self.password = ''
    
    
    def get_user_info(self):
        
        # 存储或读取用户信息
        
        sys_type = system() # 系统类型
        user_dir = os.path.expanduser('~')  #用户家目录
        if sys_type == 'Linux':
            self.userinfo_dir = user_dir + '/Documents/CU_login'
        elif sys_type == 'Windows':
            self.userinfo_dir = user_dir + '\\My Documents\\CU_login'
        else:
            print('Unsupported system.Try using Linux or Windows.')
            exit(0) # 平台不支持,直接退出
        
        if os.path.exists(os.path.join(self.userinfo_dir, 'userinfo')):
            # 有userinfo文件
            with open(os.path.join(self.userinfo_dir, 'userinfo'), 'r') as userinfo_file:
                self.phone_number = userinfo_file.readline().rstrip()    
                self.password = userinfo_file.readline()
        else:
            if not os.path.exists(self.userinfo_dir):
                os.mkdir(self.userinfo_dir)
                
            choice = input("Do you want your info be stored in this CPU? : (Y/N) ")
            
            if (True if choice=='Y' or 'y' else False):
                # 用户选择保存个人信息
                with open(os.path.join(self.userinfo_dir, 'userinfo'), 'w') as userinfo_file:
                    self.phone_number = input('Please enter your phone number: ')
                    self.password = input('Please enter your password: ')
                    userinfo_file.write(self.phone_number + '\n' + self.password)
            else:
                self.phone_number = input('Please enter your phone number: ')
                self.password = input('Please enter your password: ')
        
        print(self.phone_number, '  ', self.password)
    
    
    def login(self):
        h = httplib2.Http()
        headers = {}
        headers['accept'] = "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01"
        headers['x-requested-with'] = "XMLHttpRequest"
        headers['referer'] = "http://202.106.46.37/index.do"
        headers['accept-language'] = 'zh-CN'
        headers['accept-encoding'] = "gzip, deflate"
        headers['user-agent'] = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)'
        headers['host'] = '202.106.46.37'
        headers['dnt'] = '1'
        headers['connection'] = 'keep-alive'
        headers['cookie'] = 'JSESSIONID=4003A8C5A8DE955BABAC66B0A6405C02'
        
        url = "http://202.106.46.37/login.do?callback=jQuery17100013734368553252607_1378108363139&username=%s&password=%s&passwordType=6&wlanuserip=&userOpenAddress=bj&checkbox=1&basname=&setUserOnline=&sap=&macAddr=&bandMacAuth=0&isMacAuth=&basPushUrl=http://202.106.46.37/&passwordkey=&_=1378108463014"\
              % (self.phone_number, self.password)
        
        response, content = h.request(url, headers=headers)
        print(response)
        print(content)


    def test_state(self):
        
        #测试是否处于已登录状态
        
        h = httplib2.Http()
        response, _ = h.request('http://61.135.169.105/') # http://www.baidu.com
        
        if response['content-location'] == 'http://202.106.46.37':
            #访问baidu却跳转到CU登陆页面,说明未登陆
            self.state = False
        else:
            self.state = True
            

    def loop(self):    
        
        # 主循环
        
        self.test_state()
        ctime = time.ctime()
        if not self.state:  
            print('Current state: not logged in --- %s\n' % ctime)
            self.login()
            print('\nlogin successful --- %s\n' % ctime)
        else:
            print('Current state: logged in --- %s\n' % ctime)
        Timer(self.interval, self.loop).start()
                
                
                
if __name__ == '__main__':
    cu_login = ChinaUnicom_Login()
    cu_login.get_user_info()
    cu_login.loop()