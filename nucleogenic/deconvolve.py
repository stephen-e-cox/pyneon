from traits.api import HasTraits, Str, Int, Float
import numpy as np

# neon_20 = 3257.9747
# neon_21 = 13.48
# neon_22 = 373.0053


class DeconvolveNeonIsotopes:

    def __init__(self, neon_20_in, neon_21_in, neon_22_in):
        self.neon_20 = neon_20_in
        self.neon_21 = neon_21_in
        self.neon_22 = neon_22_in

    def deconv_calculate(self):

        # air
        # neon_20_comp1 = .9048
        # neon_21_comp1 = .0027
        # neon_22_comp1 = .0925

        neon_20_comp1 = 0.8974400683
        neon_21_comp1 = 0.002762699631
        neon_22_comp1 = 0.09979723206

        neon_20_22_comp1 = neon_20_comp1/neon_22_comp1
        neon_21_22_comp1 = neon_21_comp1/neon_22_comp1

        # cosmo (Niedermann 2002)
        # quartz
        # neon_20_comp2 = 0.4582741396
        # neon_21_comp2 = 0.3666193117
        # neon_22_comp2 = 0.1751065487

        # pyroxene
        neon_20_comp2 = 0.301659125188537
        neon_21_comp2 = 0.324283559577677
        neon_22_comp2 = 0.374057315233786

        neon_20_22_comp2 = neon_20_comp2/neon_22_comp2
        neon_21_22_comp2 = neon_21_comp2/neon_22_comp2

        # nucl
        neon_20_comp3 = .99999
        neon_21_comp3 = .000005
        neon_22_comp3 = .000005

        neon_20_22_comp3 = neon_20_comp3/neon_22_comp3
        neon_21_22_comp3 = neon_21_comp3/neon_22_comp3

        neon_20_22 = self.neon_20/self.neon_22
        neon_21_22 = self.neon_21/self.neon_22

        data_matrix = np.array([[neon_20_22], [neon_21_22], [1]])

        model_matrix = np.array([[neon_20_22_comp1, neon_20_22_comp2, neon_20_22_comp3], [neon_21_22_comp1, neon_21_22_comp2,
                                                                                          neon_21_22_comp3], [1, 1, 1]])
        inv_model = np.linalg.inv(model_matrix)

        results_matrix = np.matmul(inv_model, data_matrix)

        comp1_neon_22_frac = results_matrix[0]
        comp2_neon_22_frac = results_matrix[1]
        comp3_neon_22_frac = results_matrix[2]
        allcomps_neon_22 = comp1_neon_22_frac + comp2_neon_22_frac + comp3_neon_22_frac
        comp1_neon_22_norm = comp1_neon_22_frac/allcomps_neon_22
        comp2_neon_22_norm = comp2_neon_22_frac/allcomps_neon_22
        comp3_neon_22_norm = comp3_neon_22_frac/allcomps_neon_22

        comp1_neon_20_frac = comp1_neon_22_frac*neon_20_22_comp1
        comp2_neon_20_frac = comp2_neon_22_frac*neon_20_22_comp2
        comp3_neon_20_frac = comp3_neon_22_frac*neon_20_22_comp3
        allcomps_neon_20 = comp1_neon_20_frac + comp2_neon_20_frac + comp3_neon_20_frac
        comp1_neon_20_norm = comp1_neon_20_frac/allcomps_neon_20
        comp2_neon_20_norm = comp2_neon_20_frac/allcomps_neon_20
        comp3_neon_20_norm = comp3_neon_20_frac/allcomps_neon_20

        comp1_neon_21_frac = comp1_neon_22_frac*neon_21_22_comp1
        comp2_neon_21_frac = comp2_neon_22_frac*neon_21_22_comp2
        comp3_neon_21_frac = comp3_neon_22_frac*neon_21_22_comp3
        allcomps_neon_21 = comp1_neon_21_frac + comp2_neon_21_frac + comp3_neon_21_frac
        comp1_neon_21_norm = comp1_neon_21_frac/allcomps_neon_21
        comp2_neon_21_norm = comp2_neon_21_frac/allcomps_neon_21
        comp3_neon_21_norm = comp3_neon_21_frac/allcomps_neon_21

        comp1_neon_22_sig = self.neon_22*comp1_neon_22_norm[0]
        comp2_neon_22_sig = self.neon_22*comp2_neon_22_norm[0]
        comp3_neon_22_sig = self.neon_22*comp3_neon_22_norm[0]

        comp1_neon_21_sig = self.neon_21*comp1_neon_21_norm[0]
        comp2_neon_21_sig = self.neon_21*comp2_neon_21_norm[0]
        comp3_neon_21_sig = self.neon_21*comp3_neon_21_norm[0]

        comp1_neon_20_sig = self.neon_20*comp1_neon_20_norm[0]
        comp2_neon_20_sig = self.neon_20*comp2_neon_20_norm[0]
        comp3_neon_20_sig = self.neon_20*comp3_neon_20_norm[0]

        return comp1_neon_20_sig, comp1_neon_21_sig, comp1_neon_22_sig, comp2_neon_20_sig, comp2_neon_21_sig, comp2_neon_22_sig, comp3_neon_20_sig, comp3_neon_21_sig, comp3_neon_22_sig
