from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import sys
import codecs
from spdx.writers.tagvalue import write_document, InvalidDocumentError
from spdx.parsers.tagvalue import Parser
from spdx.parsers.loggers import StandardLogger
from spdx.parsers.tagvaluebuilders import Builder

def pprint_tv(tv_filename, outfile_name):
    p = Parser(Builder(), StandardLogger())
    p.build()
    with open(tv_filename, 'r') as f:
        data = f.read()
        document, error = p.parse(data)
        if not error:
            print('Parsing Successful')
            with codecs.open(outfile_name, mode='w', encoding='utf-8') as out:
                try:
                    write_document(document, out)
                except InvalidDocumentError:
                    print('Document is Invalid')
                    messages = []
                    document.validate(messages)
                    print('\n'.join(messages))
                    return False
        else:
            print('Errors encountered while parsing')
            return False

def main():
    args = sys.argv[1:]
    if not args:
        print(
            'Usage:python pprint_tv.py <tag-value-file> <output-file>\n'
            'Pretty print a tag-value document.'
        )
        sys.exit(1)
    tvfile = args[0]
    outputfile = args[1]
    success = pprint_tv(tvfile, outputfile)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()