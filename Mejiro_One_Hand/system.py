KEYS = (
'S-', 'T-', 'K-', 'N-', 'Y-', 'I-', 'A-', 'U-', 'n-', 't-', 'k-',
'-*',
)

IMPLICIT_HYPHEN_KEYS = ()

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = ('IU-')

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
        'Gemini PR': {
        'S-' : ('S1-','S2-'),
        'T-' : 'T-',
        'K-' : 'K-',
        'N-' : 'W-',
        'Y-' : 'P-',
        'I-' : 'H-',
        'A-' : 'R-',
        'U-' : ('*1','*2'),
        'n-' : '#3',
        't-' : ('A-'),
        'k-' : ('O-'),
        '-*' : ('#1','#2')
        },
        'Plover HID': {
        'S-' : ('S1-','S2-'),
        'T-' : 'T-',
        'K-' : 'K-',
        'N-' : 'W-',
        'Y-' : 'P-',
        'I-' : 'H-',
        'A-' : 'R-',
        'U-' : ('*1','*2'),
        'n-' : '#3',
        't-' : ('A-'),
        'k-' : ('O-'),
        '-*'  : ('#1','#2'),
        },
        'Keyboard': {
        'S-' : 'a',
        'T-' : 'w',
        'K-' : 's',
        'N-' : 'd',
        'Y-' : 'e',
        'I-' : 'r',
        'A-' : 'f',
        'U-' : ('t','g'),
        'n-' : 'space',
        't-' : ('v'),
        'k-' : ('b'),
        '-*'  : ('q'),
        'arpeggiate' : 'Return'
        }
}
DICTIONARIES_ROOT = 'asset:Mejiro_One_Hand:dictionaries/default'
DEFAULT_DICTIONARIES = ('mejiro_users.json','mejiro_commands.json','mejiro.py')



