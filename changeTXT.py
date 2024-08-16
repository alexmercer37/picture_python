import os  
  
def toggle_first_digit_in_file(input_file, output_file):  
    """  
    读取input_file中的每一行，修改每行第一个数字（0变1，1变0），  
    然后将修改后的内容写入到output_file中。  
    """  
    try:  
        with open(input_file, 'r', encoding='utf-8') as infile:  
            lines = infile.readlines()  
  
        with open(output_file, 'w', encoding='utf-8') as outfile:  
            for line in lines:  
                stripped_line = line.strip()  
                if stripped_line and stripped_line[0].isdigit():  
                    first_digit = '0' if stripped_line[0] == '1' else '1'  
                    modified_line = first_digit + stripped_line[1:] + '\n'  
                else:  
                    modified_line = line  
                outfile.write(modified_line)  
  
    except FileNotFoundError:  
        print(f"文件 {input_file} 未找到。")  
    except Exception as e:  
        print(f"处理文件 {input_file} 时发生错误: {e}")  
  
def process_txt_files_in_folder(input_folder_path, output_folder_path, output_suffix='_modified'):  
    """  
    遍历input_folder_path指定的文件夹中的所有.txt文件，  
    对每个文件执行toggle_first_digit_in_file函数，  
    并将修改后的内容保存到output_folder_path指定的文件夹中，文件名后可选添加output_suffix。  
    """  
    # 确保输出文件夹存在  
    if not os.path.exists(output_folder_path):  
        os.makedirs(output_folder_path)  
  
    for filename in os.listdir(input_folder_path):  
        if filename.endswith('.txt'):  
            input_file_path = os.path.join(input_folder_path, filename)  
            # 保持文件名不变，但添加输出文件夹路径和可选的后缀  
            output_file_path = os.path.join(output_folder_path, filename.rsplit('.', 1)[0]  + '.' + filename.rsplit('.', 1)[1])  
            toggle_first_digit_in_file(input_file_path, output_file_path)  
            print(f"处理完成: {input_file_path} -> {output_file_path}")  
  
# 示例用法  
input_folder_path = '/home/dxy/Downloads/two_labels/labels/train/1'  # 你要处理的txt文件所在的文件夹路径  
output_folder_path = '/home/dxy/Downloads/two_labels/labels/train/1/1'  # 修改后的txt文件将存储在这个文件夹中  
process_txt_files_in_folder(input_folder_path, output_folder_path)
