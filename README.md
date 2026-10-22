# omd

Python homework for the AAA course.

## Function task

`Corp_Summary.csv` is an export of employees: full name, department, team,
position, rating and salary, separated by `;`.

`main.py` reads this file and builds one of three reports, depending on the
number you choose:

1. **Hierarchy** — which teams each department has
2. **Department summary** — headcount and the minimum, maximum and average
   salary for every department
3. **The same summary, saved to a file** — written to `Output.csv`

## Structure

```
omd/
├── function/
│   ├── main.py
│   └── Corp_Summary.csv
├── .gitignore
└── README.md
```

## Requirements

- Python **3.12 or newer**

## Build

Clone the repository and go to the project directory:

```bash
git clone https://github.com/ploskiy-2/omd.git
cd omd
```

## Run

Run the script from the `function` folder

```bash
cd function
python3 main.py
```

The script asks for a report number: type `1`, `2` or `3`
Any other number ends with an error message