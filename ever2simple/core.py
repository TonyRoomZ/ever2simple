import os
from ever2simple.converter import EverConverter


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print 'Usage: ever2simple <enex_file>'
        sys.exit(1)
    filepath = os.path.expanduser(args[0])
    if not os.path.exists(filepath):
        print 'File does not exist: %s' % filepath
        sys.exit(1)
    with open(filepath, 'rw') as enex_file:
        converter = EverConverter(enex_file)
        converter.convert()
    sys.exit()


if __name__ == '__main__':
    main()
