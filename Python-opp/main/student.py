class Student:
    departement = 'Computer Engineering'
    off_subjects = ['CMP1', 'ELE1', 'MAT1', 'project']
    all_students = []
    
    def __init__(self, fname, lname, reg):
        self.fname = fname
        self.lname = lname
        self.reg = reg
        self.webmail = f'{fname}.{lname}@students.muk.ac.ug'
        self.courses = ['project']
        self.group_member = None
        self.all_students.append(self)
    
    @property
    def get_fullname(self):
        return f'{self.fname} {self.lname}'

    def __repr__(self):
        return f'{self.fname} {self.lname}-{self.reg}'

    def register_subject(self, *sub):
        for s in sub:
            if s not in Student.off_subjects:
                raise ValueError(f'{s} is not offered')
            if s in Student.off_subjects and s not in self.courses:
                self.courses.append(s)

    def set_group_member(self, other):
        if self.group_member != None:
            raise ValueError(f'{self} already has {self.group_member} as a group mamber')
        elif other.group_member != None:
            raise ValueError(f'{other} already has {other.group_member} as a group mamber')
        else:
            self.group_member = other
            other.group_member = self

    def drop_group_member(self, other):
        if self.group_member == None and other.group_member == None:
            return
        elif self.group_member != other:
            raise ValueError(f'{self} is not a group member of {other}.')
        else:
            self.group_member = None
            other.group_member = None
            
    @classmethod
    def not_registered_sub(cls):
        a = set()

        for std in cls.all_students:
            s = set(std.courses)
            a.update(s)

        return  list(set(cls.off_subjects).difference(a))

    @property
    def get_webmail(self):
        return f'{self.fname} {self.lname}@students.mak.ac.ug'
    
    # class method
    @classmethod
    def get_departement(cls):
        return cls.departement


# inheriting the Student class
class Undergraduate(Student):
    def __init__(self, fname, lname, reg, year):
        super().__init__(fname, lname, reg)
        self.year = year

    @property
    def get_year(self):
        return self.year

    @property
    def get_fullname(self):
        return f'{self.fname} {self.lname}'

    @property
    def get_webmail(self):
        return f'{self.fname} {self.lname}@student.mak.ac.ug'
