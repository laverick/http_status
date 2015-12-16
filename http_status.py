import requests

def main(input_filename, output_filename):
    infile = open(input_filename, 'r')
    outfile = open(output_filename, 'w')
    try:
        domain = infile.readline().rstrip()
        while domain:
            # May want to do some domain validity checking here
            url = "http://www.%s" % domain
            r = requests.get(url)
            result = "%s %s %s\n" % (domain, url, r.status_code)
            print(result)
            outfile.write(result)
            domain = infile.readline().rstrip()
    finally:
        infile.close()
        outfile.close()

if __name__ == '__main__':
    import sys
    import argparse
    parser = argparse.ArgumentParser(
        description='HTTP Status Code Checker.'
    )
    parser.add_argument('--input', help='input file')
    parser.add_argument('--output', help='output file')
    args = parser.parse_args()

    if args.input is None or args.output is None:
        print 'Specify input and output file'
        sys.exit(-1)
    main(input_filename=args.input, output_filename=args.output)
