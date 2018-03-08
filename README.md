### ASK
* In the programming language of your choice create a class with a method to return the length and longest words in a sentence. For example, “The cow jumped over the moon.” should return 6 and “jumped”.
* Create unit tests to test that method, reworking your code if needed.

### Instructions
This project is compatible with **[python v 3.6](https://www.python.org/downloads/)+**.
This current installation assumes an osx/linux environment

#### setup
For MacOSX, you can use [homebrew](http://brew.sh/) to install [git](https://git-scm.com/), [python v 3.6](https://www.python.org/downloads/)
Then, run the following command to install python3, git, and chromedriver to your machine:
```
brew install git python3
``` 
On your machine, make a directory for your python projects if you've not already and clone the project:
```
mkdir python_projects; cd python_projects

git clone https://github.com/rronakk/word/

cd {your_clone_directory_name}
```
#### Running unit tests
Tests are written using python unittest framework.
So running tests is simple as running the test file.
Do, once you are in your project directory
```
python3 sentence_test.py 
```