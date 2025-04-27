# MP3文件列表

这里将存放MP3文件，由于文件较大，需要使用Git LFS或在GitHub网页界面上传

# MP3文件上传指南

本仓库用于存放桌面0文件夹中的MP3文件集合。由于这些MP3文件大多超过GitHub的单文件大小限制(100MB)，需要通过以下方式上传：

## 文件列表

所有需要上传的MP3文件列表已保存在 `mp3_files_list.txt` 文件中，请查看该文件了解详细列表。

## 上传方法

### 方法一：使用GitHub网页界面（适合少量文件）

1. 打开仓库页面 https://github.com/zhclassmates/wjz5788
2. 点击"Add file"下拉菜单，选择"Upload files"
3. 拖拽文件或点击选择文件
4. 添加提交信息
5. 点击"Commit changes"按钮

注意：GitHub网页界面上传单个文件不能超过25MB

### 方法二：使用Git LFS（适合大文件）

1. 安装Git LFS：
```
brew install git-lfs   # macOS
```

2. 克隆仓库：
```
git clone https://github.com/zhclassmates/wjz5788.git
cd wjz5788
```

3. 设置Git LFS跟踪MP3文件：
```
git lfs install
git lfs track "*.mp3"
git add .gitattributes
git commit -m "设置Git LFS跟踪MP3文件"
```

4. 复制MP3文件到仓库中的mp3_files文件夹：
```
mkdir -p mp3_files
cp ~/Desktop/0/*.mp3 mp3_files/
```

5. 提交并推送：
```
git add mp3_files/
git commit -m "添加MP3文件"
git push
```

### 方法三：分批上传（推荐）

如果文件太大太多，建议分批上传，每次选择几个文件进行上传。

## 注意事项

- GitHub对仓库总大小有限制，免费账户通常建议保持在1GB以下
- 使用Git LFS会消耗GitHub提供的存储和带宽配额
- 上传大文件耗时较长，请确保网络稳定

如有问题，请联系仓库管理员。
