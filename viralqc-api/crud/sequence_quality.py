from typing import List, Dict
from uuid import uuid4
from pathlib import Path
from json import load
from importlib.metadata import version
from viralqc.core.run_nextclade import RunNextclade
from viralqc import (
    DATASETS_CONFIG_PATH,
    RUN_NEXTCLADE_SNK_PATH,
)

run_nextclade = RunNextclade()

def _get_tmp_dir_uuid() -> Path:
    tmp_dir = Path("/tmp/vqc") / str(uuid4())
    tmp_dir.mkdir(parents=True, exist_ok=True)
    return tmp_dir

def _save_input_file(sequences: List[Dict], dir: Path) -> Path:
    file_path = dir / "input.fasta"
    with open(file_path, "w") as f:
        for sequence in sequences:
            seq_id = sequence.get("id")
            seq = sequence.get("sequence")
            f.write(f">{seq_id}\n{seq}\n")

    return file_path

def run_sequence_quality_pipeline(sequences: List[Dict]) -> List[Dict]:
    """
    Run viralQC pipeline, return results for each sequence
    as well as information about pipeline.
    """

    results = []

    output_directory = _get_tmp_dir_uuid()
    input_file = _save_input_file(sequences, output_directory)

    snakemake_response = run_nextclade.run(
        snk_file=RUN_NEXTCLADE_SNK_PATH,
        config_file=DATASETS_CONFIG_PATH,
        cores=2,
        sequences_fasta=input_file,
        output_dir=output_directory,
        output_file="results.json",
        datasets_local_path="/usr/local/datasets",
        nextclade_sort_min_score=0.1,
        nextclade_sort_min_hits=10,
        blast_database="/usr/local/datasets/blast.fasta",
        blast_database_metadata="/usr/local/datasets/blast.tsv",
        blast_identity_threshold=0.9,
    )
    if snakemake_response.status == 200:
        with open(f"{output_directory}/results.json", "r") as f:
            results_data = load(f)
        pipeline_name = "viralQC"
        pipeline_version = version("viralQC")
        pipeline_description = "Quality evaluation for viral sequences."
        pipeline_docs_url = "https://github.com/InstitutoTodosPelaSaude/viralQC/wiki"
        exclude = {"index", "seqName"}
        for seq_result in results_data.get("data"):
            result = {
                "id": seq_result.get("seqName"),
                **{k: v for k, v in seq_result.items() if k not in exclude},
                "pipeline_name": pipeline_name,
                "pipeline_version": pipeline_version,
                "pipeline_description": pipeline_description,
                "pipeline_docs_url": pipeline_docs_url,
            }
            results.append(result)
    else:
        raise Exception(snakemake_response.format_log())

    return results

