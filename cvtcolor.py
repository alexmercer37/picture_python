import os  
import cv2  
  
# 输入和输出文件夹路径  
input_folder = '/media/dxy/175B-BF2C/front/1/blue'  # 替换为你的输入文件夹路径  
output_folder = '/media/dxy/175B-BF2C/front/1/blue/1'  # 替换为你的输出文件夹路径  
if not os.path.exists(output_folder):  
    os.makedirs(output_folder)  
  
# 遍历输入文件夹中的所有文件  
for filename in os.listdir(input_folder):  
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):  # 添加你希望处理的图像文件扩展名  
        # 读取BGR图像  
        img_path = os.path.join(input_folder, filename)  
        img = cv2.imread(img_path)  
        if img is not None:  
            # 将BGR转换为RGB  
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
              
            # 保存RGB图像到输出文件夹  
            output_path = os.path.join(output_folder, filename)  
            cv2.imwrite(output_path, rgb_img)  
        else:  
            print(f"无法读取文件: {img_path}")
