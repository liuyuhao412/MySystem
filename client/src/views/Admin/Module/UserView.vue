<template>
  <div class="user_wrapper">
    <div class="user_header">
      <el-input
        v-model="input_username"
        placeholder="请输入用户"
        class="user_input"
      />
      <el-input
        v-model="input_role"
        placeholder="请输入身份"
        class="user_input"
      />
      <el-button type="primary" class="user_btn" @click="search_user"
        >查询</el-button
      >
      <el-button type="primary" class="user_btn" @click="add_user"
        >添加</el-button
      >
    </div>
    <div class="user_table">
      <el-table :data="userTableData" style="width: 1050px">
        <el-table-column
          type="index"
          label="序号"
          :index="IndexMethod"
          width="80px"
        />
        <el-table-column prop="username" label="用户" width="200px" />
        <el-table-column prop="role" label="角色" width="100px" />
        <el-table-column prop="created_time" label="注册时间" width="220px" />
        <el-table-column label="操作" width="250px">
          <template #default="scope">
            <el-button size="small" @click="handleEdit(scope.$index, scope.row)"
              >修改</el-button
            >
            <el-button
              size="small"
              @click="setPassword(scope.$index, scope.row)"
              >重置密码</el-button
            >
            <el-button
              size="small"
              type="danger"
              @click="handleDelete(scope.$index, scope.row)"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div class="user_page">
      <div class="demo-pagination-block">
        <el-pagination
          v-model:current-page="currentPage"
          v-model:page-size="pageSize"
          :page-sizes="[5, 10]"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
        />
      </div>
    </div>

    <el-dialog
      v-model="dialogAdd"
      title="添加用户"
      width="25%"
      :modal="true"
      :close-on-click-modal="false"
      :before-close="handleCloseAdd"
    >
      <el-form
        :model="addUserForm"
        label-width="80px"
        class="demo-ruleForm"
        status-icon
        ><el-form-item label="用户">
          <el-input v-model="addUserForm.username" class="dialog_user_input" />
        </el-form-item>
        <el-form-item>
          <el-radio-group v-model="addUserForm.role" class="ml-4">
            <el-radio label="admin" size="large">管理员</el-radio>
            <el-radio label="user" size="large">用户</el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item>
          <el-button class="dialog_btn" type="primary" @click="add_user_btn">
            确认
          </el-button>
        </el-form-item>
      </el-form>
    </el-dialog>

    <el-dialog
      v-model="dialogUpdate"
      title="编辑用户"
      width="25%"
      :modal="true"
      :close-on-click-modal="false"
      :before-close="handleCloseUpdate"
    >
      <el-form
        :model="updateUserForm"
        label-width="80px"
        class="demo-ruleForm"
        status-icon
      >
        <el-form-item label="用户" prop="username">
          <el-input
            v-model="updateUserForm.username"
            class="dialog_user_input"
          />
        </el-form-item>

        <el-form-item prop="role">
          <el-radio-group v-model="updateUserForm.role" class="ml-4">
            <el-radio label="admin" size="large">管理员</el-radio>
            <el-radio label="user" size="large">用户</el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item>
          <el-button class="dialog_btn" type="primary" @click="update_user_btn">
            确认
          </el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ElMessage, ElMessageBox } from "element-plus";
import { ref, onMounted, toRaw } from "vue";
import {
  GetUserApi,
  AddUserApi,
  UpdateUserApi,
  DeleteUserApi,
  SetPasswordApi,
} from "@/api/admin_user";
interface User{
  user_id:string;
  username:string;
  role:string;
  time:string
}
const input_username = ref("");
const input_role = ref("");

const userTableData = ref([]);
const currentPage = ref(1);
const pageSize = ref(5);
const total = ref(1);

const dialogAdd = ref(false);
const dialogUpdate = ref(false);

const addUserForm = ref({
  username: "",
  role: "",
});
const updateUserForm = ref({
  user_id: "",
  username: "",
  role: "",
});

const loadTableData = async () => {
  try {
    const res = await GetUserApi({
      page: currentPage.value,
      limit: pageSize.value,
    });
    userTableData.value = res.data.data;
    total.value = res.data.count;
  } catch (error) {
    console.log("获取用户列表失败");
  }
};

onMounted(loadTableData);

const search_user = async () => {
  try {
    const res = await GetUserApi({
      page: currentPage.value,
      limit: pageSize.value,
      username: input_username.value,
      role: input_role.value,
    });
    userTableData.value = res.data.data;
    total.value = res.data.count;
  } catch (error) {
    console.log("查询用户失败");
  }
};

const add_user = () => {
  dialogAdd.value = true;
};

const add_user_btn = async () => {
  try {
    const res = await AddUserApi(addUserForm.value);
    if (res.status == 200) {
      ElMessage({
        type: "success",
        message: res.data.message,
        duration: 1000,
      });
      dialogAdd.value = false;
      addUserForm.value.username = "";
      addUserForm.value.role = "";
      loadTableData();
    }
  } catch (error) {
    console.log("添加用户失败");
  }
};

const handleCloseAdd = (done: () => void) => {
  done();
  addUserForm.value.username = "";
  addUserForm.value.role = "";
};

const handleEdit = (index: number, row: User) => {
  dialogUpdate.value = true;
  updateUserForm.value.user_id = toRaw(row).user_id;
  updateUserForm.value.username = toRaw(row).username;
  updateUserForm.value.role = toRaw(row).role;
};

const update_user_btn = async () => {
  try {
    const res = await UpdateUserApi(updateUserForm.value);
    if (res.status == 200) {
      ElMessage({
        type: "success",
        message: res.data.message,
        duration: 1000,
      });
      dialogUpdate.value = false;
      loadTableData();
    }
  } catch (error) {
    console.log("修改用户失败");
  }
};

const handleCloseUpdate = (done: () => void) => {
  done();
};

const setPassword = (index: number, row: User) => {
  ElMessageBox.confirm("是否要重置密码", "提示", {
    cancelButtonText: "取消",
    confirmButtonText: "确认",
    type: "warning",
  })
    .then(async () => {
      try {
        const res = await SetPasswordApi({ user_id: toRaw(row).user_id });
        if (res.status == 200) {
          ElMessage({
            type: "success",
            message: res.data.message,
            duration: 1000,
          });
          loadTableData();
        }
      } catch (error) {
        console.log("密码重置失败");
      }
    })
    .catch(() => {
      ElMessage({
        type: "info",
        message: "取消",
      });
    });
};

const handleDelete = (index: number, row: User) => {
  ElMessageBox.confirm("此操作是永久删除,是否删除该用户？", "提示", {
    cancelButtonText: "取消",
    confirmButtonText: "确认",
    type: "warning",
  })
    .then(async () => {
      try {
        const res = await DeleteUserApi({ user_id: toRaw(row).user_id });
        if (res.status == 200) {
          ElMessage({
            type: "success",
            message: res.data.message,
            duration: 1000,
          });
          loadTableData();
        }
      } catch (error) {
        console.log("删除用户失败");
      }
    })
    .catch(() => {
      ElMessage({
        type: "info",
        message: "删除取消",
      });
    });
};

const handleSizeChange = async (val: number) => {
  try {
    const res = await GetUserApi({
      page: currentPage.value,
      limit: val,
      username: input_username.value,
      role: input_role.value,
    });
    userTableData.value = res.data.data;
    total.value = res.data.count;
  } catch (error) {
    console.log("页面大小改变失败");
  }
};

const handleCurrentChange = async (val: number) => {
  try {
    const res = await GetUserApi({
      page: val,
      limit: pageSize.value,
      username: input_username.value,
      role: input_role.value,
    });
    userTableData.value = res.data.data;
    total.value = res.data.count;
  } catch (error) {
    console.log("页码跳转失败");
  }
};

const IndexMethod = (index: number) => {
  const Indexpage = currentPage.value;
  const IndexSize = pageSize.value;
  return index + 1 + (Indexpage - 1) * IndexSize;
};
</script>

<style scoped>
.user_wrapper {
  margin: 10px 20px;
}
.user_header {
  height: 60px;
  width: 1000px;
}

.user_input {
  height: 40px;
  width: 240px;
  margin-top: 10px;
  margin-right: 20px;
}
.user_btn {
  height: 40px;
  width: 100px;
  margin-top: 10px;
  font-size: 15px;
}
.dialog_user_input {
  width: 240px;
}
.dialog_btn {
  width: 150px;
  margin-left: 10px;
}
.user_table {
  margin-top: 10px;
  margin-bottom: 20px;
}
.user_page {
  margin-left: 10px;
}
</style>
