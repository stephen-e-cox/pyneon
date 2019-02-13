from traits.api import HasTraits, Str, Int, Float
import numpy as np

# neon_20 = 3257.9747
# neon_21 = 13.48
# neon_22 = 373.0053


class DeconvolveNeonIsotopes:

    def __init__(self, neon_20_in, neon_21_in, neon_22_in, system, mineral):
        self.neon_20 = float(neon_20_in)
        self.neon_21 = float(neon_21_in)
        self.neon_22 = float(neon_22_in)
        self.system = system
        self.mineral = mineral

    def deconv_calculate(self):

        # print(self.system)
        # print("Input: (", round(self.neon_20, 5), " Ne20) (", round(self.neon_21, 5), " Ne21) (", round(self.neon_22, 5),
        #       " Ne22)")

        comp = []
        comp_name = []
        comp_option = []
        neon_20_22_comp = []
        neon_21_22_comp = []
        neon_22_frac = []
        neon_20_frac = []
        neon_21_frac = []
        neon_22_norm = []
        neon_20_norm = []
        neon_21_norm = []
        neon_22_sig = []
        neon_20_sig = []
        neon_21_sig = []
        comp_results = []

        print(self.system)

        if self.system == 'Nucleogenic/Cosmogenic/Air':
            comp.append(0)
            comp.append(1)
            comp.append(2)
            comp_name.append('Nucleogenic')
            comp_name.append('Cosmogenic')
            comp_name.append('Air')

        elif self.system == 'Nucleogenic/Mantle/Air':
            comp.append(0)
            comp.append(3)
            comp.append(2)
            comp_name.append('Nucleogenic')
            comp_name.append('Mantle')
            comp_name.append('Air')

        else:
            comp.append(1)
            comp.append(3)
            comp.append(2)
            comp_name.append('Cosmogenic')
            comp_name.append('Mantle')
            comp_name.append('Air')

        # nucleogenic
        comp_option.append([.000005, .99999, .000005])

        # cosmogenic (Schaefer et al. 1999)

        if self.mineral == 'quartz':
            # quartz
            comp_option.append([0.355871886, 0.284697509, 0.359430605])
        else:
            # pyroxene
            comp_option.append([0.296735905, 0.326409496, 0.376854599])

        # air
        comp_option.append([.9048, .0027, .0925])

        # mantle (Peron et al 2016)
        comp_option.append([.9259, .0024, .0717])

        for i in range(3):
            comp[i] = comp_option[comp[i]]
            neon_20_22_comp.append(comp[i][0] / comp[i][2])
            neon_21_22_comp.append(comp[i][1] / comp[i][2])

        neon_20_22 = self.neon_20 / self.neon_22
        neon_21_22 = self.neon_21 / self.neon_22

        data_matrix = np.array([[neon_20_22], [neon_21_22], [1]])

        model_matrix = np.array(
            [[neon_20_22_comp[0], neon_20_22_comp[1], neon_20_22_comp[2]], [neon_21_22_comp[0], neon_21_22_comp[1],
                                                                            neon_21_22_comp[2]], [1, 1, 1]])
        inv_model = np.linalg.inv(model_matrix)

        results_matrix = np.matmul(inv_model, data_matrix)

        for i in range(3):
            neon_22_frac.append(results_matrix[i])
            neon_22_norm.append(results_matrix[i] / sum(results_matrix))
            neon_20_frac.append(neon_22_frac[i] * neon_20_22_comp[i])
            neon_21_frac.append(neon_22_frac[i] * neon_21_22_comp[i])

        for i in range(3):
            neon_20_norm.append(neon_20_frac[i] / sum(neon_20_frac))
            neon_21_norm.append(neon_21_frac[i] / sum(neon_21_frac))

            neon_22_sig.append(self.neon_22 * neon_22_norm[i])
            neon_20_sig.append(self.neon_20 * neon_20_norm[i])
            neon_21_sig.append(self.neon_21 * neon_21_norm[i])

            # print(comp_name[i], ": (", round(neon_20_sig[i][0], 5), " Ne20) (", round(neon_21_sig[i][0], 5),
            #           " Ne21) (", round(neon_22_sig[i][0], 5), " Ne22)")
            comp_results.extend([neon_20_sig[i][0], neon_21_sig[i][0], neon_22_sig[i][0]])

        return comp_results
