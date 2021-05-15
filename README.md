# PythonPackage
This repository contains an example for Publishing Python Packages on PyPi. The python module encrypter.py contains the function encrypt_file() which creates an encrypted copy of a file using Fernet (symmetric encryption) in the working directory.
    The function takes a file as main argument and a key_file as optional argument. If no key_file is provided, then a key for the encryption is created using Fernet.generate_key()

### The steps to publish the Package are as follows:
1. Create the python module encrypter.py and locate it in a source directory (src)
2. Create a setup.py script in the same directory containing the src folder
3. Use the command $ python setup.py bdist_wheel 
	This command will create a Wheel to avoid the intermediate step of building the package of the source distribution, i.e. it is a ready-to-install format4. Install it locally: $ pip install -e .
	This will install the package located in the current directory (hence the ".") and the -e flag means it is editable, so any future changes in the code are reflected without having to pip install again, since the package is linked to the code that is in our source directory (it is not copied to the python distribution which will isolate it from any changes)
5. Check that you have a .gitignore (template for Python, including the *.egg-info), add a LICENCE.txt, add the classifiers to the setup.py file, and add a README.md with the documentation
	*Note: The README.md file can be the official documentation of the project by modifying the setup.py (check the long_description variable in the setup.py file)*
6. Add the extras_require to setup.py. It is a dictionary where "dev" key can specify the requirements for further developments or testing of the package 
7. Create test_encrypter.py to test that after decrypting the encrypted file, it is identical to the original ussing assert.
8. Use pytest to execute the test above. ($ pytest)
9. Use $ check-manifest --create because it helps to put all the contents of the folder in the distribution that is created in the next step (e.g. the test_encrypter.py would not be included otherwise)
	if not working, use vim MANIFEST.in and manually add the files to be included
10. Create a source distribution (in case people can't access to the source in github) using $ python setup.py sdist
11. Now that both, the wheel and the distribution of the package are in the dist directory, we use twine to push to PyPI
	$ pip install twine
	$ twine upload dist/*

*Additional information:*

https://packaging.python.org/tutorials/packaging-projects/#classifiers
https://www.youtube.com/watch?v=GIF3LaRqgXo
