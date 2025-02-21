import os
import math
import pandas as pd
import time

from format_surprisals import read_roark_surprisals


def get_total_perplexity(surprisals):
    surp = list(surprisals['surp'].astype(float))
    return math.exp(sum(surp)/len(surp))


def train_and_parse(t, data_type):
    src = 'incremental-top-down-parser/'
    train_data = f'corpus/{data_type}_trees/wiki_train_{data_type}_trees_normalized.txt'
    validation_data = f'corpus/{data_type}_trees/wiki_validation_{data_type}_trees_normalized.txt'

    model_name = f'{src}model/wiki_full_model_{data_type}_t_{t}'
    output_path = f'{src}model/parse_dev_{data_type}_t_{t}.output'


    # if not os.path.exists(model_name):
    train_command = f'{src}bin/tdptrain -t{t} -p -s"(SINV(S" -v -F {model_name} -m {src}data/tree.functs.sfile {train_data}'
    os.system(train_command)
    print("train done")

    # if not os.path.exists(output_path):
    print("parse start")
    parse_command = f'{src}bin/tdparse -v -p -F {output_path} {model_name} {validation_data}'
    os.system(parse_command)

    return output_path


def main():

    thresholds = [0.02,0.04,0.06,0.08]

    for data_type in ["pos","word"]:
        summary_df = pd.DataFrame()
        summary_path = f'summary_{data_type}.csv'
        for t in thresholds:
            print(data_type,t)
            parse_output = train_and_parse(t, data_type)
            surprisals = read_roark_surprisals(parse_output)
            surprisals = surprisals[surprisals.token != '</s>']
            print(t, get_total_perplexity(surprisals))
            summary_df['token'] = surprisals['token']
            summary_df[str(t)] = surprisals['surp']
        summary_df.to_csv(summary_path, index=False)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    total_time = end_time - start_time
    print(f"{total_time//60}:{total_time%60}")
