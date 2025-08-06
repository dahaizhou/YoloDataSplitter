# YOLO Split GUI 🧩

一个简单易用的 **图形界面工具**，用于将 **YOLO格式数据集** 按照指定比例划分为 `训练集 / 验证集 / 测试集`。

![demo](assets/demo.gif)  <!-- 可选：添加演示动画 -->

---

## ✨ 功能特点

- ✅ 图形化界面（基于 Gooey）
- ✅ 支持自定义比例划分
- ✅ 自动整理为 YOLO 格式目录结构
- ✅ 零代码门槛，一键操作
- ✅ 支持中文界面

---

## 📂 输出结构示例

```text
output_dir/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
