#!/usr/bin/python

# This is a reimplementation of the JavaScript minifier included in OpenJFX
# which was derived from the non-free jsmin code by Douglas Crockford. This
# version simply copies the input file unchanged.
#
# -- Emmanuel Bourg <ebourg@apache.org>

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

def jsmin(js):
    ins = StringIO(js)
    outs = StringIO()
    JavascriptMinify().minify(ins, outs)
    return outs.getvalue()

class JavascriptMinify(object):

    def minify(self, instream, outstream):
        outstream.write(instream.read())
        instream.close()

if __name__ == '__main__':
    import sys
    jsm = JavascriptMinify()
    jsm.minify(sys.stdin, sys.stdout)
