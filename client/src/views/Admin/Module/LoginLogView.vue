<template>
  <div class="log_wrapper">
    <div class="log_header">
      <el-input
        v-model="log_username"
        placeholder="请输入用户"
        class="log_input"
      />
      <el-input v-model="log_role" placeholder="请输入身份" class="log_input" />
      <el-button type="primary" class="log_btn" @click="search_log"
        >查询</el-button
      >
    </div>
    <div class="log_table">
      <el-table :data="logTableData" style="width: 900px">
        <el-table-column
          type="index"
          label="序号"
          :index="IndexMethod"
          width="80px"
        />
        <el-table-column prop="username" label="用户" width="200px" />
        <el-table-column prop="role" label="角色" width="100px" />
        <el-table-column prop="ip" label="IP" width="200px" />
        <el-table-column prop="login_time" label="登录时间" width="200px" />
        <el-table-column label="操作" width="100px">
          <template #default="scope">
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
    <div class="log_page">
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
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, toRaw } from "vue";
import { ElMessage, ElMessageBox } from "element-plus";
import { GetLogApi, DeleteLogApi } from "@/api/admin_log";
interface Log {
  log_id: string;
  username: string;
  role: string;
  ip: string;
  time: string;
}

const log_username = ref("");
const log_role = ref("");
const logTableData = ref([]);
const currentPage = ref(1);
const pageSize = ref(5);
const total = ref(1);

const loadTableData = async () => {
  try {
    const res = await GetLogApi({
      page: currentPage.value,
      limit: pageSize.value,
    });
    logTableData.value = res.data.data;
    total.value = res.data.count;
  } catch (error) {
    console.log("获取日志列表失败");
  }
};
onMounted(loadTableData);

const search_log = async () => {
  try {
    const res = await GetLogApi({
      page: currentPage.value,
      limit: pageSize.value,
      username: log_username.value,
      role: log_role.value,
    });
    logTableData.value = res.data.data;
    total.value = res.data.count;
  } catch (error) {
    console.log("查找日志列表失败");
  }
};

const handleDelete = (index: number, row: Log) => {
  ElMessageBox.confirm("此操作是永久删除,是否删除该日志？", "提示", {
    cancelButtonText: "取消",
    confirmButtonText: "确认",
    type: "warning",
  })
    .then(async () => {
      try {
        const res = await DeleteLogApi({ log_id: toRaw(row).log_id });
        if (res.status == 200) {
          ElMessage({
            type: "success",
            message: res.data.message,
            duration: 1000,
          });
          loadTableData();
        }
      } catch (error) {
        console.log("删除日志失败");
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
    const res = await GetLogApi({
      page: currentPage.value,
      limit: val,
      username: log_username.value,
      role: log_role.value,
    });
    logTableData.value = res.data.data;
    total.value = res.data.count;
  } catch (error) {
    console.log("页面大小改变失败");
  }
};

const handleCurrentChange = async (val: number) => {
  try {
    const res = await GetLogApi({
      page: val,
      limit: pageSize.value,
      username: log_username.value,
      role: log_role.value,
    });
    logTableData.value = res.data.data;
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
.log_wrapper {
  margin: 10px 20px;
}
.log_header {
  height: 60px;
  width: 1000px;
}
.log_input {
  height: 40px;
  width: 240px;
  margin-top: 10px;
  margin-right: 20px;
}
.log_btn {
  height: 40px;
  width: 100px;
  margin-top: 10px;
  font-size: 15px;
}
.log_table {
  margin-top: 10px;
  margin-bottom: 20px;
}
.log_page {
  margin-left: 10px;
}
</style>
