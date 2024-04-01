<template>
  <div>
    <h5>大杂烩之家</h5>
    <el-menu
      :default-active="$route.path"
      class="el-menu-vertical-demo"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      router
    >
      <el-menu-item class="item" index="/user_home">
        <span class="iconfont iconfont_icon">&#xe622;</span>
        <span>首页</span>
      </el-menu-item>

      <el-sub-menu index="1">
        <template #title>
          <span class="iconfont iconfont_icon">&#xe753;</span>
          <span>打卡</span>
        </template>
        <el-menu-item class="item" index="/user_mark_card">
          <span>点击打卡</span>
        </el-menu-item>
        <el-menu-item class="item" index="/user_card_record">
          <span>打卡统计</span>
        </el-menu-item>
      </el-sub-menu>
    </el-menu>
  </div>
</template>

<script lang="ts" setup></script>

<style scoped>
@import "@/assets/css/iconfont.css";
h5 {
  height: 25px;
  font-size: 20px;
  font-weight: normal;
  text-align: center;
  margin-top: 15px;
  margin-bottom: 15px;
  color: #fff;
}
.item {
  width: 200px;
  border-bottom: 1px solid #778490;
  border-right: 1px solid #778490;
}
.iconfont_icon {
  margin-right: 15px;
  font-size: 20px;
}
</style>
