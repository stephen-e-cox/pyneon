import numpy as np

neon_20 = 185235
neon_21 = 618
neon_22 = 104580

# air
neon_20_comp1 = .9048
neon_21_comp1 = .0027
neon_22_comp1 = .0925

neon_20_22_comp1 = neon_20_comp1/neon_22_comp1
neon_21_22_comp1 = neon_21_comp1/neon_22_comp1

# cosmo
neon_20_comp2 = 0.4582741396
neon_21_comp2 = 0.3666193117
neon_22_comp2 = 0.1751065487

neon_20_22_comp2 = neon_20_comp2/neon_22_comp2
neon_21_22_comp2 = neon_21_comp2/neon_22_comp2

# nucl
neon_20_comp3 = 0
neon_21_comp3 = 0
neon_22_comp3 = 1

neon_20_22_comp3 = neon_20_comp3/neon_22_comp3
neon_21_22_comp3 = neon_21_comp3/neon_22_comp3

neon_20_22 = neon_20/neon_22
neon_21_22 = neon_21/neon_22

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

comp1_neon_22_sig = neon_22*comp1_neon_22_norm
comp2_neon_22_sig = neon_22*comp2_neon_22_norm
comp3_neon_22_sig = neon_22*comp3_neon_22_norm

comp1_neon_21_sig = neon_21*comp1_neon_21_norm
comp2_neon_21_sig = neon_21*comp2_neon_21_norm
comp3_neon_21_sig = neon_21*comp3_neon_21_norm

comp1_neon_20_sig = neon_20*comp1_neon_20_norm
comp2_neon_20_sig = neon_20*comp2_neon_20_norm
comp3_neon_20_sig = neon_20*comp3_neon_20_norm

print(comp1_neon_20_sig, comp1_neon_21_sig, comp1_neon_22_sig, comp3_neon_20_sig, comp2_neon_21_sig, comp2_neon_22_sig, comp3_neon_20_sig, comp3_neon_21_sig, comp3_neon_22_sig)
