student_data = {'id1':
    {'name': ['Shashank'],
     'class': ['XI'],
     'subject_integration': ['English, Math, Science']
    },
    'id2':
    {'name': ['Dia'],
     'class': ['IX'],
     'subject_integration': ['English, Math, Science']
    },
    'id3':
    {'name': ['Sai'],
     'class': ['X'],
     'subject_integration': ['English, Math, Science']
    },
    'id4':
    {'name': ['Siva'],
     'class': ['X'],
     'subject_integration': ['English, Math, Science']
    },
}
result = {}
for key, value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)