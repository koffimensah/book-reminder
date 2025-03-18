# import requests
# import json

# GRAFANA_URL = "http://localhost:3006"
# GRAFANA_USER = "s7koffi"
# GRAFANA_PASSWORD = "Mygrafana"

# headers = {
#     "Content-Type": "application/json"
# }

# # Function to add Prometheus as a data source
# def add_prometheus_datasource():
#     data_source = {
#         "name": "Prometheus",
#         "type": "prometheus",
#         "url": "http://prometheus:9090",
#         "access": "proxy",
#         "isDefault": True
#     }

#     response = requests.post(
#         f"{GRAFANA_URL}/api/datasources",
#         auth=(GRAFANA_USER, GRAFANA_PASSWORD),
#         headers=headers,
#         json=data_source
#     )

#     if response.status_code == 200:
#         print("✅ Prometheus data source added successfully")
#     else:
#         print(f"❌ Failed to add data source: {response.text}")

# # Function to create a sample dashboard
# def create_dashboard():
#     dashboard_payload = {
#         "dashboard": {
#             "id": None,
#             "uid": "sample_dashboard",
#             "title": "Server Metrics",
#             "panels": [
#                 {
#                     "title": "CPU Usage",
#                     "type": "graph",
#                     "targets": [
#                         {
#                             "expr": "rate(node_cpu_seconds_total[5m])",
#                             "legendFormat": "{{cpu}}",
#                             "refId": "A"
#                         }
#                     ],
#                     "gridPos": {"x": 0, "y": 0, "w": 12, "h": 8}
#                 }
#             ],
#             "schemaVersion": 17,
#             "version": 0
#         },
#         "overwrite": True
#     }

#     response = requests.post(
#         f"{GRAFANA_URL}/api/dashboards/db",
#         auth=(GRAFANA_USER, GRAFANA_PASSWORD),
#         headers=headers,
#         json=dashboard_payload
#     )

#     if response.status_code == 200:
#         print("✅ Dashboard created successfully")
#     else:
#         print(f"❌ Failed to create dashboard: {response.text}")

# if __name__ == "__main__":
#     add_prometheus_datasource()
#     create_dashboard()
