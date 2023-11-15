from open_clip.src.training.data import get_wds_dataset
import torchvision.transforms as transforms
import json
import re

from classes import item_set, item_to_class, raw_class


def CountItem(dataset_path, item_cnt_path, class_cnt_path):
    class Argument():
        def __init__(self) -> None:
            self.val_data = dataset_path
            self.val_num_samples = 10000
            self.batch_size = 1
            self.workers = 0
            self.world_size = 0

    def tokenizer(text):
        return [text]

    args = Argument()
    dataset = get_wds_dataset(
        args=args, preprocess_img=transforms.ToTensor(), is_train=False, tokenizer=tokenizer)

    item_cnt = {item: 0 for item in item_set}
    class_cnt = {cls: 0 for cls in raw_class.keys()}

    cnt = 0
    total = args.val_num_samples
    for data in dataset.dataloader:
        # 转小写
        text = data[1][0].lower()
        # 记录，每个类别出现过没有
        cur_class_set = set()
        for item in item_cnt.keys():
            # 用正则判断字符
            # if text.find(item) != -1:
            if re.search(r"\b{}\b".format(item), text):
                item_cnt[item] += 1
                for cls in item_to_class[item]:
                    cur_class_set.add(cls)
        for cls in cur_class_set:
            class_cnt[cls] += 1
        cnt += 1
        if cnt % 100 == 0:
            print("已经完成{}; 总共{}".format(cnt, total))

    print(item_cnt)
    print(class_cnt)

    with open(item_cnt_path, 'w')as f:
        json.dump(item_cnt, f)

    with open(class_cnt_path, 'w')as f:
        json.dump(class_cnt, f)


if __name__ == '__main__':
    CountItem('./laion_demo/00000.tar', './item_cnt.txt', './class_cnt.txt')
