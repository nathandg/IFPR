""" response if students are in the list """
list_students = ['AB123', 'CB234', 'DB456', 'FB567', 'GB678']


student_to_find = input('Enter the student code: ')

if student_to_find in list_students:
    print('The student is in the list')
else:
    print('The student is not in the list')


