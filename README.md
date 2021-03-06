ChinaUnicom 自动登录断线重连
========



### 功能
实现ChinaUnicom wifi登陆和实时断线检测重连,解决了网页登陆频繁掉线的问题
适合Windows和Linux

### 使用
需要``httplib2``或``requests``库,安装请访问:

httplib2:

    https://pypi.python.org/pypi/httplib2

requests:

    http://docs.python-requests.org/en/latest/user/install/#install

访问或通过``wget``下载``https://github.com/laike9m/CU_login/blob/master/src/login.py``
注意：根据Python版本不同请选择下载合适的文件

执行``python login.py``或``python3.3 login.py``即可(在windows下如果把python.exe关联了.py文件,直接双击即可)

### 注意:
弹出的窗口一直放着不管就好,每10s会检测一次当前状态.如果已经登录,关掉也可以,但就不能及时检测重连了.


ChinaUnicom auto login ,re-login after disconnection 
=====



### Function
Use it to login to ChinaUnicom wifi using your ChinaUnicom account.
it will re-login as soon as ChinaUnicom wifi log you out, solve the problem once and for all.
Windows and Linux compliant.

### Usage
``httplib2`` or ``httplib2`` are required.Visit the listed sites to install.

httplib2:

    https://pypi.python.org/pypi/httplib2

requests:

    http://docs.python-requests.org/en/latest/user/install/#install

Then download the file ``https://github.com/laike9m/CU_login/blob/master/src/login.py``,
you can download it directly or using ``wget``.
Note: download the file corresponding to your Python version  

Finally, run ``python login.py`` or ``python3.3 login.py`` in Windows and Linux, or just dbclick the file if you are  
using Windows.

### Note
You will just ignore the python.exe window, it will detect the current login state every 10s.
You can close the window after logining, which will disable subsequent detection and re-login.
