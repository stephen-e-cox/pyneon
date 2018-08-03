from traits.api import HasTraits, Str, Int, Float, Button
from traitsui.api import View, Item, Group
# from traitsui.menu import OKButton, CancelButton
# import traitsui
from nucleogenic.deconvolve import DeconvolveNeonIsotopes


class Deconvolve(HasTraits):

    Neon_20_Measured = Float
    Neon_21_Measured = Float
    Neon_22_Measured = Float

    click_counter = Int

    def _calc_fired(self):
        self.click_counter += 1
        ne_deconvoluter = DeconvolveNeonIsotopes(self.Neon_20_Measured, self.Neon_21_Measured, self.Neon_22_Measured)
        ne_results = ne_deconvoluter.deconv_calculate()
        print(ne_results)

    calc = Button("Calculate")

    view1 = View(Group(Item(name='Neon_20_Measured'),
                       Item(name='Neon_21_Measured'),
                       Item(name='Neon_22_Measured'),
                       Item('calc', name=''),
                       Item('click_counter'),
                       label='Neon Isotope Deconvolution',
                       show_border=True))


launch = Deconvolve()


launch.configure_traits()