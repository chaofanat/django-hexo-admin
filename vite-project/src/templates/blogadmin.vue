<template>
  <div class="container">
    <div class="row">
      <div class="col-md-2">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">博客列表</h5>
            <nav class="nav flex-column">
              <ul>
                <li v-for="blog in blogs">
                  <a @click="oneditblog = blog" class="nav-link" href="#">{{
                    blog.title
                  }}</a>
                </li>
              </ul>
            </nav>
            <button class="btn btn-primary btn-block" @click="createblog()">
              创建新博客
            </button>
          </div>
        </div>
      </div>
      <div id="editbox" class="col-md-10">
        <div class="mb-3">
          <div class="card">
            <div class="card-header">工具栏</div>
            <div class="card-body d-flex flex-row">
              <div class="w-50">
                <input
                  type="text"
                  class="form-control"
                  placeholder="输入标题"
                  v-model="oneditblog.title"
                />
              </div>
              <div class="btn-group w-50 text-right">
                <button type="button" class="btn btn-primary" @click="save()">
                  保存
                </button>
                <button
                  type="button"
                  class="btn btn-secondary"
                  @click="saveasnew()"
                >
                  保存为新博客
                </button>
                <button
                  type="button"
                  class="btn btn-primary"
                  @click="deleteblog()"
                >
                  删除
                </button>
                <button
                  type="button"
                  :disabled="isPublishing == '发布中。。。'"
                  class="btn btn-secondary"
                  @click="publish()"
                >
                  {{isPublishing}}
                </button>
                <router-link class="btn btn-primary" to='/'>回到主页</router-link>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">markdown编辑</div>
              <div class="card-body">
                <textarea
                  class="form-control"
                  rows="20"
                  v-model="oneditblog.md_content"
                  @change="updateMarkdownPreview()"
                ></textarea>
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

<script lang="ts">
import MarkdownIt from "markdown-it";

export default {
  name: "blog-editor",
  data() {
    return {
      blogs: [],
      oneditblog: { title: "", md_content: "" },
      markdownpreview: "",
      md: MarkdownIt(),
      isPublishing: '发布',
    };
  },

  created() {
    this.$axios.defaults.headers.common["Authorization"] =
      "Token " + localStorage.getItem("token");
    this.$axios
      .get("/hexo_blogs")
      .then((response) => {
        this.blogs = response.data;
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    createblog() {
      this.oneditblog = { title: "", md_content: "" };
    },
    updateMarkdownPreview() {
      this.markdownpreview = this.md.render(this.oneditblog.md_content);
    },
    save() {
      if (this.oneditblog.id) {
        this.$axios
          .put("/hexo_blog", {
            id: this.oneditblog.id,
            title: this.oneditblog.title,
            md_content: this.oneditblog.md_content,
          })
          .then((response) => {
            console.log(response);
            alert("保存成功");
            this.oneditblog = response.data;
          })
          .catch((error) => {
            alert("保存失败");
            console.log(error);
          });
      } else {
        this.$axios
          .post("/hexo_blog", {
            title: this.oneditblog.title,
            md_content: this.oneditblog.md_content,
          })
          .then((response) => {
            console.log(response);
            alert("保存成功");
            this.oneditblog = response.data;
            this.blogs.push(response.data);
          })
          .catch((error) => {
            alert("保存失败,已经存在相同标题的文章");
            console.log(error);
          });
      }
    },
    saveasnew() {
      this.$axios
        .post("/hexo_blog", {
          title: this.oneditblog.title,
          md_content: this.oneditblog.md_content,
        })
        .then((response) => {
          console.log(response);
          alert("保存成功");
          this.oneditblog = response.data;
          //刷新页面
          document.location.reload();
        })
        .catch((error) => {
          alert("保存失败,已经存在相同标题的文章");
          console.log(error);
        });
    },
    deleteblog() {
      this.$axios
        .delete("/hexo_blog", { data: { id: this.oneditblog.id } })
        .then((response) => {
          console.log(response);
          alert("删除成功");
          this.oneditblog = { title: "", md_content: "" };
          //刷新页面
          document.location.reload();
        })
        .catch((error) => {
          alert("删除失败");
          console.log(error);
        });
    },
    publish() {
      this.isPublishing = '发布中。。。';
      this.$axios
        .get("/hexo_blog", { params: { id: this.oneditblog.id } })
        .then((response) => {
          console.log(response);
          alert("发布成功");
          //打开一个新窗口，路径是当前页面根路径的publish文件夹
          window.open('../blog/'+localStorage.getItem('username')+'/', '_blank');
          this.isPublishing = '发布';
        })
        .catch((error) => {
          alert("发布失败");
          console.log(error);
          this.isPublishing = '发布';
        });
      
    },
  },
};
</script>
