# LatticePlane
Calculate atomic lattice plane densities in arbitrary crystal structures (CIF input) for arbitrary lattice planes (HKL indices).

## Installation
The following instructions are adapted from https://mathematica.stackexchange.com/a/672/61736.
1. Open `LatticePlane.m` in Mathematica
1. Choose `File` --> `Install...`
1. Choose `Type` --> `Package, Source` --> (the open notebook), `Install Name` --> `LatticePlane`
1. Load the package by evaluating (including the `<<`):
```mathematica
<<LatticePlane`
```

Ensure the name is not mispelled (including capitalization).

The `Install...` menu item will put the package into `FileNameJoin[{$UserBaseDirectory, "Applications"}]` which on Windows is `%AppData%\Mathematica\Applications`.

To test that it has installed correctly, open the documentation via:
```mathematica
?LatticePlane
```

## Usage
### Loading CIF Files
CIF files are loaded using a slightly modified version of [MaXrd](https://github.com/Stianpr20/MaXrd) `ImportCrystalData[]` named `ImportCrystalData2[]`. The first argument to `ImportCrystalData2` is the path to the CIF file (without the `.cif` extension), and the second argument is a key that will be used to access data relating to the compound.

### Computing Densities
The primary functionality of `LatticePlane` is contained in `DensityHKL[]`, which can be used as follows:
```mathematica
{Aoutn, AoutCt, hkl, Afulln, AfullCt, hklFull, elem}=DensityHKL[mpid,n,hklMax,radiusFactorIn];
```
where `mpid` is the Materials Project ID or other key for a CIF file assigned via `ImportCrystalData2`, `n` is the supercell size, `hklMax` is the maximum HKL index to consider, and `radiusFactorIn` is the maximum distance between the HKL plane of interest and each atom in the compound that is allowed for an atom to be considered in the intersection scheme. `Aoutn` contains the area of each element in a particular plane normalized by the radius of that atom for the unique HKL planes. `AoutCt` contains the total number of atoms (fractional values OK) of an element within a plane for the unique HKL planes. `hkl` is a list of the unique HKL planes. `Afulln`, `AfullCt`, and `hklFull` consider the degenerate HKL planes as well. Finally, `elem` is the list of unique elements.

## Plotting
To reproduce the plots from [the paper](https://doi.org/10.33774/chemrxiv-2021-l9rp7) such as the following (annotations added manually), see `PlotSymmetrizedFullHKL[]` which uses several of the outputs from `DensityHKl[]`.
![fe3c-ex](https://user-images.githubusercontent.com/45469701/147862349-365bc634-7db6-44fa-bc9e-2d1a9a0dd1dc.png)


## Examples
Please refer to `LatticePlane-example.nb`. A high-throughput calculation workflow and machine learning application is given in `ml-test.nb`.
