import request from '@/api/request'
import base from '@/api/base';
import { AxiosResponse } from 'axios';

/* 
*打卡
*data:{user_id,date,morning_checkin,morning_checkin_time}
*/

export function GetMarkCardInfoApi(params: object): Promise<AxiosResponse> {
    return request({
        url: base.get_mark_card_info,
        method: "post",
        data: params,
    })
}
/* 
*上午打卡
*data:{user_id,date,morning_checkin,morning_checkin_time}
*/

export function MarkCardAmApi(params: object): Promise<AxiosResponse> {
    return request({
        url: base.mark_card_am,
        method: "post",
        data: params,
    })
}
/* 
*下午打卡
*data:{user_id,date,evening_checkin,evening_checkin_time}
*/

export function MarkCardPmApi(params: object): Promise<AxiosResponse> {
    return request({
        url: base.mark_card_pm,
        method: "post",
        data: params,
    })
}
