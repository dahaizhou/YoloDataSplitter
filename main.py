from gooey import Gooey, GooeyParser
import os
import random
import shutil
from pathlib import Path


def make_dirs(base_dir):
    for subset in ['train', 'val', 'test']:
        (base_dir / f'images/{subset}').mkdir(parents=True, exist_ok=True)
        (base_dir / f'labels/{subset}').mkdir(parents=True, exist_ok=True)


def copy_files(file_list, source_img_dir, source_lbl_dir, output_base, subset):
    for file_path in file_list:
        img_name = file_path.name
        lbl_name = file_path.with_suffix('.txt').name

        dst_img = output_base / f'images/{subset}' / img_name
        dst_lbl = output_base / f'labels/{subset}' / lbl_name

        shutil.copy2(source_img_dir / img_name, dst_img)
        if (source_lbl_dir / lbl_name).exists():
            shutil.copy2(source_lbl_dir / lbl_name, dst_lbl)


@Gooey(program_name="YOLO 数据集划分工具", language='chinese', required_cols=2, default_size=(720, 480))
def main():
    parser = GooeyParser(description="将YOLO格式数据集按比例划分为训练/验证/测试集")

    parser.add_argument("source_images", help="原始图像目录", widget="DirChooser")
    parser.add_argument("source_labels", help="标签文件目录", widget="DirChooser")
    parser.add_argument("output_dir", help="输出目录", widget="DirChooser")

    parser.add_argument("train_ratio", help="训练集比例", type=float, default=0.7)
    parser.add_argument("val_ratio", help="验证集比例", type=float, default=0.2)
    parser.add_argument("test_ratio", help="测试集比例", type=float, default=0.1)

    args = parser.parse_args()

    img_dir = Path(args.source_images)
    lbl_dir = Path(args.source_labels)
    out_dir = Path(args.output_dir)

    make_dirs(out_dir)

    all_images = list(img_dir.glob("*.jpg"))
    random.shuffle(all_images)

    total = len(all_images)
    n_train = int(total * args.train_ratio)
    n_val = int(total * args.val_ratio)

    train_files = all_images[:n_train]
    val_files = all_images[n_train:n_train + n_val]
    test_files = all_images[n_train + n_val:]

    copy_files(train_files, img_dir, lbl_dir, out_dir, 'train')
    copy_files(val_files, img_dir, lbl_dir, out_dir, 'val')
    copy_files(test_files, img_dir, lbl_dir, out_dir, 'test')

    print(f"✔ 数据集划分完成！共 {total} 张图像")
    print(f"训练集: {len(train_files)} 张")
    print(f"验证集: {len(val_files)} 张")
    print(f"测试集: {len(test_files)} 张")


if __name__ == '__main__':
    main()
