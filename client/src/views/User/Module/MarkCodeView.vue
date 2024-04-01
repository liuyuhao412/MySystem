<template>
  <div class="wrapper">
    <div class="container">
      <div class="content">
        <div class="title">
          <span>今日打卡</span>
        </div>

        <div class="item">
          <div class="label">
            今日时间 <span>{{ cardRecord.date }}</span>
          </div>
        </div>

        <div class="item">
          <div class="label">
            早上打卡
            <span v-if="cardRecord.morningChecked">{{
              cardRecord.morningTime
            }}</span>
          </div>
        </div>

        <div class="item">
          <el-button
            type="primary"
            @click="morningCheckIn"
            :disabled="cardRecord.morningChecked"
            class="check-in-button"
          >
            {{ cardRecord.morningChecked ? "已打卡" : "打卡" }}
          </el-button>
        </div>

        <div class="item">
          <div class="label">
            晚上打卡
            <span v-if="cardRecord.eveningChecked">{{
              cardRecord.eveningTime
            }}</span>
          </div>
        </div>

        <div class="item">
          <el-button
            type="primary"
            @click="eveningCheckIn"
            :disabled="cardRecord.eveningChecked"
            class="check-in-button"
          >
            {{ cardRecord.eveningChecked ? "已打卡" : "打卡" }}
          </el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from "vue";
import {
  GetMarkCardInfoApi,
  MarkCardAmApi,
  MarkCardPmApi,
} from "@/api/user_mark_card";

interface Record {
  username: string;
  date: string;
  morningChecked: boolean;
  morningTime: string;
  eveningChecked: boolean;
  eveningTime: string;
}

const cardRecord = ref<Record>({
  username: "",
  date: "",
  morningChecked: false,
  morningTime: "",
  eveningChecked: false,
  eveningTime: "",
});

const user: string = localStorage.getItem("access_user") || "";

const get_today_date = async () => {
  // 创建一个 Date 对象，表示当前日期
  const specificDate = new Date();
  // 获取当前日期的年份
  const year = specificDate.getFullYear();
  // 获取当前日期的月份（注意：月份从0开始，所以需要加1）
  const month = specificDate.getMonth() + 1;
  // 获取当前日期的日期
  const day = specificDate.getDate();
  // 格式化年份，月份和日期为两位数
  const formattedYear = year.toString().padStart(4, "0");
  const formattedMonth = month.toString().padStart(2, "0");
  const formattedDate = day.toString().padStart(2, "0");
  const formattedDateString = `${formattedYear}年${formattedMonth}月${formattedDate}日`;
  cardRecord.value.date = formattedDateString;
};

const get_mark_card_info = async () => {
  cardRecord.value.username = user;
  try {
    const res = await GetMarkCardInfoApi({
      username: user,
      date: cardRecord.value.date,
    });
    if (res.status == 200) {
      const data = res.data.data;
      cardRecord.value.morningChecked = data.morning_checkin;
      cardRecord.value.morningTime = data.morning_checkin_time;
      cardRecord.value.eveningChecked = data.evening_checkin;
      cardRecord.value.eveningTime = data.evening_checkin_time;
    }
  } catch (error) {
    console.log("获取打卡信息失败");
  }
};

const mark_card_am = async (mark_card_am: boolean) => {
  cardRecord.value.username = user;
  try {
    const res = await MarkCardAmApi({
      username: user,
      date: cardRecord.value.date,
      morningChecked: mark_card_am,
    });
    if (res.status == 200) {
      const data = res.data.data;
      cardRecord.value.morningChecked = data.morning_checkin;
      cardRecord.value.morningTime = data.morning_checkin_time;
    }
  } catch (error) {
    console.log("上午打卡失败");
  }
};

const mark_card_pm = async (mark_card_pm: boolean) => {
  cardRecord.value.username = user;
  try {
    const res = await MarkCardPmApi({
      username: user,
      date: cardRecord.value.date,
      eveningChecked: mark_card_pm,
    });
    if (res.status == 200) {
      const data = res.data.data;
      cardRecord.value.eveningChecked = data.evening_checkin;
      cardRecord.value.eveningTime = data.evening_checkin_time;
    }
  } catch (error) {
    console.log("下午打卡失败");
  }
};

onMounted(() => {
  get_today_date();
  get_mark_card_info();
});

const morningCheckIn = async () => {
  cardRecord.value.morningChecked = true;
  mark_card_am(cardRecord.value.morningChecked);
};

const eveningCheckIn = () => {
  cardRecord.value.eveningChecked = true;
  mark_card_pm(cardRecord.value.eveningChecked);
};
</script>

<style scoped>
.wrapper {
  height: 100%;
  display: flex;
  align-items: center;
}
.container {
  width: 400px;
  height: 400px;
  margin-left: 50px;
  margin-top: 30px;
  background-color: rgba(144, 136, 136, 0.1);
  box-shadow: 2px 2px 5px 0px rgba(0, 0, 0, 0.5),
    -2px -2px 5px 0px rgba(255, 255, 255, 0.5);
}

.content {
  padding: 20px;
}

.title {
  height: 40px;
  line-height: 40px;
  text-align: center;
  margin-bottom: 20px;
}

.title > span {
  font-size: 30px;
}

.item {
  height: 40px;
  line-height: 40px;
  margin-bottom: 10px;
}

.label {
  font-size: 20px;
}
.label > span {
  margin-left: 20px;
}

.time {
  font-size: 20px;
  margin-left: 100px; /* 与按钮对齐 */
}
.check-in-button {
  width: 150px;
  height: 40px;
  margin-left: 100px;
}
</style>
