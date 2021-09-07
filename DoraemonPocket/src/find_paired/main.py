import multiprocessing as mp
from sys import path
from tqdm import trange
import imagehash
import Image
import os
from DoraemonPocket.src.utils import log_error
from DoraemonPocket.src.multiprocessor import multiprocessing

HASH_DICTS = {
    "ahash" : imagehash.average_hash,
    "phash" : imagehash.phash,
    "dhash" : imagehash.dhash,
    "whash-haar" : imagehash.whash,
    "colorhash" : imagehash.colorhash,
    "crop-resistant" : imagehash.crop_resistant_hash
}


def init_hash_table(path:str,  hash_func:function):
    hash_table = hash_func(Image.open(path))
    return hash_table

def find_hash(tar_hash:str, source_hash_table:list):
    try:
        return source_hash_table.index(tar_hash)
    except:
        return -1


def find_paired(sources:list, targets:list, hash_func:str="ahash"):
    '''Find target images from source images'.

    Using multiprocessing.

    Args:
        sources (list[str]): source images' paths.
        targets (list[str]): target images' paths.
        hash_func (str) [optional]:   Options "ahash", "phash", "dhash", "whash-haar", "colorhash", "crop-resistant". See https://github.com/JohannesBuchner/imagehash for details.

    Returns:
        pairs [str, ..., str], [str, ..., str]: source paths and paired target paths
    '''
    assert type(sources)==list, log_error("sources should be list, ", find_paired)
    assert type(targets)==list, log_error("targets should be list, ", find_paired)
    assert hash_func in HASH_DICTS.keys(), log_error("hash_func option not permitted, ", find_paired)
    for s in sources+targets:
        assert os.path.exists(s), log_error("{} do not exists".format(s))
    src_hash_table = multiprocessing(init_hash_table, sources, HASH_DICTS[hash_func])
    tar_hash_table = multiprocessing(init_hash_table, targets, HASH_DICTS[hash_func])
    idx = multiprocessing(find_hash, tar_hash_table, [src_hash_table for _ in range(len(tar_hash_table))])
    
    pairs = [[], []]
    for i, id in enumerate(idx):
        pairs[0] += src_hash_table[i]
        pairs[1] += tar_hash_table[id]
    
    return pairs