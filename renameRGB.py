import os  
  
def rename_txt_files(folder_path):  
    """  
    在指定文件夹内，将所有.txt文件的名字前添加两个'0'。  
      
    :param folder_path: 包含.txt文件的文件夹路径  
    """  
    # 确保提供的路径是一个存在的文件夹  
    if not os.path.isdir(folder_path):  
        print(f"错误：{folder_path} 不是一个有效的文件夹路径。")  
        return  
  
    # 遍历文件夹中的所有文件  
    for filename in os.listdir(folder_path):  
        # 检查文件是否是.txt文件  
        if filename.endswith('.jpg'):  
            # 构建原始文件路径  
            old_file_path = os.path.join(folder_path, filename)  
            # 构建新文件名（在文件名前添加两个'0'）  
            # 注意：这里假设文件名不包含'.'（除了扩展名之前的点）  
            # 如果文件名以'.'开头（虽然不常见），则需要调整这个逻辑  
            new_filename = '00' + filename  
            # 构建新文件路径  
            new_file_path = os.path.join(folder_path, new_filename)  
              
            # 重命名文件  
            os.rename(old_file_path, new_file_path)  
            print(f"文件已重命名：{old_file_path} -> {new_file_path}")  
  
# 示例用法  
folder_path = '/media/dxy/175B-BF2C/front/1/blue/1'  # 修改为你的.txt文件所在的文件夹路径  
rename_txt_files(folder_path)
