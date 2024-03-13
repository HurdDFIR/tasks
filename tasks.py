import argparse
from pathlib import Path
import xml.etree.ElementTree as ET
import re
import xmltodict
from flatdict import FlatDict
import csv

class AllScheduledTasks:
    def __init__(self, task_root):
        self.path = Path(task_root).resolve()
        self.tasks = self._get_tasks()
        self.properties = self._get_task_properties()


    def _get_tasks(self):
        tasks = []
        for file in self.path.glob('**/*'):
            try:
                if file.is_file():
                    tasks.append(ScheduledTask(file))

            except PermissionError:
                print(f'{file} is not accessible')

        return tasks
    
    def _get_task_properties(self):
        all_properties = []
        for task in self.tasks:
            all_properties += task.properties

        all_properties = list(set(all_properties))
        all_properties.sort()
        
        return all_properties

    def write_csv(self, path):
        with open(Path(path).resolve(), 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.properties)
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(task.data)

class ScheduledTask: 
    def __init__(self, path):
        self.path = Path(path).resolve()
        self.name = self.path.name
        self.tree = ET.parse(self.path)
        self.root = self.tree.getroot()
        self.xml = ET.tostring(self.root, encoding='utf-8', method='xml')
        self.data = self._get_task_data()
        self.properties = self._get_task_properties()        

    def _get_task_data(self):
        data = xmltodict.parse(self.xml)
        d =  dict(FlatDict(data, delimiter='.'))
        task_data = {}
        temp_data = {}
        for k, v in d.items():
            # get rid of namespace prefixes 
            temp_data[re.sub(r'ns0:','',k)] = v

        task_data['@Name'] = self.name 
        task_data['@Path'] = self.path
        task_data.update(temp_data)

        return task_data
    
    def _get_task_properties(self):
        properties = []
        for task_property in self.data:
            properties.append(task_property)
        return properties

def main():
    __version__ = '1.0.0'
    __author__ = 'Stephen Hurd | @HurdDFIR'
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Tasks is a tool that will recursivley search a directory of scheduled task XML files and process the data within into an output CSV file.',
        epilog=f'v{__version__} | Author: {__author__}')
    parser.add_argument('-t', '--tasks', type=str, required=False, default='C:\\windows\\system32\\tasks\\', help='Path to the root of the tasks folder. Default is the local system tasks folder.')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output csv file.')
    args = parser.parse_args()

    t = AllScheduledTasks(args.tasks)
    t.write_csv(args.output)

if __name__ == '__main__':
    main()