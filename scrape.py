import requests

from cltsalary.model import db, Employee

def int_or_null(obj, key):
    val = obj.get(key)
    if not val:
        return None
    return int(val)

def main():
    try:
        resp = requests.get('https://opendata.arcgis.com/datasets/54e0445a54c144cda3ce09596f50a134_0.geojson')
    except requests.exceptions.RequestException as e:
        raise Exception(f'Unable to fetch request: {e}')

    try:
        payload = resp.json()
    except ValueError as e:
        raise Exception(f'Unable to parse response JSON: {e}')

    for employee_json in payload['features']:
        emp_props = employee_json['properties']

        # A horse with no name?
        if not emp_props.get('Name'):
            continue

        emp = Employee.create(
            name=emp_props['Name'],
            unit=emp_props['Unit'],
            dept=emp_props['Dept'],
            job_title=emp_props['Job_Title'],
            salary=int_or_null(emp_props, 'Annual_Rt'),
            hourly=int_or_null(emp_props, 'Hrly_rate'),
            full_or_part=emp_props['Full_Part'],
            reg_or_temp=emp_props['Reg_Temp'],
            FID=emp_props['FID'],
        )
        emp.save()

if __name__ == "__main__":
    main()
