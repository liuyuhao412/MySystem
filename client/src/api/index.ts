import request from '@/api/request'
import base from '@/api/base';
import { AxiosResponse } from 'axios';

/* 
 * 修改密码
    data: { username, newPassword, confirmPassword}
 */
export function UpdatePasswordApi(params: object): Promise<AxiosResponse> {
    return request({
        url: base.update_password,
        method: 'post',
        data: params,
    })
}

/* 
*获取签到记录表格信息
*params：{page,limit,month,day}
*/
export function GetRecordApi(params: object): Promise<AxiosResponse> {
    return request({
        url: base.get_record_list,
        method: "post",
        data: params,
    })
}

/* 
*删除签到记录信息
*params：{record_id}
*/
export function DeleteRecordApi(params: object): Promise<AxiosResponse> {
    return request({
        url: base.delete_record,
        method: "post",
        data: params,
    })
}