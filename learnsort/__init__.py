# This file tells the python interpreter that this folder and everything in it is a "package".
# Essentially, this is used to tell python how to use the import statment.
# You can look at the test/test_sort.py file to see the import statment.
# You want the import statement because it let's you split your code across several files.

# There is some weirdness with python's import statement. You get used to it, but the basics are:
#   1. Python will try to import relative to wherever you started running Pyton.
#       e.g. Take the statement 'import foo.bar'.  If you started python in C:/projects/, then
#            the interperter will look for foo.bar in C:/projects/foo/bar
#   2. Put an empty __init__.py file in any folder you want to import from. 
