<template>
  <div>
    <div class="header">
      <div class="hearer_div">
        <el-dropdown>
          <el-button type="primary" class="hearer_button">
            <span>更多</span>
            <el-icon class="el-icon--right"><arrow-down /></el-icon>
          </el-button>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="update_password"
                >修改密码</el-dropdown-item
              >
              <el-dropdown-item @click="exit">退出</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
      <div class="text">{{user}}</div>
    </div>

    <div>
      <router-view></router-view>
    </div>
    <div class="bottom">
      <div class="bottom_text">
        Copyright © 我的系统，本系统为自己所做，仅供学习参考
      </div>
    </div>
    <el-dialog
      v-model="dialogVisibleUpdatePassword"
      title="修改密码"
      width="28%"
      :modal="true"
      :close-on-click-modal="false"
      :before-close="handleClosePassword"
    >
      <el-form :model="PasswordForm" label-width="80px" status-icon>
        <el-form-item label="用户" prop="username">
          <el-input
            v-model="PasswordForm.username"
            class="dialog_user_input"
            disabled
          />
        </el-form-item>
        <el-form-item label="密码">
          <el-input
            v-model="PasswordForm.newPassword"
            class="dialog_user_input"
            type="password"
          />
        </el-form-item>
        <el-form-item label="确认密码">
          <el-input
            v-model="PasswordForm.confirmPassword"
            class="dialog_user_input"
            type="password"
          /><span class="dialog_text"
            >8位以上,包括大小写字母、数字、特殊字符</span
          >
        </el-form-item>
        <el-form-item>
          <el-button
            class="dialog_btn"
            type="primary"
            @click="update_password_require"
            >确认</el-button
          >
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { ElMessage, ElMessageBox } from "element-plus";
import { UpdatePasswordApi } from "@/api/index";
import { ArrowDown } from "@element-plus/icons-vue";
import { useRouter } from "vue-router";
const router = useRouter();
const user = localStorage.getItem("access_user");

const dialogVisibleUpdatePassword = ref(false);
const PasswordForm = ref({
  username: "",
  newPassword: "",
  confirmPassword: "",
});

const exit = () => {
  ElMessageBox.confirm("您确认要退出吗？", "提示", {
    cancelButtonText: "取消",
    confirmButtonText: "确认",
    type: "warning",
  })
    .then(() => {
      ElMessage({
        type: "success",
        message: "退出成功",
        duration: 1000,
      });
      setTimeout(() => {
        router.push({ path: "/login" });
      }, 1000);
    })
    .catch(() => {
      ElMessage({
        type: "info",
        message: "取消退出",
        duration: 1000,
      });
    });
};

const update_password = () => {
  if (user != null) {
    dialogVisibleUpdatePassword.value = true;
    PasswordForm.value.username = user;
  }
};
const update_password_require = async () => {
  try {
    const res = await UpdatePasswordApi(PasswordForm.value);

    if (res.status == 200) {
      ElMessage({
        message: res.data.message,
        type: "success",
        duration: 1000,
      });
      dialogVisibleUpdatePassword.value = false;
    }
  } catch (error) {
    console.log("修改密码失败");
  }
};

const handleClosePassword = (done: () => void) => {
  done();
  PasswordForm.value.newPassword = "";
  PasswordForm.value.confirmPassword = "";
};
</script>

<style scoped>
.header {
  height: 55px;
  background-color: #7fadb6;
}
.hearer_div {
  float: right;
  width: 100px;
  height: 35px;
  line-height: 35px;
  padding-left: 10px;
  margin-top: 10px;
}
.hearer_div span {
  margin-left: 10px;
}
.hearer_button {
  width: 80px;
  padding-left: 10px;
}
.text {
  float: right;
  height: 55px;
  line-height: 55px;
  margin-right: 20px;
}
.bottom {
  height: 20px;
  padding-left: 20px;
  padding-bottom: 5px;
  position: fixed;
  bottom: 0;
}
.bottom_text {
  font-size: 15px;
}
.dialog_user_input {
  width: 260px;
}
.dialog_btn {
  width: 150px;
  margin-left: 50px;
}
</style>
