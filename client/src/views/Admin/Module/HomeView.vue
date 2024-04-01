<template>
  <div class="wrapper">
    <div class="top">
      <div class="user_count">
        <span class="label">用户总数</span>
        <span class="total">{{ userTotal }}</span>
      </div>
      <div class="log_count">
        <span class="label">用户登录次数</span>
        <span class="total">{{ logTotal }}</span>
      </div>
    </div>
    <div class="bottom">
      <div ref="chartUserRef" class="chart-container"></div>
      <div ref="chartLogRef" class="chart-container"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import * as echarts from "echarts";
import { ref, onMounted, Ref } from "vue";
import {
  GetUserCountApi,
  GetUserLogCountApi,
  GetUserListApi,
  GetUserLogListApi,
} from "@/api/admin_home";

const userTotal = ref(0);
const logTotal = ref(0);
const chartUserRef = ref<HTMLElement | null>(null);
const chartLogRef = ref<HTMLElement | null>(null);
const userList = ref([]);
const logList = ref([]);

const initCharts = () => {
  initChart(chartUserRef, userList, "新注册用户数", "bar");
  initChart(chartLogRef, logList, "用户登录次数", "line");
};
const initChart = (
  ref: Ref<HTMLElement | null>,
  data: Ref<never[]>,
  name: string,
  type: string
) => {
  const options = {
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "shadow",
        crossStyle: {
          color: "#999",
        },
      },
    },
    toolbox: {
      feature: {
        dataView: { show: true, readOnly: false },
        magicType: { show: true, type: ["line", "bar"] },
        saveAsImage: { show: true },
      },
    },
    legend: {
      data: [name],
    },
    xAxis: [
      {
        type: "category",
        data: [
          "2024-01",
          "2024-02",
          "2024-03",
          "2024-04",
          "2024-05",
          "2024-06",
          "2024-07",
          "2024-08",
          "2024-09",
          "2024-10",
          "2024-11",
          "2024-12",
        ],
        axisPointer: {
          type: "shadow",
        },
      },
    ],
    yAxis: [
      {
        type: "value",
        name: name,
        min: 0,
        max: 50,
        interval: 5,
        axisLabel: {
          formatter: "{value}人 ",
        },
      },
    ],
    series: [
      {
        name: name,
        type: type,
        tooltip: {
          valueFormatter: function (value: number) {
            return value + " 人";
          },
        },
        data: data.value,
      },
    ],
  };

  if (ref.value) {
    const chart = echarts.init(ref.value, { width: 600, height: 300 });
    chart.setOption(options);
    window.addEventListener("resize", function () {
      chart.resize();
    });
  }
};

const get_user_count = async () => {
  try {
    const get_user_count_res = await GetUserCountApi();
    userTotal.value = get_user_count_res.data.count;
    const get_user_log_count_res = await GetUserLogCountApi();
    logTotal.value = get_user_log_count_res.data.count;
  } catch (error) {
    console.log("获取用户信息失败");
  }
};

const get_user_list = async () => {
  try {
    const get_user_list_res = await GetUserListApi();
    userList.value = get_user_list_res.data.user_list;
    const get_log_list_res = await GetUserLogListApi();
    logList.value = get_log_list_res.data.log_list;
    initCharts();
  } catch (error) {
    console.log("获取用户列表信息失败");
  }
};
onMounted(() => {
  get_user_count();
  get_user_list();
});
</script>

<style scoped>
.top {
  height: 100px;
  width: 100%;
  margin-top: 30px;
  display: flex;
  position: relative;
}
.user_count,
.log_count {
  width: 250px;
  height: 100px;
  margin-left: 40px;
  background-color: #f4f4f4;
  box-shadow: 2px 2px 5px 0px rgba(0, 0, 0, 0.5),
    -2px -2px 5px 0px rgba(255, 255, 255, 0.5);
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.log_count {
  margin-left: 350px;
}
.bottom {
  width: 1200px;
  height: 400px;
  margin-left: 20px;
  margin-top: 50px;
  display: flex;
}

.label {
  font-size: 20px;
  color: blueviolet;
  margin-bottom: 10px;
  margin-left: 20px;
  text-align: left;
}

.total {
  font-size: 24px;
  color: blueviolet;
  text-align: center;
}

.chart-container {
  width: 100%;
  height: 100%;
}
</style>
