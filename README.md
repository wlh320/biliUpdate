# XXX今天更新了嘛
一个简单的CLI脚本,提示你b站某个用户是否更新了

用处不大, 一时兴起写着玩

## Usage
直接运行脚本, 参数是脚本中设定好的简称,可以自行添加,需要该用户的 mid,点开他主页就看到了

## Example
```
❯ ./bup.py LXH
============
 罗小黑战记 今天更新了嘛?
============
更新啦!更新啦!
然而距离上一次更新已经过去了 78 天 1 小时 9 分钟 27 秒
快到 https://www.bilibili.com/video/av9479373 去看吧!

❯ ./bup.py LS
============
 泪腺战士 今天更新了嘛?
============
并没有
而且距离上一次更新已经过去了 74 天 3 小时 42 分钟 29 秒
回顾一下上一个视频吧: https://www.bilibili.com/video/av8019339

```

## Dependencies
需要 `requests` 库