#!/bin/bash

# 确保脚本可执行
chmod +x upload_files.py

# 设置变量
REPO_DIR="/Users/shengmo/github_upload/wjz5788"  # 本地仓库目录

# 检查参数
if [ $# -lt 1 ]; then
    echo "用法: $0 <文件路径>"
    echo "例如: $0 /Users/shengmo/Desktop/0/某个MP3文件.mp3"
    exit 1
fi

FILE_PATH="$1"

# 检查文件是否存在
if [ ! -f "$FILE_PATH" ]; then
    echo "错误: 文件 '$FILE_PATH' 不存在!"
    exit 1
fi

# 显示信息
echo "===== GitHub单文件上传工具 ====="
echo "将上传以下文件到GitHub仓库:"
echo "文件: $FILE_PATH"
echo "仓库: $REPO_DIR"
echo ""

# 确认是否继续
read -p "是否开始上传此文件？(y/n): " CONFIRM
if [[ $CONFIRM != "y" && $CONFIRM != "Y" ]]; then
    echo "已取消上传"
    exit 0
fi

# 创建临时目录并复制文件
TEMP_DIR=$(mktemp -d)
cp "$FILE_PATH" "$TEMP_DIR/"
FILENAME=$(basename "$FILE_PATH")

# 执行Python上传
echo "开始上传文件..."
./upload_files.py --source "$TEMP_DIR" --repo "$REPO_DIR" --pattern "$FILENAME"

# 清理临时目录
rm -rf "$TEMP_DIR"

echo "脚本执行完成" 