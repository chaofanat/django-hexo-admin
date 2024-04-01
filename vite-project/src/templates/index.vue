<template>
  <div class="container-fluid vh-100">
    <div class="row vh-100 justify-content-center align-items-center">
      <div class="col-8">
        <div class="card border-0 shadow-lg p-5 mb-5 bg-white rounded">
          <h1 class="card-title">{{username}}你好，欢迎使用django-hexo-admin！</h1>
          <h2 class="card-subtitle mb-2 text-muted">
            请设置你的hexo配置，或者开始写博客吧！
          </h2>
          <div class="card-body w-25">
            <div class="d-grid gap-2">
              <router-link class="btn btn-primary" to='/hexo_config'>Hexo配置</router-link>
              <router-link class="btn btn-secondary" to='/blog'>开始写博客</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
    
export default {
  name: 'index',
  components: {},
  data() {
    return {
      username: localStorage.getItem('username'),
    }
  },
  methods: {},
  mounted() {
  }
}
   
  
   
</script>
<style>
 
</style>