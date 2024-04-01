import request from '@/api/request'
import base from '@/api/base';
import { AxiosResponse } from 'axios';

/* 
*获取登录日志表格数据
*params：{page,limit,username,role}
*/
export function GetLogApi(params: object) : Promise<AxiosResponse> {
    return request({
        url: base.get_log,
        method: "post",
        data:params,
    })
}


/* 
*删除用户信息
*params：{log_id}
*/
export function DeleteLogApi(params: object): Promise<AxiosResponse> {
    return request({
        url: base.delete_log,
        method: "post",
        data: params,
    })
}
