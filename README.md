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

    git clone https://github.com/biosustain/pyOpenMS_UmetaFlow.git

### Step 2: Install all dependencies in a conda environment

It is recommended to install all dependencies in a conda environment via the provided `environment.yml` file:

    cd pyOpenMS_UmetaFlow
    conda env create -f environment.yml
    conda activate umetaflow-pyopenms

### Step 3 (optional): Get example data from zenodo 

This data can be used for testing the workflow:

    wget https://zenodo.org/record/6948449/files/Commercial_std_raw.zip -O Commercial_std_raw.zip
    unzip Commercial_std_raw.zip -d Commercial_std_raw
    mv Commercial_std_raw/*.* data/raw/
    rm Commercial_std_raw.zip
    rm -rf Commercial_std_raw

Otherwise, the user can simply transfer their own data under the directory `data/raw/` or `data/mzML/`.

### Step 4: Run all notebooks and investigate the results

Each processing step is implemented in a separate notebook.

    jupyter notebook

All the results are in a .TSV format and can be opened simply with excel or using pandas dataframes.

### Citations

- Kontou, E.E., Walter, A., Alka, O. et al. UmetaFlow: an untargeted metabolomics workflow for high-throughput data processing and analysis. J Cheminform 15, 52 (2023). https://doi.org/10.1186/s13321-023-00724-w

- Pfeuffer J, Sachsenberg T, Alka O, et al. OpenMS – A platform for reproducible analysis of mass spectrometry data. J Biotechnol. 2017;261:142-148. doi:10.1016/j.jbiotec.2017.05.016

- Dührkop K, Fleischauer M, Ludwig M, et al. SIRIUS 4: a rapid tool for turning tandem mass spectra into metabolite structure information. Nat Methods. 2019;16(4):299-302. doi:10.1038/s41592-019-0344-8

- Dührkop K, Shen H, Meusel M, Rousu J, Böcker S. Searching molecular structure databases with tandem mass spectra using CSI:FingerID. Proc Natl Acad Sci. 2015;112(41):12580-12585. doi:10.1073/pnas.1509788112

- Nothias LF, Petras D, Schmid R, et al. Feature-based molecular networking in the GNPS analysis environment. Nat Methods. 2020;17(9):905-908. doi:10.1038/s41592-020-0933-6

### Test Data (only for testing the workflow with the example dataset)
* The current test data are built from known metabolite producer strains or standard samples that have been analysed with a Thermo IDX mass spectrometer. The presence of the metabolites and their fragmentation patterns has been manually confirmed using TOPPView.
