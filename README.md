# cedarkit

![Maturity-Sandbox](https://img.shields.io/badge/Maturity-Sandbox-F9D71C)
![GitHub Release](https://img.shields.io/github/v/release/cemc-oper/cedarkit)
![PyPI - Version](https://img.shields.io/pypi/v/cedarkit)
![GitHub License](https://img.shields.io/github/license/cemc-oper/cedarkit)
![GitHub Action Workflow Status](https://github.com/cemc-oper/cedarkit/actions/workflows/ci.yaml/badge.svg)

`cedarkit` is the **meta package** of the cedarkit tool suite: it contains no
code itself, but aggregates the component packages of the suite through its
dependencies, so a single installation provides the complete data processing
and visualization toolchain.

The design follows ECMWF's [earthkit](https://github.com/ecmwf/earthkit) meta
package: this distribution ships no Python modules
(`[tool.setuptools] packages = []`). The `cedarkit` namespace is provided by
the component packages (`cedarkit-comp`, `cedarkit-plots`) as PEP 420
namespace packages.

## Components

| Package | Namespace | Description |
| --- | --- | --- |
| [reki](https://github.com/cemc-oper/reki) | `reki` | Data access and preparation (GRIB2/GrADS/NetCDF/CMADaaS), local file finding on CMA-HPC |
| [cedarkit-comp](https://github.com/cemc-oper/cedarkit-comp) | `cedarkit.comp` | Meteorological computation utilities (smoothing, grid calculations, ...) |
| [cedarkit-plots](https://github.com/cemc-oper/cedarkit-plots) | `cedarkit.plots` | Plotting primitives: Panel, Chart, map domains, styles, colormaps |

## Installation

```bash
pip install cedarkit
```

## Usage

```python
import reki
from cedarkit.comp.smooth import smth9
from cedarkit.plots.chart import Panel
```

## Development

In this monorepo, the component packages are referenced as local editable
paths via `[tool.uv.sources]`:

```bash
uv pip install -e ".[test]"
pytest
```

The version is generated from git tags by `setuptools_scm`; this meta package
ships no module-level version file.

## LICENSE

Apache License 2.0
