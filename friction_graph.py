import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
import tkinter.simpledialog as sd
import json

# Load configuration from JSON file
config_path = os.path.join(os.path.dirname(__file__), "config.json")
if os.path.exists(config_path):
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
        NETWORK_DIR = config.get("NETWORK_DIR", "")
else:
    print("エラー: config.json が見つかりません")
    print("config.json is missing.")
    print("Please create a config.json file with a Directry path.")
    sys.exit(1)

def main():
    # GUIのルートウィンドウを作成（非表示）
    root = tk.Tk()
    root.withdraw()

    # ファイル選択ダイアログを表示
    filename = filedialog.askopenfilename(
        title="データファイルを選択してください",
        filetypes=[("テキストファイル", "*.TXT"), ("すべてのファイル", "*.*")],
        initialdir=os.getcwd()
    )

    # キャンセルされた場合
    if not filename:
        print("ファイルが選択されませんでした")
        sys.exit(1)

    # ファイル存在確認
    if not os.path.isfile(filename):
        print(f"エラー: ファイルが見つかりません → {filename}")
        sys.exit(1)

    try:
        # ファイル読み込み
        df = pd.read_csv(filename, skiprows=21, header=None, sep=r'\s+', encoding='shift_jis')

        # 必要な列を抽出（1列目と3列目のみ）
        x = df[0]
        y = df[2]

        # グラフ描画
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label='Friction force')
        plt.xlabel("Sliding count [times]")
        plt.ylabel("Friction Force [mN]")
        plt.title(f"Graph from: {os.path.basename(filename)}")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # 保存するファイル名を入力するダイアログを表示
        default_name = os.path.splitext(os.path.basename(filename))[0]
        
        # カスタムダイアログクラスの定義
        class LargerDialog(sd.Dialog):
            def body(self, master):
                self.geometry("400x150")  # ダイアログのサイズを設定
                return super().body(master)
        
        save_name = sd.askstring("ファイル名入力", 
                               "保存するファイル名を入力してください\n(拡張子は自動的に付加されます)",
                               initialvalue=default_name,
                               parent=root)  # parentを指定して親ウィンドウを設定
        
        if not save_name:  # キャンセルされた場合
            print("ファイル名が入力されませんでした")
            sys.exit(1)

        # グラフの保存（オリジナルの場所）
        save_dir = os.path.dirname(filename)
        save_path = os.path.join(save_dir, f"{save_name}.png")
        plt.savefig(save_path)
        
        # グラフの追加保存先（ネットワークドライブ）
        if os.path.exists(NETWORK_DIR):
            network_save_path = os.path.join(NETWORK_DIR, f"{save_name}.png")
            plt.savefig(network_save_path)
        else:
            print(f"警告: ネットワークドライブにアクセスできません → {NETWORK_DIR}")
        
        # データをCSVとして保存（オリジナルの場所のみ）
        data_for_csv = pd.DataFrame({
            'Sliding_count': x,
            'Friction_Force': y
        })
        csv_save_path = os.path.join(save_dir, f"{save_name}_data.csv")
        data_for_csv.to_csv(csv_save_path, index=False)
        
        plt.show()
    except Exception as e:
        print(f"エラーが発生しました:\nエラーの種類: {type(e).__name__}\nエラーの内容: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
