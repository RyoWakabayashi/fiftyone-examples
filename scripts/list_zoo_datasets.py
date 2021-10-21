"""
データセットZOOのデータセット一覧表示
"""

import fiftyone.zoo as foz


def main():
    """メイン処理"""

    for dataset_name in foz.list_zoo_datasets():
        print(dataset_name)


if __name__ == "__main__":
    main()
