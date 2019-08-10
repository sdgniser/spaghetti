import random
from string import ascii_letters, digits

def random_string(size, chars=ascii_letters+digits):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

def gen_file_name(instance, filename):
    ext = filename.split('.')[-1]
    return 'code/' + random_string(12) + '.' + ext

allowed_langs = (
    ('apl', 'APL'),
    ('ass', 'Assembly'),
    ('awk', 'AWK'),
    ('bs', 'Bourne Shell'),
    ('basic', 'BASIC'),
    ('c', 'C'),
    ('cpp', 'C++'),
    ('boost', 'C++ with Boost'),
    ('stl', 'C++ with Standard Template Library'),
    ('csharp', 'C#'),
    ('clojure', 'Clojure'),
    ('cobol', 'COBOL'),
    ('cl', 'Common Lisp'),
    ('cudac', 'CUDA C'),
    ('d', 'D'),
    ('go', 'Go'),
    ('j', 'J'),
    ('java', 'Java'),
    ('js', 'JavaScript'),
    ('scm', 'Scheme'),
    ('curl', 'Curl'),
    ('fortran', 'Fortran'),
    ('haskell', 'Haskell'),
    ('holyc', 'HolyC'),
    ('kotlin', 'Kotlin'),
    ('julia', 'Julia'),
    ('logo', 'Logo'),
    ('lua', 'Lua'),
    ('machine', 'Machine Code'),
    ('maple', 'Maple'),
    ('matlab', 'MATLAB'),
    ('octave', 'Octave'),
    ('objc', 'Objective C'),
    ('pascal', 'Pascal'),
    ('perl', 'Perl'),
    ('php', 'PHP'),
    ('powershell', 'PowerShell'),
    ('py2', 'Python 2'),
    ('py3', 'Python 3'),
    ('numpy', 'Python with Numpy'),
    ('scipy', 'Python with SciPy'),
    ('othpy', 'Python with Other Libraries'),
    ('r', 'R'),
    ('ruby', 'Ruby'),
    ('rust', 'Rust'),
    ('swift', 'Swift'),
    ('sed', 'Sed'),
    ('sql', 'SQL'),
    ('tex', 'TeX'),
    ('tur', 'Turing'),
    ('wolf', 'WolframScript'),
)

langs = [lang[1] for lang in allowed_langs]
