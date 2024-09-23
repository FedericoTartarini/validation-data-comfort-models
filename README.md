# Reference tables to validate thermal comfort models

This repository contains reference data to validate thermal comfort functions. It is currently being used to validate the following tools:

* [pythermalcomfort](https://pythermalcomfort.readthedocs.io/en/latest/)
* [comf](https://cran.r-project.org/web/packages/comf/index.html)
* [CBE Thermal Comfort Tool](https://comfort.cbe.berkeley.edu)

We realsed this cource code under a MIT Licence hence you can freely used this data to validate your functions.

## Check JSON file
When you update a JSON file, please run `check_json_files.py` to check the format of the file. This script ensures that the JSON structure adheres to the expected schema. To run the script, follow these steps:

1. Open a terminal and navigate to the root directory of the repository.
2. Run the following command:

    ```bash
    python check_json_files.py [fill_miss_output]
    ```

3. The script will check all JSON files in the directory and report any format issues.

### `fill_miss_output` Parameter:

- `fill_miss_output` is an optional parameter. When set to `True`, the script will try to use the variables in inputs to call the corresponding method in the pythermalcomfort package by parsing the JSON file name. It will use the return to fill the missing key in outputs, which refers to tolerance.
- By default, `fill_miss_output` is `False`, meaning the script will only check the file format without modifying the files.

#### Example Usage:
- To only check the JSON file format without filling missing outputs:

    ```bash
    python check_scripts/check_json_files.py
    ```

- To check and automatically fill missing outputs:

    ```bash
    python check_scripts/check_json_files.py True
    ```

## File structure

### v1.0.0 - JSON Schema

Data are stored as a JSON file. The JSON schema is describe below:

```yaml
information:
  summary: string, descirbe functions of the file.
  version: string, the version of the file.
  license: "MIT"

tolerance: {}, contains the tolerance value for Specified keys in outputs. The tolerance keys must show in outputs too.
data: [], array
  source: str, indicate the source of test data, optional
  inputs: {}, contains the model inputs
  outputs: {}, contains the validation data
```