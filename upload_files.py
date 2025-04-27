#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GitHub文件逐个上传工具
这个脚本可以帮助您逐个上传文件到GitHub仓库，适合处理大量大文件的情况。
"""

import os
import subprocess
import time
import argparse
import glob
import shutil

def check_git_lfs():
    """检查是否安装了Git LFS"""
    try:
        subprocess.run(['git', 'lfs', 'version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def setup_git_lfs(repo_dir):
    """设置Git LFS跟踪.mp3文件"""
    os.chdir(repo_dir)
    subprocess.run(['git', 'lfs', 'install'], check=True)
    subprocess.run(['git', 'lfs', 'track', '*.mp3'], check=True)
    subprocess.run(['git', 'add', '.gitattributes'], check=True)
    subprocess.run(['git', 'commit', '-m', '设置Git LFS跟踪MP3文件'], check=True)
    subprocess.run(['git', 'push'], check=True)

def upload_file(file_path, repo_dir, commit_message=None):
    """上传单个文件到仓库"""
    file_name = os.path.basename(file_path)
    target_dir = os.path.join(repo_dir, 'mp3_files')
    
    # 确保目标目录存在
    os.makedirs(target_dir, exist_ok=True)
    
    # 复制文件到仓库
    target_path = os.path.join(target_dir, file_name)
    print(f"复制文件 {file_path} 到 {target_path}")
    shutil.copy2(file_path, target_path)
    
    # 添加并提交文件
    os.chdir(repo_dir)
    subprocess.run(['git', 'add', target_path], check=True)
    
    if not commit_message:
        commit_message = f"添加文件: {file_name}"
    
    subprocess.run(['git', 'commit', '-m', commit_message], check=True)
    
    # 尝试推送文件
    try:
        subprocess.run(['git', 'push'], check=True)
        print(f"✅ 成功上传文件: {file_name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 上传文件失败: {file_name}")
        print(f"错误信息: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='逐个上传文件到GitHub仓库')
    parser.add_argument('--source', '-s', required=True, help='源文件夹路径，包含要上传的MP3文件')
    parser.add_argument('--repo', '-r', required=True, help='本地仓库路径')
    parser.add_argument('--pattern', '-p', default='*.mp3', help='文件匹配模式，默认为 *.mp3')
    parser.add_argument('--delay', '-d', type=int, default=5, help='每个文件上传后的延迟时间(秒)，默认为5秒')
    args = parser.parse_args()
    
    # 检查Git LFS
    if not check_git_lfs():
        print("⚠️ Git LFS未安装。大文件上传可能会失败。")
        print("建议安装Git LFS: brew install git-lfs")
        answer = input("是否继续？(y/n): ")
        if answer.lower() != 'y':
            return
    else:
        # 设置Git LFS
        setup_git_lfs(args.repo)
    
    # 获取所有匹配的文件
    files = glob.glob(os.path.join(args.source, args.pattern))
    
    if not files:
        print(f"没有找到匹配的文件: {os.path.join(args.source, args.pattern)}")
        return
    
    print(f"找到 {len(files)} 个文件需要上传")
    
    # 逐个上传文件
    success_count = 0
    for i, file_path in enumerate(files):
        print(f"\n[{i+1}/{len(files)}] 正在处理: {os.path.basename(file_path)}")
        
        try:
            if upload_file(file_path, args.repo):
                success_count += 1
        except Exception as e:
            print(f"处理文件时出错: {e}")
        
        # 延迟一段时间，避免连续请求
        if i < len(files) - 1:
            print(f"等待 {args.delay} 秒...")
            time.sleep(args.delay)
    
    print(f"\n上传完成! 成功: {success_count}/{len(files)}")

if __name__ == "__main__":
    main() 