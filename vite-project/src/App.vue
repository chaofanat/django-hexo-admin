<template>
  <div>
  <el-config-provider :size="size" :z-index="zIndex">
    <HelloWorld msg="Vite + Vue" />
  </el-config-provider>
  </div>
 
</template>





<script>
import HelloWorld from './components/HelloWorld.vue'
import { defineComponent } from 'vue'
import { ElConfigProvider } from 'element-plus'

export default defineComponent({
  components: {
    ElConfigProvider,
  },
  setup() {
    return {
      zIndex: 3000,
      size: 'medium',
    }
  },
})
</script>




<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
