<template>
  <div class="container vh-100">
    <div class="row">
      <div class="col-md-2 vh-100">
        <div>
          <div class="card h-100">
            <div class="card-body p-2">
              <nav
                id="sidebarMenu"
                class="d-flex flex-column align-items-start p-0 bg-light"
              >
                <span class="bi bi-card-list me-1"></span>
                导航栏

                <ul class="nav nav-pills flex-column mb-auto">
                  <li class="nav-item">
                    <a class="nav-link" href="#">
                      <span class="d-flex align-items-center">
                        <span class="bi bi-collection me-1"></span>
                        hexo配置
                      </span>
                    </a>
                  </li>
                  <li class="nav-item">
                      <router-link class="nav-link" to="/hexo_theme">主题配置</router-link>
                  </li>
                  <li class="nav-item">
                    <router-link class="nav-link" to="/">回到主页</router-link>
                  </li>
                </ul>
              </nav>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-10 vh-100">
        <div class="row row-cols-1 row-cols-md-2 h-100 g-4">
          <div class="col">
            <div class="card h-100">
              <div class="card-body p-4 h-100">
                <div class="d-flex justify-content-between align-items-center">
                  <div class="fs-5">hexo配置</div>
                  <div>
                    <button
                      class="btn btn-primary"
                      @click="parse()"
                      type="button"
                    >
                      预览
                    </button>
                  </div>
                </div>
                <hr class="my-3" />
                <textarea
                  class="form-control h-75"
                  aria-label="With textarea"
                  @change="parse()"
                  v-model="config"
                ></textarea>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card h-100">
              <div class="card-body p-4">
                <div class="d-flex justify-content-between align-items-center">
                  <div class="fs-5">yml配置json格式预览</div>
                  <div>
                    <button
                      class="btn btn-primary"
                      @click="update()"
                      type="button"
                    >
                      保存
                    </button>
                  </div>
                </div>

                <hr class="my-3" />
                <textarea
                  class="form-control h-75"
                  aria-label="With textarea"
                  v-model="jsonconfig"
                ></textarea>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
//导入 js-yaml
import yaml from "js-yaml";
//导入Json
import Json from "json5";
export default {
  name: "HexoConfig",
  data() {
    return {
      config: "",
      jsonconfig: "",
    };
  },
  created() {
    //从客户端请求数据并显示
    this.$axios.defaults.headers.common["Authorization"] =
      "Token " + localStorage.getItem("token");
    this.$axios
      .get("/hexo_config")
      .then((response) => {
        console.log(response.data.config);
        this.config = yaml.dump(Json.parse(response.data.config));
      })
      .catch((error) => {
        console.log(error);
        console.log(localStorage.getItem("token"));
      });
  },
  methods: {
    parse() {
      try {
      this.jsonconfig = this.jsonstotring(Json.stringify(yaml.load(this.config),null,2));
       
      } catch (e) {
        alert("yml配置存在问题！");
      }
    },

    update() {
      this.parse();
      this.$axios
        .post("/hexo_config", {
          config: this.jsonstotring(Json.stringify(yaml.load(this.jsonconfig))),
        })
        .then((response) => {
          if (response.data.message != "success") {
            alert("保存失败:" + response.data.message);
          } else {
            alert("配置已上传至服务器");
          }
        })
        .catch((error) => {
          alert("保存失败:" + error);
        });
    },

    jsonstotring(str) {
      str = str.replace(/(\w+)\s*:/g, '"$1":');
      str = str.replace(/"http"/g, 'http').replace(/"https"/g, 'https');
      str = str.replace(/"mailto":name@email.com/g, 'mailto:name@email.com');
      str = str.replace(/(\d{1,3})\.(\d{1,3})\.(\d{1,3})\."(\d{1,3})"/g, '$1.$2.$3.$4');
      str = str.replace(/"HH":"mm":ss/g, 'HH:mm:ss');
      str = str.replace(/\'/g,'"');
      return str;
    },
  },
  mounted() {},
};
</script>

<style>
input {
  word-wrap: break-word;
}
</style>
