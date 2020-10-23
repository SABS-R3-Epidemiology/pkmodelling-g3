"""
Tests the :class:`Visualisation` module.
"""

import unittest
from unittest.mock import patch
from pkmodel import Model, Protocol
import pkmodel.visualisation as pkv


class VisualisationTest(unittest.TestCase):
    @patch("%s.pkv.plt" % __name__)
    def test_one_plot(self, mock_plt):
        pkv.plot_behaviour_one_experiment(Model(0, 1, [1], [0], 1), Protocol('intravenous', 'instantaneous', [5],  T=[10]), 10, 10)   # noqa

        # Assert plt.figure is called once
        mock_plt.figure.assert_called_once()

    @patch("%s.pkv.plt" % __name__)
    def test_two_plots(self, mock_plt):
        pkv.plot_comparison_experiments([Model(0, 1, [1], [0], 1), Model(0, 1, [1], [0], 1)], [Protocol('intravenous', 'instantaneous', [5],  T=[10]), Protocol('subcutaneous', 'continuous', 7, T=[10], absorption_rate=0.7)], 10, 10)  # noqa

        # Assert plt.figure is called once
        mock_plt.figure.assert_called_once()
