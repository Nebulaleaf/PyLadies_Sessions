print('--\N{LATIN SMALL LETTER L WITH STROKE}--')
print('--\N{SECTION SIGN}--')
print('--\N{PER MILLE SIGN}--')
print('--\N{BLACK STAR}--')
print('--\N{SNOWMAN}--')
print('--\N{KATAKANA LETTER TU}--')
print('--\N{WHITE MEDIUM STAR}--')
print('--\N{BLACK DIAMOND}--')

import unicodedata
names = [unicodedata.name(chr(c)) for c in range(0, 0x10FFFF+1) if unicodedata.name(chr(c), None)]
print(names)