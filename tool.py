import os
import json
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pympler import tracker

tr = tracker.SummaryTracker()


def Classification(root, img_name_list, json_info_list, reserve_path, discard_path, img_row_num, img_col_num):
    if not os.path.exists(reserve_path):
        with open(reserve_path, 'w'):
            pass

    if not os.path.exists(discard_path):
        with open(discard_path, 'w'):
            pass

    f_reserve = open(reserve_path, 'a')
    f_discard = open(discard_path, 'a')

    total_set = set(os.listdir(root))
    with open(reserve_path, 'r') as f:
        reserve_set = set(f.read().split('\n'))
    with open(discard_path, 'r') as f:
        discard_set = set(f.read().split('\n'))
    remain_set = total_set.difference(reserve_set).difference(discard_set)

    plt.ion()
    for idx in remain_set:
        cur_path = os.path.join(root, idx)

        if not os.path.isdir(cur_path):
            continue

        with open(os.path.join(cur_path, "metadata.json"), 'r') as f:
            jsonData = json.load(f)
            info_list = [jsonData[item] for item in json_info_list]

        print(f"当前类别为: " + ', '.join(info_list))

        plt.figure(figsize=(18, 6))
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1, hspace=0.1, wspace=0.1)

        images = [mpimg.imread(os.path.join(cur_path, name)) for name in img_name_list]
        for i in range(len(img_name_list)):
            plt.subplot(img_row_num, img_col_num, i + 1)
            plt.imshow(images[i])
            plt.axis('off')  # 不显示坐标轴

        flag = False
        while True:
            result = input("输入q退出，输入y保留: ")
            if result == 'q':
                flag = True
            elif result == 'y':
                f_reserve.write(idx + "\n")
            elif result == 'query':
                with open(reserve_path, 'r') as f:
                    print("总数为: {}".format(len(f.read().split('\n'))))
                continue
            elif result == 'memory':
                tr.print_diff()
                continue
            else:
                f_discard.write(idx + "\n")
            break

        plt.clf()
        plt.close('all')
        del jsonData
        for item in images:
            del item

        if flag:
            f_reserve.close()
            f_discard.close()
            break
