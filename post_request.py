import requests
import json
payload=json.dumps({"type":"kdm","params":{"from":"2018-05-16T21:03:00","to":"2018-05-19T21:04:00","filter":{"composition":["Kalari-v4_1-24_SHR_S_EN-XX_51_48_ST_20130509_FAC_i3D-ngb_OV"]}}})
headers = {"Authorization": "Bearer jKbfflvlRFdTOW8l6jFEBsuxVddS1uhmej6eIfUIQUNpsgj2Oy7Z7UpS2XnSsT3ec17EHSoIjYKHWWDHzdCFViJ2QxkzTK0sJFuhgw8kJrXJ8fR6xn8lttzhROTle3YzRqRqioT6f1MrZawovudyQ8OBfHsm3dFV8mwkoX3JbRt1MnnpJjZdYWjPyRHeK6BYQk35ypb88515dnNqymNXVCC741ly857U2uBFlWs30DUugiELTniojR2qboursjd","Content-Type": "application/json"}
for i in range (1, 30):
    r = requests.post('https://services.alpha.staging.qubewire.com/admin/api/v1/admin/reports', data=payload, headers=headers)
    print(r.text)
