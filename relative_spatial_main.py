from tool import Classification

root = "../datas/relative-spatial_0-999"
img_name_list = [f"{i}.jpg" for i in range(4)] + ['obj.jpg', 'sub.jpg']
img_col_num = 3
img_row_num = (len(img_name_list) - 1) // img_col_num + 1
reserve_path = "../relative_spatial/reserve.txt"
discard_path = "../relative_spatial/discard.txt"
json_info_list = ["object", "subject"]

Classification(root=root, img_name_list=img_name_list, json_info_list=json_info_list, reserve_path=reserve_path,
               discard_path=discard_path, img_row_num=img_row_num, img_col_num=img_col_num)
