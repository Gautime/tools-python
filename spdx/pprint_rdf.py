
import sys
import spdx.file as spdxfile
from spdx.parsers.rdf import Parser
from spdx.parsers.loggers import StandardLogger
from spdx.parsers.rdfbuilders import Builder
from spdx.writers.rdf import write_document, InvalidDocumentError

def pprint_rdf(rdf_filename, outfile_name):
    p = Parser(Builder(), StandardLogger())
    with open(rdf_filename) as f:
        doc, error = p.parse(f)
        if not error:
            with open(outfile_name, mode='w') as out:
                write_document(doc, out)
            
        else:
            print('Errors while parsing')
            return False
    return True

def main():
    args = sys.argv[1:]
    if not args:
        print(
            'Usage:python pprint_rdf.py <tag-value-file> <output-file>\n'
            'Pretty print a rdf document.'
        )                   

        sys.exit(1)
    rdf_file = args[0]
    outputfile = args[1]
    success = pprint_rdf(rdf_file, outputfile)
    print(success,' - point 2')
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()