import argparse

if __name__ == "__main__":

    ###########################################
    # ファイルからデータの取得
    ###########################################
    _parser = argparse.ArgumentParser(description='AVILENインターン課題')
    _parser.add_argument('file_name', type=str, help='input file name for an extended FizzBuzz')
    _args = _parser.parse_args()
    _f = open(_args.file_name)
    _lines = _f.read().split('\n') # 行ごとにスプリットして取得
    _f.close()
    _lines.pop() # 最終行の''を削除

    ###########################################
    # データの前処理
    ###########################################
    _data_dict = {}
    for _line in _lines[:-1]:
        _data = _line.split(":")
        _data_dict[int(_data[0])] = _data[1]
    _data_list = sorted(_data_dict.items())
    _m = int(_lines[-1])

    ###########################################
    # FizzBuzzの拡張版の処理
    ###########################################
    _count = 0
    for _i, _s in _data_list:
        if _m % _i == 0:
            print(_s, end="")
            _count = _count + 1
    
    if _count == 0:
        print(_m)