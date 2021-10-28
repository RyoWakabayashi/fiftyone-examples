"""
データセットのエクスポート
"""

import fiftyone as fo
import fiftyone.zoo as foz


def main():
    """メイン処理"""

    # データセット名
    dataset_name = "open-images-v6-cat-dog-duck-yolo"
    classes = ["Cat", "Dog", "Duck"]

    # 未取得の場合、データセットZOOからダウンロードする
    # 取得済であればローカルからロードする
    if dataset_name in fo.list_datasets():
        dataset = fo.load_dataset(dataset_name)
    else:
        # 猫・犬・アヒルの画像と物体検出アノテーションデータを300件取得する
        dataset = foz.load_zoo_dataset(
            "open-images-v6",
            label_types=["detections"],
            classes=classes,
            max_samples=300,
            only_matching=True,
        )
        dataset.name = dataset_name
        # 永続化
        dataset.persistent = True

    # データセットを分割
    train_dataset = dataset[:700]
    val_dataset = dataset[700:800]
    test_dataset = dataset[800:]

    # YOLO V5 形式でエクスポート
    train_dataset.export(
        export_dir=f"~/yolov5-train-{dataset_name}",
        dataset_type=fo.types.YOLOv5Dataset,
        split="train",
        classes=classes,
    )
    val_dataset.export(
        export_dir=f"~/yolov5-val-{dataset_name}",
        dataset_type=fo.types.YOLOv5Dataset,
        split="val",
        classes=classes,
    )
    test_dataset.export(
        export_dir=f"~/yolov5-test-{dataset_name}",
        dataset_type=fo.types.YOLOv5Dataset,
        split="test",
        classes=classes,
    )


if __name__ == "__main__":
    main()
