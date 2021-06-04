# fhmlib

> ## 引用 `igolibrary` 的声明
> 
> 我去图书馆 对爬虫的防护较弱且更新不及时, 网络上已经开始流传收费的抢座助手; 这些对正常抢座的普通同学不公平;
> 
> - igotolibrary 无意侵犯任务组织或个人的权益, 仅作学习交流;
> - igotolibrary 已经三次向 我去图书馆 反馈了抢座漏洞的问题, 但没有得到积极的反馈和有效的响应, 反馈截图;
> - igotolibrary 开源, 供大家公平使用; 欢迎有兴趣的同学一起维护更新, 直到修复漏洞为止;
> - **希望大家不要二次开发后用来提供收费服务。**
> 
> ### 注：切勿二次开发提供收费服务
> 
> ### 注：切勿二次开发提供收费服务
> 
> ### 注：切勿二次开发提供收费服务

### 如果您觉得本项目对您有帮助，请看看下面这个项目您是否感兴趣

> ### [BookmarkTomb](http://wzl20001001.github.io/BookmarkTomb_Docs/)
> 本项目实现了跨浏览器的书签同步以及在线查阅功能。详情可以查看帮助文档(上方的超链接)。
> 
> 如果您觉得还不错，请给其中的几个仓库点个 `star`。

新版我去图书馆改版后，依旧有好些人通过付费的脚本订座，每次座位都是满满当当的。抢不到的人只能最后捡漏了，外加学校的规则太恶心，一次预定，整天无忧，空座却到处都是，真的让人寒心，然而这又无处反馈。

然后看到了Github上的捡漏脚本，就写了一个辅助脚本。仅适用于捡漏，只是自动化了订座流程，没有其他任何功能。

所有的使用教程请查阅该项目：[igotolibrary](https://github.com/qmppz/igotolibrary) ，以下只说不同点。

- 本项目仅适用于新版我去图书馆(圆角图标版)。
- 需要的Cookie字段相较于 `igotolibrary` 有所变化，具体看 `conf.json`。
- 新版采用了 `Token` 认证机制，过期时间为一小时。

> 配置文件 conf.json
> ```json5
> {
>   "cookies": [
>       // Cookies 字段模板大概如此，新增了 Token 字段
>       {
>         "v": "5.5",
>         "FROM_TYPE": "weixin",
>         "wechatSESS_ID": "",
>         "SERVERID": "",
>         "Authorization": "eyJ0eXAiOiJKVUzI1NiJ9.eyJ1c2VySWQiOjIxMjYwNjY1LCJzY2hJZCI6MjANzc5ODc0fQ.vbMikWWv4aRtK69_AJl8uufnZk9OLd_Nkuq6qWkgIJzDUoCy2yhY-6jdr1R1axZE6efhIGv26D6qTudw1tR-IcIJbxsLmS9DmY1iST1hMEiOfdGmRQKDBnH6Um3IZi2a3COefStOUILUBGVDgvtqtjdd2odDF9rpfcEPmhPW9TbpYw17VkEhW6yqhlYQmxG8DMZN-9a0WxzY-jmUGiVEAd5wV39QH16yADRorsfWeJRkUaqTUW072qKQUUbvmukWgHJXub8euc7pFZRsM1ouA6KZdJBnCdHjfkDiNy2hpzf4fFjqCnjp4cXDxEYJrNrZ4A1XyB26m14DJNROKw"
>       }
>   ],
>   // 仅有 lib_id 时，随机在 lib_id 房间中预定第一个扫描到的第一个空座 
>   // 指定 lib_id 和 seat_key 时，监控指定的座位
>   // 如果两者都不指定，那么监控自己的常用座位
>   "lib_id": 114118,
>   "seat_key": 202,
>   // 这两个字段指定监控的时间间隔和未预定成功时的重试次数
>   // 时间间隔单位为秒，两者乘积即为监控时间，最好不要超过一小时，Token 最大有效期为一小时
>   "interval": 30, // 扫描间隔，最好设置为20秒以上
>   "retry_times": 30   // 重试次数
> }
> ```

### 参考

`igolibrary`: https://github.com/qmppz/igotolibrary