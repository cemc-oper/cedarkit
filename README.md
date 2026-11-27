# cedarkit

![Maturity-Sandbox](https://img.shields.io/badge/Maturity-Sandbox-F9D71C)
![GitHub Release](https://img.shields.io/github/v/release/cemc-oper/cedarkit)
![PyPI - Version](https://img.shields.io/pypi/v/cedarkit)
![GitHub License](https://img.shields.io/github/license/cemc-oper/cedarkit)
![GitHub Action Workflow Status](https://github.com/cemc-oper/cedarkit/actions/workflows/ci.yaml/badge.svg)

`cedarkit` is the meta package for the CEMC meteorological data-processing and
visualization toolkit. Installing it provides the core data-access,
meteorological-computation, and plotting packages as a compatible set.

`cedarkit` itself intentionally ships no Python modules. It exists to provide a
single installation target and a tested dependency set, following the meta-
package model used by [earthkit](https://github.com/ecmwf/earthkit). The
`cedarkit` namespace is supplied by component packages as a PEP 420 namespace
package.

> This project is at the Sandbox maturity level. Component APIs and the
> dependency set may still evolve.

## Included components

| Package | Namespace | Responsibility |
| --- | --- | --- |
| [reki](https://github.com/cemc-oper/reki) | `reki` | Locate, read, query, and process meteorological data, including GRIB2 data in CMADaaS-mounted directories. |
| [cedarkit-comp](https://github.com/cemc-oper/cedarkit-comp) | `cedarkit.comp` | Meteorological computation utilities, such as smoothing and grid calculations. |
| [cedarkit-plots](https://github.com/cemc-oper/cedarkit-plots) | `cedarkit.plots` | Plotting primitives, map domains, styles, colormaps, and declarative plot recipes. |

Together, the components form a simple workflow:

```text
CMADaaS-mounted data → reki → cedarkit.comp → cedarkit.plots → figures
```

Use the components independently when only one layer is needed, or install
this meta package when an application needs the complete toolkit.

## Installation

Python 3.11 or later is required.

```bash
pip install cedarkit
```

The runtime dependencies install `reki`, `cedarkit-comp`, and
`cedarkit-plots`. Reading GRIB2 data requires an ecCodes installation provided
by the target environment.

## Quick check

After installation, the component namespaces should import directly:

```python
import reki

from cedarkit.comp.smooth import smth9
from cedarkit.plots.chart import Panel

print("cedarkit components are available")
```

For CMADaaS-mounted GRIB data, declare a local `reki` source and select by
UTC initialization time and forecast lead.

```python
import reki

with reki.from_source(
    {"kind": "local", "dataset": "cma_gfs_gmf", "root": "/CMADAAS"}
) as source:
    field = source.sel(
        parameter="t2m",
        time="2026-11-02T12:00:00Z",
        step="PT6H",
    ).one()
    t2m = field.to_xarray()["t2m"]
```

The mounted-directory workflow reads local files and does not require CMADaaS
remote-service credentials.

## 2026.11.0 release verification

A clean Python 3.12.3 environment installed the meta package and then the
plotting application from PyPI.

```bash
python -m pip install 'cedarkit==2026.11.0'
python -m pip check
python -m pip install 'cemc-plots-kit==2026.11.0'
python -m pip check
```

The first install resolved `reki 2026.11.0`, `cedarkit-plots 2026.11.0`, and
`cedarkit-comp 2026.7.0`. The second added `cedar-graph 2026.11.0` and
`cemc-plots-kit 2026.11.0`. Both dependency checks passed.

The installed application ran the tagged CMA-GFS temperature task against the
mounted archive. It compiled the v3 recipe, read the 2 m temperature for the
2026-11-02 12 UTC run at +6 h, and wrote a 1193 × 856 PNG.
[CMA-GFS temperature task](https://github.com/cemc-oper/cemc-plots-kit/blob/v2026.11.0/examples/task-v2-gfs-t2m.yaml)

## Development

In this workspace, the three components are configured as local editable
dependencies. Install the meta package and its test extra from this directory:

```bash
cd repo/cedarkit
uv pip install -e ".[test]"
pytest
```

The version is derived from Git tags by `setuptools_scm`. Since this is a meta
package, it has no module-level version file and ships no code of its own.

## License

Copyright &copy; 2021-2026, developers at cemc-oper.

`cedarkit` is licensed under the [Apache License 2.0](LICENSE).
