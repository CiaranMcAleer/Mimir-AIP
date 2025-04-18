import pytest
import os
from Plugins.Output.HTMLReport.HTMLReport import HTMLReport

def test_html_report_initialization():
    """Test HTMLReport plugin initialization"""
    plugin = HTMLReport()
    assert isinstance(plugin, HTMLReport)

def test_html_report_generate():
    """Test generating HTML report with sample data"""
    plugin = HTMLReport()
    
    # Test with sample report data
    config = {
        "title": "Sample Report",
        "sections": "[{'heading': 'Introduction', 'text': 'This is a sample report generated by the HTMLReport plugin.'}, {'heading': 'Data Analysis', 'text': 'Here we present the analysis of the collected data.'}]",
        "output_dir": "reports"
    }
    
    result = plugin.execute_pipeline_step({
        "config": config,
        "output": "report.html"
    }, {})
    
    assert "report.html" in result
    assert isinstance(result["report.html"], str)
    
    # Verify the file exists
    assert os.path.exists(result["report.html"])
    
    # Read the file content
    with open(result["report.html"], "r") as f:
        html_content = f.read()
        assert "<title>Sample Report</title>" in html_content
        assert "<h2>Introduction</h2>" in html_content
        assert "<h2>Data Analysis</h2>" in html_content
        assert "This is a sample report generated by the HTMLReport plugin." in html_content
        assert "Here we present the analysis of the collected data." in html_content
