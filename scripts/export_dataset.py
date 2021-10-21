"""
データセットのエクスポート
"""

import fiftyone as fo
import fiftyone.zoo as foz


def main():
    """メイン処理"""

    # データセット名
    dataset_name = "open-images-v6-cat-dog-duck"

    # 未取得の場合、データセットZOOからダウンロードする
    # 取得済であればローカルからロードする
    if dataset_name in fo.list_datasets():
        dataset = fo.load_dataset(dataset_name)
    else:
        # 猫・犬・アヒルの画像と物体検出アノテーションデータを200件取得する
        dataset = foz.load_zoo_dataset(
            "open-images-v6",
            split="validation",
            label_types=["detections"],
            classes=["Cat", "Dog", "Duck"],
            max_samples=200,
        )
        dataset.name = dataset_name
        # 永続化
        dataset.persistent = True

    # VOC 形式でエクスポート
    dataset.export(
        export_dir=f"~/voc-{dataset_name}",
        dataset_type=fo.types.VOCDetectionDataset,
    )


if __name__ == "__main__":
    main()
