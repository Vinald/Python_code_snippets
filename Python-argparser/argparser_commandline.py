import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')

    # Add a positional argument
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')

    # Add an optional argument
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
        
    args = parser.parse_args()
    
    print(args.accumulate(args.integers))
    
    # Run the script with the following command:
    # python 2_intermmediate/7_argparser_commandline.py 1 2 3 4 5 --sum
    