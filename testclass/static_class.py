# クラスの定義
class Error_info():
    __counter = 0
    # コンストラクタ(初期化メソッド)
    def __init__(self):
        Error_info.__counter += 1

    def rtn_counter(self):
        return Error_info.__counter