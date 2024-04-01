<template>
  <div class="layout">
    <MenuVue class="menu"></MenuVue>
    <ContentVue class="content"></ContentVue>
  </div>
</template>

<script lang="ts" setup>
import MenuVue from "@/views/Admin/MenuView.vue";
import ContentVue from "@/views/Admin/ContentView.vue";
</script>

<style scoped>
.menu {
  width: 200px;
  min-height: 500px;
  background-color: #6d7379;
  /*固定定位*/
  position: fixed;
  top: 0;
  bottom: 0;
}

.content {
  margin-left: 200px;
  min-height: 500px;
}
</style>
