#
#
# Container class in Docker file containered
#
#
import iso6346
import math
import tensorflow

class Container:

    next_serial = 1000

    @staticmethod
    def _generate_serial():
        result = Container.next_serial
        Container.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    @classmethod
    def _create_empty_container(cls, company_name):
        return cls(company_name, container_contents=[])

    @classmethod
    def _create_loaded_container(cls, company_name, container_contents):
        return cls(company_name, container_contents=list(container_contents))

    def __init__(self, company_name, container_contents):
        self.company_name = company_name
        self.container_contents = container_contents
        #self.container_serial = Container._generate_serial()
        self.bic_code = Container._make_bic_code(
            owner_code=company_name,
            serial=Container._generate_serial()
        )
        self.whatevervalue = "whatever goes here"

        print("==========================================")
        print("Container Name: " + self.company_name)
        print("Container Contenets: " + str(self.container_contents))
        #print("Container Serial Number: " +  str(self.container_serial))
        print("Container Serial Number: " + self.bic_code)
        print("Whatever variable:" + self.whatevervalue)
        print("==========================================")
