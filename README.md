# doodle repo

### python 3.6

### requirements:
> run ./requirements.sh
```
# run requirement shell script which find & install one depts path requirements.txt

example
├── 20171012
│   ├── git-ls-files.md
│   └── requirements.txt v
├── README.md
├── bear_exporter
│   ├── Untitled.ipynb
│   ├── __pycache__
│   │   ├── custom_fields.cpython-36.pyc
│   │   └── models.cpython-36.pyc
│   ├── custom_fields.py
│   ├── database.sqlite
│   ├── get_query.py
│   ├── models.py
│   ├── requirements.txt v
│   └── test.py
├── gh-issue-slack
├── requirements.sh
└── requirements.txt v (base)

```
# bear exporter
[bear](http://www.bear-writer.com/) is markdown like writing app with tags for crafting notes and prose.
bear exporter can dump out md file with days
### env settings
- env settings
  - PROJECT_ROOT_PATH
  - └ set project root, and bear exporter save md file on {PROJECT_ROOT_PATH}/output_md/*.md)
  - BEAR_DB_PATH
  - └ default is /Users/{username}/Library/Containers/net.shinyfrog.bear/Data/Documents/Application Data/databse.sqlite

```
python ./bear_exporter/bear_exporter.py {days}
or
./md_out.sh {days}

# days default is 1, below command exporting from 1days ago to now
./md_out.sh
#exameple of exporting bear md from 7days ago to now
./md_out.sh 7

```
