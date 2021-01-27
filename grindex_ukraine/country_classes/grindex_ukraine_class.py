from global_classes.grindeks_company_class import Grindex


class GrindexUkraine(Grindex):
    def __init__(self,company_name,repres_office='AC Grindeks Ukraine'):
        Grindex.__init__(self,company_name)
        self.repres_office = repres_office
    @property
    def repres_office(self):
        return self.__repres_office

    @repres_office.setter
    def repres_office(self, value):
        value = 'AC Grindeks Ukraine'
        self.__repres_office = value

    def __str__(self):
        return f'{Grindex.__str__(self)} \nCountry Office: {self.repres_office}'

    def __repr__(self):
        return f'{Grindex.__str__(self)},{self.repres_office}'