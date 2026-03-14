from text_processor import format_as_slug

def test_slug_formatting():
    assert format_as_slug('Patch Pilot Agent') == 'patch-pilot-agent'
