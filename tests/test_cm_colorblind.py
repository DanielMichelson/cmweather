""" Unit Tests for cmweather's cm_colorblind.py module. """


import matplotlib

from cmweather import cm_colorblind


def test_colormaps_exist():
    assert isinstance(cm_colorblind.HomeyerRainbow, matplotlib.colors.Colormap)
    assert isinstance(cm_colorblind.HomeyerRainbow_r, matplotlib.colors.Colormap)
    assert isinstance(cm_colorblind.balance, matplotlib.colors.Colormap)
    assert isinstance(cm_colorblind.balance_r, matplotlib.colors.Colormap)
    assert isinstance(cm_colorblind.ChaseSpectral, matplotlib.colors.Colormap)
    assert isinstance(cm_colorblind.ChaseSpectral_r, matplotlib.colors.Colormap)
    assert isinstance(cm_colorblind.SpectralExtended, matplotlib.colors.Colormap)
    assert isinstance(cm_colorblind.SpectralExtended_r, matplotlib.colors.Colormap)


def test_colormaps_registered():
    cmap = matplotlib.colormaps.get_cmap('HomeyerRainbow')
    assert isinstance(cmap, matplotlib.colors.Colormap)

    cmap = matplotlib.colormaps.get_cmap('HomeyerRainbow_r')
    assert isinstance(cmap, matplotlib.colors.Colormap)

    cmap = matplotlib.colormaps.get_cmap('balance')
    assert isinstance(cmap, matplotlib.colors.Colormap)

    cmap = matplotlib.colormaps.get_cmap('balance_r')
    assert isinstance(cmap, matplotlib.colors.Colormap)

    cmap = matplotlib.colormaps.get_cmap('ChaseSpectral')
    assert isinstance(cmap, matplotlib.colors.Colormap)

    cmap = matplotlib.colormaps.get_cmap('ChaseSpectral_r')
    assert isinstance(cmap, matplotlib.colors.Colormap)

    cmap = matplotlib.colormaps.get_cmap('SpectralExtended')
    assert isinstance(cmap, matplotlib.colors.Colormap)

    cmap = matplotlib.colormaps.get_cmap('SpectralExtended_r')
    assert isinstance(cmap, matplotlib.colors.Colormap)
