<template>
  <div class="home">
    <h1 class="animate__animated animate__backInDown">欢迎来到大杂烩之家！</h1>
    <h1 class="animate__animated animate__backInDown">欢迎您，{{ user }}，请先修改密码！</h1>
    <h1 class="animate__animated animate__backInDown">
      {{ time }}
    </h1>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { GetLoginTimeApi } from "@/api/user_home";
const user: string | null = localStorage.getItem("access_user");
const time = ref("");

const get_login_time = async () => {
  try {
    const res = await GetLoginTimeApi({ username: user });
    time.value = res.data.message;
  } catch (error) {
    console.log("获取登录时间失败");
  }
};

onMounted(get_login_time);
</script>

<style scoped>
@import "animate.css";
.home {
  text-align: center;
  margin-top: 150px;
}
h1 {
  font-size: 50px;
  margin-top: 30px;
  font-family: "华文楷体";
  color: #bbb;
}
</style>
