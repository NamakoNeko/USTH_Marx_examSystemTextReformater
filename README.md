# 适用于黑龙江科技大学马院在线测试系统的题库拉取工具

本项目的目的是用于拉取来自黑龙江科技大学马克思主义学院在线测试系统的题库，并整理成对应章节的txt文件。

## 目前实现的功能

1. 整理获取到的JSON文件并输出成可供人阅读的txt格式。（第一行题号 第二行答案 第三行选项供校对）

## 使用方法

先安装[Fiddler](https://www.telerik.com/fiddler)，[安装教程](https://blog.csdn.net/ychgyyn/article/details/82154433)。

仅参考Fiddler中电脑抓包的部分，因安卓高版本系统的缘故导致目前在手机上无法正常进行抓包。

安装[Python](https://www.python.org/)，[安装教程](https://www.cnblogs.com/lvtaohome/p/11121377.html)。

以管理员身份启动命令行（不知道怎么弄的点开任务管理器左上角文件-运行 输入cmd勾上以管理员权限创建此项目并确定），在弹出的cmd窗口中输入`pip install --upgrade pip` ，必须以管理员权限运行否则此步在Win10下会报错，安装需要的依赖包`pip install jsonpath`。

登录电脑版微信，找到马院思政之音公众号并点开，选取右上角三个点里的进入公众号，找到在线测试系统，此时会启动一个微信小程序。

打开Fiddler，在Fiddler右侧栏位中找到Filter选项卡，在Process-how only traffic from的下拉栏中选取WeChatApp:**** -智能化学习考试系统 (**** 是任意数字)，选中 点击此页面右上角Actions-Run Filterset Now启动筛选。

登录在线测试系统系统，选择练习-你要抓取的科目，进入章节选择页面后先不要动。

在Fiddler左侧栏点击右键-Remove-All Sessions清理掉现在里面的所有数据，回到在线测试系统依次点击进入测试并回退，此时你在Fiddler里应该可以看到抓取到的JSON。选中它们，右键-Save-...and Open as Local File，打开弹出的所有编辑器窗口，这些JSON文件已经保存到了桌面，把它们重命名成对应章节名字，然后移动到你保存工具目录里的qstorage文件夹下。

打开命令提示符(Win+R输入cmd并回车)，定位到工具所在目录，输入`py reformate.py`并回车，qstorage目录下应该生成了整理好的txt文件，保存你要的txt文件。

使用完之后记得清理掉qstorage目录下的所有文件，不然下次运行会混乱（我调试的时候故意没加清理目录的代码，防止误删要的文件）。
