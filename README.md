# Probabilistic Context-Free Grammar (PCFG)

The code in [incremental-top-down-parser](incremental-top-down-parser) is the work of Roark et al. (2009):

> https://github.com/roarkbr/incremental-top-down-parser 

> [Deriving lexical and syntactic expectation-based measures for psycholinguistic modeling via incremental top-down parsing](https://aclanthology.org/D09-1034) (Roark et al., EMNLP 2009)


The following files are my own work: 
* [format_surprisals.py](format_surprisals.py)
* [PCFG_hyperparameter_tuning.py](PCFG_hyperparameter_tuning.py)
* [PCFG_parse.py](PCFG_parse.py)

To run this code, Stanford's tsurgeon package is required: http://nlp.stanford.edu/software/tregex.shtml
Update the `TSURGEONPATH` variable in [incremental-top-down-parser/data/tbnorm/tbnorm.sh](incremental-top-down-parser/data/tbnorm/tbnorm.sh) to be the path to tsurgeon.

Update the `INSTDIR` variable in [incremental-top-down-parser/Makedefs](incremental-top-down-parser/Makedefs) to be the path to [incremental-top-down-parser](incremental-top-down-parser).

