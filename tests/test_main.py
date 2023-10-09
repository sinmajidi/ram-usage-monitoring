import sys
sys.path.append('..')
from main import get_memory_info
def test_get_memory_info():
    memory_info = get_memory_info()
    assert isinstance(memory_info, dict)
    assert 'total' in memory_info
    assert 'free' in memory_info
    assert 'used' in memory_info