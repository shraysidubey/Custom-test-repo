from django.core.management.base import BaseCommand
from customTest.models import Customer
import os
from datetime import datetime

class Command(BaseCommand):

    def __get_file_path(self):
        ## CODE TO READ FILE 
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Getting the resources's path
        path_components = script_dir.split("/")
        # Remove "management/commands" from the path components
        path_components.remove("management")
        path_components.remove("commands")
        # Add "resources" to the path components
        path_components.append("resources")

        # Join the path components back together
        resources_directory = "/".join(path_components)
        
        file_path = resources_directory+ '/customer_data1.txt'
        return file_path

    def handle(self, *args, **kwargs):
        file_path = self.__get_file_path()
        
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR('File does not exist'))
            return

        with open(file_path, 'r') as file:
            for line in file:
                # Process each line here and save to database
                data = line.split(':')  # Assuming comma-separated values
                msisdn = data[0]
                imsi = data[1]
                imei= data[2]
                plan= data[3]
                call_type= data[4]
                corresp_type= data[5]
                corresp_isdn= data[6]
                duration= data[7]
                date_time_string = data[8]+":"+data[9]+":"+data[10].strip() # data in format "HH:MM:SS:DD/MM/YYYY" and "HH:MM:SS:YYYY-MM-DD"                
                if len(data) > 11:
                    date_time_string = data[8]+":"+data[9]+":"+data[10] +":"+ data[11].strip() # data in format "HH:MM:SS:DD/MM/YYYY" and "HH:MM:SS:YYYY-MM-DD"

                if "-" in date_time_string and len(data) == 11:
                    datetime_format = '%H:%M:%Y-%m-%d'
                elif "-" in date_time_string and len(data) > 11:                    
                    datetime_format = '%H:%M:%S:%Y-%m-%d'
                elif len(data) == 11:
                    datetime_format = '%H:%M:%d/%m/%Y'
                else:                    
                    datetime_format = '%H:%M:%S:%d/%m/%Y'
                
                date_time_object = datetime.strptime(date_time_string, datetime_format)
                
                customer_model_instance = Customer(msisdn=msisdn, imsi=imsi, imei=imei,
                                               plan=plan, call_type=call_type, corresp_type=corresp_type,
                                               corresp_isdn=corresp_isdn, duration=duration,
                                               date_time=date_time_object)  # Create your model instance
                customer_model_instance.save()
                self.stdout.write(self.style.SUCCESS('successfully inserted msisdnid:'+ msisdn))        
        self.stdout.write(self.style.SUCCESS('Data parsed and saved successfully'))