// tdparse.c
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// Copyright 2004-2013 Brian Roark
// Author: roarkbr@gmail.com  (Brian Roark)
//

#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <getopt.h>
#include "pstruct.h"
#include "putil.h"
#include "parser.h"

#define USAGE "Usage: %s [-opts] model string                              \n\
                                                                           \n\
Options:                                                                   \n\
 -F file         output file                                               \n\
 -e              easier to read labeled bracketing                         \n\
 -a              all possible extensions (competititon)                    \n\
 -p              prefix probabilities                                      \n\
 -c list         closed class word list                                    \n\
 -z              partial parses                                            \n\
 -k n            n-best parses returned (default: 1)                       \n\
 -t x            base parsing threshold x (default: 12)                    \n\
 -v              verbose                                                   \n\
 -?              info/options                                              \n"

int main(int ac, char *av[])
{
  int c, err=0;
  char *ifile=NULL;
  extern char *optarg;
  extern int optind;
  TDParPtr ParseConf = TDParseDefault();

  while ((c = getopt(ac, av, "F:t:k:c:pzeav?")) != -1)
    switch (c) {
    case 'v':
      ParseConf->verbose = 1;
      break;  
    case 'p':
      ParseConf->prefix=1;
      break;  
    case 'z':
      ParseConf->partial=1;
      break;  
    case 'e':
      ParseConf->tabtree=1;
      break;
    case 'a':
      ParseConf->allpossible=1;
      break;  
    case 't':
      ParseConf->thresh=atof(optarg);
      break;
    case 'k':
      ParseConf->nbest=atoi(optarg);
      break;
    case 'c':
      ParseConf->sfile=optarg;
      break;
    case 'F':
      ParseConf->ofile = optarg;
      break;
    case '?':
    default:
      err++;
    }

  if (err || ac < optind+1) {
    fprintf(stderr, USAGE, av[0]);
    exit(1);
  }
  if (ac > optind+1) ParseConf->pfile=av[optind+1];
  run_parser(av[optind], ParseConf);
}
