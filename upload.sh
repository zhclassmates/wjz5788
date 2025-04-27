#!/bin/bash

# 确保脚本可执行
chmod +x upload_files.py

# 设置变量
SOURCE_DIR="/Users/shengmo/Desktop/0"  # MP3文件源目录
REPO_DIR="/Users/shengmo/github_upload/wjz5788"  # 本地仓库目录
DELAY=5  # 每个文件上传后的延迟时间(秒)

# 显示帮助信息
echo "===== GitHub MP3文件上传工具 ====="
echo "这个脚本将逐个上传文件到GitHub仓库"
echo ""
echo "源目录: $SOURCE_DIR"
echo "仓库目录: $REPO_DIR"
echo "延迟时间: $DELAY 秒"
echo ""

# 确认是否继续
read -p "是否开始上传文件？(y/n): " CONFIRM
if [[ $CONFIRM != "y" && $CONFIRM != "Y" ]]; then
    echo "已取消上传"
    exit 0
fi

# 执行Python脚本
echo "开始上传文件..."
./upload_files.py --source "$SOURCE_DIR" --repo "$REPO_DIR" --delay "$DELAY"

echo "脚本执行完成" 