from traits.api import HasTraits, Str, Int, Float, Button
from traitsui.api import View, Item, Group, CheckListEditor, HGroup, VGroup
# from traitsui.menu import OKButton, CancelButton
# import traitsui
from nucleogenic.deconvolve import DeconvolveNeonIsotopes
from neon_ternary import plot_tern

class Deconvolve(HasTraits):

    Neon_20_Measured = Float
    Neon_21_Measured = Float
    Neon_22_Measured = Float
    system = Str
    mineral = Str
    comp1 = Str
    comp2 = Str
    comp3 = Str
    comp1_20 = Float
    comp1_21 = Float
    comp1_22 = Float
    comp2_20 = Float
    comp2_21 = Float
    comp2_22 = Float
    comp3_20 = Float
    comp3_21 = Float
    comp3_22 = Float

    Neon_20_Measured = 9048
    Neon_21_Measured = 27
    Neon_22_Measured = 925
    system = 'Nucleogenic/Cosmogenic/Air'
    mineral = 'quartz'

    Mass = 1

    Nucleogenic_neon_21_mol = Float
    Nucleogenic_neon_21_ncc = Float
    Nucleogenic_neon_21_Mat = Float
    Cosmogenic_neon_21_mol = Float
    Cosmogenic_neon_21_ncc = Float
    Cosmogenic_neon_21_Mat = Float
    Uranium_ppm = Float
    Thorium_ppm = Float
    Nucl_Age = Float
    Cos_Age = Float

    def _calc_fired(self):
        ne_deconvoluter = DeconvolveNeonIsotopes(self.Neon_20_Measured, self.Neon_21_Measured, self.Neon_22_Measured, self.system, self.mineral)
        ne_results = ne_deconvoluter.deconv_calculate()
        # print(ne_results)
        self.comp1 = self.system.split('/')[0]
        self.comp2 = self.system.split('/')[1]
        self.comp3 = self.system.split('/')[2]
        self.comp1_20 = round(ne_results[0], 5)
        self.comp1_21 = round(ne_results[1], 5)
        self.comp1_22 = round(ne_results[2], 5)
        self.comp2_20 = round(ne_results[3], 5)
        self.comp2_21 = round(ne_results[4], 5)
        self.comp2_22 = round(ne_results[5], 5)
        self.comp3_20 = round(ne_results[6], 5)
        self.comp3_21 = round(ne_results[7], 5)
        self.comp3_22 = round(ne_results[8], 5)

    def _plot_data_fired(self):
        neon_20_frac = float(self.Neon_20_Measured)
        neon_21_frac = float(self.Neon_21_Measured)
        neon_22_frac = float(self.Neon_22_Measured)
        neon_sum = neon_20_frac + neon_21_frac + neon_22_frac
        neon_20_perc = 100*neon_20_frac/neon_sum
        neon_21_perc = 100*neon_21_frac/neon_sum
        neon_22_perc = 100*neon_22_frac/neon_sum
        plot_tern([neon_20_perc, neon_21_perc, neon_22_perc])

    def _transfer_fired(self):
        self.Mass = float(self.Mass)
        for i in (self.comp1, self.comp2, self.comp3):
            if i == 'Nucleogenic':
                self.Nucleogenic_neon_21_mol = self.comp1_21/self.Mass
            if i == 'Cosmogenic':
                self.Cosmogenic_neon_21_mol = self.comp1_21/self.Mass

    calc = Button("Calculate Deconvolution")
    plot_data = Button("Plot")
    transfer = Button("Transfer")
    date_nuc = Button("Calculate Age")
    date_cos = Button("Calculate Age")

    view1 = View(HGroup(
                    VGroup(Item(name='Neon_20_Measured'),
                       Item(name='Neon_21_Measured'),
                       Item(name='Neon_22_Measured'),
                       Item(name='system', editor=CheckListEditor(values=['Nucleogenic/Cosmogenic/Air',
                                                                          'Nucleogenic/Mantle/Air',
                                                                          'Cosmogenic/Mantle/Air'])),
                       Item(name='mineral', editor=CheckListEditor(values=['quartz', 'pyroxene'])),
                       Item('plot_data', name='', show_label=False),
                       Item('calc', name='', show_label=False),
                       VGroup(Item(name='comp1'),
                       HGroup(Item(name='comp1_20'), Item(name='comp1_21'), Item(name='comp1_22')),
                       Item(name='comp2'),
                       HGroup(Item(name='comp2_20'), Item(name='comp2_21'), Item(name='comp2_22')),
                       Item(name='comp3'),
                       HGroup(Item(name='comp3_20'), Item(name='comp3_21'), Item(name='comp3_22')),
                       label='Results', show_border=True),
                       HGroup(Item(name='Mass', label='Mass (mg)'),
                              Item('transfer', label='Transfer to Age Calculator')),
                       label='Neon Isotope Deconvolution',
                       show_border=True),
                       VGroup(
                            VGroup(Item(name='Nucleogenic_neon_21_mol', label='Nucleogenic neon-21 (mol/g)'),
                                   Item(name='Nucleogenic_neon_21_ncc', label='Nucleogenic neon-21 (ncc/g)'),
                                   Item(name='Nucleogenic_neon_21_Mat', label='Nucleogenic neon-21 (Mat/g)'),
                                   Item(name='Uranium_ppm', label='Uranium (ppm)'),
                                   Item(name='Thorium_ppm', label='Thorium (ppm)'),
                                   Item('date_nuc', name='', show_label=False),
                                   VGroup(
                                       Item(name='Nucl_Age', label='Age'),
                                       label='Results', show_border=True),
                                   label='Nucleogenic Neon Age Calculation',
                                   show_border=True),
                            VGroup(Item(name='Cosmogenic_neon_21_mol', label='Cosmogenic neon-21 (mol/g)'),
                                   Item(name='Cosmogenic_neon_21_ncc', label='Cosmogenic neon-21 (ncc/g)'),
                                   Item(name='Cosmogenic_neon_21_Mat', label='Cosmogenic neon-21 (Mat/g)'),
                                   Item('date_cos', name='', show_label=False),
                                   VGroup(
                                       Item(name='Cos_Age', label='Age'),
                                       label='Results', show_border=True),
                                   label='Cosmogenic Neon Age Calculation',
                                   show_border=True)
                       )
                    )
                )


launch = Deconvolve()


launch.configure_traits()
