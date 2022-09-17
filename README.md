Gmail 与2022年5月取消了简单登录协议，以前直接用账号密码自动发邮件的方法已经没法用了，必须要使用 Oauth2.0，以下是申请使用办法。

## 如何申请 Gmail Oauth2.0
- 参考 https://www.youtube.com/watch?v=8RaSbyk-DJY 的前5分30秒, 但是不要申请为 Web App, 而是直接申请为 **桌面应用**。
- API申请地址: https://console.cloud.google.com/
- 申请好 APP 后, 去 **Oauth 同意屏幕** 增加测试用户，本邮箱地址即可

## 获得 fresh token

- 先要在海外 VPS 运行该脚本（VPN好像不行），并输入前面下载的 json 文件里的参数
- 按照步骤完成用户登录验证，拷贝验证码，然后输入到终端
- 此时程序会在目录下生成 credentials.json
- 随后修改 send_test.py 里的发件箱和收件人来测试是否成功

## 注意事项
GmailAPP 测试版的 fresh token 7天后会过期，随后不可再次申请，正式环境请一定 **发布应用**。