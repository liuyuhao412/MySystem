<template>
  <div class="wrapper">
    <div class="container">
      <div class="header">
        <h1>注册</h1>
      </div>
      <div class="main">
        <el-form :model="RegisterForm" label-width="60px">
          <el-form-item>
            <el-input
              v-model="RegisterForm.email"
              class="input_box"
              placeholder="请输入邮箱"
            />
            <template #label>
              <span>
                <i class="iconfont">&#xe908;</i>
              </span>
            </template>
          </el-form-item>
          <el-form-item>
            <el-input
              v-model="RegisterForm.code"
              class="input_code"
              placeholder="验证码"
            />
            <el-button
              type="default"
              class="code_btn"
              :disabled="isButtonDisabled"
              @click="sendCode"
              >{{ buttonLabel }}</el-button
            >
            <template #label>
              <span>
                <i class="iconfont">&#xe624;</i>
              </span>
            </template>
          </el-form-item>
          <el-form-item>
            <el-input
              v-model="RegisterForm.password"
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
            <el-input
              v-model="RegisterForm.confirmPassword"
              class="input_box"
              placeholder="请再次输入密码"
              type="password"
            />
            <template #label>
              <span>
                <i class="iconfont">&#xe62f;</i>
              </span>
            </template>
          </el-form-item>
          <el-form-item>
            <div class="msg">
              如果你有账号，请?
              <span class="to_login" @click="to_login">登录</span>
            </div>
          </el-form-item>
          <el-form-item>
            <el-button class="register_btn" type="primary" @click="onSubmit"
              >注册</el-button
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
import { SendCodeApi, RegisterApi } from "@/api/login";
import { useRouter } from "vue-router";
const router = useRouter();

const RegisterForm = ref({
  email: "",
  code: "",
  password: "",
  confirmPassword: "",
});
const isButtonDisabled = ref(false);
const buttonLabel = ref("发送验证码");

const startCountDown = () => {
  isButtonDisabled.value = true;
  let countdownTime = 60;
  const updateCountdown = () => {
    if (countdownTime === 0) {
      isButtonDisabled.value = false;
      buttonLabel.value = "发送验证码";
    } else {
      buttonLabel.value = ` 请在${countdownTime}秒后重试`;
      countdownTime--;
      setTimeout(updateCountdown, 1000);
    }
  };
  updateCountdown();
};

const sendCode = async () => {
  try {
    const res = await SendCodeApi({ email: RegisterForm.value.email });
    console.log(res);
    if (res.status == 200) {
      ElMessage({
        message: res.data.message,
        type: "success",
        duration: 1000,
      });
      startCountDown();
    }
  } catch (error) {
    console.log("发送验证码失败");
  }
};

const onSubmit = async () => {
  try {
    const res = await RegisterApi(RegisterForm.value);
    if (res.status == 200) {
      ElMessage({
        message: res.data.message,
        type: "success",
        duration: 1000,
      });
      setTimeout(() => {
        router.push({ path: "/login" });
      }, 1500);
    }
  } catch (error) {
    console.log("注册失败");
  }
};

const to_login = () => {
  setTimeout(() => {
    router.push({ path: "/login" });
  }, 500);
};
</script>

<style scoped>
@import "@/assets/css/iconfont.css";

.wrapper {
  height: 100vh;
  background-image: url("@/assets/images/login_bkg.png");
  overflow: hidden; /*溢出隐藏*/
  background-size: cover;
}

.container {
  width: 400px;
  margin: 7% auto;
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
  height: 350px;
  padding-left: 20px;
  padding-top: 20px;
}

span {
  color: #000;
  height: 40px;
  line-height: 40px;
  font-weight: bold;
}

.input_code {
  width: 120px;
  height: 40px;
  font-size: 15px;
  border: none;
  outline: none;
}

.code_btn {
  width: 125px;
  height: 40px;
  margin-left: 5px;
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
  color: #333;
  font-size: 15px;

  margin-left: 10px;
}

.msg a {
  color: rgb(79, 65, 92);
}

.to_login {
  color: #333;
}

.to_login:hover {
  color: rgb(162, 117, 82);
  cursor: pointer;
}

.register_btn {
  width: 160px;
  height: 40px;
  margin-left: 40px;
  font-size: 15px;
  font-weight: bold;
}
</style>
