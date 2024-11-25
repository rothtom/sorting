import argparse
from List import DEFAULT_LIST_LENGTH, DEFAULT_RANDOM_SEED, POSSIBLE_ALGORITHMS
from List import MAX_WIDTH

def check_usage():
    # check for right usage of command line arguments
    parser = argparse.ArgumentParser(
        prog="main.py",
        usage="python main.py --list_length {int} (default=100) --seed {float} (default=current timestamp) --start_tuple a series of ints seperated by ONLY a comma --delay how many seconds you want to wait after each draw call",
    )
    parser.add_argument("-l", "--length", default=DEFAULT_LIST_LENGTH, type=max_length_check)
    parser.add_argument("--seed", default=DEFAULT_RANDOM_SEED, type=float)
    # for now not required and defaults to bogo
    parser.add_argument("-a", "--algorithm", help=f"determins which algorythm to use, choices are: {POSSIBLE_ALGORITHMS}, you can leave out the '-sort'.",
                        #required=True,
                        # add more algorithms later
                        choices=POSSIBLE_ALGORITHMS,
                        default="selection"
                        )
    parser.add_argument("--start_tuple", default=None, type=str, help="A series of ints seperated by ONLY commas")
    parser.add_argument("-d", "--delay", default=0, type=float, help="how many secounds you want the comuter to wait after every step")
    parser.add_argument("-s", "--stop", default=False, action="store_true")
    # args is a dict of the key-value pairs from the command-line
    args = vars(parser.parse_args())
    args["algorithm"] = args["algorithm"].split("-sort")[0]
    if args["start_tuple"]:
        args["start_tuple"] = args["start_tuple"].split(",")
        for i in range(len(args["start_tuple"])):
            args["start_tuple"][i] = int(args["start_tuple"][i])
        args["start_tuple"] = tuple(args["start_tuple"])
    return args

def max_length_check(l):
    try:
        l = float(l)
    except:
        raise argparse.ArgumentTypeError("length must be an integer")
    
    if (l % 1) != 0:
        raise argparse.ArgumentTypeError("length must be an int, not a float")
    l = int(l)
    
    max_length = (MAX_WIDTH // 2)
    if l > max_length or l < 1:
        raise argparse.ArgumentTypeError(f"Length must not be greater than {max_length}, because the max width is {MAX_WIDTH}.")
    return l