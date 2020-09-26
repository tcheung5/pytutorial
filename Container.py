#Container class
import iso6346
class Container:

    next_serial = 1000

    @staticmethod
    def _generate_serial():
        result = Container.next_serial
        Container.next_serial += 1
        return result

    @classmethod
    def _create_empty_container(cls, company_name):
        return cls(company_name, container_contents=[])

    @classmethod
    def _create_loaded_container(cls, company_name, container_contents):
        return cls(company_name, container_contents=list(container_contents))

    def __init__(self, company_name, container_contents):
        self.company_name = company_name
        self.container_contents = container_contents
        self.container_serial = Container._generate_serial()

        print("==========================================")
        print("Container Name: " + company_name)
        print("Container Contenets: " + str(container_contents))
        print("Container Serial Number: " +  str(self.container_serial))
        print("==========================================")
