<template>
    <div class="container">
        <div class="row">
            <div class="col-md-2">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">博客列表</h5>
                        <nav class="nav flex-column">
                            <a v-for="blog in blogs" @click="oneditblog=blog" class="nav-link" href="#">{{blog.title}}</a>
                            
                        </nav>
                        <button class="btn btn-primary btn-block" @click="createblog()">创建新博客</button>
                    </div>
                </div>
            </div>
            <div  id='editbox' class="col-md-10">
                <div class="mb-3">
                    <div class="card">
                        <div class="card-header">
                            工具栏
                        </div>
                        <div class="card-body d-flex flex-row">
                            <div class="w-50">
                                <input type="text" class="form-control" placeholder="输入标题" v-model="oneditblog.title">
                            </div>
                            <div class="btn-group  w-50 text-right ">
                                <button type="button" class="btn btn-primary" @click="save()">保存</button>
                                <button type="button" class="btn btn-secondary" @click="saveasnew()">保存为新博客</button>
                                <button type="button" class="btn btn-primary" @click="publish()">发布</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <div class="card">
                            <div class="card-header">markdown编辑</div>
                            <div class="card-body">
                                <textarea class="form-control" rows="20" v-model="oneditblog.md_content" @change="updateMarkdownPreview()"></textarea>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="card h-100">
                            <div class="card-header">markdown预览界面</div>
                            <div class="card-body h-100">
                                <div class="markdown-body h-100">
                                    <div v-html="markdownpreview"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" >
    import MarkdownIt from 'markdown-it'
    
    export default {
        name: 'blog-editor',

        data() {
            return {
                blogs:[],
                oneditblog: {'title':'','md_content':''},
                markdownpreview:'',
                md:MarkdownIt(),
              
            }
        },
      
        created() {
            this.$axios.defaults.headers.common["Authorization"] =
      "Token " + localStorage.getItem("token");
            this.$axios.get('/hexo_blogs').then(response => {
                this.blogs = response.data;
            }).catch(error => {
                console.log(error);
            });
        },
        methods: {
            createblog(){
                this.oneditblog = {'title':'','md_content':''};
            },
            updateMarkdownPreview() {
                
                this.markdownpreview = this.md.render(this.oneditblog.md_content);
            },
            save(){},
            
            publish(){},
        }
    };
    
</script>
