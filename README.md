## Citation
If you find the code useful, please cite:
[1] DOI for that repository: https://doi.org/10.5281/zenodo.4755961
[2] K. Karu, F. Elhi, K. Põhako-Esko, V. Ivaništšev, Predicting Melting Points of Biofriendly Choline-Based Ionic Liquids with Molecular Dynamics, Appl. Sci. 9 (2019) 5367. https://doi.org/10.3390/app9245367.

## Description

Force fields of biofriendly ionic liquid' ions and an example of the melting point estimation workflow.
The example workflow description is in ./example_workflow/README

### Abbreviations

The abbreviations are as follows:
Ace – Acesulfamate
Ac – Acetate
Acs – Acetylsalicylate
Ben – Benzoate
Ch – Choline
Cit – Citrate
Glt – Glutarate
Ibu – Ibuprofenate
Iso – Isobutanoate
Iva – Isovalerate
Lac – Lactate
Mal – Malonate
Mbu – 2-Methylbutanoate
Sac – Saccharinate
Sal – Salicylate
TFSI – bis[(trifluoromethyl)sulfonyl]imide


### Choline cation

Choline force fields are located inside anion folders.
Depending on the counter-ion, the charges are different.

Ch.pdb – ion geometry
ils_nb_Ch.itp – non-bonded interactions and atom types
ils_bon_Ch.itp – bonded interactions
ils_param_Ch.itp – links bonded and non-bonded files together
Ch_0.8samb.itp – molecule definition


### TFSI anion

TFSI.pdb – ion geometry
TFSI_AtTy_OPLSAA.itp – non-bonded interactions and atom types
TFSI.itp – molecule definition and bonded interaction parameters


### Rest of the anions

Anion.pdb – ion geometry
Anion.itp – molecule definition (and some bonded interaction parameters)


### OPLSA-AA atom types

As these force fields use default OPLS-AA atom types, they include parameters defined in:
oplsaa.ff/ffnonbonded.itp
oplsaa.ff/ffbonded.itp
oplsaa.ff/gbsa.itp
