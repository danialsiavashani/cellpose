from pathlib import Path

import pytest
from cellpose import io


def test_get_image_files_filters_generated_outputs(tmp_path):
    image_files = ["cell1.png", "cell2.tif", "cell3.tiff"]
    excluded_files = ["cell1_masks.png", "cell2_flows.tif", "notes.txt"]

    for filename in image_files + excluded_files:
        (tmp_path / filename).touch()

    results = io.get_image_files(str(tmp_path), mask_filter="_masks")
    found_names = {Path(filename).name for filename in results}

    assert found_names == set(image_files)


def test_get_image_files_empty_directory(tmp_path):
    with pytest.raises(ValueError):
        io.get_image_files(str(tmp_path), mask_filter="_masks")