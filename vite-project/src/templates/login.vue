<template>
  <div class="container">
    <div class="row">
      <div class="col-md-4 mx-auto">
        <div class="card mt-5">
          <div class="card-body">
            <h5 class="card-title text-center">用户登录</h5>
            <hr />
            <div class="card-text">
              <form @submit.prevent="login">
                <div class="mb-3">
                  <label for="username" class="form-label" >用户名</label>
                  <input
                    type="text"
                    class="form-control"
                    id="username"
                    v-model.lazy="username"
                    required
                  />
                </div>
                <div class="mb-3">
                  <label for="password" class="form-label" >密码</label>
                  <input
                    type="password"
                    class="form-control"
                    id="password"
                    v-model.lazy="password"
                    required
                  />
                </div>
                <button type="submit" class="btn btn-primary">登录</button>
              </form>
              <hr />
              <div class="text-left">
                <router-link class="text-secondary " to="/register">还没有账号？</router-link>
              </div>
              

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">

export default {
  data() {
    return {
        username: "",
        password: "",
    };
  },
  methods: {
    login() {
      //使用axios库向服务器发送请求，验证用户名和密码是否正确
      //console.log(username, password);
      this.$axios.post("/api-auth", {
        username: this.username,
        password: this.password,
      })
      .then((response) => {
        
        //如果登录成功，从本地存取token并设置到headers中
        if (response.data.token) {
          localStorage.setItem("token", response.data.token);
          localStorage.setItem("username", response.data.username);
          localStorage.setItem("user_id", response.data.user_id);
          this.$axios.defaults.headers.common["Authorization"] = "Token " + response.data.token;
          alert("用户"+response.data.username+"登录成功",{noresume:true});
          this.$router.push("/");
        } else {
          alert("登录失败,用户名或密码错误");
          console.log(response);
        }
      })
      .catch((error) => {
        console.log(error);
        alert("登录失败,用户名或密码错误");
      });
    
      //this.$router.push("/");
    },
  },
 
};
</script>
<style></style>
