# SPE_Handler
This library is for SPE-Files created by LightField 5.3 from Princeton Instruments<br>
It is designed to work with SPE2.x and SPE3.0-Files and requires Python 3.

## Installation & Requirements
Just copy the library (SPE_Handler.py) in your project folder.<br>
Requires "struct", "os", "time", "math", normally preinstalled and "matplotlib" and "numpy".

## Supports the major SPE features:
- Read the XML-Fileending for important settings
- Read single spectra
- Read series spectra
- SpecralMaps
- Convert to TXT-File

## Usage
Load the "SPE_Handler" in your project (as shown is "Test.py") and use the "spectra_from_spe" command to run the plotting of your spectra, or the "convert_txt" command to convert the SPE-File to a TXT-File<br>

<b>"spectra_from_spe"-Command</b><br>
The "spectra_from_spe" command requires only the filepath of your SPE-File as string, but you have different setting options:<br>
- spectralMap=True -> Plots a SpectralMap of your SPE-File as 3D-Plot
- singleSpectra=True -> Plots every spectra in your SPE-File as 2D-Plot
- convert=True -> Converts your SPE-File into a TXT-File
- space="tab" -> Uses Tabs as spacers between the values in the converted TXT-File (other Option is ";")
- header=True -> Activates the header with all the important settings for the TXT-File
- invert=True -> inverts the TXT-File. If true the X-Values will be left and the single frames will be as columns, if false the frames will be in lines
- name_stays=True -> TXT-File will be named after the original file, otherwise it will be named SpectraNew.txt

All these settings are true by default.<br><br>

<b>"convert_txt"-Command</b><br>
You can also use only the "convert_txt" command. It requires the filepath of you SPE-File and the folder where to create the new TXT-File, but you have different setting options:<br>
- space="tab" -> Uses Tabs as spacers between the values in the converted TXT-File (other Option is ";")
- header=True -> Activates the header with all the important settings for the TXT-File
- invert=False -> inverts the TXT-File. If true the X-Values will be left and the single frames will be as columns, if false the frames will be in lines

All these settings are true by default.<br><br>

**"multiple_spectra"-Command**  
The function converts multiple .spe Files into one large .csv File. The columns are named after the individual Files
* FolderName (str): Path to Folder, inside the Folder should be the .spe-Files and no other Files.

## Extra
In the repo you will find the "Test.py" Testfile and the "Testspectra" Folder with some Examples for Usage and Testing.
