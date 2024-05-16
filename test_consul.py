import pytest
import requests

@pytest.mark.parametrize("path", ["v1/agent/self"])
class TestMembers:
    @pytest.mark.parametrize("ip_node", [
        "10.0.2.9",
        "10.0.2.10",
        "10.0.2.11",
        "10.0.2.12"
    ])
    def test_status(self, path, ip_node):
        response = requests.get(f"http://{ip_node}:8500/{path}")
        response_json = response.json()
        assert response_json['Member']['Status'] == 1

    @pytest.mark.parametrize("ip_node", [
        "10.0.2.9",
        "10.0.2.10",
        "10.0.2.11",
        "10.0.2.12"
    ])
    def test_version(self, path, ip_node):
        response = requests.get(f"http://{ip_node}:8500/{path}")
        response_json = response.json()
        assert response_json['Config']['Version'] == "1.18.1"

    @pytest.mark.parametrize("ip_node, type", [
        ("10.0.2.9", "server"),
        ("10.0.2.10", "server"),
        ("10.0.2.11", "server"),
        ("10.0.2.12", "client")
    ])
    def test_type(self, path, ip_node, type):
        response = requests.get(f"http://{ip_node}:8500/{path}")
        response_json = response.json()
        type = True if type == "server" else False
        assert response_json['Config']['Server'] == type