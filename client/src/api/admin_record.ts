import request from '@/api/request'
import base from '@/api/base';
import { AxiosResponse } from 'axios';
/* 
*获取签到记录表格信息
*params：{page,limit,month,day}
*/
export function GetRecordApi(params: object): Promise<AxiosResponse> {
    return request({
        url: base.admin_get_record_list,
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
        url: base.admin_delete_record,
        method: "post",
        data: params,
    })
}