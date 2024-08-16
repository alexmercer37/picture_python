'''
Author: Yolohe 2284907789@qq.com
Date: 2023-12-02 19:47:21
LastEditors: Yolohe 2284907789@qq.com
LastEditTime: 2023-12-02 19:56:51
FilePath: /new/a.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os

def merge_folders(folder1_path, folder2_path, output_folder_path):
    # 获取两个文件夹中的所有文件
    folder1_files = os.listdir(folder1_path)
    folder2_files = os.listdir(folder2_path)

    # 确保两个文件夹中的文件数量一致
    if len(folder1_files) != len(folder2_files):
        print("Error: 两个文件夹中的文件数量不一致")
        return

    # 合并文件夹中的txt文件
    for i in range(len(folder1_files)):
        file1_path = os.path.join(folder1_path, folder1_files[i])
        file2_path = os.path.join(folder2_path, folder2_files[i])

        with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
            content1 = file1.read()
            content2 = file2.read()

            # 合并内容
            merged_content = content1 + '\n' + content2

            # 写入新文件
            output_file_path = os.path.join(output_folder_path, f"{i+1}.txt")
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(merged_content)

    print("合并完成")

# 用法示例
folder1_path = "/home/y2/Desktop/new/labels/train"
folder2_path = "/home/y2/Desktop/new/labels/Train"
output_folder_path = "/home/y2/Desktop/new/labels/val"

merge_folders(folder1_path, folder2_path, output_folder_path)

