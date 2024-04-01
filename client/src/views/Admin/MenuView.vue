<template>
  <div>
    <h5>后台管理系统</h5>
    <el-menu
      :default-active="$route.path"
      class="el-menu-vertical-demo"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      router
    >
      <el-menu-item class="item" index="/admin_home">
        <span class="iconfont">&#xe622;</span>
        <span>首页</span>
      </el-menu-item>
      <el-menu-item class="item" index="/admin_user">
        <span class="iconfont">&#xe697;</span>
        <span>用户管理</span>
      </el-menu-item>
      <el-menu-item class="item" index="/admin_login_log">
        <span class="iconfont">&#xe7d4;</span>
        <span>登录日志管理</span>
      </el-menu-item>
      <el-menu-item class="item" index="/admin_card_record">
        <span class="iconfont">&#xe753;</span>
        <span>签到管理</span>
      </el-menu-item>
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
.iconfont {
  margin-right: 15px;
  font-size: 20px;
}
</style>
