# tabtree_covert_folder

covert folder trees by tab structure tree

# Sample data

`sample.txt` like:

```text
1
	1.1
		1.1.1
		1.1.2
	1.2
2
	2.1
	2.2
		2.2.1
		2.2.2
		2.2.3
		2.3.4
	2.3
	2.4
3
4
5
	5.1
6
	6.1
```

# Use

```bash
git clone git@github.com:kioipp/tabtree_covert_folder.git
cd tabtree_covert_folder
cp xxxx.txt sample.txt  # COPY your tab-tree datas
python3 converter.py
```

STDOUT will show like:

```bash
$ python3 convert.py
1
1/1.1
1/1.1/1.1.1
1/1.1/1.1.2
1/1.2
2
2/2.1
2/2.2
2/2.2/2.2.1
2/2.2/2.2.2
2/2.2/2.2.3
2/2.2/2.3.4
2/2.3
2/2.4
3
4
5
5/5.1
6
6/6.1
```