from AB import Contact
from AB import *

def test_same_contact():
    obj_1 = Contact("Kevin","Guo","9178086521","gmail")
    obj_2 = Contact("Kevin","Guo","9178086521","gmail")
    assert obj_1.__eq__(obj_2) == True

def test_edit_phone():
    obj_1 = Contact("Kevin","Guo","9178086521","gmail")
    obj_1.edit_phone("2128856563")
    assert obj_1.phone == "2128856563"

def test_user_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    
