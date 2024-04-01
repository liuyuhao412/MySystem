import request from '@/api/request'
import base from '@/api/base';
import { AxiosResponse } from 'axios';

/* 
 * 获取用户总数
 */
export function GetUserCountApi(): Promise<AxiosResponse> {
    return request({
        url: base.get_user_count,
        method: 'get',
    })
}

/* 
 * 获取用户总数
 */
export function GetUserLogCountApi(): Promise<AxiosResponse> {
    return request({
        url: base.get_user_log_count,
        method: 'get',
    })
}

/* 
 * 获取用户总数
 */
export function GetUserListApi(): Promise<AxiosResponse> {
    return request({
        url: base.get_user_list,
        method: 'get',
    })
}
/* 
 * 获取用户总数
 */
export function GetUserLogListApi(): Promise<AxiosResponse> {
    return request({
        url: base.get_user_log_list,
        method: 'get',
    })
}
