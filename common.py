import os
import re
from os.path import join as pjoin


def extract_x_from_file(keys: [str], file_path: str):
    patterns = []
    for k in keys:
        pattern = re.compile('({})\s+(\d+\.?\d*)\s+#'.format(k))
        patterns.append(pattern)

    assert(os.path.isfile(file_path))
    results = []
    with open(file_path) as f:
        for line in f:
            for pattern in patterns:
                m = pattern.match(line)
                if m:
                    results.append((m.group(1), m.group(2)))
    return results


def extract_x_from_files(bm_keys: [str], keys: [str], file_paths: [str]):
    assert( len(bm_keys) == len(file_paths) )
    results = {}
    for k, p in zip(bm_keys, file_paths):
        results[k] = extract_x_from_file(keys, p)
    return results


def get_all_benchmarks():
    b = []
    with open('./all_compiled_spec.txt') as f:
        for line in f:
            if not line.startswith('#'):
                b.append(line.strip())
    return b


def has_stats(path: str):
    return os.path.isfile(pjoin(path, 'stats.txt'))
