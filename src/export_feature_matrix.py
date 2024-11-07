# cleans up interim feature matrix

import pandas as pd
from pathlib import Path


def export(df: pd.DataFrame):
    if not df.empty:
        # Save df to interim, to be accessible anywhere
        df.to_csv(Path("results", "interim", "FeatureMatrix.tsv"), sep="\t", index=False)

        # Fill numerical columns with 0
        df[df.select_dtypes(include="number").columns] = df.select_dtypes(
            include="number"
        ).fillna(0)

        # Fill non-numerical columns with ""
        df[df.select_dtypes(exclude="number").columns] = df.select_dtypes(
            exclude="number"
        ).fillna("")

        # Remove individual SIRIUS, CSI and CANOPUS file columns
        df = df.drop(
            columns=[
                c
                for c in df.columns
                if ("_SIRIUS" in c or "_CSI" in c or "_CANOPUS" in c)
            ]
        )

        # Remove columns which contain feature IDs for individual files
        df = df.drop(columns=[c for c in df.columns if c.endswith("_IDs")])

        # Remove "SCANS", "id" and "quality" columns
        df = df.drop(columns=[c for c in ["SCANS", "id", "quality"] if c in df.columns])

        # Move "charge" column to index 3
        charge = df.pop("charge")
        df.insert(3, "charge", charge)

        # Generate a new "metabolite" index, with format f"{mz}@{RT}@{adduct}"
        df.insert(
            0,
            "metabolite",
            df.apply(
                lambda x: f"{round(x['mz'], 5)}@{round(x['RT'], 2)}"
                + (f"@{x['adduct']}" if pd.notnull(x["adduct"]) else ""),
                axis=1,
            ),
        )
        df = df.set_index("metabolite")

        # Rename RT and mz columns
        df = df.rename(columns={"RT": "RT (s)", "mz": "m/z"})

        # Save to top level results directory
        df.to_csv(Path("results", "FeatureMatrix.tsv"), sep="\t")
