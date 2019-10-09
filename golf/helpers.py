import random
from string import ascii_letters, digits

def random_string(size, chars=ascii_letters+digits):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

def gen_file_name(instance, filename):
    ext = filename.split('.')[-1]
    return 'code/' + random_string(12) + '.' + ext

incorrect_reasons = (
    'it throws an error during compilation/execution',
    'it gives incorrect output'
)

incorrect_reason_options = ((reason, reason) for reason in incorrect_reasons)

langs = (
    'APL',
    'Assembly',
    'AWK',
    'Bourne Shell',
    'BASIC',
    'C',
    'C++',
    'C++ with Boost',
    'C++ with Standard Template Library',
    'C#',
    'Clojure',
    'COBOL',
    'Common Lisp',
    'CUDA C',
    'D',
    'Go',
    'J',
    'Java',
    'JavaScript',
    'Scheme',
    'Curl',
    'Fortran',
    'Haskell',
    'HolyC',
    'Kotlin',
    'Julia',
    'Logo',
    'Lua',
    'Machine Code',
    'Maple',
    'MATLAB',
    'Octave',
    'Objective C',
    'Pascal',
    'Perl',
    'PHP',
    'PowerShell',
    'Python 2',
    'Python 3',
    'Python with Numpy',
    'Python with SciPy',
    'Python with Other Libraries',
    'R',
    'Ruby',
    'Rust',
    'Swift',
    'Sed',
    'SQL',
    'TeX',
    'Turing',
    'WolframScript',
)

allowed_langs = ((lang, lang) for lang in langs)
