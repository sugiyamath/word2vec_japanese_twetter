import pandas as pd
from functools import partial
from multiprocessing import Pool

def replace_nl(string):
    return ' '.join(string.split())

def write_them(d, outfile="tweet.txt"):
    with open(outfile, "a") as f:
        f.write('\n'.join(list(map(replace_nl, d['text']))))
        
def run_it(df_iter):
    while(True):
        try:
            for d in df_iter:
                try:
                    write_them(d)
                except:
                    pass
        except:
            print("iter_error")
            continue
        
    #pool = Pool(8)
    #pool.map(write_them, df_iter)
            
if __name__ == "__main__":
    df_iter = pd.read_json("../tweet.dat", chunksize=100, lines=True)
    run_it(df_iter)