# django-hexo-admin
一个基于django的hexo可视化博客管理平台
计划用vue进行前端界面的设计，django提供功能api。

项目计划：
1. Hexo与Django的整合
理解Hexo的工作原理：Hexo是一个快速、简洁且高效的博客框架，它使用Markdown（md）文件生成静态网页。了解Hexo的文件结构和生成流程对整合非常重要。
Hexo内容管理：通过Django管理Hexo博客的内容，包括创建、编辑Markdown文件，并能够触发Hexo的生成命令重新生成静态文件。
自动化部署：集成Hexo的生成和部署过程到Django平台，实现一键发布。这可能需要编写脚本或使用CI/CD工具自动化Hexo的构建和部署流程。
2. 数据库设计
由于Hexo是静态网站生成器，使用文件系统而非数据库来管理内容，因此，需要在Django中设计一套模型来管理和映射到Hexo的内容结构，例如：
文章（Posts）：对应Hexo的Markdown文件，模型中应包含标题、内容、创建时间、更新时间等字段。
分类（Categories）和标签（Tags）：在Django中管理，通过生成或更新Markdown文件头部的元数据来实现。
3. 前端界面与Hexo主题的整合
主题定制：根据需要定制或选择合适的Hexo主题，保证博客的前端展示效果。
Vue与Hexo主题的协同工作：在Vue中设计管理界面，而博客展示则使用Hexo生成的静态页面。两者可以通过Django作为中介，使得Vue开发的管理界面能够控制Hexo内容的生成和更新。
4. 功能实现细节
文章编辑器：在Vue前端实现Markdown编辑器，方便直接在Web界面上编写和编辑文章。
预览功能：集成Markdown预览功能，让用户在提交文章之前能够预览最终的展示效果。
静态文件管理：设计一个高效的方式来同步和管理Hexo生成的静态文件，以及与之相关的资源文件，如图片、JavaScript和CSS文件。
