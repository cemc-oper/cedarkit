def test_reki_obj():
    from reki.data_finder import find_local_file

    assert callable(find_local_file)


def test_cedarkit_comp_obj():
    from cedarkit.comp.smooth import smth9

    assert callable(smth9)


def test_cedarkit_plots_obj():
    from cedarkit.plots.chart import Panel

    assert callable(Panel)
