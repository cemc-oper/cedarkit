import re

VERSION_RX = re.compile(r"""\d+\.\d+\.*""")


def test_reki_version():
    import reki

    assert VERSION_RX.match(reki.__version__) is not None


def test_cedarkit_comp_version():
    import cedarkit.comp

    assert VERSION_RX.match(cedarkit.comp.__version__) is not None


def test_cedarkit_plots_version():
    import cedarkit.plots

    assert VERSION_RX.match(cedarkit.plots.__version__) is not None
