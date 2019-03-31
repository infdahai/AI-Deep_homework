# Python与深度学习基础

​																				PB16080377 聂雷海 组别



### 功能和使用说明: (含GUI图片截图，后续有详细解释)

​	本工程构造了一个简易的聊天app，图形界面使用kivy,聊天信息传输 采用twisted库。

​	第一张图，表明连接ip地址，即localhost地址，采用Nickname进行聊天。

​	客户端进程通过输入消息后，点击send，显示在框内。服务器收到消息后，调用[图灵机器人](<http://www.tuling123.com/>)api，然后接受返回信息，再传回到服务器，服务器将信息返回到客户端界面内。

![](/home/nlh/Pictures/Screenshot from 2019-03-31 21-35-43.png)

![](/home/nlh/Pictures/Screenshot from 2019-03-31 21-37-57.png)


##### 	





### 关于代码的解释:

​	文件结构如下图

​		![](/home/nlh/Pictures/Screenshot from 2019-03-31 21-43-39.png)	

​	api_use.py使用json请求图灵机器人的api,然后受到回复. server.py作为服务器进程，监听ip:0.0.0.0端口(9006)，等待客户端发送信息。

​	client.py则接收标准输入流，将输入串读入，发送到服务端。  main.py 作为程序执行入口， 开启serve和client进程，维持整个程序执行。

​	代码上,  我为了在server.py中能使用api_use.py中定义的函数，我在server.py中 echo类的初始化中引入private变量self._use_api,作为api_use生成的实例，然后在之后dataReceived函数中，用这个变量来进行数据的传输与接收，实现api的调用。GUI界面上，使用kivy代码 构建了GUI中各个对象、试图的属性，以及触发函数，从而实现了GUI内部逻辑和布局。



### Summay：

​	由于大三下时间很紧，导致这个工程并没有多长时间写。

​	我使用kivy的原因在于，前期调研发现reddit论坛上有人说kivy可以给python GUI开发非常feature的界面，因此我就打算入坑。并且它主要依托于社区维护(我混迹于github中国各大社区，感觉社区很靠谱)，我就开始用kivy编写GUI。

​	但渐渐发现不是这回事，kivy 官方文档少有例子，更多的是讲这个库有怎样的api，能实现什么样的功能。kivy github地址还在更新，但热度下降。我在时间很有限的情况下，决定去做一个漂亮的界面，于是我去调研了kivy designer。我的环境时arch linux,在我解决了各路安装bug，以及多次忙等情况下，最后出了个bug，始终保存不了我建立的工程(查阅发现，这个bug早在2017年就在论坛里提出，至今没有响应)。以及它推荐的twisted 库用来作CS架构网络引擎，事实上twisted对python3 竟然只能部分支持，我在使用它所提供api写CS架构时，竟然不允许unicode传输(因为我要传输中文)。

​	经过上述bug之后，着实有点心灰意冷。  早知道应该跟着大家做差不多的东西，用比较成熟的Qt Designer。外国的社区还是比如国人的社区靠谱。python我在上这门课之前就已经使用过一段时间，并用它写了许多经典算法代码，如今因为环境上的选择导致我实验难以完成，确实不应该。