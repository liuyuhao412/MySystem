import request from '@/api/request'
import base from '@/api/base';
import { AxiosResponse } from 'axios';

/* 
*获取用户表格数据
*params：{page,limit,username,role}
*/
export function GetUserApi(params: object): Promise<AxiosResponse> {
    return request({
        url: base.get_user,
        method: "post",
        data: params,
    })
}
/* 
*添加用户信息
*params：{username,role}
*/
export function AddUserApi(params: object): Promise<AxiosResponse> {
    return request({
        url: base.add_user,
        method: "post",
        data: params,
    })
}
/* 
*编辑用户信息
*params：{user_id,username,role}
*/
export function UpdateUserApi(params: object): Promise<AxiosResponse> {
    return request({
        url: base.update_user,
        method: "post",
        data: params,
    })
}
/* 
*删除用户信息
*params：{user_id}
*/
export function DeleteUserApi(params: object): Promise<AxiosResponse> {
    return request({
        url: base.delete_user,
        method: "post",
        data: params,
    })
}
/* 
*重置密码
*params：{user_id}
*/
export function SetPasswordApi(params: object): Promise<AxiosResponse> {
    return request({
        url: base.set_password,
        method: "post",
        data: params,
    })
}