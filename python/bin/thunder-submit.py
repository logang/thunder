#!/usr/bin/env python

try:
    import thunder
except ImportError:
    thunder = None
    raise Exception("Unable to import Thunder. Please make sure that the Thunder installation directory is listed in " +
                    "the PYTHONPATH environment variable.")

from thunder.utils.launchutils import *


def main():
    SPARK_HOME = getSparkHome()

    from optparse import OptionParser  # use optparse instead of argparse for python2.6 compat
    parser = OptionParser(usage="%prog [submit options] yourapp.py [application arguments]",
                          version=thunder.__version__)
    parser.disable_interspersed_args()  # stop parsing options after first positional arg; pass remaining args to app
    addOptionsToParser(parser, SPARK_HOME)
    opts, args = parser.parse_args()

    childArgs = parseOptionsIntoChildProcessArguments(opts)

    sparkSubmit = os.path.join(SPARK_HOME, 'bin', 'spark-submit')
    childArgs = [sparkSubmit] + childArgs + args

    subprocess.call(childArgs, env=os.environ)

if __name__ == "__main__":
    main()