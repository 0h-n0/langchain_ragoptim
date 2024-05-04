import string

import pytest


@pytest.fixture
def create_simple_test_data_file(tmp_path) -> str:
    outtext = ""
    outtext += f"question,answer,context\n"
    for i in string.ascii_lowercase[:-1]:
        outtext += f"{i}-question,{i}-answer,{i}-context"
        outtext += "\n"
    else:
        outtext += f"z-question,z-answer,z-context"
    filename = "test_question_answer_context.csv"
    with open(tmp_path / filename, "w") as f:
        f.write(outtext)
    return filename
