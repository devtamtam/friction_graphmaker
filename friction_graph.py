import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
from datetime import datetime

def main():
    # 引数チェック
    if len(sys.argv) != 2:
        print("使い方: python friction_graph.py ファイル名.txt")
        sys.exit(1)

    filename = sys.argv[1]

    # ファイル存在確認
    if not os.path.isfile(filename):
        print(f"エラー: ファイルが見つかりません → {filename}")
        sys.exit(1)

    try:
        # ファイル読み込み
        df = pd.read_csv(filename, skiprows=22, header=None, sep=r'\s+', encoding='shift_jis')

        # 必要な列を抽出
        x = df[0]
        y1 = df[2]
        y2 = df[3]

        # グラフ描画
        plt.figure(figsize=(10, 6))
        plt.plot(x, y1, label='Load')  # Changed from 'Friction force' to 'Load'
        plt.plot(x, y2, label='Friction force')  # Changed from 'Y2 (Column 4)' to 'Friction force'
        plt.xlabel("Sliding count [times]")
        plt.ylabel("Force [Nm]")
        plt.title(f"Graph from: {os.path.basename(filename)}")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        
        # グラフの保存
        save_dir = 'graphis'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        # 入力ファイル名から.txtを除いてpngを付ける
        base_name = os.path.splitext(os.path.basename(filename))[0]
        save_path = os.path.join(save_dir, f"{base_name}.png")
        plt.savefig(save_path)
        plt.show()
    except Exception as e:
        print(f"エラーが発生しました:\nエラーの種類: {type(e).__name__}\nエラーの内容: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
