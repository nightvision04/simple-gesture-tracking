### Installation

##### Requirements
- Anaconda Python >= 3.7
- Mysql

##### OSX

Before running `python setup.py install` on osx, run (takes a while):
```
brew install mysql
```

##### Create a fresh environment and Run

```
conda create --name head python=3.7
conda activate head
# Navigate to the head_controller directory
python setup.py install
```

Then use:

```
python init_db.py
```
