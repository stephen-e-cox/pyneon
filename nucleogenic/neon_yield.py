import pandas as pd
from cross_section import xsection
from nucleogenic.stopping_power import stoppingpower
import numpy as np
from scipy.integrate import cumtrapz


def yieldcalc(mineral, target, weight_fraction_species, isotopic_fraction_species, molecular_mass_species):

    cross_section = xsection(target)
    min_energy = cross_section[2]
    max_energy = cross_section[3]
    cross_section = pd.DataFrame({'Energy': cross_section[0], 'CrossSection': cross_section[1]})
    cross_section = cross_section.set_index('Energy').squeeze()

    stopping_power = stoppingpower(mineral, min_energy, max_energy)

    common_energies = cross_section.align(stopping_power, join='inner')
    cross_section = common_energies[0]
    stopping_power = common_energies[1]

    quotient = cross_section/stopping_power

    integral = cumtrapz(quotient.values, cross_section.index.astype(np.float64))

    integral = pd.DataFrame(integral, index=cross_section.iloc[1:].index)
    integral.columns = ['Unscaled Yield']

    # Prefactor to scale yield
    F = 10**(-30)  # correction factor for non-SI units
    Na = 6.02214129e23  # Avogadro constant
    X_species = weight_fraction_species  # Mass fraction of target element (O, for example) in material of interest
    X_isotope = isotopic_fraction_species  # Mole fraction of 18O in O, for example (0.002012405 for d18O +6)
    M_species = molecular_mass_species  # Molecular mass of target element
    prefactor = F*(Na/M_species)*X_species*X_isotope

    scaled_yield = integral.multiply(prefactor)

    return scaled_yield