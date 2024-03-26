<script setup lang="ts">


defineProps<{ msg: string }>()


</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <el-button type="primary">使用element-plus的第一个按钮</el-button>
  </div>

</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
