# Gfriends Inputer
适用于 Emby/Jellyfin 的媒体服务器头像导入工具。
> *There is no correlation between this repo and Korean girl group GFRIEND.*

## 目录
* [快速开始](#快速开始)
* [进阶说明](#进阶说明)
   * [导入本地头像图片到媒体服务器](#导入本地头像图片到媒体服务器)
   * [使用百度AI精准裁剪头像](#使用百度AI精准裁剪头像)
   * [自定义头像来源](#自定义头像来源不导入某些来源的头像)

## 快速开始

**Windows 用户** 解压后直接运行可执行程序 `Gfriends Inputer.exe` <br>
**Mac / Linux 用户** 解压后打开命令终端：运行 `chmod +x "Gfriends Inputer"` 来赋予权限，然后执行 `./"Gfriends Inputer"` 启动程序

程序首次运行将自动生成配置文件 `Config.ini`。配置文件的必填项为 “媒体服务器的地址” 和 “API 密钥”。<br>
媒体服务器 API 密钥的获取：进入 Emby / Jellyfin 控制台，`高级` — `API 密钥`  — `新 API 密钥` ，根据提示即可生成 API 密钥。

```
命令: "Gfriends Inputer" [-h] [-c [CONFIG]] [-q] [-v]

选项说明:
  -h, --help            显示本帮助信息。
  -c [CONFIG], --config [CONFIG]
                        指定配置文件路径，默认为运行目录。
  -q, --quiet           静默模式运行，并保存日志到文件。
  -v, --version         显示当前版本。
```


## 进阶说明
本项目以抓取官方高质量大图为主要目标，头像图片为自动化抓取，部分人工筛选。

推荐搭配任一刮削整理项目 [AVDC](https://github.com/yoshiko2/AV_Data_Capture "AV Data Capture")([GUI](https://github.com/moyy996/AVDC "AVDC GUI"))、[JavScraper](https://github.com/JavScraper/Emby.Plugins.JavScraper "JavScraper")、[JAVSDT](https://github.com/junerain123/javsdt "JAVSDT")、[JAVOneStop](https://github.com/ddd354/JAVOneStop "JAVOneStop")。

### 导入本地头像图片到媒体服务器
Gfriends Inputer v2.5 及后续版本支持导入本地头像到媒体服务器。

程序首次启动时会自动创建 `Avatar` 文件夹（可在配置文件中修改）。将本地头像图片重命名为`演员姓名.jpg`，或将第三方头像包移动至该文件夹。此后，导入工具优先从该文件夹查找并导入头像，本地路径中不存在的则会尝试从本仓库搜索并导入。

### 使用百度AI精准裁剪头像
Gfriends Inputer v2.7 及后续版本支持使用百度AI精准裁剪头像。

> *此服务需使用中国大陆居民身份证进行实名认证、并理解同意百度智能云的 [服务协议](https://cloud.baidu.com/doc/Agreements/s/yjwvy1x03) 、[隐私政策](https://cloud.baidu.com/doc/Agreements/s/Kjwvy245m) 以及百度AI开放平台的 [服务协议](https://ai.baidu.com/ai-doc/REFERENCE/kk3dwjg7d)。*

您可以在通过如下途径申请相关 API：
1. 访问 https://ai.baidu.com 百度 AI 开放平台，登录并进入控制台。
2. 进入 “人体分析” —— “创建应用”，按要求填写表单，并勾选 “人体分析” 接口。
3. 进入 “人体分析” —— “管理应用”，获取 `BD_App_ID`、`BD_API_Key`、`BD_Secret_Key`。编辑 `Config.ini` 文件中 `百度AI API` 部分并运行程序。

### 自定义头像来源（不导入某些来源的头像）
Gfriends Inputer v2.73 及后续版本支持自定义头像来源。

在仓库中，可能收录了多张不同来源的同一女友头像。这时，默认根据头像质量及尺寸，自动选优后导入头像。<br>
但是，每个人的喜好不同。比如，有的人可能不喜欢 Graphis 的头像，因为上面有标记女友名。有些人可能不喜欢 EBODY 的头像，因为女友衣着太暴露了。

编辑 `Config.ini` 文件 “厂牌黑名单”，填入厂牌后，相应的头像将不会被获取。具体厂牌名可以在下述 [图片来源](#图片来源) 或从 [`Content`](https://github.com/xinxin8816/gfriends/tree/master/Content) 目录获取。