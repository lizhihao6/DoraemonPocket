from logging import log
import multiprocessing as mp
from tqdm import trange
from DoraemonPocket.src.utils import log_error

def son_process(start_id:int, stop_id:int, func:function, *args):
    iter = trange(start_id, stop_id) if start_id == 0 else range(start_id, stop_id)
    results = []
    for i in iter:
        _args = (arg[i] for arg in args)
        results.append((i, func(*_args)))
    return results

def multiprocessing(func:function, *args):
    '''User friendly multiprocessing function.

    Just input function name and its corresponding args.

    Args:
        func (str): function name.
        args (list, ... or other type): Args is function's args, should be list with same length. (Part of args could be other type, which would be auto amplification)
        hash_func (str) [optional]:   Options "ahash", "phash", "dhash", "whash-haar", "colorhash", "crop-resistant". See https://github.com/JohannesBuchner/imagehash for details.

    Returns:
        pairs [[str, ..., str], [str, ..., str]]: source paths and paired target paths
    '''
    task_num = -1
    for arg in args:
        if type(arg) in [list, tuple]:
            if task_num != -1:
                assert task_num == len(arg),  ("input list or tuple shoule be same size", multiprocessing)
            else:
                task_num = len(arg)
    assert task_num != -1, log_error("at least need one ", multiprocessing)

    # auto amplification
    for i, arg in enumerate(args):
        if type(arg) not in [list, tuple]:
            args[i] = [arg for _ in range(task_num)]
      
    num_cores = int(mp.cpu_count())
    print("Using multiprocessor, num cores: {}".format(num_cores), flush=True)
    pool = mp.Pool(num_cores)
    params = []
    for k in range(0, task_num - task_num // num_cores, task_num // num_cores):
        params.append([k, k + task_num // num_cores])
    pools = [pool.apply_async(son_process, args=(para[0], para[1], func, *args)) for para in params]
    results = []
    results += [p.get() for p in pools]
    results += son_process(params[-1][1], task_num, func, args)
    re_rank_results = [None for _ in range(task_num)]
    for r in results:
        re_rank_results[r[0]] = r[1]
    return re_rank_results