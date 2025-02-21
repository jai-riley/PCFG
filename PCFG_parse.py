import os
import math
import time
from format_surprisals import read_roark_surprisals


def get_total_perplexity(surprisals):
    surp = list(surprisals['surp'].astype(float))
    return math.exp(sum(surp) / len(surp))


def parse(data_path, data_split, t, data_type):
    src = 'incremental-top-down-parser/'
    output = '../../../output/PCFG/'
    model_name = f'/Users/jairiley/Desktop/BOW_Ngrams/PCFG/incremental-top-down-parser/model/wiki_full_model_{data_type}_t_0.02'
    output_path = f'/Users/jairiley/Desktop/BOW_Ngrams/PCFG/incremental-top-down-parser/model/wiki_{data_type}_02.output'

    # if not os.path.exists(output_path):
    print("start parse")
    parse_command = f'{src}bin/tdparse -v -p -F {output_path} {model_name} {data_path}'
    os.system(parse_command)
    print("finish parse")
    return output_path


def main():
    # data = '../../../data/'
    for data_type in ["pos", "word"]:
        for data_split in ['L2']:
            # if data_split == 'test':
            #     data_path = f'{data}wiki/sequences/{data_type}/wiki_test_{data_type}.txt'
            # else:
            data_path = f'/Users/jairiley/Desktop/BOW_Ngrams/corpus/L2/stimuli_L2_{data_type}.txt'

            output_path = parse(data_path, data_split, 0.02, data_type)
            surprisals = read_roark_surprisals(output_path)
            surprisals = surprisals[surprisals.token != '</s>']
            print(f'{data_split}, {data_type}, perplexity: {get_total_perplexity(surprisals)}')


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    total_time = end_time - start_time
    print(f"{total_time//60}:{total_time%60}")

