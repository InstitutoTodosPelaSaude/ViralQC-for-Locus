from typing import List, Dict

def run_sequence_quality_pipeline(sequences: List[Dict]) -> List[Dict]:
    """
    Mock implementation of the sequence quality pipeline.
    Returns only mandatory columns for now.
    Additional dynamic columns will be added in the future.
    """

    results = []

    for item in sequences:
        seq_id = item["id"]

        # Mock values (to be replaced when the real pipeline is implemented)
        result = {
            "id": seq_id,
            "pipeline_name": "viralQC-seq-quality",
            "pipeline_version": "1.0.0",
            "pipeline_description": "Mocked quality evaluation for viral sequences.",
            "pipeline_docs_url": "https://docs.viralqc.org/pipeline/seq-quality",
            # Additional fields will be appended here in the future
        }

        results.append(result)

    return results

