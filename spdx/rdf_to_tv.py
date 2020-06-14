from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import sys
import codecs
from spdx.parsers.rdf import Parser
from spdx.parsers.loggers import StandardLogger
from spdx.parsers.rdfbuilders import Builder
from spdx.writers.tagvalue import write_document, InvalidDocumentError


def rdf_to_tv(rdf, tv):
    rdfparser = Parser(Builder(), StandardLogger())
    with open(rdf) as infile:
        document, error = rdfparser.parse(infile)
        if not error:
            print('Parsing Successful')
            with codecs.open(tv, mode='w', encoding='utf-8') as outfile:
                try:
                    write_document(document, outfile)
                except InvalidDocumentError:
                    # Note document is valid if error is False
                    print('Document is Invalid')
        else:
            print('Errors encountered while parsing RDF file.')
            messages = []
            document.validate(messages)
            print('\n'.join(messages))


def main():
    args = sys.argv[1:]
    if not args:
        print(
            'Usage: rdf_to_py <rdf-file> <tag-file>\n'
            'Convert an SPDX RDF document to tag/value.'
        )
        sys.exit(1)

    rdffile = args[0]
    tvfile = args[1]
    success = rdf_to_tv(rdffile, tvfile)
    sys.exit(0 if success else 1)
if __name__ == '__main__':
    main()
