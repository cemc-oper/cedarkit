# cedarkit

`cedarkit` 是 cedarkit 工具套件的 **meta package**：本身不包含任何代码，
通过依赖将套件中的各个组件包聚合在一起，一次安装即可获得完整的数据处理与可视化工具链。

设计参考 ECMWF 的 [earthkit](https://github.com/ecmwf/earthkit) meta package：
本包发布时不携带任何 Python 模块（`[tool.setuptools] packages = []`），
`cedarkit` 命名空间由组件包（`cedarkit-comp`、`cedarkit-plots`）以 PEP 420
namespace package 的方式提供。

## 组件

| 组件包 | 命名空间 | 说明 |
| --- | --- | --- |
| [reki](https://github.com/cemc-oper/reki) | `reki` | 数据访问与准备（GRIB2/GrADS/NetCDF/CMADaaS），CMA-HPC 本地文件查找 |
| [cedarkit-comp](https://github.com/cemc-oper/cedarkit-comp) | `cedarkit.comp` | 气象计算工具（平滑、网格计算等） |
| [cedarkit-plots](https://github.com/cemc-oper/cedarkit-plots) | `cedarkit.plots` | 绘图组件：Panel、Chart、地图区域、样式、色标 |
| [cedar-graph](https://github.com/cemc-oper/cedar-graph) | `cedar_graph` | 面向 CEMC 数值预报系统的预置图形产品（t_2m、wind_10m、rain_24h 等） |

## 安装

```bash
pip install cedarkit
```

## 使用

```python
import reki
from cedarkit.comp.smooth import smth9
from cedarkit.plots.chart import Panel
from cedar_graph.quickplot import quick_plot
```

## 开发

本 monorepo 中各组件通过 `[tool.uv.sources]` 以本地 editable 路径引用：

```bash
uv pip install -e ".[test]"
pytest
```

版本由 `setuptools_scm` 从 git tag 生成，构建时写入 `cedarkit/_version.py`
（仅用于构建期版本标记，不随包发布）。

## LICENSE

Apache License 2.0
