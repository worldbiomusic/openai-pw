##################################################
# Update version of setup.py and setup.cfg first #
##################################################


# remove exist files in dist dir
rm dist/*

# update setup
python setup.py sdist bdist_wheel

# upload to pypi
#twine upload dist/*