# Peng-dirscan

一个轻量级的 Python Web 目录爆破工具，用于渗透测试信息收集阶段的隐藏目录/文件发现。

## 功能

- 多线程并发扫描，速度快
- 自定义字典文件
- 状态码过滤（默认保留 200/301/302/403）
- 目标可达性预检，避免静默失败
- 结果保存到文件

## 环境要求

- Python 3.x
- requests 库

```bash
pip install requests
```

## 使用方法

```bash
python dirscan.py -u http://目标地址 -w 字典文件路径 -t 线程数
```

### 参数说明

| 参数 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `--url` | `-u` | 目标 URL（必填），如 `http://example.com` | 无 |
| `--wordlist` | `-w` | 字典文件路径 | `common.txt` |
| `--threads` | `-t` | 并发线程数 | `10` |

### 示例

```bash
# 使用默认字典，10线程扫描
python dirscan.py -u http://192.168.123.138 -w common.txt -t 10

# 快速扫描，5线程
python dirscan.py -u http://example.com -w common.txt -t 5
```

## 输出

扫描结果会即时打印到终端，同时自动保存到 `results.txt` 文件中。

```
存在的目录：http://192.168.123.138/admin  状态码：403
结果已保存到results.txt文件中。
```

## 字典说明

默认字典 `common.txt` 来自 [SecLists](https://github.com/danielmiessler/SecLists)（约 4700 条常见目录/文件路径），是目前 Web 内容发现最常用的起步字典。

## 注意事项

- 本工具仅用于授权的渗透测试或安全学习
- 扫描前工具会自动检测目标是否可达，不可达时将报错退出
