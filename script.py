def main(n, t, v):
    from time import sleep

    try:
        import numpy
    except:
        raise ImportError('could not import numpy!')

    for i in range(1, n + 1):
        sleep(t)
        print(f'\riteration {i}', end = ['\n',''][i % v > 0])
    
if __name__ == '__main__':

    import argparse
    
    import json
    import os

    py     = os.path.basename(__file__)
    parser = argparse.ArgumentParser('example script')

    parser.add_argument('n' , type = int  , help = 'number of iterations')
    parser.add_argument('-t', type = float, help = 'time in seconds', default = 0.5)
    parser.add_argument('-v', type = int  , help = 'verbosity'      , default = 10)

    args = parser.parse_args()
    
    print(f'executing {py} with parameters:')
    print(json.dumps(dict(args._get_kwargs()), indent = 4))

    main(args.n, args.t, args.v)

    print(f'executed {py}')
