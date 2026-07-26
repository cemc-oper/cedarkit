def test_reki_obj():
    import reki

    assert callable(reki.from_source)


def test_cedarkit_comp_obj():
    from cedarkit.comp.smooth import smth9

    assert callable(smth9)


def test_cedarkit_plots_obj():
    from cedarkit.plots.chart import Panel

    assert callable(Panel)
