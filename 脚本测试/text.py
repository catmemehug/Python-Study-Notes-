import os
import glob

def convert_to_yolo_format(input_file, output_file, image_width, image_height):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            parts = line.strip().split()
            class_id = parts[0]
            xmin = int(parts[1])
            ymin = int(parts[2])
            xmax = int(parts[3])
            ymax = int(parts[4])
            
            # 计算中心点坐标和宽高
            x_center = ((xmin + xmax) / 2.0) / image_width
            y_center = ((ymin + ymax) / 2.0) / image_height
            width = (xmax - xmin) / float(image_width)
            height = (ymax - ymin) / float(image_height)
            
            # 写入YOLO格式的标注
            outfile.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

# 读取文件夹下的所有txt文件
file_path = r"E:\python pj\learn\脚本测试\labels\label-trainA"
input_files = glob.glob(os.path.join(file_path, "*.txt"))

image_width = 1280  # 图像宽度
image_height = 720  # 图像高度

# 创建输出文件夹
output_folder = r"E:\python pj\learn\脚本测试\labels\new_labels"
os.makedirs(output_folder, exist_ok=True)

i = 1501  # 设置起始文件编号为1501

for input_file in input_files:
    out_file_name = f"trainA_{i}.txt"
    out_file_path = os.path.join(output_folder, out_file_name)
    
    # 转换并写入新的YOLO格式文件
    convert_to_yolo_format(input_file, out_file_path, image_width, image_height)
    print(f"创建文件: {out_file_path}")
    
    i += 1  # 递增计数器
