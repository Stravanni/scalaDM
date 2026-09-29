# Lab on SkipLists and HNSW

## Part 0: setup 
**Clone** the course repository or update it:
```
git clone https://github.com/Stravanni/scalaDM.git
```

or 
```
git pull https://github.com/Stravanni/scalaDM.git
```

in case of conflicts with previous changes, *stash* your changes; once the repo is updated, you can *pop* or *apply* them again.


**Change** working directory to lab/skiplist_hnsw (this folder), so your editor knows that you are working right here and not somewhere else:
```
cd lab/skiplist_hnsw
```

**Install** the required packages: ideally, you can use a nice package manager like [uv](https://docs.astral.sh/uv/getting-started/installation/#installing-uv) (best choice!) but you can use also the simplest pip.

We need to create a dedicated environement to run the code. With **uv** it is as simple as:
```
uv sync
uv pip install -e .     # just if you want to use a visualization tool
```

or with *venv+pip*:
```
# create the virtual environment
python3 -m venv .venv

# on *nux (check for the path)
source .venv/bin/activate

# on Windows (check for the path)
.venv\Scripts\activate

# install the packages
pip install -r requirements.txt

# install the project in editable mode
pip install -e .     # just if you want to use a visualization tool
```

Create the **data directory** mainly for Part 2. On *nix CLI:
```
mkdir data
```

Only if you are interested in larger experiments, you can copy the pre-built indexes for Part 2 at https://drive.google.com/file/d/1xXyaGlkfjkkSZh1xia6DxXmm2nx0tNsE/view?usp=sharing or recreate them (see notebooks)


## Part 1: SkipList implementation

In `tinyhnsw/teaching/skip_list_exercise.py` there is the partial implementation of a Skip List data structure for the first part of the lab.

Complete implementation will be uploaded later.

## Part 2: HNSW

In `notebooks/hnsw_exercise.ipynb` there is a Jupyter Notebook containing the second part of the lab:

1. Visualization of HNSW layers with *tinyhnsw* tools;
2. HNSW parameters exploration with pre-built indexes on [SIFT1M](http://corpus-texmex.irisa.fr/)
3. Filter movie embeddings based on their genre