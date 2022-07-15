# Gfriends Inputer 一键导入工具
适用于 Emby/Jellyfin 的媒体服务器头像导入工具，[Gfriends 女友头像仓库](https://github.com/gfriends/gfriends) 衍生项目。
> *There is no correlation between this repo and Korean girl group GFRIEND.*

## 目录
* [快速开始](#快速开始)
* [进阶说明](#进阶说明)
   * [使用 AI 精准裁剪头像](#精准裁剪头像)
   * [导入本地头像图片](#导入本地头像图片)
   * [自定义头像来源](#自定义头像来源)
   * [第三方刮削工具](#第三方刮削工具)
* [许可证及法律信息](#许可证及法律信息)

## 快速开始
#### 1. 下载并解压
请在 [Release](https://github.com/gfriends/gfriends-inputer/releases) 下载并解压 Gfriends Inputer 程序压缩包。<br>
*提示：程序可以连接**远程**媒体服务器，因此请选择自己顺手的系统。*

#### 2. 获取媒体服务器 API 密钥
进入 Emby / Jellyfin 控制台，`高级` — `API 密钥`  — `新 API 密钥` ，根据提示即可生成 API 密钥。

#### 3. 编辑配置文件并运行
**Mac / Windows 用户** 直接运行可执行程序 `Gfriends Inputer.exe` <br>
**Linux 用户** 打开命令终端：运行 `chmod +x "Gfriends Inputer"` 来赋予权限，然后执行 `./"Gfriends Inputer"` 启动程序

程序首次运行将自动生成配置文件 `Config.ini`，配置文件的必填项为 `媒体服务器的地址` 和获取的 `API 密钥`。

*提示：v2.x 旧版本的 Mac/Linux 配置文件在用户根目录，常见在：`/Users/username/`、`/home/username/`、`/root/`*

```
命令: "Gfriends Inputer" [-h] [-c [CONFIG]] [-q] [-v]

选项说明:
  -h, --help            显示本帮助信息。
  -c [CONFIG], --config [CONFIG]
                        指定配置文件路径，默认为运行目录。
  -q, --quiet           静默模式运行，并保存日志到文件。
  -v, --version         显示当前版本。
```

您亦可在 Python 3.6 及以上版本环境下直接运行源码
```
git clone https://github.com/gfriends/gfriends-inputer.git
cd ./gfriends-inputer
pip install -r requirements.txt
python "./Gfriends Inputer.py"
```

## 进阶说明

按需完成进阶配置有助于提升使用体验。

### 【精准裁剪头像】

仓库中的头像可能尺寸不标准，媒体服务器会自动拉伸使头像变形，这时需要裁剪头像。虽很少遇到这种情况，但为避免裁剪到演员面部，您应当配置 AI 精准裁剪。

**1. Pigo AI**<br>
*Gfriends Inputer v3.0 及后续版本支持*

[Pigo](https://github.com/esimov/pigo) 提供无感知的人脸识别。准确度偏低，但速度极快且无需联网。仅需在配置文件中开启。

**2. 百度 AI**<br>
*Gfriends Inputer v2.7 及后续版本支持*

> *此服务需使用中国大陆居民身份证进行实名认证、并理解同意百度智能云的 [服务协议](https://cloud.baidu.com/doc/Agreements/s/yjwvy1x03) 、[隐私政策](https://cloud.baidu.com/doc/Agreements/s/Kjwvy245m) 以及百度AI开放平台的 [服务协议](https://ai.baidu.com/ai-doc/REFERENCE/kk3dwjg7d)。*

您可以在通过如下途径申请相关 API：
1. 访问 https://ai.baidu.com 百度 AI 开放平台，登录并进入控制台。
2. 进入 “人体分析” —— “创建应用”，按要求填写表单，并勾选 “人体分析” 接口。
3. 进入 “人体分析” —— “管理应用”，获取 `BD_App_ID`、`BD_API_Key`、`BD_Secret_Key`，并编辑配置文件中 `百度AI API` 部分。

### 【导入本地头像图片】
*Gfriends Inputer v2.5 及后续版本支持*

程序首次启动时会自动创建 `Avatar` 文件夹（可在配置文件中修改）。将本地头像图片重命名为`演员姓名.jpg`，或将第三方头像包移动至该文件夹。此后，导入工具优先从该文件夹查找并导入头像，本地路径中不存在的则会尝试从 Gfriends 仓库搜索并导入。

### 【自定义头像来源】

在仓库中，可能收录了多张不同来源的同一女友头像。这时，默认根据头像质量及尺寸，自动选优后导入头像。<br>
但是，每个人的喜好不同。比如，有的人可能不喜欢 Graphis 的头像，因为上面有标记女友名。有些人可能不喜欢 EBODY 的头像，因为女友衣着太暴露了。

**1. 手动选择头像**<br>
*Gfriends Inputer v3.0 及后续版本支持，仅 Windows*

程序在遇到多头像时，自动弹窗罗列所有头像，您只需点击即可选择对应的头像。

**2. 厂牌黑名单**<br>
*Gfriends Inputer v2.x 支持*

编辑配置文件的 `厂牌黑名单`，填入厂牌后，相应的头像将不会被获取。具体厂牌名可以在主仓库 [图片来源](https://github.com/gfriends/gfriends#%E5%9B%BE%E7%89%87%E6%9D%A5%E6%BA%90) 或 [`Content`](https://github.com/gfriends/gfriends/tree/master/Content) 目录获取。

### 【第三方刮削工具】
推荐与 Gfriends Inputer 搭配刮削整理项目，神兵利器助您事半功倍。

[Movie Data Capture](https://github.com/yoshiko2/AV_Data_Capture "AV Data Capture")：本地电影元数据刮削器。<br>
  衍生项目：[AVDC GUI](https://github.com/moyy996/AVDC "AVDC GUI")、[MDCx](https://github.com/anyabc/something "MDCx")

[JavScraper](https://github.com/JavScraper/Emby.Plugins.JavScraper "JavScraper")：一个 Jellyfin/Emby 的日本电影刮削器插件，可以从某些网站抓取影片信息。

[Javtube](https://github.com/javtube/jellyfin-plugin-javtube "Javtube")：另一个为 Jellyfin/Emby 开发的超级好用的 JAV 插件。（部分开源）

[JAVSDT](https://github.com/junerain123/javsdt "JAVSDT")：日本影片标准化工具。（已闭源）

[JAVOneStop](https://github.com/ddd354/JAVOneStop "JAVOneStop")：一站 JAV，All-in-One 的 JAV 处理工具。

*您知道其他相似的开源工具？欢迎提交 issues 告诉我。*

## 许可证及法律信息
本项目授权在 [MIT](https://github.com/gfriends/gfriends-inputer/blob/main/LICENSE) 许可下，此外：

1. 项目仅用于技术、学术交流，严禁用于商业和其他盈利目的。
2. 请自觉遵守当地法律法规，产生的一切后果由用户自行承担。
3. 作者保留最终决定权和最终解释权。

若您不同意上述任一条款，请勿直接或间接使用本项目。
