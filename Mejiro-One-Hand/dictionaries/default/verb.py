from Mejiro.dictionaries.default.settings import DOT
from Mejiro.dictionaries.default.func import get_conso
from Mejiro.dictionaries.default.abbreviations import VERB_KAMI_MAP, VERB_SIMO_MAP, VERB_GODAN_MAP

CONJUGATE_GODAN_MAP = { # (五段活用限定)
    #行: [0.ない形, 1.使役形, 2.受身形, 3.ます形, 4.辞書形, 5.て・た形, 6.意向形, 7.仮定形, 8.可能形, 9.命令形]
    'k': ['か', 'か', 'か', 'き', 'く', 'い', 'こう', 'け', 'け', 'け'],
    'g': ['が', 'が', 'が', 'ぎ', 'ぐ', 'い', 'ごう', 'げ', 'げ', 'げ'],
    's': ['さ', 'さ', 'さ', 'し', 'す', 'し', 'そう', 'せ', 'せ', 'せ'],
    't': ['た', 'た', 'た', 'ち', 'つ', 'っ', 'とう', 'て', 'て', 'て'],
    'n': ['な', 'な', 'な', 'に', 'ぬ', 'ん', 'のう', 'ね', 'ね', 'ね'],
    'b': ['ば', 'ば', 'ば', 'び', 'ぶ', 'ん', 'ぼう', 'べ', 'べ', 'べ'],
    'm': ['ま', 'ま', 'ま', 'み', 'む', 'ん', 'もう', 'め', 'め', 'め'],
    'r': ['ら', 'ら', 'ら', 'り', 'る', 'っ', 'ろう', 'れ', 'れ', 'れ'],
    'w': ['わ', 'わ', 'わ', 'い', 'う', 'っ', 'おう', 'え', 'え', 'え'],
}
CONJUGATE_KAMI_MAP = { # (上一段活用限定)
    #行: [0.ない形, 1.使役形, 2.受身形, 3.ます形, 4.辞書形, 5.て・た形, 6.意向形, 7.仮定形, 8.可能形, 9.命令形]
    'k': ['き', 'きさ', 'きら', 'き', 'きる', 'き', 'きよう', 'きれ', 'きれ', 'きろ'],
    'g': ['ぎ', 'ぎさ', 'ぎら', 'ぎ', 'ぎる', 'ぎ', 'ぎよう', 'ぎれ', 'ぎれ', 'ぎろ'],
    'z': ['じ', 'じさ', 'じら', 'じ', 'じる', 'じ', 'じよう', 'じれ', 'じれ', 'じろ'],
    't': ['ち', 'ちさ', 'ちら', 'ち', 'ちる', 'ち', 'ちよう', 'ちれ', 'ちれ', 'ちろ'],
    'n': ['に', 'にさ', 'にら', 'に', 'にる', 'に', 'によう', 'にれ', 'にれ', 'にろ'],
    'b': ['び', 'びさ', 'びら', 'び', 'びる', 'び', 'びよう', 'びれ', 'びれ', 'びろ'],
    'm': ['み', 'みさ', 'みら', 'み', 'みる', 'み', 'みよう', 'みれ', 'みれ', 'みろ'],
    'r': ['り', 'りさ', 'りら', 'り', 'りる', 'り', 'りよう', 'りれ', 'りれ', 'りろ'],
    'w': ['い', 'いさ', 'いら', 'い', 'いる', 'い', 'いよう', 'いれ', 'いれ', 'いろ'],
}
CONJUGATE_SIMO_MAP = { # (下一段活用限定)
    #行: [0.ない形, 1.使役形, 2.受身形, 3.ます形, 4.辞書形, 5.て・た形, 6.意向形, 7.仮定形, 8.可能形, 9.命令形]
    'k': ['け', 'けさ', 'けら', 'け', 'ける', 'け', 'けよう', 'けれ', 'けれ', 'けろ'],
    'g': ['げ', 'げさ', 'げら', 'げ', 'げる', 'げ', 'げよう', 'げれ', 'げれ', 'げろ'],
    's': ['せ', 'せさ', 'せら', 'せ', 'せる', 'せ', 'せよう', 'せれ', 'せれ', 'せろ'],
    'z': ['ぜ', 'ぜさ', 'ぜら', 'ぜ', 'ぜる', 'ぜ', 'ぜよう', 'ぜれ', 'ぜれ', 'ぜろ'],
    't': ['て', 'てさ', 'てら', 'て', 'てる', 'て', 'てよう', 'てれ', 'てれ', 'てろ'],
    'd': ['で', 'でさ', 'でら', 'で', 'でる', 'で', 'でよう', 'でれ', 'でれ', 'でろ'],
    'n': ['ね', 'ねさ', 'ねら', 'ね', 'ねる', 'ね', 'ねよう', 'ねれ', 'ねれ', 'ねろ'],
    'h': ['へ', 'へさ', 'へら', 'へ', 'へる', 'へ', 'へよう', 'へれ', 'へれ', 'へろ'],
    'b': ['べ', 'べさ', 'べら', 'べ', 'べる', 'べ', 'べよう', 'べれ', 'べれ', 'べろ'],
    'm': ['め', 'めさ', 'めら', 'め', 'める', 'め', 'めよう', 'めれ', 'めれ', 'めろ'],
    'r': ['れ', 'れさ', 'れら', 'れ', 'れる', 'れ', 'れよう', 'れれ', 'れれ', 'れろ'],
    'w': ['え', 'えさ', 'えら', 'え', 'える', 'え', 'えよう', 'えれ', 'えれ', 'えろ'],
}
CONJUGATE_MAP = {
    '五': CONJUGATE_GODAN_MAP,
    '上': CONJUGATE_KAMI_MAP,
    '下': CONJUGATE_SIMO_MAP,
}
SAHEN_LIST =  ['し', 'さ', 'さ', 'し', 'する', 'し', 'しよう', 'すれ', 'でき', 'しろ'] # "*"
KAHEN_LIST =  ['こ', 'こさ', 'こら', 'き', 'くる', 'き', 'こよう', 'くれ', 'これ', 'こい'] # "K-*"
IKU_LIST =    ['いか', 'いか', 'いか', 'いき', 'いく', 'いっ', 'いこう', 'いけ', 'いけ', 'いけ'] # "I-K*"
ARU_LIST =    ['', 'あら', 'あら', 'あり', 'ある', 'あっ', 'あろう', 'あれ', 'ありえ', 'あれ'] # "A-*"

AUXILIARY_VERB_MAP = { # ストローク: [活用形, 助動詞]
    ''   : [4, ""],
    'n'  : [0, "ない"],
    't'  : [5, "た"],
    'k'  : [3, "ます"],
    'nt' : [0, "なかった"],
    'nk' : [3, "ません"],
    'tk' : [3, "ました"],
    'ntk': [5, "て"],
}
DESU_CONJUGATE_MAP = { # ですの活用形
    '':"です",
    'n':"でして",
    't':"でした",
    'k':"でしょう",
    'nt':"です" + DOT,
    'nk':"ですが",
    'tk':"ですか?",
    'ntk':"ですね",
}

def stroke_to_conjugate(particle_stroke: str) -> list:
    auxiliary_list = [None, ""]
    auxiliary_list = AUXILIARY_VERB_MAP[particle_stroke]
    return auxiliary_list

def translate_ta_te_form(string: str, auxiliary: int, conso: str) -> str:
    if auxiliary == 5 and conso in ['g', 'n', 'b', 'm']:
        if conso == 'g':
            if string.startswith("いて"):
                string = "いで" + string[2:]
            elif string.startswith("いた"):
                string = "いだ" + string[2:]
        else:  # n, b, m
            if string.startswith("んて"):
                string = "んで" + string[2:]
            elif string.startswith("んた"):
                string = "んだ" + string[2:]
    return string

def stroke_to_verb(kana, syllable, conso_stroke, vowel_stroke, particle_stroke) -> str:

    kana_stroke = conso_stroke + vowel_stroke + '-'

    conso = get_conso(conso_stroke)

    output = ""

    # 活用を取得
    auxiliary_list = stroke_to_conjugate(particle_stroke)

    # 登録された五段活用
    if kana_stroke in VERB_GODAN_MAP:
        verb_list = VERB_GODAN_MAP[kana_stroke]
        output = verb_list[0] + translate_ta_te_form(CONJUGATE_GODAN_MAP[verb_list[1]][auxiliary_list[0]] + auxiliary_list[1], auxiliary_list[0], verb_list[1])
    # 登録された上一段活用
    elif kana_stroke in VERB_KAMI_MAP:
        verb_list = VERB_KAMI_MAP[kana_stroke]
        output = verb_list[0] + CONJUGATE_KAMI_MAP[verb_list[1]][auxiliary_list[0]] + auxiliary_list[1]
    # 登録された下一段活用
    elif kana_stroke in VERB_SIMO_MAP:
        verb_list = VERB_SIMO_MAP[kana_stroke]
        output = verb_list[0] + CONJUGATE_SIMO_MAP[verb_list[1]][auxiliary_list[0]] + auxiliary_list[1]
    # 行く (ゆく)
    elif kana_stroke == "YU-":
        output += IKU_LIST[auxiliary_list[0]] + auxiliary_list[1]
    # ある
    elif kana_stroke == "A-":
        output += ARU_LIST[auxiliary_list[0]] + auxiliary_list[1]
    # カ変活用
    elif kana_stroke == "KU-":
        output += KAHEN_LIST[auxiliary_list[0]] + auxiliary_list[1]
    # サ変活用
    elif not kana:
        output = SAHEN_LIST[auxiliary_list[0]] + auxiliary_list[1]
    # ～です
    elif kana_stroke == 'TN-':
        output = DESU_CONJUGATE_MAP[particle_stroke]
    # ～いう
    elif kana_stroke == 'IU-':
        output = "い" + CONJUGATE_GODAN_MAP['w'][auxiliary_list[0]] + auxiliary_list[1]
    # 五段活用
    elif vowel_stroke == "" and conso in ['k', 'g', 's', 't', 'n', 'b', 'm', 'r', 'w']:
        output = kana + translate_ta_te_form(CONJUGATE_GODAN_MAP[conso][auxiliary_list[0]] + auxiliary_list[1], auxiliary_list[0], conso)
    # 上一段活用
    elif vowel_stroke == "I" and conso in ['k', 'g', 'z', 't', 'n', 'b', 'm', 'r', 'w', '']:
        if conso == '':
            conso = 'w'
        output = kana + CONJUGATE_KAMI_MAP[conso][auxiliary_list[0]] + auxiliary_list[1]
    # 下一段活用
    elif vowel_stroke == "IA" and conso in ['k', 'g', 's', 'z', 't', 'd', 'n', 'h', 'b', 'm', 'r', 'w', '']:
        if conso == '':
            conso = 'w'
        output = kana + CONJUGATE_SIMO_MAP[conso][auxiliary_list[0]] + auxiliary_list[1]
    # 「～る」動詞(五段活用)
    else:
        output = kana + CONJUGATE_GODAN_MAP['r'][auxiliary_list[0]] + auxiliary_list[1]
    return output
