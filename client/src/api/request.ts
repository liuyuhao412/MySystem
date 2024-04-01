import axios, { AxiosError } from "axios";
// import { ElLoading, ElMessage } from 'element-plus'
import { ElMessage } from 'element-plus'

//创建 Loading 实例
// type LoadingInstance = ReturnType<typeof ElLoading.service>;
// let requestLoadingInstance: LoadingInstance;
interface ErrorResponse {
    message: string;
}

const request = axios.create({
    baseURL: "/api",
    timeout: 10000,
    headers: {
        "Content-Type": "application/json;charset=utf-8",
    }
});

//请求拦截器,就是说请求在到达服务器之前,你对发送到服务器的数据进行一些处理,比如后端说除了登录之外的接口都要在请求头上面带上token,你就可以在这里处理
request.interceptors.request.use(
    (config) => {
        // requestLoadingInstance = ElLoading.service({ text: 'Loading...', spinner: 'el-icon-loading', background: 'rgba(0, 0, 0, 0.7)' });
        const accessToken = localStorage.getItem("access_token");
        if (accessToken) {
            config.headers.Authorization = `Bearer ${accessToken}`;
        }
        return config;
    },
    (error) => {
        // 隐藏 Loading
        // requestLoadingInstance.close();
        return Promise.reject(error);
    }
);

//响应拦截器,后端数据真正被你的变量接收之前,进行一些预处理,比如对于一些5,4开头的状态码进行统一处理
request.interceptors.response.use(
    (config) => {
        // requestLoadingInstance.close();
        return config;
    },
    (error) => {
        // requestLoadingInstance.close();
        // 显示错误提示
        handleErrorResponse(error);
        return Promise.reject(error);
    }
);

function handleErrorResponse(error: AxiosError): void {
    let errorMessage: string;
    if (error.response) {
        let responseData: ErrorResponse; //在case作用域之外声明变量
        console.log(error)
        switch (error.response.status) {
            case 400:
                //请求内容不为空或格式错误
                responseData = error.response.data as ErrorResponse;
                errorMessage = responseData.message || "请求的语法格式有错误";
                break;
            case 401:
                //请求内容不成功
                responseData = error.response.data as ErrorResponse;
                errorMessage = responseData.message || "请求要求身份验证";
                break;
            case 409:
                //请求内容已经存在
                responseData = error.response.data as ErrorResponse;
                errorMessage = responseData.message || "请求与现有资源冲突";
                break;
            case 500:
                //请求操作失败
                responseData = error.response.data as ErrorResponse;
                errorMessage = responseData.message || "服务器配置或网络不可达";
                break;
            default:
                errorMessage = `未知错误${error.response.status}`;
        }
    } else {
        errorMessage = "连接到服务器失败";
    }
    ElMessage({
        message: errorMessage,
        type: "error",
        duration: 1000,
    });

}

export default request;
