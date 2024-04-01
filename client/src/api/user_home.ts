import request from '@/api/request'
import base from '@/api/base';
import { AxiosResponse } from 'axios';
/* 
*获取用户登录的时间
*data:{username}
*/

export function GetLoginTimeApi(params: object): Promise<AxiosResponse> {
    return request({
        url: base.get_time,
        method: "post",
        data:params,
    })
}