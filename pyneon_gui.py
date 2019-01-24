from traits.api import HasTraits, Str, Int, Float, Button
from traitsui.api import View, Item, Group, CheckListEditor
# from traitsui.menu import OKButton, CancelButton
# import traitsui
from nucleogenic.deconvolve import DeconvolveNeonIsotopes


class Deconvolve(HasTraits):

    Neon_20_Measured = Float
    Neon_21_Measured = Float
    Neon_22_Measured = Float
    system = Str
    mineral = Str

    Neon_20_Measured = 9048
    Neon_21_Measured = 27
    Neon_22_Measured = 925
    system = 'Nucleogenic/Cosmogenic/Air'
    mineral = 'quartz'

    def _calc_fired(self):
        self.click_counter += 1
        ne_deconvoluter = DeconvolveNeonIsotopes(self.Neon_20_Measured, self.Neon_21_Measured, self.Neon_22_Measured, self.system, self.mineral)
        ne_results = ne_deconvoluter.deconv_calculate()
        print(ne_results)

    calc = Button("Calculate")

    view1 = View(Group(Item(name='Neon_20_Measured'),
                       Item(name='Neon_21_Measured'),
                       Item(name='Neon_22_Measured'),
                       Item(name='system', editor=CheckListEditor(values=['Nucleogenic/Cosmogenic/Air', 'Nucleogenic/Mantle/Air', 'Cosmogenic/Mantle/Air'])),
                       Item(name='mineral', editor=CheckListEditor(values=['quartz', 'pyroxene'])),
                       Item('calc', name=''),
                       label='Neon Isotope Deconvolution',
                       show_border=True))


launch = Deconvolve()


launch.configure_traits()