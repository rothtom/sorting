import argparse
from List import DEFAULT_LIST_LENGTH, DEFAULT_RANDOM_SEED, POSSIBLE_ALGORITHMS

def check_usage():
    # check for right usage of command line arguments
    parser = argparse.ArgumentParser(
        prog="main.py",
            usage="python main.py --list_length {int} (default=100) --seed {float} (default=current timestamp)",
    )
    parser.add_argument("-l", "--length", default=DEFAULT_LIST_LENGTH, type=int)
    parser.add_argument("-s", "--seed", default=DEFAULT_RANDOM_SEED, type=float)
    # for now not required and defaults to bogo
    parser.add_argument("-a", "--algorithm", 
                        #required=True,
                        # add more algorithms later
                        choices=POSSIBLE_ALGORITHMS,
                        default="bubble"
                        )
    parser.add_argument("--start_list", default=None, type=str, help="A series of string seperated by ONLY commas")
    # args is a dict of the key-value pairs from the command-line
    args = vars(parser.parse_args())
    
    # format the start_list if given as a CLA.
    if args["start_list"] != None:
        args["start_list"] = tuple(args["start_list"].split())
    return args