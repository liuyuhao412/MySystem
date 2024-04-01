<template>
  <div class="record_wrapper">
    <div class="record_header">
      <el-input v-model="month" placeholder="请输入月份(例如:1)" class="record_input" />
      <el-input v-model="day" placeholder="请输入日期(例如:1)" class="record_input" />
      <el-button type="primary" class="record_btn" @click="search_record"
        >查询</el-button
      >
    </div>
    <div class="record_table">
      <el-table :data="RecordTableData" style="width: 1000px">
        <el-table-column
          type="index"
          label="序号"
          :index="IndexMethod"
          width="80px"
        />
        <el-table-column prop="date" label="日期" width="200px" />
        <el-table-column
          prop="morning_checkin"
          label="早上打卡"
          width="100px"
        />
        <el-table-column
          prop="morning_checkin_time"
          label="早上打卡时间"
          width="200px"
        />
        <el-table-column
          prop="evening_checkin"
          label="晚上打卡"
          width="100px"
        />
        <el-table-column
          prop="evening_checkin_time"
          label="晚上打卡时间"
          width="200px"
        />
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
    <div class="record_page">
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
import { ref, onMounted,toRaw } from "vue";
import { ElMessage, ElMessageBox } from "element-plus";
import { GetRecordApi, DeleteRecordApi } from "@/api/user_record";
interface Record {
  record_id: number;
  date: string;
  morning_checkin: string;
  morning_checkin_time: string;
  evening_checkin: string;
  evening_checkin_time: string;
}
const month = ref("");
const day = ref("");
const RecordTableData = ref<Record[]>([]);
const currentPage = ref(1);
const pageSize = ref(5);
const total = ref(0);
const user: string = localStorage.getItem("access_user") || "";

const loadTableData = async () => {
  try {
    const res = await GetRecordApi({
      username: user,
      page: currentPage.value,
      limit: pageSize.value,
    });
    RecordTableData.value = res.data.data;
    total.value = res.data.count;
  } catch (error) {
    console.log("获取签到记录失败");
  }
};
onMounted(loadTableData);

const search_record = async () => {
  try {
    const res = await GetRecordApi({
      username: user,
      page: currentPage.value,
      limit: pageSize.value,
      month: month.value,
      day: day.value,
    });
    RecordTableData.value = res.data.data;
    total.value = res.data.count;
  } catch (error) {
    console.log("查找签到记录失败");
  }
};

const handleDelete = (index: number, row: Record) => {
  ElMessageBox.confirm("此操作是永久删除,是否删除该记录？", "提示", {
    cancelButtonText: "取消",
    confirmButtonText: "确认",
    type: "warning",
  })
    .then(async () => {
      try {
        const res = await DeleteRecordApi({ record_id: toRaw(row).record_id });
        if (res.status == 200) {
          ElMessage({
            type: "success",
            message: res.data.message,
            duration: 1000,
          });
          loadTableData();
        }
      } catch (error) {
        console.log("删除记录失败");
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
    const res = await GetRecordApi({
      username: user,
      page: currentPage.value,
      limit: val,
      month: month.value,
      day: day.value,
    });
    RecordTableData.value = res.data.data;
    total.value = res.data.count;
  } catch (error) {
    console.log("查找签到记录失败");
  }
};

const handleCurrentChange = async (val: number) => {
  try {
    const res = await GetRecordApi({
      username: user,
      page: val,
      limit: pageSize.value,
      month: month.value,
      day: day.value,
    });
    RecordTableData.value = res.data.data;
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
.record_wrapper {
  margin: 10px 20px;
}
.record_header {
  height: 60px;
  width: 1000px;
}
.record_input {
  height: 40px;
  width: 240px;
  margin-top: 10px;
  margin-right: 20px;
}
.record_btn {
  height: 40px;
  width: 100px;
  margin-top: 10px;
  font-size: 15px;
}
.record_table {
  margin-top: 10px;
  margin-bottom: 20px;
}
.record_page {
  margin-left: 10px;
}
</style>
