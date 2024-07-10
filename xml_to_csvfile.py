import pandas as pd
import xml.etree.ElementTree as etree
with open(r"C:\Users\KEERTHANA R\Downloads\student_data.xml", encoding='UTF-8') as xml_file:
    tree = etree.parse(xml_file)

root = tree.getroot()

ids= []
names= []
ages= []
genders= []
streets= []
cities= []
states= []
zipcodes= []
phones = []
emails= []
courses= []
years= []


for student in root.findall('student'):
    ids.append(student.findtext('id'))
    names.append(student.findtext('name'))
    ages.append(student.findtext('age'))
    genders.append(student.findtext('gender'))

    address = student.find('address')
    streets.append(address.findtext('street'))
    cities.append(address.findtext('city'))
    states.append(address.findtext('state'))
    zipcodes.append(address.findtext('zipcode'))

    contact = student.find('contact')
    phones.append(contact.findtext('phone'))
    emails.append(contact.findtext('email'))

    course = student.find('course')
    courses.append(course.findtext('name'))
    years.append(course.findtext('year'))



Jobs_df = pd.DataFrame({
    'id': ids,
    'name': names,
    'age': ages,
    'gender': genders,
    'street': streets,
    'cit': cities,
    'state': states,
    'zipcode': zipcodes,
    'phone': phones,
    'email': emails,
    'course': courses,
    'year': years
})


print(Jobs_df)


output_csv_path = r'C:\Users\KEERTHANA R\Downloads\student_data.csv'
Jobs_df.to_csv(output_csv_path, index= False)

print('The xml file is sucessfully converted into the Excel file and saved in the output path')
