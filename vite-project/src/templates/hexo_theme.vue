<template>
  <div class="container">
    <div class="mb-3">
      <label for="themeSelect" class="form-label">选择你想使用的主题：</label>
      <select
        v-model="selecttheme_name"
        @change="
          selecttheme = themes.find(
            (theme) => theme.theme_name === selecttheme_name
          )
        "
        id="themeSelect"
        class="form-select"
      >
        <option v-for="theme in themes" v-bind:value="theme.theme_name">
          {{ theme.theme_name }}
        </option>
      </select>
    </div>

    <div class="card mb-3">
      <div class="card-body">
        <h5 class="card-title">主题详情</h5>
        <div>
          <p>主题名称：{{ selecttheme.theme_name }}</p>
          <p>Git地址：{{ selecttheme.theme_url }}</p>
          <p>预览地址：{{ selecttheme.theme_preview_url }}</p>
        </div>

        <div>
          <button class="btn btn-primary" @click="useTheme">使用此主题</button>
        </div>
      </div>
    </div>
    <div class="card mb-3">
      <div class="card-body d-flex flex-column">
        <div><p class="card-text">你目前使用的主题是：{{ selectedTheme.theme_title }}</p></div>
        <div class="mt-auto d-grid gap-2">
          <router-link class="btn btn-primary w-25" to="/hexo_config"
            >回到Hexo配置</router-link
          >

          <router-link class="btn btn-secondary w-25" to="/blog"
            >开始写博客</router-link
          >
        </div>
      </div>
    </div>
    <div class="card mb-3">
      <div class="col-md-10 vh-100">
        <div class="row row-cols-1 row-cols-md-2 h-100 g-4">
          <div class="col">
            <div class="card h-100">
              <div class="card-body p-4 h-100">
                <div class="d-flex justify-content-between align-items-center">
                  <div class="fs-5">主题相关配置</div>
                  <div>
                    <button
                      class="btn btn-primary"
                      @click="parsethemeconfig()"
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
                  @change="parsethemeconfig()"
                  v-model="themeconfig"
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
                      @click="updatethemeconfig()"
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
                  v-model="jsonthemeconfig"
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
  data() {
    return {
      themes: [],
      selecttheme_name: "",
      selecttheme: "",
      selectedTheme: "",
      themeconfig: "",
      jsonthemeconfig: "",
    };
  },
  created() {
    this.$axios.defaults.headers.common["Authorization"] =
      "Token " + localStorage.getItem("token");
    this.$axios
      .get("/hexo_theme")
      .then((res) => {
        //如果data是一个空列表，则返回一个空对象，而不是一个空列表。
        if (res.data == []) {
          this.updateThemeList();
        } else {
          this.themes = res.data;
        }
        this.themes = res.data;
      })
      .catch((err) => {});

    this.$axios
      .get("/hexo_theme_config")
      .then((res) => {
        if (res.data == null) {
          this.selectedTheme = { theme_title: "还未设置主题！" };
        } else {
          this.selectedTheme = res.data;
          this.themeconfig = yaml.dump(Json.parse(res.data.config));
        }
      })
      .catch((err) => {});
  },
  mounted() {},

  methods: {
    jsonstotring(str) {
      str = str.replace(/(\w+)\s*:/g, '"$1":');
      str = str.replace(/"http"/g, 'http').replace(/"https"/g, 'https');
      str = str.replace(/(\d{1,3})\.(\d{1,3})\.(\d{1,3})\."(\d{1,3})"/g, '$1.$2.$3.$4');
      str = str.replace(/"HH":"mm":ss/g, 'HH:mm:ss');
      str = str.replace(/\'/g,'"');
      return str;
    },
    updateThemeList() {
      this.$axios
        .get("/pull_hexo_theme")
        .then((res) => {
          this.themes = res.data;
          console.log(this.themes);
        })
        .catch((err) => {});
    },
    useTheme() {
      this.$axios
        .get("/hexo_theme_config", {
          params: { theme_name: this.selecttheme_name },
        })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    parsethemeconfig() {
      try {
      this.jsonthemeconfig = this.jsonstotring(Json.stringify(yaml.load(this.themeconfig),null,2));
       
      } catch (e) {
        alert("yml配置存在问题！");
      }
    },

    updatethemeconfig() {
      this.parsethemeconfig();
      this.$axios
        .post("/hexo_theme_config", {
          config: this.jsonstotring(Json.stringify(yaml.load(this.jsonthemeconfig))),
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
  },
};
</script>
