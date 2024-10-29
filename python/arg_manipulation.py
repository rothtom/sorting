import argparse
from List import DEFAULT_LIST_LENGTH, DEFAULT_RANDOM_SEED, POSSIBLE_ALGORITHMS

def check_usage():
    # check for right usage of command line arguments
    parser = argparse.ArgumentParser(
        prog="main.py",
            usage="python main.py --list_length {int} (default=100) --seed {float} (default=current timestamp) --start_list a series of ints seperated by ONLY a comma --delay how many seconds you want to wait between every comparison --steps a bool that determins wether the algorythm runs thorough without clicking through every step",
    )
    parser.add_argument("-l", "--length", default=DEFAULT_LIST_LENGTH, type=int)
    parser.add_argument("-s", "--seed", default=DEFAULT_RANDOM_SEED, type=float)
    # for now not required and defaults to bogo
    parser.add_argument("-a", "--algorithm", help=f"determins which algorythm to use, choices are: {POSSIBLE_ALGORITHMS}",
                        #required=True,
                        # add more algorithms later
                        choices=POSSIBLE_ALGORITHMS,
                        default="selection"
                        )
    parser.add_argument("--start_list", default=None, type=str, help="A series of ints seperated by ONLY commas")
    parser.add_argument("-d", "--delay", default=0, type=float, help="how many secounds you want the comuter to wait after every step")
    # args is a dict of the key-value pairs from the command-line
    args = vars(parser.parse_args())
    return args