
# [django-hexo-admin](https://github.com/chaofanat/django-hexo-admin)

**一个过分简单的前后端分离的基于django、vue3的[hexo博客](https://hexo.io/zh-cn/)平台后台管理系统**

---

### 1. 项目介绍
一个异常简单的但理论上能够完全保留hexo生态的博客后台管理系统。仅仅对hexo的source以及输出路径public做出了一定的硬性调整，所以如果你很熟悉hexo，那么你将非常轻松的使用这套系统进行hexo配置和hexo主题配置的录入、修改、应用。并非常方便的进行博客的撰写与发布。（至少我希望的是这样。）此外，设计上，可以部署为服务器，作为博客发布平台，每个人都可以在这个平台上发布自己的博客空间，当然一个人只能使用一种主题，虽然你能够很快的进行主题的切换。
### 2. 快速开始

要开始使用此项目，请按照以下步骤操作：

1. 下载整个项目文件或者直接git clone

```powershell
git clone https://github.com/chaofanat/django-hexo-admin.git
```

2. python安装依赖包
进入django项目文件夹

```powershell
cd django-hexo-admin
cd django_hexo_admin
pip install -r requirements.txt
```

3.  django初始化
同样在django项目文件夹下
```powershell
#运行django服务,8081是默认端口，如果要调整需要更改django项目setting.py的FOR_HEXOCONFIG_URL属性以及nginx的配置文件nginx.config
python manage.py runserver 127.0.0.1:8081
```
*此项目的测试数据并未清除，django超级用户为admin，密码123456，服务运行后，可以登录http://127.0.0.1:8081/admin访问django自带的后台管理系统，可以很方便的进行数据库的管理*

4. 全局安装hexo-cli
建议使用npm进行安装

```powershell
npm install hexo-cli -g
```

5.  运行nginx服务
进入nginx目录启动服务

```powershell
cd ..
cd nginx-1.24.0
start nginx
```
6. 浏览器登录127.0.0.1即可
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/c0535d29fea3456cad66f88bddd1ee1c.png)


### 3. 项目逻辑与架构

- 前后端分离
前端使用vite-vue进行vue单页面应用开发。样式使用bootstrap5进行简单的布局以及样式设计。
后端使用django序列化器进行api的模块化开发。
- 系统与hexo集成逻辑
hexo博客网站生成器的关键在于其配置文件也就是_config.yml文件，为用户生成个人独有的配置文件，使用subprocess进行shell命令的运行，将生成的站点文件复制到nginx指定的访问目录。
- 用户的每一次博客发布都会执行：
1. 文章写入hexo的source目录。
2. congfig文件的重写入。
3. hexo clean
4. hexo generate --config xx.hexoconfig.json
5. 生成的站点文件复制到nginx指定目录
- 数据库
数据库使用django默认的sqlite3。
设计详情请查看django应用下的models.py文件
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/b444ac193e81441cbfe5eb6528d8232d.png)
- api设置
功能基本和数据库一一对应，处理函数在views.py文件中
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/e16c561b84d44e2e9d612d595c4643b6.png)

### 4. 运行效果截图

- 主页
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/c4d6805892194b49a1a979caeb384acb.png)
- hexo配置
hexo配置直接关系到hexo生成器的运行，至关重要，对于hexo及其主题配置需要一定的研究，系统会自动拉取hexo的默认配置。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/8b1d3ac5a9724aad9127129b1d56ee95.png)
- hexo主题选择及配置
主题选择后请注意对配置进行保存（无论是否修改），才能挂接到hexo配置文件中。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/a92467f4db7641acb725ddf1b79db99b.png)
- 博客写作及发布
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/9651b44297ad4f9a869a19c210e76671.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/7cea23130e4040568475087a1c7c45d9.png)
- 发布成功后会自动跳转至你的个人博客空间（可能会被拦截）
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/06c60538791742bfaeeacc71322ae1eb.png)
- 个人博客空间地址为blog/用户名
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/08569352c15e43fe89225aaab005f5c3.png)





### 5. 依赖项

1. 本项目的开发环境为python3.11.7
2.  Django版本为5.0.3
3.  前端框架为vite-vue3
4.  hexo版本为7.1.0
*如果您想要进行二次开发，可能不得不安装nodejs，前端的开发项目也包含在这个项目中了（vite-project)。另外整个项目是在vscode中进行开发的。*

### 6. 贡献指南

由于本人非职业程序员，也是第一次接触github，无论是前端还是后端的代码都可能不那么规范与高效，欢迎everybody通过邮箱联系我，我可以将你的ssh进行密钥进行登记，然后你可以直接对此项目进行优化甚至是重新架构。

### 7. 联系方式

如果你有任何问题或建议，请通过以下方式联系我：

- 邮箱：chaofanat@qq.com
- chaofanat@gmai.com




