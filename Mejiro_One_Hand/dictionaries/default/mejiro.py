#      [STKNYIAUntk#STKNYIAUntk*]
# ┌─────┬─────┬─────┬─────┬─────┬─────┐
# │     │     │  T  │  Y  │  I  │     │
# │  *  │  S  ├─────┼─────┼─────┤  U  │
# │     │     │  K  │  N  │  A  │     │
# └─────┴─────┴─────┴─────┴─────┴─────┘
#                         ┌───────────┐
#                         │     n     │
#                         ├─────┬─────┤
#                         │  t  │  k  │
#                         └─────┴─────┘

import re
from Mejiro.dictionaries.default.settings import conso_stroke_to_roma
from Mejiro.dictionaries.default.func import (stroke_to_kana, stroke_to_syllable, joshi)
from Mejiro.dictionaries.default.abbreviations import USERS_MAP
from Mejiro.dictionaries.default.verb import stroke_to_verb
from Mejiro.dictionaries.default.translate import kana_to_typing_output

# ファイル構成
# Mejiro ┬ system.py
#        └ dictionaries ─ default ┬ mejiro.py
#                                 ├ mejiro_commands.json
#                                 ├ mejiro_users.json
#                                 ├ settings.py
#                                 ├ func.py
#                                 ├ abbreviations.py
#                                 ├ verb.py
#                                 └ translate.py

# グローバル変数の定義
LONGEST_KEY = 1
is_typing_mode = True

# タイピングゲーム時の入力法設定
typing_mode = 0 # 0: ローマ字入力, 1: JISかな入力

# メインの関数
def lookup(key):
    global LONGEST_KEY
    global typing_mode
    global is_typing_mode
    assert len(key) <= LONGEST_KEY
    stroke = key[0]

    if stroke == "n#":
        if is_typing_mode:
            print("typing mode off")
        else:
            print("typing mode on")
        is_typing_mode = not is_typing_mode

    regex = re.compile(r"(S?T?K?N?)(Y?I?A?U?)(n?t?k?)(-)(\*?)")
    regex_groups = re.search(regex, stroke)

    conso_stroke = regex_groups.group(1)
    vowel_stroke = regex_groups.group(2)
    particle_stroke = regex_groups.group(3)
    asterisk = regex_groups.group(5)
    kana_stroke = conso_stroke + vowel_stroke
    syllable_stroke = conso_stroke + vowel_stroke + particle_stroke
    raw_stroke = conso_stroke + vowel_stroke + particle_stroke + '-' + asterisk

    result = "" # 初期化

    # かなを変数に格納
    kana = stroke_to_kana(conso_stroke, vowel_stroke)

    # 左右の音節を変数に格納
    syllable = stroke_to_syllable(conso_stroke, vowel_stroke, particle_stroke)

    # 助詞を変数に格納
    mini_joshi = joshi(particle_stroke)

    message = ""
    # メインの変換処理
    if raw_stroke in USERS_MAP and asterisk: # ユーザー略語
        result = USERS_MAP[raw_stroke]
        message = "ユーザー辞書"
    elif kana_stroke is None and joshi and not asterisk: # 助詞
        result = mini_joshi
        message = "助詞"
    elif asterisk:
        # 動詞変換処理
        verb = stroke_to_verb(kana, syllable, right_kana, stroke_list)
        # 動詞略語
        if verb:
            result = verb
            message = "動詞略語"
    # 通常
    else :
        message = "通常出力"
        result = syllable

    # タイピングゲーム時の変換処理
    if is_typing_mode:
        translated_result = kana_to_typing_output(result, typing_mode)
        result = translated_result

    if stroke == "STKNYIAUntk-*":
        message = "出力取止"
        result = ""
    # デバッグ画面に入力と結果を表示
    print("|\t" + stroke + "\t|\t" + result + "\t|\t" + message + "\t|\t" + ("on" if is_typing_mode else "off") + "\t|")

    # 結果の出力(両端に{^ ^}をつけることで、英語の自動スペースを防ぐ)
    return "{^" + result + "^}"

# 逆引き関数（ストローク検索用）
def reverse_lookup(text):
    result = ""
    string = kana_to_typing_output(text, 0) # ローマ字に変換してから解析
    conso_stroke = next((stroke for roma, stroke in conso_stroke_to_roma if roma == string), None)
    # 一例
    if text == "きき":
        return [("KI-KI", ), ("KInk-", ), ("KI-", "KI-")]

    return []
