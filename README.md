## Final project: Nobel laureates

`laureates.json` is a dump of the Nobel Prize API

The notebook parses this file into flat records and analyses it:

1. **Data preparation** - nested json is turned into flat dictionaries
   with configs for people, organizations and prizes
2. **EDA** - number of records, missing values
3. **Own mini-pandas** - filter, group by and aggregations
   (mean, median, min, max, count, top-N)
4. **Analysis** - age of laureates at their first prize and women laureates:

## Structure

```
omd/
├── final-project/
│   ├── laureates_countries_task.ipynb  # notebook with the analysis
│   ├── json_dict_processing.py         # nested json -> flat dict by config
│   ├── prizes_configs.py               # config for prizes
│   ├── laureates_configs.py            # configs for people and organizations
│   ├── eda.py                          # functions for EDA
│   ├── dataset_helpers.py              # filter, group by, aggregation of groups
│   ├── aggregations.py                 # mean, median, min, max, count, top-N
│   ├── atribute_manager.py             # adding and removing fields
│   ├── plots.py                        # bar and line charts
│   └── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- `matplotlib` and `jupyter`

## Build

1. Clone the repository and go to the project directory:

   ```bash
   git clone https://github.com/ploskiy-2/omd.git
   cd omd
   ```

2. Install the dependencies:

   ```bash
   pip install -r final-project/requirements.txt
   ```

3. Put `laureates.json` into the `final-project` folder, next to the notebook.
   Do not rename it

## Run

Start Jupyter from the `final-project` folder

```bash
cd final-project
jupyter notebook laureates_countries_task.ipynb
```

Then restart the kernel and run all cells