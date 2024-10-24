### pyOpenMS: Jupyter Notebook implementation of [UmetaFlow](https://github.com/biosustain/snakemake_UmetaFlow)

#### This is a workflow for untargeted metabolomics data preprocessing and analysis tailored in Jupyter notebooks by [Eftychia Eva Kontou](https://github.com/eeko-kon) and [Axel Walter](https://github.com/axelwalter) using pyOpenMS which are python bindings to the cpp OpenMS alogithms. The workflow is compatible for Linux, Windows and MacOS operating systems.
Publication DOI: https://doi.org/10.1186/s13321-023-00724-w

## Workflow overview

The pipeline consists of seven interconnected steps:

1) [File conversion](1_FileConversion.ipynb) (optional): Simply add your Thermo raw files in `data/raw/` and they will be converted to centroid mzML files. If you have Agilent or Bruker files, skip that step - convert them independently using proteowizard (see https://proteowizard.sourceforge.io/) and add them to the `data/mzML/` directory.

2) [Pre-processing](2_Preprocessing.ipynb): Converting your raw data to a table of metabolic features with a series of algorithms.

3) [Re-quantification](3_Requantification(optional).ipynb): Re-quantify all raw files to avoid missing values resulted by the pre-processing workflow for statistical analysis and data exploration (optional step).

4) [GNPSexport](4_GNPSExport.ipynb): generate all the files necessary to create a [FBMN](https://ccms-ucsd.github.io/GNPSDocumentation/featurebasedmolecularnetworking-with-openms/) or [IIMN](https://ccms-ucsd.github.io/GNPSDocumentation/fbmn-iin/#iimn-networks-with-collapsed-ion-identity-edges) job at GNPS.  

5) Structural and formula predictions with [SIRIUS and CSI:FingerID](5_SIRIUS_CSI.ipynb).

6) [Annotations](6_Annotation.ipynb): annotate the feature tables with #1 ranked SIRIUS and CSI:FingerID predictions (MSI level 3), spectral matches from a local MGF file (MSI level 2).

7) [Data integration](7_FBMN_data_integration.ipynb): Integrate the #1 ranked SIRIUS and CSI:FingerID predictions to the graphml file from GNPS FBMN for visualization. Optionally, annotate the feature tables with GNPS MSMS library matching annotations (MSI level 2).
### Overview
![dag](/images/UmetaFlow_graph.svg)
## Usage
### Step 1: Clone the workflow

[Clone](https://help.github.com/en/articles/cloning-a-repository) this repository to your local system, into the place where you want to perform the data analysis.

(Make sure to have the right access / SSH Key. If **not**, follow the steps:
Step 1: https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

Step 2: https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)


    git clone https://github.com/biosustain/pyOpenMS_UmetaFlow.git

### Step 2: Install all dependencies
> **Mono**, **homebrew** and **wget** dependencies:
>>#### <span style="color: green"> **For Linux only(!)** </span>
>>Install [mono](https://www.mono-project.com/download/stable/#download-lin) with sudo:
>>
>>      sudo apt install mono-devel
>>
>>#### <span style="color: green"> **For both systems** </span>
>>Install homebrew and wget:
>>
>>      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
>>Press enter (RETURN) to continue
>>
>>#### <span style="color: green"> **For Linux only(!)** </span>
>>Follow the Next steps instructions to add Linuxbrew to your PATH and to your bash shell profile script, either ~/.profile on Debian/Ubuntu or ~/.bash_profile on CentOS/Fedora/RedHat (https://github.com/Linuxbrew/brew).
>>
>>      test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
>>      test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
>>      test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile
>>      echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile
>>#### <span style="color: green"> **For both systems** </span>
>>      brew install wget
> **pyOpenMS** and other libraries:
>>
>>Installing pyOpenMS using [conda](https://github.com/conda) is advised:
>>First, create a conda environment and install the wheels and other dependencies. Then get the latest wheels and install all dependencies:
>>
>>        conda create --name pyopenms python=3.10
>>        conda activate pyopenms
>>        pip install pyopenms==3.1
>>        pip install -U numpy==1.26.4
>>        conda install -n pyopenms ipykernel --update-deps --force-reinstall
>>        pip install pyteomics
>>        pip install --upgrade nbformat
>>        pip install matplotlib
>>        conda install sirius-ms==5.8.6
>>
>>For installation details and further documentation, see [pyOpenMS documentation](https://pyopenms.readthedocs.io/en/latest/).
>>
### Step 3: Install executables (ThermoRawFileParser & SIRIUS):
>>**ThermoRawFileParser** 
>>
>>        (cd resources/ThermoRawFileParser && wget https://github.com/compomics/ThermoRawFileParser/releases/download/v1.3.4/ThermoRawFileParser.zip && unzip ThermoRawFileParser.zip)
>>
>>**SIRIUS (if not already installed via conda)**
>>
>>Download the [SIRIUS 5.8.6](https://github.com/sirius-ms/sirius/releases/tag/v5.8.6) executable. Choose the zipped file compatible with your operating system (linux, macOS or windows) and unzip it under the directory `resources/`.  Make sure to register using your university email and password.
>>
>>1. Specify the operating system
>>
>>        MY_OS="linux64" # or "osx64" for macOS or "win64" for windows 
>>
>>2. Get the SIRIUS executable and unpack to resources
>>
>>        cd resources && curl -L -o sirius.zip https://github.com/sirius-ms/sirius/releases/download/v5.8.6/sirius-5.8.6-${MY_OS}.zip && unzip sirius.zip
>>
>>#### <span style="color: red"> **Tip:** </span> If you get the executable manually, make sure to download a version >5.6. Avoid SNAPSHOT versions and get the headless zipped file.
>>
### Step 4 (optional): Get example data from zenodo 
>>
>>        (cd data && wget https://zenodo.org/record/6948449/files/Commercial_std_raw.zip?download=1 && unzip *.zip -d raw)
>>
>>The data can be used for testing the workflow. Otherwise, the user can simply transfer their own data under the directory `data/raw/` or `data/mzML/`.
>>
### Step 5: Run all kernels and investigate the results
>>
>>All the results are in a .TSV format and can be opened simply with excel or using pandas dataframes. 
>>
### Citations

- Kontou, E.E., Walter, A., Alka, O. et al. UmetaFlow: an untargeted metabolomics workflow for high-throughput data processing and analysis. J Cheminform 15, 52 (2023). https://doi.org/10.1186/s13321-023-00724-w

- Pfeuffer J, Sachsenberg T, Alka O, et al. OpenMS – A platform for reproducible analysis of mass spectrometry data. J Biotechnol. 2017;261:142-148. doi:10.1016/j.jbiotec.2017.05.016

- Dührkop K, Fleischauer M, Ludwig M, et al. SIRIUS 4: a rapid tool for turning tandem mass spectra into metabolite structure information. Nat Methods. 2019;16(4):299-302. doi:10.1038/s41592-019-0344-8

- Dührkop K, Shen H, Meusel M, Rousu J, Böcker S. Searching molecular structure databases with tandem mass spectra using CSI:FingerID. Proc Natl Acad Sci. 2015;112(41):12580-12585. doi:10.1073/pnas.1509788112

- Nothias LF, Petras D, Schmid R, et al. Feature-based molecular networking in the GNPS analysis environment. Nat Methods. 2020;17(9):905-908. doi:10.1038/s41592-020-0933-6

### Test Data (only for testing the workflow with the example dataset)
* The current test data are built from known metabolite producer strains or standard samples that have been analysed with a Thermo IDX mass spectrometer. The presence of the metabolites and their fragmentation patterns has been manually confirmed using TOPPView.
