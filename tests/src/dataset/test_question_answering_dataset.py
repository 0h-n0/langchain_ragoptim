import pytest

from langchain_ragoptim.dataset.question_answering_dataset import (
    QuestionAnasweringDataset
)


def test_quesiton_answer_file_not_found():
    with pytest.raises(FileNotFoundError):
        qio = QuestionAnasweringDataset(inputfile="test.csv")


def test_simple_question_answer_case(tmp_path, create_simple_test_data_file):
    inputfile = tmp_path / create_simple_test_data_file
    qadataset = QuestionAnasweringDataset(inputfile=inputfile, context=True)
    assert len(qadataset) == 26
    assert qadataset.context == True
    assert qadataset.inputfile == inputfile
    assert qadataset.dataframe.shape == (26, 3)
    assert qadataset.dataframe.columns == ["question", "answer", "context"]
    assert qadataset.dataframe["question"].to_list() == [
        f"{i}-question" for i in "abcdefghijklmnopqrstuvwxyz"
    ]
    assert qadataset.dataframe["answer"].to_list() == [
        f"{i}-answer" for i in "abcdefghijklmnopqrstuvwxyz"
    ]
    assert qadataset.dataframe["context"].to_list() == [
        f"{i}-context" for i in "abcdefghijklmnopqrstuvwxyz"
    ]
    assert qadataset[0] == {
        "question": "a-question",
        "answer": "a-answer",
        "context": "a-context",
    }
