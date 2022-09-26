### pyOpenMS_untargeted_metabolomics

##### This is the progress of a pyOpenMS workflow in a Jupyter notebook for untargeted metabolomics data preprocessing and analysis tailored by [Eftychia Eva Kontou](https://github.com/eeko-kon) and [Axel Walter](https://github.com/axelwalter) using OpenMS and pyOpenMS which are python bindings to the cpp OpenMS alogithms. 

## Workflow overview

The pipeline consists of seven interconnected steps:

1) [File conversion](1_FileConversion.ipynb) (optional): Simply add your Thermo raw files in data/raw/ and they will be converted to centroid mzML files. If you have Agilent or Bruker files, skip that step - convert them independently using proteowizard (see https://proteowizard.sourceforge.io/) and add them to the data/mzML/ directory.

2) [Pre-processing](2_Preprocessing.ipynb): Converting your raw data to a table of metabolic features with a series of algorithms.

3) [Re-quantification](3_Requantification(optional).ipynb): Re-quantify all raw files to avoid missing values resulted by the pre-processing workflow for statistical analysis and data exploration (optional step)

4) [GNPSexport](4_GNPSExport.ipynb): generate all the files necessary to create a [FBMN](https://ccms-ucsd.github.io/GNPSDocumentation/featurebasedmolecularnetworking-with-openms/) or [IIMN](https://ccms-ucsd.github.io/GNPSDocumentation/fbmn-iin/#iimn-networks-with-collapsed-ion-identity-edges) job at GNPS.  

5) Structural and formula predictions with [SIRIUS and CSI:FingerID](5_SIRIUS_CSI.ipynb)

6) [Annotations](6_Annotation.ipynb): annotate the feature tables with #1 ranked SIRIUS and CSI:FingerID predictions (MSI level 3), spectral matches from a local MGF file (MSI level 2).

7) [Data integration](7_FBMN_data_integration.ipynb): Integrate the #1 ranked SIRIUS and CSI:FingerID predictions to the graphml file from GNPS FBMN for visualization. Optionally, annotate the feature tables with GNPS MSMS library matching annotations (MSI level 2).

![dag](/images/UmetaFlow_graph.svg)


## Usage
### Step 1: Clone the workflow

[Clone](https://help.github.com/en/articles/cloning-a-repository) this repository to your local system, into the place where you want to perform the data analysis.

(Make sure to have the right access / SSH Key. If **not**, follow the steps:
Step 1: https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

Step 2: https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)


    git clone https://github.com/eeko-kon/pyOpenMS_UmetaFlow.git

### Step 2: Create a conda environment& install pyopenms
    
Installing pyOpenMS using [conda](https://github.com/conda) is advised:
First, get the latest wheels:

    MY_OS="Linux" # or "macOS" or "Windows" (case-sensitive)
    wget https://nightly.link/OpenMS/OpenMS/workflows/pyopenms-wheels/nightly/${MY_OS}-wheels.zip\?status\=completed
    mv ${MY_OS}-wheels.zip\?status=completed ${MY_OS}-wheels.zip
    unzip *.zip

Then, create a conda environment and install the wheels and other dependencies:

    conda create --name pyopenms python=3.10
    conda activate pyopenms
    pip install *cp310*.whl
    rm *.zip & rm *.whl
    conda install -n pyopenms ipykernel --update-deps --force-reinstall
    conda install -c bioconda sirius-csifingerid
    pip install pyteomics
    pip install --upgrade nbformat
    pip install matplotlib

For installation details and further documentation, see: [pyOpenMS documentation](https://pyopenms.readthedocs.io/en/latest/).

#### For Linux only !

Install [mono](https://www.mono-project.com/download/stable/#download-lin) with sudo:

    sudo apt install mono-devel

#### For both systems

Install homebrew and wget (for **iOS** only!):

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
Press enter (RETURN) to continue 

#### For Linux only !

Follow the Next steps instructions to add Linuxbrew to your PATH and to your bash shell profile script, either ~/.profile on Debian/Ubuntu or ~/.bash_profile on CentOS/Fedora/RedHat (https://github.com/Linuxbrew/brew).

    test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
    test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
    test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile
    echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile

#### For both systems

    brew install wget

### Step 3: Retrieve files (optional) and executables (not optional)

#### Get example data from zenodo (only for testing the workflow with the example dataset) or simply transfer your own data under the directory "data/raw/"

(cd data && wget https://zenodo.org/record/6948449/files/Commercial_std_raw.zip?download=1 && unzip *.zip -d raw)

#### Get the necessary executables (ThermoRawFileParser & Sirius):

    (cd resources/ThermoRawFileParser && wget https://github.com/compomics/ThermoRawFileParser/releases/download/v1.3.4/ThermoRawFileParser.zip && unzip ThermoRawFileParser.zip)

### Step 5: Run all kernels and investigate the results

All the results are in a tsv format and can be opened simply with excel or using pandas dataframes. 


### Citations

Pfeuffer J, Sachsenberg T, Alka O, et al. OpenMS – A platform for reproducible analysis of mass spectrometry data. J Biotechnol. 2017;261:142-148. doi:10.1016/j.jbiotec.2017.05.016

Dührkop K, Fleischauer M, Ludwig M, et al. SIRIUS 4: a rapid tool for turning tandem mass spectra into metabolite structure information. Nat Methods. 2019;16(4):299-302. doi:10.1038/s41592-019-0344-8

Dührkop K, Shen H, Meusel M, Rousu J, Böcker S. Searching molecular structure databases with tandem mass spectra using CSI:FingerID. Proc Natl Acad Sci. 2015;112(41):12580-12585. doi:10.1073/pnas.1509788112

Nothias LF, Petras D, Schmid R, et al. Feature-based molecular networking in the GNPS analysis environment. Nat Methods. 2020;17(9):905-908. doi:10.1038/s41592-020-0933-6

### Test Data (only for testing the workflow with the example dataset)
* Current test data are built from known metabolite producer strains or standard samples that have been analysed with a Thermo IDX mass spectrometer. The presence of the metabolites and their fragmentation patterns has been manually confirmed using TOPPView.
