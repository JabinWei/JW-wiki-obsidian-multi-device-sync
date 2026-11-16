---
type: learning
status: 学习中
domain: Linux
tags: [Linux, 操作系统, VMware]
created: 2026-11-10
updated: 2026-11-10
---

## 🎯 学习目标

- 为什么学 Linux 要先装虚拟机，而不是直接装双系统？
- VMware Workstation 和 VirtualBox 有什么区别？为什么选 VMware？
- 新建虚拟机时 CPU、内存、磁盘、网络该怎么配？
- CentOS 7 安装过程中分区、软件选择、网卡配置有哪些关键点？
- 安装完成后如何配置网络，让虚拟机既能上网又能被宿主机访问？
- CentOS 7 已停止维护（EOL），yum 源该怎么换？

## 📖 前置知识

- 了解操作系统的基本概念（[[OSB001-进程与线程]] 等原理笔记后续补充）
- 能在 Windows / macOS 上下载软件、安装软件

## 📚 核心内容

### 为什么用虚拟机学 Linux

直接在物理机装 Linux（双系统或裸机）门槛高、风险大：

- 双系统切换麻烦，学习过程中经常要回宿主机查资料
- 误操作可能影响宿主机数据
- 一旦装坏要重装，浪费时间

虚拟机在宿主机里虚拟出一台独立电脑，**快照**功能可以在装坏时一键回滚，是初学 Linux 的标准姿势。

### 一、安装 VMware Workstation

#### 下载

VMware Workstation Pro 从 **2024 年起对个人用户免费**，不再需要付费许可证：

- Windows：在 Broadcom 官网注册账号后下载 Workstation Pro for Windows
- macOS：Apple Silicon 上用 VMware Fusion（同样个人免费），Intel Mac 也可装 Workstation

> [!warning] 下载渠道
> 不要从第三方下载站下，捆绑插件多。国内访问 Broadcom 官网较慢，可通过公司/学校网络或代理下载；实在不行，国内软件站（如「Vmware 中国官网」认证渠道）也有分发，但要核对版本号和数字签名。

#### 安装

Windows 上一路 Next 即可，注意：

- 安装路径不要带中文和空格（如 `D:\VMware\`）
- 安装时会提示网络断开几秒（VMware 会安装虚拟网卡），属正常现象

安装完成后打开，主界面左侧是虚拟机列表，右侧是新建虚拟机入口。

### 二、下载 CentOS 7 镜像

> [!important] CentOS 7 已 EOL
> CentOS 7 于 **2024 年 6 月 30 日停止维护**，官方镜像站 `mirror.centos.org` 已下线。现在要用**归档源**（vault）。国内推荐直接用阿里云镜像，速度快、文件全。

国内镜像地址：

- 阿里云：`https://mirrors.aliyun.com/centos-vault/7.9.2009/isos/x86_64/`
- 清华大学：`https://mirrors.tuna.tsinghua.edu.cn/centos-vault/7.9.2009/isos/x86_64/`
- 官方归档（国外，慢）：`https://vault.centos.org/7.9.2009/isos/x86_64/`

选哪个文件：

| 文件 | 大小 | 用途 |
|------|------|------|
| `CentOS-7-x86_64-DVD-2009.iso` | ~4.5 GB | **标准版**，包含常用软件，安装时可不联网 |
| `CentOS-7-x86_64-Minimal-2009.iso` | ~1 GB | 最小化安装，只有命令行，后续用 yum 装软件 |
| `CentOS-7-x86_64-Everything-2009.iso` | ~10 GB | 全量包，一般用不上 |

初学建议用 **DVD 版**，图形界面和常用工具都在里面。

> [!tip] 镜像校验
> 下载后可以对比同目录下的 `sha256sum.txt` 文件，确认 ISO 没损坏、没被篡改。Windows 上用 `certutil -hashfile CentOS-7-x86_64-DVD-2009.iso SHA256`。

### 三、新建虚拟机

打开 VMware → 创建新的虚拟机 → 选择「典型（推荐）」，关键配置：

#### 1. 选择镜像

选择「稍后安装操作系统」（不要直接把 ISO 拖进去让向导自动识别，后面手动挂更可控），客户机系统选 **Linux → CentOS 7 64 位**。

#### 2. 虚拟机命名与位置

- 名称：`CentOS7-Learning`（见名知意）
- 位置：**不要放 C 盘**，放到数据盘如 `D:\VMware\CentOS7-Learning\`。虚拟机磁盘文件会随使用膨胀，C 盘容易被塞满。

#### 3. 硬件配置

| 项目 | 建议值 | 说明 |
|------|--------|------|
| 处理器 | 2 核 | 学习够用；宿主机如果是 4 核，分 2 核给虚拟机 |
| 内存 | 2 GB（2048 MB） | 图形界面最低要求；宿主机 16 GB 以上可给 4 GB |
| 磁盘 | 20 GB | 选「将虚拟磁盘拆分成多个文件」；不要选「立即分配所有磁盘空间」 |
| 网络适配器 | NAT | **关键**：NAT 模式下虚拟机能通过宿主机上网，且宿主机能 ping 通虚拟机 |

> [!tip] 三种网络模式区别
> - **NAT**：虚拟机共享宿主机 IP 上网，宿主机能访问虚拟机，虚拟机外面的机器访问不到 —— 学习首选
> - **桥接**：虚拟机在局域网里等于一台独立电脑，有独立 IP，局域网其他机器能访问 —— 做服务器实验时用
> - **仅主机**：只有宿主机能和虚拟机通信，虚拟机不能上网 —— 调试隔离环境用

#### 4. 自定义硬件（可选）

- 打印机、声卡可以移除，没用
- 显示器勾选「加速 3D 图形」可开可不开

完成后点击「完成」，虚拟机就建好了，还没装系统。

### 四、安装 CentOS 7

#### 1. 挂载 ISO

编辑虚拟机设置 → CD/DVD → 选择「使用 ISO 映像文件」→ 选中下载好的 `CentOS-7-x86_64-DVD-2009.iso`。

#### 2. 启动安装

开启虚拟机，grub 菜单选 **Install CentOS 7**（不要选 Test this media，慢）。

> [!warning] 鼠标跳出虚拟机
> 进入虚拟机窗口后鼠标会被「捕获」，按 `Ctrl + Alt` 可以释放回宿主机。装好 VMware Tools 后可以自动跟随，不用手动切。

#### 3. 安装向导关键页面

**语言**：选中文（简体）或 English。初学建议中文，但后续命令报错信息是英文的，**熟悉英文报错更快定位问题**。

**安装信息页**（带黄色感叹号的都要设）：

- **软件选择**：
  - 「最小安装」= 纯命令行
  - 「GNOME 桌面」= 图形界面（初学推荐，和 Windows 操作类似）
  - 右侧附加选项建议勾上「开发工具」（后面要装 gcc、make）

- **安装位置**：
  - 直接选 20 GB 磁盘，勾「我要配置分区」
  - 初学用「自动分区」即可；手动分区建议：
    - `/boot`：1 GB（系统引导）
    - `swap`：2 GB（内存不足时当虚拟内存）
    - `/`（根分区）：剩余全部空间

- **网络和主机名**：
  - **打开以太网开关**（默认是关的！装完没网的罪魁祸首）
  - 主机名改成 `centos7-learning` 点「应用」

- **KDUMP**：可以关掉省内存

- **root 密码**：设一个简单的如 `123456`（学习环境，别用在生产）。如果密码太简单，要点两次「完成」确认。

#### 4. 等待安装

点「开始安装」，期间设 root 密码。装完点「重启」。

> [!warning] 重启前弹出安装介质
> 重启时如果卡在 `to boot from media`，是因为还挂着 ISO。解决：VMware 菜单 → 虚拟机 → 电源 → 关闭，然后在 CD/DVD 设置里取消「已连接」，再开机。

### 五、安装后配置

#### 1. 首次启动

重启后进入「欢迎」向导：

- 许可信息：勾选「我同意许可」
- 用户设置：创建一个普通用户（如 `jabin`），设为管理员

#### 2. 验证网络

打开终端（Applications → Utilities → Terminal）：

```bash
# 看 IP 地址
ip addr
# 应该能看到 ens33 网卡有 192.168.x.x 的地址（NAT 网段）

# 测试外网
ping -c 4 baidu.com
```

如果 `ip addr` 里 ens33 没有 IP，或者 ping 不通，说明网卡没开机自启：

```bash
# 编辑网卡配置
sudo vi /etc/sysconfig/network-scripts/ifcfg-ens33
```

把 `ONBOOT=no` 改成 `ONBOOT=yes`，保存后重启网络：

```bash
sudo systemctl restart network
```

> [!note] 为什么默认不开机自启
> CentOS 7 的安装程序里，网络开关虽然在安装向导打开了，但有些版本的最小安装不会写 `ONBOOT=yes`，这是新手最常见的「装完没网」问题。

#### 3. 更换 yum 源（关键，因为 CentOS 7 EOL）

默认 yum 源指向已下线的 `mirror.centos.org`，必须换成阿里云 vault 源：

```bash
# 1. 备份原有源
sudo mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak

# 2. 写入阿里云 vault 源
sudo curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-vault-7.9.2009.repo

# 3. 清理缓存并重建
sudo yum clean all
sudo yum makecache

# 4. 测试安装
sudo yum install -y vim
```

> [!tip] 为什么要换源
> EOL 后官方服务器把包移到了 `vault.centos.org`，原 repo 里的地址失效，`yum install` 会报 `Could not resolve host` 或 `404`。国内直接用阿里云镜像，不依赖境外服务器。

> [!note] curl 没装怎么办
> Minimal 版可能连 `curl` 都没有，用 `wget` 也行：
> ```bash
> sudo wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-vault-7.9.2009.repo
> ```
> 如果 wget 也没有，就只能临时用 DVD 本地源，或先从图形界面浏览器下好再传进虚拟机。

#### 4. 安装常用工具

```bash
sudo yum install -y vim net-tools wget git gcc
```

| 包 | 作用 |
|----|------|
| `vim` | 增强版编辑器（最小安装默认只有 vi） |
| `net-tools` | 提供 `ifconfig`、`netstat` 等老命令 |
| `wget` | 命令行下载工具 |
| `git` | 版本控制 |
| `gcc` | C 编译器 |

### 六、打快照（强烈建议）

环境配好后，在 VMware 里：虚拟机 → 快照 → 拍摄快照，命名为「**初始环境完成**」。

> 以后玩坏了（比如配错网卡、删错文件），一键回滚到这个状态，不用重装。初学 Linux 每周可能都要回滚一两次，快照是救命用的。

## 🤔 常见误区

| 误区 | 事实 |
|------|------|
| 「直接在 Windows 上装个 Git Bash 就能学 Linux」 | Git Bash 只是模拟了部分命令行，没有 systemd、没有真正的包管理、没有 Linux 内核，学不到进程/服务/文件系统这些核心概念 |
| 「虚拟机内存给得越大越快」 | 内存是从宿主机划走的，给虚拟机 8 GB 宿主机就少 8 GB。2~4 GB 对学习足够，给多了宿主机反而卡 |
| 「装完没网是 VMware 的 bug」 | 90% 是安装时网络开关没打开，或 `ONBOOT=no` 没改 |
| 「CentOS 7 还能继续用官方源」 | 2024 年 6 月已 EOL，必须换 vault 源，否则 yum 完全不可用 |
| 「磁盘选了『立即分配所有空间』更好」 | 会立即占满 20 GB，且无法动态扩展。选「拆分文件 + 按需增长」更灵活 |
| 「root 密码设复杂点安全」 | 虚拟机是隔离环境，设太复杂自己都记不住。学习环境 `123456` 反而高效，真要对外暴露服务再加固 |

## 📝 待补充内容

- [ ] VMware Tools 的安装与作用（共享文件夹、自适应分辨率）——国内下载 VMware Tools 的替代渠道
- [ ] 桥接模式的配置场景（以后做 Web 服务器实验时补）
- [ ] 从 NAT 网段固定 IP（DHCP 默认每次开机 IP 可能变）
- [ ] EPEL 第三方源配置（国内镜像）
- [ ] 国内 Docker、pip、npm 等后续常用工具的镜像加速配置（作为系列笔记单独写）

## 🔗 相关资源

- 上一篇：（本系列开篇，暂无）
- 下一篇：[[LX002-常用命令]]（待写）
- 原理关联：[[OSB001-进程与线程]]、[[OSB002-内存管理]]（待写）
- 阿里云 CentOS Vault 镜像：https://mirrors.aliyun.com/centos-vault/7.9.2009/
- 清华 TUNA CentOS Vault：https://mirrors.tuna.tsinghua.edu.cn/centos-vault/
- CentOS 7 EOL 说明：https://www.centos.org/centos-linux-eol/
