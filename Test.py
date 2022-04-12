import SPE_Handler as SPE

SPE.spectra_from_spe("Testspectra/Testfile_SpectralMap.spe", invert=False, singleSpectra=False)
SPE.spectra_from_spe("Testspectra/Testfile_Single.spe", spectralMap=False)