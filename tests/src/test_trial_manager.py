from langchain_ragoptim.trial_manager import TrialManager


def test_simple_trial_manager_read():
    tm = TrialManager()
    tm.run()
