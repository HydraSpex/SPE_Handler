import SPE_Handler as SPE

SPE.spectra_from_spe("Testspectra/Testfile_SpectralMap.spe", spectralMap=True, singleSpectra=False, invert=False)
SPE.spectra_from_spe("Testspectra/Testfile_Single_SPE3.spe", spectralMap=False)
SPE.spectra_from_spe("Testspectra/Testfile_Single_SPE2.spe", spectralMap=False)