<template>
  <div class="wrapper">
    <div class="container">
      <div class="header">
        <h1>登录</h1>
      </div>
      <div class="main">
        <el-form :model="LoginForm" label-width="60px">
          <el-form-item>
            <el-input
              v-model="LoginForm.username"
              class="input_box"
              placeholder="请输入账号"
            />
            <template #label>
              <span>
                <i class="iconfont">&#xe697;</i>
              </span>
            </template>
          </el-form-item>
          <el-form-item>
            <el-input
              v-model="LoginForm.password"
              class="input_box"
              placeholder="请输入密码"
              type="password"
            />
            <template #label>
              <span>
                <i class="iconfont">&#xe601;</i>
              </span>
            </template>
          </el-form-item>
          <el-form-item>
            <div class="msg">
              假若你没有账号,请先进行<span
                class="to_register"
                @click="to_register"
                >注册</span
              >
            </div>
          </el-form-item>
          <el-form-item>
            <el-button class="login_btn" type="primary" @click="onSubmit"
              >登录</el-button
            >
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { ElMessage } from "element-plus";
import { LoginApi } from "@/api/login";
import { useRouter } from "vue-router";
const router = useRouter();

const LoginForm = ref({
  username: "",
  password: "",
});

const onSubmit = async () => {
  try {
    const res = await LoginApi(LoginForm.value);
    if (res.status == 200) {
      ElMessage({
        message:  res.data.message,
        type: "success",
        duration: 1000,
      });
      localStorage.setItem("access_token", res.data.token);
      localStorage.setItem("access_user", res.data.username);
      if (res.data.role == "admin") {
        setTimeout(() => {
          router.push({ path: "/admin_index" });
        }, 1500);
      } else {
        setTimeout(() => {
          router.push({ path: "/user_index" });
        }, 1500);
      }
    }
  } catch (error) {
    console.log("登录失败");
  }
};
const to_register = () => {
  setTimeout(() => {
    router.push({ path: "/register" });
  }, 500);
};
</script>

<style scoped>
@import "@/assets/css/iconfont.css";

.wrapper {
  height: 100vh;
  background-image: url("@/assets/images/login_bkg.png");
  background-size: cover;
  overflow: hidden; /*溢出隐藏*/
}

.container {
  width: 400px;
  margin: 10% auto;
  border-radius: 25px;
  background-color: rgba(0, 0, 0, 0.1);
  box-shadow: 0 0 17px #333; /*阴影部分*/
}

.header {
  padding-top: 60px;
}

.header h1 {
  text-align: center;
  color: #333;
  font-size: 40px;
}

.main {
  text-align: center;
  width: 380px;
  height: 260px;
  padding-top: 20px;
  padding-left: 20px;
}

span {
  color: #000;
  height: 40px;
  line-height: 40px;
  font-weight: bold;
}

.input_box {
  width: 250px;
  height: 40px;
  font-size: 15px;
  border: none;
  outline: none;
}

.msg {
  height: 30px;
  text-align: center;
  color: #000;
  font-size: 15px;
  margin-left: 10px;
}

.to_register {
  color: #333;
}

.to_register:hover {
  color: rgb(162, 117, 82);
  cursor: pointer;
}

.login_btn {
  width: 160px;
  height: 40px;
  margin-left: 40px;
  font-size: 15px;
  font-weight: bold;
}
</style>
