import os
import random
from PIL import Image

# 设置文件夹路径
folder_path = '/etc/disks/omniai/data/zhangkai/mycache/gen_images/Bedroom128_ckpt/'

# 获取文件夹中的所有图片文件
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 随机抽取100张图片
selected_images = random.sample(image_files, 100)

# 打开图片并调整大小
images = [Image.open(os.path.join(folder_path, img)).resize((100, 100)) for img in selected_images]

# 创建一个新的空白图像用于拼贴
collage_width = 10 * 100
collage_height = 10 * 100
collage_image = Image.new('RGB', (collage_width, collage_height))

# 将图片粘贴到拼贴图像中
for i in range(10):
    for j in range(10):
        collage_image.paste(images[i * 10 + j], (j * 100, i * 100))

# 保存拼贴图像
collage_image.save('bedroom.jpg')

# import os
# import random
# from PIL import Image
#
# # 设置文件夹路径
# folder_path = '/etc/disks/omniai/data/zhangkai/mycache/gen_images/horse128_ckpt/'
#
# # 获取文件夹中的所有图片文件
# image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
#
# # 随机抽取25张图片
# selected_images = random.sample(image_files, 25)
#
# # 打开图片并调整大小
# images = [Image.open(os.path.join(folder_path, img)).resize((100, 100)) for img in selected_images]
#
# # 创建一个新的空白图像用于拼贴
# grid_size = 5
# image_size = 100
# collage_width = grid_size * image_size
# collage_height = grid_size * image_size
# collage_image = Image.new('RGB', (collage_width, collage_height))
#
# # 将图片粘贴到拼贴图像中
# for i in range(grid_size):
#     for j in range(grid_size):
#         collage_image.paste(images[i * grid_size + j], (j * image_size, i * image_size))
#
# # 保存拼贴图像
# output_path = '.jpg'
# collage_image.save(output_path)
# print(f"Saved the collage image to {output_path}")
