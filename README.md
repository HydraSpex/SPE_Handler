# SPE_Handler
This Library is for SPE-Files created by LightField 5.3 from Princeton Instruments<br>
It is designed to work with SPE3.0-Files and requires Python 3.

## Installation & Requirements
Just copy the Library (SPE_Handler.py) in your Project Folder.<br>
Requires "struct", "os", "time", "math", normally preinstalled and "matplotlib" and "numpy".

## Supports the major SPE features:
- Read the XML Fileending for important Settings
- Read single Spectra
- Read series Spectra
- Specral Maps
- Convert to txt-File

## Usage
Load the "SPE_Handler" in your Project (as shown is "Test.py") and use the "spectra_from_spe" command to run the plotting of your spectra.
The "spectra_from_spe" command requires only the Filepath of your SPE-File as string, but you have different setting options.
- spectralMap=True -> Plots a SpectralMap of your SPE-File as 3D-Plot
- singleSpectra=True -> Plots every Spectra in your SPE-File as 2D-Plot
- convert=True -> Converts your SPE-File into a TXT-File
- space="tab" -> Uses Tabs as Specers between the Values in the converted TXT-File (other Option is ";")
- header=True -> Activates the header with all the important Settings for the TXT-File
- invert=True -> inverts the TXT-File. If true the X-Values will be left and the single Frames will be as columns, if false the Frames will be in lines
All these settings are True by default.

## Extra
In the repo you will find the "Test.py" Testfile and the "Testspectra" Folder with some Examples for Usage and Testing.
