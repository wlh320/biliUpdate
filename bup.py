#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""b站上的XXX今天更新了嘛?"""
from datetime import datetime
import sys
import requests

# 用户的mid, 举例:
PO_DICT = {
    'LXH' : '5632230',
    'LS' : '374377',
    'MOS' : '673816',
    'CH' : '585267'
}


def get_up_name(mid):
    """获取up主名字"""
    payload = {'mid': mid}
    headers = {'referer': 'https://space.bilibili.com/' + str(mid) + '/'}
    url = 'https://space.bilibili.com/ajax/member/GetInfo'
    req = requests.post(url, data=payload, headers=headers)
    up_name = req.json()['data']['name']
    return up_name


def get_video_info(mid):
    """获取视频信息"""
    url = 'https://space.bilibili.com/ajax/member/getSubmitVideos?mid=' + mid
    req = requests.get(url)
    video_info = req.json()['data']['vlist']
    return video_info


def get_created_time(video):
    """返回投稿时间"""
    return datetime.fromtimestamp(video['created'])


def strfdelta(tdelta, fmt):
    """格式化timedelta 什么鬼还要我来做"""
    fmtd = {"days" : tdelta.days}
    fmtd["hours"], rem = divmod(tdelta.seconds, 3600)
    fmtd["minutes"], fmtd["seconds"] = divmod(rem, 60)
    return fmt.format(**fmtd)


def is_update_today(mid):
    """今天更新了嘛"""
    video_info = get_video_info(mid)
    aid = video_info[0]['aid']
    newest = get_created_time(video_info[0])
    older = get_created_time(video_info[1])
    now = datetime.now()

    fmtstr = "{days} 天 {hours} 小时 {minutes} 分钟 {seconds} 秒"
    passday = strfdelta((newest - older), fmtstr)
    if (now - newest).days == 0:
        print("更新啦!更新啦!\n然而距离上一次更新已经过去了", passday)
        print("快到 https://www.bilibili.com/video/av" + str(aid) + " 去看吧!")
    else:
        passday = strfdelta((now - newest), fmtstr)
        print("并没有\n而且距离上一次更新已经过去了", passday)
        print("回顾一下上一个视频吧: https://www.bilibili.com/video/av" + str(aid))


def main():
    """main"""
    author = sys.argv[1] if len(sys.argv) > 1 else "???"
    if author in PO_DICT.keys():
        mid = PO_DICT[author]
        print("============\n", get_up_name(mid), "今天更新了嘛?\n============")
        is_update_today(mid)
    else:
        print('谁?我不认识')


if __name__ == '__main__':
    main()
