class Grindex:
    def __init__(self,company_name='AC Grindeks'):
        self.company_name = company_name

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, value):
        value = 'AC Grindeks'
        self.__company_name = value

    def __str__(self):
        return f'HeadQuarters Office: {self.company_name}'
    def __repr__(self):
        return f'{self.company_name}'