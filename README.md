# Reference tables to validate thermal comfort models

This repository contains reference data to validate thermal comfort functions. It is currently being used to validate the following tools:

* [pythermalcomfort](https://pythermalcomfort.readthedocs.io/en/latest/)
* [comf](https://cran.r-project.org/web/packages/comf/index.html)
* [CBE Thermal Comfort Tool](https://comfort.cbe.berkeley.edu)

We realsed this cource code under a MIT Licence hence you can freely used this data to validate your functions.

## Versioning

Releases are tagged (e.g. `v1.0.0`) and documented in [CHANGELOG.md](CHANGELOG.md).
Downstream projects should pin fixture URLs to a tag rather than `main` — a
fixture change here can otherwise silently affect another repository's CI
before anyone reviews it.

### Version numbering (SemVer)

Tags follow `vMAJOR.MINOR.PATCH`:

- **PATCH** (`v1.0.0` → `v1.0.1`): a fixture was corrected without changing
  its meaning — a wrong reference value, a mislabeled boundary-test case, a
  fixed typo. Existing consumers should be able to bump straight to it.
- **MINOR** (`v1.0.0` → `v1.1.0`): a new JSON file was added, or new test
  cases were added to an existing file, in a backwards-compatible way (i.e.
  nothing existing was removed or renamed). Consumers not yet using the new
  data are unaffected.
- **MAJOR** (`v1.0.0` → `v2.0.0`): a breaking change — a key was renamed or
  removed (e.g. the `sweat_rate_gram` → `sweat_loss_g` rename), the JSON
  schema itself changed, or a file was renamed/deleted. Consumers must
  update their code, not just bump the pin, when picking this up.

When unsure which applies, prefer the smaller bump only if you're confident
no consumer's assertions would need to change to keep passing; otherwise
treat it as breaking.

### How to cut a release

1. Merge the change(s) into `main` as usual.
2. Add an entry under `## [Unreleased]` in `CHANGELOG.md` as you go (or before
   tagging, if it was missed) describing what changed and why — not just
   which file, but what a consumer needs to know before bumping their pin.
3. Decide the version bump (see above) and move the `[Unreleased]` entries
   under a new `## [X.Y.Z] - YYYY-MM-DD` heading.
4. Commit the changelog update:

    ```bash
    git add CHANGELOG.md
    git commit -m "docs(changelog): release vX.Y.Z"
    ```

5. Tag and push:

    ```bash
    git tag -a vX.Y.Z -m "vX.Y.Z: <one-line summary>"
    git push origin main --follow-tags
    ```

6. Let known consumers (e.g. `pythermalcomfort`) know a new tag exists —
   ideally by opening a PR/issue there bumping the pin — so nobody keeps
   running against an old tag once a newer one is available.

## Check JSON file
When you update a JSON file, please run `check_json_files.py` to check the format of the file. This script ensures that the JSON structure adheres to the expected schema. To run the script, follow these steps:

1. Open a terminal and navigate to the root directory of the repository.
2. Run the following command:

    ```bash
    python check_json_files.py [fill_miss_output]
    ```

3. The script will check all JSON files in the directory and report any format issues.

### `fill_miss_output` Parameter:

- `fill_miss_output` is an optional parameter. When set to `True`, the script will try to use the variables in `inputs` to call the corresponding method in the pythermalcomfort package by parsing the JSON file name(Take the string between ts_ and .json). It will use the return to fill the missing key in `outputs`, which refers to `tolerance`.
- By default, `fill_miss_output` is `False`, meaning the script will only check the file format without modifying the files.

#### Example Usage:
- To only check the JSON file format without filling missing outputs:

    ```bash
    python check_json_files.py
    ```

- To check and automatically fill missing outputs:

    ```bash
    python check_json_files.py True
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