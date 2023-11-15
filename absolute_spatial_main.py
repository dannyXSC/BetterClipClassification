from tool import Classification

# 根目录
root = "../datas/absolute_spatial_0-3999"
# 每个文件夹里要显示图片的名字
img_name_list = [f"{i}.jpg" for i in range(9)]
# 每行显示多少个图片
img_col_num = 3
img_row_num = (len(img_name_list) - 1) // img_col_num + 1
# 要的数据（文件夹的 id）保存的位置
reserve_path = "../absolute_spatial/reserve.txt"
# 不要的数据保存的位置
discard_path = "../absolute_spatial/discard.txt"
# 要显示的metadata里的内容
json_info_list = ["object"]

Classification(root=root, img_name_list=img_name_list, json_info_list=json_info_list, reserve_path=reserve_path,
               discard_path=discard_path, img_row_num=img_row_num, img_col_num=img_col_num)
