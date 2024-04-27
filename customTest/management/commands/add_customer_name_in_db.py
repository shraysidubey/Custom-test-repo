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
        
        file_path = resources_directory+ '/customer_data2.txt'
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
                msisdn = data[1]
                customer_name = data[2].strip()
                customer_model_instance = Customer.objects.get(msisdn=msisdn)  # Create your model instance
                customer_model_instance.customer_name = customer_name
                customer_model_instance.save()
                self.stdout.write(self.style.SUCCESS('successfully updated customer name for msisdnid:'+ msisdn + ' as '+ customer_name))
        self.stdout.write(self.style.SUCCESS('Data parsed and saved successfully'))